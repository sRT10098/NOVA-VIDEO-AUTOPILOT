from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4
import os
import subprocess
import sys
import tempfile

from fastapi import FastAPI, HTTPException
from fastapi.background import BackgroundTask
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="NOVA Video Autopilot", version="0.2.0")
ROOT = Path(__file__).resolve().parent.parent
JOBS_DIR = ROOT / "outputs"
JOBS_DIR.mkdir(parents=True, exist_ok=True)


class JobRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=500)
    language: str = Field(default="English", max_length=40)
    target_minutes: int = Field(default=5, ge=1, le=60)
    style: str = Field(default="documentary", max_length=80)


class TTSRequest(BaseModel):
    text: str = Field(min_length=2, max_length=12000)
    language: str = Field(default="fa", pattern="^(fa|en)$")


@app.get("/", include_in_schema=False)
def dashboard():
    return FileResponse(ROOT / "frontend" / "index.html")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "NOVA",
        "version": "0.2.0",
        "tts_ready": bool(os.getenv("PIPER_DATA_DIR") and Path(os.getenv("PIPER_DATA_DIR", "")).is_dir()),
    }


@app.post("/api/tts")
def create_narration(request: TTSRequest):
    data_dir = Path(os.getenv("PIPER_DATA_DIR", ROOT / "models")).resolve()
    if not data_dir.is_dir():
        raise HTTPException(status_code=503, detail="Piper voice folder is missing. Configure PIPER_DATA_DIR and install a voice model.")
    voice = os.getenv(
        "PIPER_FA_VOICE" if request.language == "fa" else "PIPER_EN_VOICE",
        "fa_IR-amir-medium" if request.language == "fa" else "en_US-lessac-medium",
    )
    if not (data_dir / f"{voice}.onnx").is_file() or not (data_dir / f"{voice}.onnx.json").is_file():
        raise HTTPException(status_code=503, detail=f"Piper model {voice} is not installed in the configured voice folder.")
    fd, output_name = tempfile.mkstemp(prefix="nova-voice-", suffix=".wav")
    os.close(fd)
    output_path = Path(output_name)
    command = [
        sys.executable, "-m", "piper", "-m", voice,
        "--data-dir", str(data_dir), "-f", str(output_path), "--", request.text,
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=180, check=False)
        if result.returncode != 0 or not output_path.is_file() or output_path.stat().st_size < 44:
            detail = (result.stderr or result.stdout or "Piper could not synthesize the narration.")[-1200:]
            raise HTTPException(status_code=502, detail=detail)
        return FileResponse(
            output_path,
            media_type="audio/wav",
            filename="nova-narration.wav",
            background=BackgroundTask(lambda: output_path.unlink(missing_ok=True)),
        )
    except subprocess.TimeoutExpired:
        output_path.unlink(missing_ok=True)
        raise HTTPException(status_code=504, detail="Narration generation timed out.")
    except HTTPException:
        output_path.unlink(missing_ok=True)
        raise
    except Exception:
        output_path.unlink(missing_ok=True)
        raise


@app.post("/api/jobs", status_code=201)
def create_job(request: JobRequest):
    job_id = str(uuid4())
    job = {
        "id": job_id,
        "status": "planned",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "brief": request.model_dump(),
        "note": "Planning-only milestone; no external AI or paid provider is called.",
    }
    (JOBS_DIR / f"{job_id}.json").write_text(
        __import__("json").dumps(job, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return job


@app.get("/api/jobs/{job_id}")
def get_job(job_id: str):
    path = JOBS_DIR / f"{job_id}.json"
    if not path.is_file():
        raise HTTPException(status_code=404, detail="Job not found")
    return __import__("json").loads(path.read_text(encoding="utf-8"))

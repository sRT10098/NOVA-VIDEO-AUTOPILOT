from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="NOVA Video Autopilot", version="0.1.0")
JOBS_DIR = Path(__file__).resolve().parent.parent / "outputs"
JOBS_DIR.mkdir(parents=True, exist_ok=True)


class JobRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=500)
    language: str = Field(default="English", max_length=40)
    target_minutes: int = Field(default=5, ge=1, le=60)
    style: str = Field(default="documentary", max_length=80)


@app.get("/health")
def health():
    return {"status": "ok", "service": "NOVA", "version": "0.1.0"}


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

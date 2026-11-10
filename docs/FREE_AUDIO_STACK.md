# NOVA free audio stack

## Browser MVP
- Preview voice: Web Speech API. This only plays through the device and cannot be captured as a portable audio file.
- Background score: generated procedurally with Web Audio API and recorded in the WebM.
- Video container: WebM via MediaRecorder. MP4 export is not implemented yet.

## Embedded narration (Piper)
NOVA now has a server endpoint at `POST /api/tts`. It generates a WAV file with Piper; the browser decodes that file and records the narrator together with the procedural score and canvas video.

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Download a Persian voice into the server's `models` directory:
```bash
python -m piper.download_voices fa_IR-amir-medium --data-dir models
```
The Persian Amir model card identifies the training dataset license as CC0. Review the engine license and each model card before commercial redistribution. Official voice catalogue: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/VOICES.md

For English, download:
```bash
python -m piper.download_voices en_US-lessac-medium --data-dir models
```

Environment settings:
- `PIPER_DATA_DIR=models` (directory containing both ONNX model and matching JSON)
- `PIPER_FA_VOICE=fa_IR-amir-medium`
- `PIPER_EN_VOICE=en_US-lessac-medium`

The web app and API must be served by the same FastAPI origin (or a reverse proxy must route `/api` to FastAPI). GitHub Pages alone is static hosting and cannot run this Python endpoint. Backend deployment and end-to-end recording are not yet verified.

## Free asset sources for a future library
- Pixabay audio: free use under Pixabay Content License, subject to prohibited uses and full terms: https://pixabay.com/service/license-summary/
- Mixkit: check the individual asset page license before use.
- Freesound: check each asset license; prefer CC0 or CC-BY and preserve attribution. Avoid CC-BY-NC for monetized videos.

No paid TTS API or API key is used by this implementation.

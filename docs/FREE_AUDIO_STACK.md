# NOVA free audio components

## Current browser MVP
- Narration preview: Web Speech API SpeechSynthesis. Uses voices available on the visitor's device/browser; language and voice quality vary. It is playback only and is not embedded in the exported WebM.
- Background score: generated procedurally with the Web Audio API. No copyrighted track is bundled. The generated soundtrack is recorded as an audio track in the WebM export.
- Video output: WebM through MediaRecorder; not MP4.

## Free media sources for a later asset-library integration
- Pixabay audio: free use under Pixabay Content License, subject to prohibited uses and full license terms. Do not mirror/rehost catalog files or treat standalone redistribution as allowed. See https://pixabay.com/service/license-summary/ and https://pixabay.com/service/faq/
- Mixkit: review the license on each asset page before including an asset, especially commercial-use restrictions.
- Freesound: check each individual sound license; prefer CC0 or CC-BY and preserve attribution metadata. Avoid CC-BY-NC for monetized videos.

## Later server-side voice option
Piper is a free, self-hostable neural TTS option. The original rhasspy/piper repository is archived; active development moved to OHF-Voice/piper1-gpl. Review the engine and each voice/model license before redistribution or commercial use:
https://github.com/OHF-Voice/piper1-gpl

No external paid API, API key, account, or subscription is required for the current browser audio features.

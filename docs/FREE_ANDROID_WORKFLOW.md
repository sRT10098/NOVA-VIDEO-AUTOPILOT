# Free Android production path — MØNO Episode 001

This workflow is designed around an Android phone, zero paid subscriptions, and no API keys.

## What is already available

- The episode script and seven-shot production pack: [EPISODE_001_PRODUCTION_PACK.md](EPISODE_001_PRODUCTION_PACK.md)
- The static NOVA Studio app is deployed from `frontend/` through GitHub Pages.
- The app's current renderer creates a simple animated text-card WebM. It is a prototype, not the finished cinematic episode.
- Fal video generation is currently unavailable while its account balance is exhausted. No paid call should be made without explicit approval.
- Canva AI video creation is unavailable on the connected plan. Do not retry it as a workaround.

## Recommended free Android editor

**LibreCuts (F-Droid, beta)** is the first editor to test:
- Free and open source.
- On-device editing and watermark-free export.
- Supports trimming, merging, overlays, subtitles, audio, crop, transitions, speed and basic adjustments.
- It is beta software, so test with a short disposable clip before relying on it for the final master.

Official F-Droid listing: https://f-droid.org/packages/com.tharunbirla.librecuts/

Do not install APK mirrors or repackaged copies. Use the F-Droid listing and review the permissions shown by Android.

## Production sequence

1. Lock the MØNO character reference before making scene variations. Preserve the round pale head, dark expressive eyes, green-left/pink-right antenna tips, thin black stick limbs, dark scarf and warm chest emblem.
2. Produce one approved visual per shot before attempting animation. The environment must be photorealistic while MØNO remains a simple stylized figure.
3. Keep clean visuals free of text. Add the episode title and subtitles in the editor.
4. Assemble the seven shots in the order and timings in the production pack. Use restrained cuts and dissolves; avoid template-heavy transitions.
5. Add ORION narration first, then MIKO dialogue, then quiet ambience/music. Dialogue must remain clearly audible.
6. Export a short 10–15 second test first. Check framing, audio sync, export quality and watermark status before rendering the full 80–90 second episode.
7. Review the exported file from beginning to end before calling the episode complete.

## Free asset rules

- Prefer assets created for this project or assets whose individual license is clearly compatible with the intended publication.
- Keep a record of source and license for every downloaded music or sound effect.
- Never use a random social-media clip as if it were cleared for reuse.
- Do not pay, start a trial, or consume a paid AI quota without the user's explicit approval.

## Current blockers (honest status)

- No photorealistic scene clips have been generated yet.
- No final MØNO reference sheet has been approved as an image asset.
- The Piper narration endpoint requires a deployed backend and voice model; GitHub Pages alone cannot run it.
- The current browser prototype exports WebM, not MP4.
- LibreCuts is an editor recommendation, not an integration that NOVA can control remotely.

## Next engineering milestone

Make NOVA's static studio accept local scene images/video and a narration audio file, then build a low-resolution preview before a final render. Keep all media local to the phone wherever the browser permits. Do not imply that the editor can remotely operate CapCut, InShot or LibreCuts.

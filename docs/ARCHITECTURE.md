# NOVA architecture

NOVA is an on-demand video-production workflow controlled from a mobile-friendly interface.

## Pipeline

1. Accept a topic and production brief.
2. Research the topic and collect source notes.
3. Draft the script and narration.
4. Break the script into scenes and visual prompts.
5. Generate or import visual and audio assets.
6. Assemble scenes, narration, music, and subtitles.
7. Render and validate the final MP4.
8. Present the output and production notes to the user.

## Initial implementation boundaries

- Start with a simple web control panel and a Python orchestration backend.
- Run jobs only when explicitly requested; do not run a permanent background worker by default.
- Keep providers behind adapters so services can be changed later.
- Require explicit user approval before enabling paid providers or incurring costs.
- Store credentials in environment variables or a secrets manager, never in source control.
- Track each job's status, logs, assets, and errors.

## First milestone

Build a local development version that accepts a brief, creates a structured production plan, and exports a job folder. Add media-provider integrations only after the workflow is tested.

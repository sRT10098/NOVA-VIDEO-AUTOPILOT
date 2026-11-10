# NOVA VIDEO AUTOPILOT — Provider Integration Roadmap

**Status:** Planning baseline — no provider is connected yet.
**Primary target:** Android-first, on-demand workflow.
**Budget rule:** Free tiers only unless the owner explicitly approves a paid service.
**Security:** Never commit API keys, cookies, session tokens, or personal credentials.

## 1. Verified provider constraints (10 Nov 2026)

### Google Flow
- The official Flow page advertises 50 daily credits on its free tier.
- Listed capabilities include text-to-video, frames-to-video, ingredients-to-video, video extension, video-to-video editing, Scenebuilder, and character tools.
- Treat Flow as a user-operated web provider for now. Do not assume a public API or automate private browser sessions.
- NOVA should prepare scene prompts, reference assets, shot metadata, and a production checklist that the user can take into Flow. The user then imports the resulting clips back into the project.

### OpenMontage Studio
- The official site describes a Windows desktop application currently in private alpha / waitlist.
- It expects a local Claude Code or Codex agent and user-selected media providers.
- It is not a deployable Android integration at this stage. Reassess only if access and a supported integration interface become available.

### Higgsfield
- Its free tier is limited and does not provide a dependable recurring video-credit budget.
- Keep it optional. Before each generation, the user must see the model, estimated credit cost, and confirm the action.

## 2. Architecture principles

1. **Provider-neutral core:** episode planning must work even when every media provider is unavailable.
2. **Explicit generation:** no background generation, auto-refill, purchases, or paid API calls.
3. **Bring-your-own-output:** users can upload generated clips, audio, and images from any provider.
4. **Reference continuity:** each episode stores one approved character reference and attaches it to every relevant scene.
5. **Traceability:** every asset records its source provider, model (if known), prompt, creation date, and local filename.
6. **Graceful fallback:** if a provider has no API, NOVA offers a copyable prompt and an import slot rather than pretending to connect.

## 3. Provider adapter contract

A future adapter may implement:

- `capabilities()`: report supported media types, reference-image support, duration/resolution limits, and whether an official API exists.
- `estimateCost(request)`: return a known credit estimate or `unknown`; never guess.
- `prepare(request)`: validate the scene and produce provider-specific prompt/metadata.
- `generate(request)`: only for documented, authorized APIs; require explicit user confirmation before any billable call.
- `importAsset(file)`: attach user-provided output to the correct scene.
- `status(jobId)`: report real provider job status only when an official API supports it.

A browser-only provider must use the manual handoff path. Do not scrape, bypass login, or store browser credentials.

## 4. Initial implementation phases

### Phase A — reliable production workspace
- Episode and scene records.
- Character reference library.
- Prompt builder with global style and per-scene prompt.
- Scene status: planned, prompt-ready, generated, reviewed, approved.
- Asset import and metadata manifest.
- Export a production pack (prompts + shot list + asset manifest).

### Phase B — media assembly
- Timeline ordering, clip trims, narration/music/SFX tracks, subtitle timing.
- Render only through a supported local or hosted renderer.
- Validate aspect ratio, resolution, duration, missing media, and audio peaks before marking complete.

### Phase C — official provider APIs
- Add one adapter at a time after verifying public API documentation, authentication, pricing, free-tier limits, and output rights.
- Start with the provider that offers a documented API and a genuinely usable free allowance.
- Keep Flow's manual handoff available even if an API adapter is added elsewhere.

## 5. MØNO Episode 001 acceptance checks

- The approved MØNO reference is reused consistently.
- Environment remains photorealistic and cinematic; MØNO remains a simple stick-figure design.
- Each selected shot contains real motion, not a still-image slideshow.
- Narration and Miko dialogue remain intelligible above music.
- Final timeline is widescreen 16:9 and has a reviewed ending hook.
- No scene is marked approved until a human has reviewed the actual generated clip.

## 6. Current next step

Implement Phase A against the existing repository structure. First inspect the existing source tree before replacing or creating application files. Preserve the existing Episode 001 script until the creative direction is explicitly revised.

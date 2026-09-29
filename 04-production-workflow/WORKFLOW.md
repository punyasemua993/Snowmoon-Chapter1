# Reproducible Production Workflow

0. Source/rights: retain source URL and reference; document provider licenses.
1. Character lock: generate references, select canonical image, record model/version/seed/settings/hash.
2. Environment lock: create canonical Meldan, sky bridge, Badra, concert, autobus and home references.
3. Keyframes: generate each of 30 shots; save selected keyframe and provenance.
4. Animation: animate each keyframe for ~9 seconds; reject identity drift/morphing/broken anatomy.
5. Japanese voice: generate each line separately using a distinct character profile; record TTS provenance.
6. Sound: add dialogue, foley, crowd, music and ambience; duck music under dialogue.
7. Subtitles: English subtitles as a separate track/file, not baked into images.
8. Edit: target 30 x 9s = 270s / 4:30; preserve shot order and cliffhanger.
9. QC: continuity, lip-sync, subtitle timing, UI, watermarks, logos, provenance, secrets.
10. Release: regenerate SHA-256 manifest; publish the pipeline with the final adaptation.

Never commit API keys, private credentials, proprietary model weights or assets whose license forbids redistribution.

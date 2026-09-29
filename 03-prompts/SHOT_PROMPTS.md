# Shot Prompt Assembly

For every shot combine:
1. `GLOBAL_VISUAL_PROMPT.txt`
2. relevant character reference(s)
3. relevant environment prompt
4. shot entry from `snowmoon_ch1_shot_manifest.json`
5. `NEGATIVE_PROMPT.txt`

## Animation template
Animate the approved keyframe while preserving exact identity and costume. Natural anime body mechanics, readable hand actions, subtle eye movement, cloth/hair response, realistic camera parallax, controlled secondary motion, no morphing. Duration 9 seconds. Keep background architecture stable.

## Camera arc
S01–S06 slow cinematic tracking/reveals; S07–S11 contemplative close-ups/UI inserts; S12–S20 increasingly energetic concert camera; S21–S26 abrupt but controlled chase camera; S27–S29 stable warm domestic camera; S30 peaceful wide shot to ominous macro close-up.

## UI
Prefer compositing exact UI text in post instead of asking the image model to render text.

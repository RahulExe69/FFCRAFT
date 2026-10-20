# FFCRAFT project vision and Mobile map-making roadmap

**Status:** Living project brief  
**Primary focus:** Helping a creator build real maps in Free Fire Craftland Mobile  
**Secondary focus:** Reliable scripting knowledge for Craftland Mobile and Craftland Studio PC

## The vision in plain language

FFCRAFT should become an external, reusable Craftland skill: the creator describes a map, gameplay experience, or mechanic in ordinary language, and the assistant helps turn that idea into a practical build plan—with accurate editor steps, layout guidance, visual-block logic, PC code where relevant, dependencies, and tests.

The immediate priority is **creating maps in Craftland Mobile**. The goal is not merely to collect every API name or produce a giant technical encyclopedia. The knowledge base should teach the assistant how the real Mobile editor works, so future collaboration can focus on making maps rather than repeatedly rediscovering the interface.

The creator can teach the workflow through screenshots, screen recordings, explanations, exported project data, and results from trying a suggested step. FFCRAFT should turn those observations into clear, searchable documentation that can be reused across future map projects.

## What success looks like

A successful FFCRAFT session should be able to help with tasks such as:

- Plan a map concept, player flow, layout, landmarks, routes, cover, spawn areas, and points of interest.
- Understand how to navigate Craftland Mobile's editor and locate the relevant building, object, gameplay, and scripting controls.
- Turn a rough map idea into manageable construction steps that can be followed on a phone.
- Explain what an editor control or block does using the exact label and context shown in the user's version.
- Design gameplay systems such as arenas, rounds, spawns, scoring, checkpoints, parkour, races, puzzles, and other challenges.
- Connect visual blocks in the correct order, with the right input values and script context.
- Diagnose unexpected results using the observed editor state and a repeatable test.
- Keep map design and gameplay logic connected: where an object is placed can affect triggers, sightlines, movement, pacing, and game rules.
- Reuse proven patterns without pretending an untested idea has already been verified.

## Priority order

### 1. Learn the real Craftland Mobile workflow

Capture the editor as the creator actually sees it. Record navigation paths, tabs, panels, object placement, transforms, terrain/building tools where available, object settings, map configuration, script entry points, dropdown options, and save/test/publish flows when they are demonstrated.

Do not assume that a PC Studio workflow exists identically on Mobile. A PC manual, library, or API can be a useful clue, but it is not proof of a Mobile editor control or visual block.

### 2. Build map-making playbooks

Organize guidance around creator goals, not just API categories. Initial playbook families should include:

- **Custom environment:** layout, terrain, buildings, props, landmarks, navigation, and visual composition.
- **Combat/arena map:** spawn fairness, routes, cover, sightlines, boundaries, rounds, and scoring.
- **Minigame:** parkour, race, puzzle, challenge, checkpoint, timer, and reset flows.
- **Interactive map:** buttons, triggers, object interactions, UI feedback, and event-driven mechanics.
- **Advanced mechanics:** multi-step state, team/player tracking, persistence where supported, and complex win conditions.

These are planning categories, not claims that every feature or editor tool is available in every version.

### 3. Teach visual-block logic through real examples

For each captured block or editor feature, record the exact visible label, category, context, input/output sockets, dropdown options, version, evidence source, and any observed limitations. Prefer complete examples with connected blocks and neighboring context over isolated names.

A recipe should explain what the mechanic does, where to build it, how the blocks connect, how to configure it, how to test it, and what to inspect if it fails.

### 4. Keep the technical reference as a support layer

The existing API, enum, event, type, and crosswalk research remains valuable. Use it to answer concrete map-making questions and to bridge Mobile visual blocks with PC code when justified. Do not let bulk cataloguing displace the primary Mobile map-making goal.

## How the assistant should learn from the creator

When the creator shares an editor screenshot or recording:

1. Identify the visible editor screen, current task, and any clearly readable labels.
2. Describe only what the evidence supports. Mark obscured or ambiguous controls as unknown.
3. Ask one focused question only when it blocks the next step.
4. Convert confirmed information into a concise human-readable guide and, when useful, a structured record.
5. Link the record to the original screenshot/clip or its filename, editor version, and capture date when available.
6. Separate a user observation from an official-documentation match and from a behavior that has actually been tested.
7. Reuse the captured knowledge in future instructions instead of asking the creator to explain the same confirmed workflow again.

The assistant cannot directly manipulate the creator's phone merely by reading this repository. The workflow is collaborative: the assistant plans and explains; the creator operates the editor and shares evidence/results; FFCRAFT records the knowledge.

## Evidence and accuracy rules

Every important editor claim should have an identifiable evidence state:

- **User-observed:** shown or described by the creator; independent confirmation may still be missing.
- **Officially documented:** supported by a current official source, with its URL and relevant scope.
- **Editor-verified:** exact label, socket, setting, or dropdown confirmed in the specified installed editor/version.
- **Tested in map:** the result was reproduced in a real test, with steps and outcome recorded.
- **Candidate / unresolved:** plausible lead only; not safe to present as fact.

Never invent block names, menu labels, dropdown values, APIs, asset IDs, or editor capabilities. Never call a recipe compiled or playtested unless that validation actually occurred. Record platform and version caveats.

## Repository organization principles

The repository should serve two readers:

1. **The creator:** wants a direct, readable answer to “How do I build this map or mechanic?”
2. **The research workflow / assistant:** needs precise records, source links, machine-readable inventories, and unresolved questions.

Use Markdown documents for explanations, workflows, examples, and playbooks. Keep JSON for searchable inventories, crosswalks, and data intended for structured processing. Link the two so a human never has to reverse-engineer a large JSON file just to understand the current finding.

Keep raw evidence separate from interpretations. Preserve the original `Rough.txt` byte-for-byte as the creator's source notes. Improvements belong in derived documentation and indexes; do not delete obscure entries just because they are old, duplicated, unclear, or unverified.

## Suggested workflow for a new map

1. **Describe the idea:** map genre, player count if known, core loop, desired mood, and what makes the map fun.
2. **Sketch the player journey:** spawn, first objective, main routes, encounters, checkpoints, finish/win condition, and reset path.
3. **Check editor capabilities:** verify the relevant Mobile tools, objects, settings, and blocks in the actual editor.
4. **Build the environment in small passes:** greybox layout first, then routes/cover, then details and visual polish.
5. **Add gameplay logic:** document each event, variable/state, block connection, and dependency before adding complexity.
6. **Test the core loop:** start, normal play, edge cases, death/respawn, round reset, and end condition as relevant.
7. **Record what happened:** expected vs. actual behavior, screenshots, editor version, and the smallest next fix.
8. **Promote reusable learning:** update the relevant human guide and structured index only when the observation is clear enough to preserve.

## Current state and next milestone

FFCRAFT already contains a substantial research base: a normalized draft from `Rough.txt`, a block-symbol crosswalk, PC library/API and enum catalogs, official Mobile source maps, recipe indexes, and a queue of unresolved editor-verification work. These are useful foundations, but they do not yet amount to a complete, current Mobile editor manual.

**Next milestone:** build a creator-first Mobile guide from real editor walkthroughs, then produce the first reusable map-building playbook and one end-to-end gameplay recipe. Expand the technical catalog when a real map-building task exposes a gap, while continuing to preserve the existing research.

## Definition of done for a useful guide

A guide is useful when a creator can follow it without guessing: it names the screen/control, gives the sequence of actions, explains the expected result, notes version/evidence limits, and says what to check if the result differs. A guide is not complete merely because it lists the names of relevant blocks or APIs.

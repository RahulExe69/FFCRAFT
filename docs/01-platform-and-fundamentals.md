# Platform map and core concepts

## Craftland in one sentence

Craftland is Free Fire's custom-map/gameplay creation environment. Depending on the tool and feature set, creators can edit scenes and rules, assemble visual logic, customize UI, and use code/scripts to produce gameplay beyond static map placement.

## Two environments — do not blur them

| Environment | Practical focus | Important caveat |
|---|---|---|
| Craftland Mobile | Build/play custom maps using the in-game creator experience; beginner guides cover scene editing, game parameters, objects, economy, monsters, blocks, and UI. | A PC Studio code API or editor workflow may not exist here. |
| Craftland Studio PC | Broader authoring environment: scene/level editing, game rules, visual logic, code scripts, libraries, custom UI/resources, asset store, data storage, and debugging. | Exact functions still vary by installed version, runtime side, and editor/platform support. |

Official starting points: [Craftland home](https://ffcraftland.garena.com/en/), [Mobile beginner tutorial](https://ffcraftland.garena.com/en/tutorial/cl/3), [PC user manual](https://ffcraftland.garena.com/en/tutorial/fe/1).

## Core model

- **Scene/world:** geometry, placed entities, triggers, spawn points, props, sound/visual entities, and object hierarchy.
- **Game rules/workflow:** match objectives, rounds, phases, team logic, respawn behavior, and game end conditions.
- **Entities/components/properties:** objects have components and properties. Scripts can read/write only what the current entity and API allow.
- **Scripts:** respond to events and call APIs to mutate game state or presentation.
- **UI/HUD:** built-in HUDs and custom UI can expose information, buttons, prompts, and player-facing interactions.
- **Resources/assets:** official and creator-made assets, templates, prefabs, animations, effects, sounds, and other resources may have version/dependency constraints.
- **Data Storage:** optional persistent data features for archives, rankings, statistics, and some cross-game data on the same map, subject to quotas/limits.

## Block scripts versus code scripts

| | Visual block scripts | Code scripts |
|---|---|---|
| Strength | Fast to build, inspect, and teach; event/action flow is visible. | Better for longer, reusable, structured logic; easier to review complex algorithms in text. |
| Trade-off | Large graphs can become hard to maintain; available blocks depend on script context/type. | Requires learning Craftland's own script syntax, imports, types, and runtime restrictions. |
| Good use | Triggers, simple interactions, HUD actions, effects, basic score/health logic. | Shared helpers, complex state transitions, reusable systems, more involved calculations. |

Garena's manual describes block scripts as more intuitive but says complexity and maintenance become harder as logic grows; code scripting is more flexible for complex logic. That is a guideline, not a rule that every feature should be rewritten in code. Source: [PC Scripts manual](https://ffcraftland-pre.garena.com/en/tutorial/fe/1-7/).

## Common contexts/scopes

The official Block Scripts guide describes default **global**, **party/team**, and **player** scripts; additional scripts can be attached to objects or UI elements. The right scope matters:

- Global: match-wide state, centralized rules, win checks, or a global event receiver.
- Player: individual state, player-specific UI or custom properties, personal stats.
- Team/party: squad/team-specific state and rules.
- Object/trigger: interactions tied to a door, zone, lift, button, monster spawn, or prop.
- UI/HUD: player input and presentation; check whether logic belongs on the client.

Source: [Block Scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-101).

## Mental model for designing any mechanic

1. Define the exact gameplay outcome and its reset/persistence rules.
2. Identify the event that starts it.
3. Decide what data is state (counter, owner, cooldown, score) and who owns it.
4. Choose the smallest correct scope and runtime side.
5. Check required block/API availability in that context.
6. Implement the state change and any presentation separately.
7. Test the normal path, repeated triggers, simultaneous players, disconnect/rejoin, round reset, and match end.

## Reusable official examples

Garena-hosted tutorials include Game Mechanics, Myconsole, Big Head Mode, and custom trigger examples. These are valuable starter maps for learning damage/healing zones, teleportation, text display, costume changes, elevators/doors, custom HUDs, batch item/equipment changes, and player-specific events. Prefer inspecting and re-editing official templates over guessing an API from its name:

- [Game Mechanics template](https://ffcraftland.garena.com/en/tutorial/cl/4-87)
- [Myconsole template](https://ffcraftland.garena.com/en/tutorial/cl/4-86)
- [Big Head Mode template](https://ffcraftland.garena.com/en/tutorial/cl/4-85)
- [Official beginner tutorial index](https://ffcraftland.garena.com/en/tutorial/cl/3)

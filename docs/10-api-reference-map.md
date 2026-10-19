# API and module discovery map

This is a **navigation map**, not a copied API inventory. Use it to locate the right family, then verify the actual function/event/type in the installed Craftland Studio library. The official online index includes legacy entries and some API pages are explicitly marked obsolete.

## Start with the right reference

1. Open the relevant event/API/type page in the official docs.
2. Read its runtime label: Server Side, Client Side, Both Server and Client.
3. Read its platform label: Only PC, Both Mobile and PC, or other stated scope.
4. Check whether it is marked Obsolete/deprecated.
5. Inspect parameters, types, outputs/return values, and side effects.
6. Confirm the installed editor's built-in `.fcc` declaration matches the page.
7. Test it in a minimal map before using it in a larger system.

Primary discovery links: [Official API index](https://ffcraftland.garena.com/en/docs/api-1-26), [Event index](https://ffcraftland.garena.com/en/docs/type-11/), [Type index](https://ffcraftland.garena.com/en/docs/type-10), [official patch notes](https://ffcraftland.garena.com/en/patch-notes/).

## Module family map

The official standard-library index groups APIs into many families. Naming and availability can evolve, so use these as search terms rather than guarantees.

| Module/family | Typical questions it helps answer | Common cautions |
|---|---|---|
| Standard library / entity helpers | How do I get the current script entity, global entity, children, owner, type, or all players/teams? | Null checks and exact entity type matter. A global/player/object context may not match. |
| List / Map / Math / Strings / Convert | How do I transform values, look up keys, compare numbers, parse strings, or process arrays/lists? | Match value types; avoid expensive/unbounded loops. |
| Scene / Level Object / Physics / Camera / Minimap | How do I inspect or modify world objects, physics, camera, or map presentation? | Many APIs are side-specific; test scene/runtime behavior and performance. |
| Player / Team / Combat / Items / Safe Zone / Airdrop | How do I read player/team state, react to damage/elimination, manipulate supported items, or influence combat? | Distinguish player-death vs kill-credit events; keep competitive decisions authoritative. |
| HUD / Custom UI / Input System / Chat Channel / Social | How do I build custom interfaces, react to buttons/joysticks, show messages, or handle chat? | UI can be local to a player; current 1.19.0 changes add PC Studio chat APIs and new UI/input capabilities. |
| Workflow / Game Time / Game Results | How do I move rounds/phases, track time, or determine/end a match? | Avoid conflicting workflow owners and race conditions at round/game boundaries. |
| Playable / Animation / Animation Controller / Behavior Tree / Avatar / Morph / Dyeing | How do I trigger effects, sound, motion, behavior, or character appearance changes? | Asset references can break; separate cosmetic state from match logic; inspect dependency resources. |
| Economy / Collection / Football | How do I handle shop/economy/collections or specialized mode systems? | Specialized systems may be PC-only or template-specific. |
| Data Storage / Data Store | How do I persist player state, access tables/rankings/statistics, or query cross-map data? | Do not conflate configured storage types with newer code APIs; read quotas, status outputs, and platform labels. |
| AI / Read Table Content / CSV | How do I query supported data tables or use AI-related APIs? | Table-key/column behavior changed in recent releases; check the current API for key/column-name support. |
| Collection / wardrobe | How do I present and process outfit/wardrobe interactions? | Latest patch notes add in-match wardrobe features; verify supported API and resource download state. |

## Useful event map

The official event index includes these useful families:

- Game flow: On Game Start, On Game End, On Round Start/End, On Phase Start/End.
- Player life cycle: On Player Join, On Player Quit Midway, On Player Revived, On Disconnect, On Reconnect.
- Combat: On Player Be Eliminated, On Player Assist, On Player Deal Damage, On Player Eliminate, On Team Ace.
- Scene and input: On Scene Load, On Scene Switch, On Camera Raycast, On Screen Touch Begin/End.
- Spectator/network: On Spectator Join/Quit, On Player Out Of Sync.
- Custom/runtime state: On Custom Property Change and On Custom Player State Changed are listed in official reference pages.

Names can be similar but semantically different. Check the exact description, owner, parameters, platform and obsolete marker on the selected event page.

## Examples of documented platform constraints

- `Get Local Player` is labelled Client Side and Only PC in the current surfaced API reference. Do not assume it can run in a server-side script or on mobile.
- `Set Custom Player State` / `Get Custom Player State` are also labelled Client Side and Only PC in the surfaced references. The set operation says it uploads state to the server and syncs it with all clients; that does not turn the function into a server-side API.
- `Bind Custom Player` is labelled Server Side and Only PC in the surfaced reference.
- `ReadFromDataStoreByColumn`, `ReadFromDataStoreSteady`, and `WriteToDataStoreV2` are labelled Server Side and Only PC in the surfaced pages.
- Legacy `WriteToDataStore` is marked obsolete; use the currently documented replacement when appropriate.

These examples are precisely why the page-level tags matter. A feature being documented on the Craftland website does not guarantee it is supported in Craftland Mobile.

## New API surface highlighted by Studio 1.19.0

The September 2026 patch notes mention newer APIs/features for:

- Distance-based visibility/fade/hide/scale components.
- UI click detection and retrieving actual UI-control positions.
- Large-number operations, scientific notation, and additional numeric formatting.
- Table data access by column name or key.
- Client-side emote play/pause.
- High-performance reusable scrolling lists.
- Player rotation speed by stance and improved Player CCT movement/jump/stance events.
- Player information such as camera sensitivity, character appearance ID, and actual movement speed.
- Chat-window creation and chat-message events.
- Wardrobe opening/closing, outfit selection, equipment confirmation, and resource download status.
- Camera sensitivity and camera-shake APIs.

Treat the patch notes as feature discovery, not a substitute for each API's signature/side/platform docs.

## Obsolete/deprecation policy

If a page is marked obsolete, don't use it in new work unless maintaining an older project and you have confirmed no viable replacement. Search the current standard library for replacement APIs and review their behavioral differences (parameters, side effects, caching, return/status values, target platform).

## Suggested next research artifact

A true exhaustive API catalogue should be generated from the release installed by the user, not manually inferred from the website. For every API/event/type, store: exact name, declaration, parameter/return types, runtime side, editor/client platform, obsolete flag, module, release checked, a concise behavior summary, and a tiny test result. This file is the taxonomy to build that catalogue from.

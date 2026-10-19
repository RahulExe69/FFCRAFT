# Reusable logic recipes (design-level examples)

These recipes turn official concepts into reusable patterns. Unless a section explicitly says otherwise, they are **design-level, not compile-ready source code**: use current block/API names and signatures from the editor. No live game test was run as part of this research pass.

## Recipe 1 — Sequential player join serial

**Goal:** assign a per-match serial 1, 2, 3, … in join-event order, not a reusable player slot.

**Flow:** initialize one authoritative global counter → On Player Join (server-side) → increment once → write the number to the arriving player's supported custom property → update that player's HUD/display if needed.

**Must test:** initial counter lifetime, near-simultaneous joins, slot reuse, disconnect/reconnect semantics, match versus round reset, replication to clients. Full design: [Player roster and join serials](05-player-roster-join-serials.md).

## Recipe 2 — First-to-N elimination win condition

**Goal:** end the round when the configured score objective is reached.

**Flow:** combat/player handler listens to the event that means a player caused an elimination → validates the killer and state → increments authoritative score once → dispatches a custom score/win-check event → global controller compares current score with the configured objective → if reached, advances the game workflow/phase → UI displays result.

**Why split it:** the combat event, score storage, win decision, and UI feedback have different owners and failure cases. The official tutorial demonstrates incrementing an elimination point and dispatching a custom global event to check an objective.

**Must test:** simultaneous kills, score at N-1, repeated event delivery, player leaving after a kill, correct winner, tie behavior, phase changes, and obsolete score-change events. Sources: [official game rules example](https://ffcraftland-pre.garena.com/en/tutorial/fe/1-51/) and [event catalogue](https://ffcraftland.garena.com/en/docs/type-11/).

## Recipe 3 — Healing zone

**Goal:** restore health while a player is inside a defined zone, with safe stop/exit behavior.

**Flow:** trigger enter → validate player → mark player as inside zone → run a bounded/controlled heal interval while still inside and alive → apply allowed heal amount → show effect/UI feedback → trigger exit/death/leave/round-end cancels the recurring work and clears the state.

The official Game Mechanics template documents a healing area that restores 15 HP per second and displays a healing effect. Treat 15 HP/sec as that template's example, not a universal Craftland constant.

**Must test:** health cap, two overlapping zones, re-entry, death/revive, trigger spam, tick cleanup, and whether health writes are authoritative.

Source: [Game Mechanics template](https://ffcraftland.garena.com/en/tutorial/cl/4-87).

## Recipe 4 — Teleport trigger

**Goal:** move a valid player to a destination when entering a zone or pressing a button.

**Flow:** trigger → validate player and game phase → reject if teleport is on cooldown → mark transition in progress → invoke the current supported teleport mechanism → clear transition after completion/failure → show feedback.

**Must test:** invalid/destroyed destination, repeat collision events, spawn/respawn, fall-through or stuck states, and whether teleport is supported on target runtime. Avoid legacy APIs marked obsolete.

Source: [Game Mechanics template](https://ffcraftland.garena.com/en/tutorial/cl/4-87), [API index](https://ffcraftland.garena.com/en/docs/api-1-26).

## Recipe 5 — Player-specific HUD on join

**Goal:** create or show a HUD for one player without accidentally showing private UI to every player.

**Flow:** On Player Join receives Player → call the currently supported HUD create/apply action with that Player and target HUD configuration → wait only if current API requires readiness timing → assign supported properties/bind actions → verify UI owner/visibility → clean up or recreate on supported lifecycle events.

The official block tutorial demonstrates passing the Player from On Player Join into a HUD-creation action and then setting a property on the returned UI entity. Don't blindly copy the wait block if the current version exposes a more reliable ready event.

**Must test:** second player, reconnect, respawn, UI index/config changes, local versus shared visibility, and player leave during creation.

Source: [Block Scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-101).

## Recipe 6 — Persistent player archive

**Goal:** save progress across sessions without exhausting Data Storage quotas.

**Flow:** configure the Data Storage module and accepted table value type → when a meaningful checkpoint occurs, build a compact supported value from player attributes → write once and check success → on player join/load, read by the proper player UUID/key → validate schema/version and restore safely → use defaults if absent/failure.

The official example stores position, orientation, and score in a normal data-storage table and recommends avoiding excess tables/read/write operations. Consider storing related values together when the configured type allows it.

**Must test:** missing record, invalid/old schema, operation failure, reconnect, limit boundaries, match exit during write, and restore order relative to player spawn.

Source: [Data Storage](https://ffcraftland.garena.com/en/tutorial/fe/1-35).

## Recipe 7 — Client request, server validation, client feedback

**Goal:** let a client UI/button request a shared gameplay change safely.

**Flow:** client button/input → send supported event/message → server checks sender, phase, ownership, cooldown, and arguments → server mutates authoritative state → server sends/causes an appropriate state/event update → client UI reflects the approved result.

This follows the documented rule that server/client scripts cannot call each other directly and should communicate through events. Do not trust the client's requested score, item amount, kill count, or win claim.

**Must test:** forged/repeated requests, simultaneous requests, invalid player/entity, event receiver lifecycle, and replication delay.

Source: [Code Scripts](https://ffcraftland.garena.com/en/tutorial/fe/1-9).

## Recipe 8 — Runtime sound or effect

**Goal:** play a supported effect at a defined moment and for the intended audience.

**Flow:** gameplay event → validate target and runtime side → call the current non-obsolete sound/effect API or trigger a configured entity → choose local-target versus spatial/3D behavior → stop/clean up if the workflow supports lifecycle control.

**Must test:** sound distance attenuation, whether other players can hear/see it, multiple concurrent instances, resource availability, audio-track overlap, and mobile support.

Sources: [Audio Tracks](https://ffcraftland.garena.com/en/tutorial/cl/4-89), [Playable](https://ffcraftland.garena.com/en/tutorial/fe/1-24), [API index](https://ffcraftland.garena.com/en/docs/api-1-26).

## Minimum playtest matrix

| Test | Why it matters |
|---|---|
| Solo player, fresh match | Baseline path and initialization |
| Two players joining in quick succession | Sequence/order and race conditions |
| Player leaves/rejoins | Identity and cleanup semantics |
| Player dies/revives | Respawned entities, properties, UI and ongoing timers |
| New round, same match | Match-scoped state should remain or reset intentionally |
| New match | State should start cleanly |
| Target mobile client | PC-only APIs/features can differ |
| Low performance/network conditions | Timing and synchronization assumptions |
| Missing resource/storage read failure | Error handling and safe defaults |
| Repeated trigger/button input | Idempotence, cooldowns, duplicate event paths |

## Recipe status convention

A recipe becomes **verified** only after someone records the editor/client version, map used, exact API/block names, reproduction steps, expected outcome, observed outcome, and supporting evidence (logs/video/screenshots). Until then, keep it labelled design-level or test-needed.

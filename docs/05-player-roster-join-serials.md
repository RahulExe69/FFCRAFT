# Player roster and sequential join serials

This document records the robust design for assigning each arriving player a monotonic join-order serial instead of relying on a slot/index that may later be reused.

## The requirement

For one match/session, each player-join event should receive the next integer in sequence: 1, 2, 3, 4, and so on. The assigned number should remain attached to the intended player for the relevant lifetime. If a player leaves and a new player occupies the same engine slot, the new player must not inherit the old player's serial.

The official event catalogue includes **On Player Join**, whose documented meaning is that it triggers when a player joins the game. The event page describes its owner as the game entity. Exact parameter types and platform tags should be checked on the live event page/editor.

References: [On Player Join](https://ffcraftland.garena.com/en/docs/event-11-14), [event catalogue](https://ffcraftland.garena.com/en/docs/type-11/).

## Recommended implementation architecture

1. Create one authoritative global/server-side script (or equivalent server-side block script) that owns a match-scoped integer counter.
2. Initialize the counter once at a known session initialization point. Do not reset it casually on every round if serials should remain stable for the full match.
3. When On Player Join arrives, increment the counter exactly once in that authoritative handler.
4. Store the resulting number on the joining player's own supported custom property/player data field. The exact setter/property name must be selected from the installed editor's current libraries.
5. Send/display the serial through the supported player/UI path. Keep display formatting separate from the authoritative stored value.
6. Log event order, player identity, and assigned serial during test runs; remove or filter noisy logs before release.

### Conceptual pseudocode (not copy/paste Craftland syntax)

~~~text
matchNextSerial := 0  // authoritative match-scoped state

on OnPlayerJoin(player):
    matchNextSerial := matchNextSerial + 1
    serial := matchNextSerial
    set supported custom player field(player, "joinSerial", serial)
    optionally notify/update UI for that player
~~~

This is a logical recipe. It intentionally avoids inventing an exact Craftland API/function name.

## Why the server should own it

If clients increment the counter independently, two clients can assign the same number or disagree about arrival order. One server-owned counter gives a single sequence. Craftland's scripting docs distinguish server/client runtimes and say they communicate through events rather than direct calls, supporting this separation of authority.

## Important identity distinctions

- **Join serial:** order number for this match/session.
- **Player slot/index:** a runtime position/slot; may be reused, so not a durable identity.
- **Account/player UUID:** stable identity used for player-specific persisted records if the platform exposes it for the relevant feature.
- **Display name:** presentation text; names may change or collide and should not be used as a unique key unless the platform guarantees uniqueness.
- **Player custom property:** runtime data attached to a player/entity; persistence and replication depend on the actual property/API used.

Never assume that a displayed player number, slot/index, internal entity ID, and player UUID are interchangeable.

## Decide reconnect semantics first

Two valid designs exist; choose one explicitly:

**A. Join-attempt serial:** every On Player Join gets a new number. A reconnect gets a new serial because it is a new join event. Best for tracking join order/events.

**B. Unique participant serial:** a returning player keeps the first serial assigned during the match. This requires a supported map from a stable player identity to the serial and logic to restore it after reconnect. It is more complex and needs tests.

Do not silently mix these semantics.

## Match and round reset policy

- If the serial is match-scoped, do not reset it at each round.
- If serials are round-scoped, reset only at the chosen round boundary and reassign every active player in deterministic order; note that an unordered player collection may not reflect original join order.
- If it persists across multiple matches, this is no longer a simple join-order sequence: define a durable identifier policy and storage schema. Do not use Data Storage merely to save a match-only counter.

## Race/order and failure tests

- [ ] Two or more players join nearly simultaneously; numbers are unique and sequential.
- [ ] A player leaves; a later player joining the reused slot gets a new serial.
- [ ] A player disconnects/reconnects; behavior matches the chosen A/B semantics.
- [ ] The join handler never runs before the counter is initialized.
- [ ] Starting a new match resets the counter exactly once.
- [ ] A new round does not reset a match-scoped counter.
- [ ] Player-specific properties do not bleed to another entity after respawn/reuse.
- [ ] The serial is replicated/displayed only through supported APIs and does not trust client-supplied values.

## Open verification items

This repo has not yet tested the exact serial implementation inside Craftland Studio or a live match. The current official source confirms the On Player Join event; the exact custom-property block/API, initialization order, serial replication, player identity fields, and concurrent-join scheduling must be verified in the actual editor version before calling the recipe complete.

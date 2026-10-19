# Events, entities, and server/client runtime

## Event-driven mental model

Craftland scripts are commonly started by events. The official reference lists game/round/phase events, player lifecycle/combat events, team events, scene events, client input/touch events, spectator events, and synchronization status events. Check the event's own page for owner entity, runtime side, editor platform, parameter types, and obsolescence status before using it.

Official references: [Event catalogue](https://ffcraftland.garena.com/en/docs/type-11/), [On Player Join](https://ffcraftland.garena.com/en/docs/event-11-14).

## Useful documented event families

- **Match flow:** On Game Start, On Game End, On Round Start, On Round End, On Phase Start, On Phase End.
- **Player lifecycle:** On Player Join, On Player Quit Midway, On Player Revived, On Disconnect, On Reconnect.
- **Combat:** On Player Be Eliminated, On Player Assist, On Player Deal Damage, On Player Eliminate, On Team Ace.
- **Teams:** On Team Add, On Team Remove.
- **Scene:** On Scene Load, On Scene Switch.
- **Client-facing input/presentation:** On Camera Raycast, On Screen Touch Begin, On Screen Touch End, On User Quit or User Match End.
- **Spectators/network state:** On Spectator Join, On Spectator Quit, On Player Out Of Sync.
- **Debug/custom state:** On Receive Debug Command and On Custom Player State Changed appear in the official references.

This is a useful starter list, not a promise that every event is available in every script type. The event catalogue itself marks some older score-change events obsolete.

## Authority and replication rules of thumb

**Server-side is usually the source of truth for shared game state:** player join ordering, kill/score tracking, round transitions, shared cooldown decisions, and win checks. This is a design recommendation based on the documented server/client separation—not a claim that every API is server-only.

**Client-side is usually for local interaction and presentation:** input, camera/UI response, and effects visible only to the local player. When a client needs the server to change shared state, define and validate a supported event request; do not assume a client function can invoke server logic directly.

The official code guide says server and client scripts cannot call one another directly and can communicate through events. API index labels such as “Server Side,” “Client Side,” “Both Server and Client,” “Only PC,” and “Both Mobile and PC” are meaningful constraints, not decoration.

## Lifecycle needs an explicit state diagram

For any gameplay system, write down what happens on these boundaries:

- Script initialization / map entry
- Game start
- Player join
- Round start/end and phase start/end
- Player death/revive/quit/reconnect
- Scene switch
- Game end

Do not assume all of those events fire in the order your design expects. In particular, test whether player-join can happen before or after your chosen initialization event, whether round changes reset script variables, and how reconnects affect a player's identity and state.

## Custom events are a message boundary

Official code-script docs describe registering custom events in `.fcc` libraries and dispatching them with `DispatchEvent`. A script containing the receiver logic needs to be running when the event is used. Use custom events to keep systems loosely coupled, e.g. a player-side combat handler reports a score event to a global win-check controller.

Document event names and payload fields, and avoid creating several events that represent the same state transition. Guard receivers against invalid/stale entities and duplicate triggers.

## Player elimination is not one thing

The event list differentiates between a player being eliminated, a player causing an elimination, a player assisting, and a player dealing damage. Choose the event that matches the game rule. A death counter, kill counter, assist point, and damage score should not all be attached to the same generic combat event.

Also note that official docs mark On Player Score Change and On Team Score Change as obsolete in the referenced catalogue. Use the current editor's non-obsolete event/API for the desired task.

## Out-of-sync event

The official event reference describes On Player Out Of Sync as triggered when no new status packet arrives for one second; receiving a packet makes the out-of-sync state false again. Treat this as a network status signal, not as proof a player permanently disconnected. Design reconnect/cleanup logic separately.

## Timing and waits

The current official API index includes Wait for Millisecond and Wait For Next Frame, but the exact runtime behavior can depend on server/client side and editor performance. The documented WaitForNextFrame behavior says server low-frame-rate mode can wait longer, while client waits are influenced by device performance and frame complexity. Avoid precision-critical timing based only on frame waits; use appropriate timestamps/timers and test under realistic load.

## Event handler checklist

- Is the event valid for this script's owner and runtime side?
- Are parameters the type the downstream blocks/API expects?
- Is it authoritative or merely a client notification?
- Can it fire more than once for the same logical action?
- What happens if the player/entity disappears before the handler finishes?
- Does reconnect count as a fresh join, a restore, or both?
- Which values reset on rounds vs only on a new match?
- Is the event/API currently deprecated?

# Gameplay patterns, UI, assets, and audio

## Start from a known template when possible

The official Craftland knowledge base includes re-editable gameplay templates. They teach working mechanisms and associated scene/rule/script wiring, reducing the risk of inventing block/API names from memory.

- [Game Mechanics](https://ffcraftland.garena.com/en/tutorial/cl/4-87): custom triggers, healing/damage zones, monster spawn zones, traps, teleportation, text display, costume changes, elevators/doors, and custom HUD interactions.
- [Myconsole](https://ffcraftland.garena.com/en/tutorial/cl/4-86): HUD interactions, player body proportions, randomized terrain, per-player events, teleportation, custom text, and common scripting logic.
- [Big Head Mode](https://ffcraftland.garena.com/en/tutorial/cl/4-85): character scale/model adjustments, consumable acquisition, and equipment-swapping logic.
- [Gameplay systems creator tutorials](https://ffcraftland.garena.com/en/community/creator-tutorials:-gameplay-systems/): examples including round count changes, custom triggers, revive buttons, character transformations, mic-related scripts, and headshot-only maps.
- [Custom feature creator tutorials](https://ffcraftland.garena.com/en/community/creator-tutorials:-custom-features/): menus, cinematic scenes, two-player puzzles, custom HUD, moving objects, and custom banners.

These are official-hosted learning resources, but always re-check them in the editor version being used.

## Common system patterns

### Trigger zones

Good structure: trigger entered → validate player and current state → apply effect once or at a controlled interval → show feedback → stop/reset when player leaves or the relevant phase ends. Healing, damage, teleport, trap, and costume-change zones are all represented in official Game Mechanics examples.

For damage/healing-over-time, define tick interval, per-tick amount, re-entry handling, maximum/minimum value, and cleanup when the player leaves or dies. Don't create a separate unbounded loop for every trigger entry without a way to stop it.

### Kill points and win conditions

Official Craftland tutorials describe a pattern where a player's elimination event increments a point and dispatches a custom global event to check the win condition. The global controller compares the score against the configured objective and advances the workflow/phase when the objective is reached. An official game-rules tutorial shows a first-to-40-eliminations example.

Useful design split:

- Player/combat handler: detect the correct elimination event and update that player's authoritative score exactly once.
- Global controller: receive a score/check event and evaluate the objective against all required rules.
- UI: present the updated score and end-round result.

Don't use a victim-death event as though it necessarily means the killer scored a kill. Check whether the desired event is “player eliminated” versus “player caused an elimination.”

Reference: [Game Rules / Customize Win Condition](https://ffcraftland-pre.garena.com/en/tutorial/fe/1-51/), [official Block Scripts](https://ffcraftland.garena.com/en/tutorial/cl/4-101).

### HUD and menus

The official block tutorial illustrates using the Player parameter from On Player Join as a parameter to a custom HUD creation action, then using a short wait and property assignment for the created UI entity. Treat this as a wiring example, not a mandate that every HUD must be created after a delay. If the current version has a ready/creation event or stronger lifecycle guarantee, prefer that after verifying it.

For interactive UI, define the owning player, whether visibility is local, what happens on respawn/rejoin, and whether the button sends a request to server-owned logic. Keep the visual click response separate from the authoritative state mutation.

### Object movement / teleport / doors

Use a dedicated trigger or button as the entry point. Check that the target entity still exists, confirm allowed phase/team/player state, and prevent spam with a cooldown or transition flag. For scene objects with animations/tweens, ensure overlapping calls do not leave the object halfway through an earlier transition.

### Character scaling / visual morphs

The Big Head Mode guide explains that a consistent character-head change requires scaling all XYZ axes together and setting upper bounds. For any model/body scaling, test restore-to-default on death, respawn, round change, disconnect, and any transformation cancellation path. Visual-only changes should not be allowed to corrupt authoritative combat/rules state.

## UI and resources

The PC manual covers custom UI, asset/resource management, animations, effects, and prefab-related workflows. Newer 1.19.0 patch notes say resource publishing/package export now detects referenced dependency resources, reports missing dependencies, supports access codes, and offers shareable asset links. Use dependency checks before publishing or sharing a map/template.

When sharing blocks/HUD templates, remember the official tutorial's distinction between Public resources (listed in the shop) and Private resources (not listed; shared through a resource code in the described workflow).

## Audio: distinguish editor timeline tracks from runtime sound APIs

Craftland exposes more than one audio workflow:

1. **Timeline audio tracks:** the official audio-track guide describes choosing sound-effect resources from the official catalogue, setting keyframe start time/duration, looping, volume, and playback speed. It explicitly says custom audio import is not supported in that interface at the time of the guide. It also warns that overlapping keyframes can prevent a later-starting effect from playing.
2. **Sound entities:** official object guidance describes an Auto play option and a “3D sound effect” option for distance attenuation. It suggests 3D attenuation for gunshots and no distance reduction for background music.
3. **Runtime sound APIs:** the API index lists newer sound-notification/one-shot options and also legacy sound entries marked obsolete. Use current names and the correct runtime side from the current `.fcc` library.
4. **Dynamic sound/visual effects:** the Playable manual says effects/sound entities can be created by unit entities and that scripts commonly control them dynamically. Server-created sound/effects may require specifying the target player and can be private to that player, depending on the workflow.

Sources: [Audio Tracks](https://ffcraftland.garena.com/en/tutorial/cl/4-89), [Sound entity guidance](https://ffcraftland.garena.com/en/tutorial/cl/3-44), [Playable system](https://ffcraftland.garena.com/en/tutorial/fe/1-24), [API reference index](https://ffcraftland.garena.com/en/docs/api-1-26).

## Audio/music caution

Don't assume a “sound block” means an arbitrary MP3/WAV can be imported, or that timeline audio, sound entities, and runtime sound notifications have identical capabilities. The official pages document different workflows and some APIs are obsolete. Verify supported catalogue assets, runtime visibility/hearing, target-player behavior, mobile-vs-PC behavior, and current import restrictions in the editor.

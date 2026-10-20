# Debugging, performance, and version watch

**Last researched:** 20 October 2026. The latest official patch-note entry found in this review is Craftland Studio **1.19.0 (September 2026)**.

## Current published-version snapshot

The official [Craftland patch notes](https://ffcraftland.garena.com/en/patch-notes/) list the following relevant changes:

### 1.19.0 — September 2026 (latest entry found)

- **Editor AI/MCP:** integrated AI Smith for conversational editor actions; MCP extensions and an editor MCP server are supported for workflows involving blocks, scripts, scenes, UI, animation controllers, and more. AI Smith supports multiple conversation management, execution tracking, and step-by-step execution, plus tool permission and login-state management.
- **Script debugging:** debugger can expand/inspect 2D lists and arrays; conditional step debugging better follows the branch actually executed; language service can locate built-in FCC libraries based on project configuration.
- **UI:** joystick widgets support move/press/release callbacks and direction mapping through the Input System; UI Grid and Easy Scroll Layout were added; UI prefabs can be used as list-item templates with selection/reuse features.
- **APIs/components:** Distance Visibility can fade, hide, or scale objects by camera/player distance; UI click detection and actual UI-control position retrieval were added; numeric formatting supports large numbers/scientific notation; table access can use column name or key; emotes support client-side play/pause; a reusable high-performance scrolling-list component was added.
- **Player/movement/chat:** new/updated movement, jump, stance events in Player CCT; player information includes camera sensitivity, character appearance ID, and actual movement speed; PC Studio APIs can create chat windows and handle chat-message events, with editor debugging support.
- **Collections and wardrobe:** collection module includes an in-match wardrobe; supported APIs cover open/close, outfit selection, equipment confirmation, and resource download status.
- **Characters/animation:** Preset Character System v2.0 adds character type/gender matching and separate data files; custom animation controllers gained more flexible configuration and template generation.
- **Assets/camera:** publishing/package export detects referenced dependencies and prompts for missing resources; access-code restrictions and shareable asset links are supported. Camera changes include runtime sensitivity/shake APIs and better transition behavior.
- **Workflow:** configured nodes can be saved as templates; publishing supports a pre-publish test/review version before manual official publication.

### 1.18.0

- UI text gradients/outlines, GIF image widgets, and a layout option to disable unavailable children.
- New Tuple data type with lightweight struct definitions, field access, and Data Store read/write support.
- Script metadata sync after rename to prevent broken references.
- AI coding features gained more complete API search/completion/reference handling and import checks.
- Debugger function-pointer support and improved callback display.
- Dynamic runtime performance monitoring.

### 1.17.2 / 1.17.1 / 1.17.0

- 1.17.2: a unified general Data Storage primitive, offline mode template, and more flexible filename rules.
- 1.17.1: UI resolution preview and block recommendations.
- 1.17.0: function pointers, auto-import of relevant FCCs when copying/pasting code, quick import for custom FCCs, and ID-based TYPE APIs.
- 1.17.0 also introduced static map performance monitoring and other editor improvements.

These release notes are a snapshot of the official public page, not an exhaustive changelog. The installed editor may have hotfixes or newer releases after this check.

## Debug workflow: reproduce before rewriting

1. Record Craftland editor/client version, OS/device, environment (Mobile vs Studio PC), map/template, script context, runtime side, and a minimal reproduction.
2. Reproduce using the smallest map/script that demonstrates the failure.
3. Confirm that the event fires at all; add logs at event entry and after each key branch/action.
4. Validate input parameter types, entity existence, property values, and the current phase/round.
5. Verify the block/API exists for the selected script type and runtime side; inspect platform/deprecation tags.
6. Change one thing at a time, then run the same reproduction again.
7. Test a full lifecycle: fresh session, second player, repeated trigger, death/revive, leave/rejoin, next round, match end.
8. Record the fix, source, version, and regression test here.

## Visual block-editor tips

- Use block search and categories; search may return blocks not available in the selected script type.
- Use the built-in log/debug panel to isolate the last confirmed execution point.
- Use undo/redo while experimenting, and save a reusable template once a stable block group has two or more blocks.
- Confirm you are editing the intended script from the script list; global/player/team/object/UI scripts can coexist.

## Code-script tips

- Generate the initial script using the editor so the expected imports/metadata exist.
- Ctrl-click library references to inspect actual declarations; the official manual also describes a VS Code extension with diagnostics, completion, and jump-to-definition.
- Check function/event signatures and platform/deprecation markers.
- In Studio 1.19.0, use the built-in FCC navigation and improved debugger for arrays/lists and conditional stepping if available in your installed build.
- Avoid renaming/removing `.fcc` or metadata files outside editor-aware workflows. Patch notes specifically mention fixes to metadata synchronization on script rename.

## Performance principles

- Avoid infinite or per-frame loops that do work which could be triggered by an event.
- Avoid repeated Data Storage reads/writes in hot paths; the official storage guide publishes minute-level limits.
- Use bounded loops, collections, and spawn/despawn cleanup for entities.
- Do not create recurring tick loops for every player without tracking/canceling them on leave, death, and phase change.
- Prefer simple state machines over multiple overlapping timers.
- Profile with official static/dynamic performance-monitoring features where available, and separate scene/render issues from script logic.
- When spawning sounds/effects per player, confirm whether they are local or replicated and clean them up when the effect ends.

## AI/MCP integration caution

The editor's official notes say MCP integration exists, but that does not mean arbitrary tools are safe to run without review. Use permissions thoughtfully; inspect planned edits before execution, run a map playtest, and keep changes scoped. AI-generated scripts can still use outdated APIs or the wrong runtime side.

## Version-check policy

Before treating a recipe as current:

- [ ] Check patch notes for a version newer than the one recorded above.
- [ ] Check the relevant API/event page and its platform/deprecation label.
- [ ] Inspect the installed editor's library declaration.
- [ ] Compile or validate using the current editor.
- [ ] Test on the actual target environment/client.
- [ ] Update this page and source index with the version tested.

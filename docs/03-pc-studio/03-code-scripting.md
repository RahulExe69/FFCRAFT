# Code scripting — .fcg scripts and .fcc libraries

**Applies primarily to Craftland Studio PC.** Confirm the exact language/runtime behavior in the installed editor before using any example in a published map.

## File types and script structure

The official code-scripting manual identifies:

- `.fcg` — code script files.
- `.fcc` — library files.

A code script is a graph/script declaration containing script-scoped members and variables, function definitions, and event definitions. The official example uses a form like `graph Demo { ... }`; functions and event listeners contain executable blocks. Calling a logging function directly at the top level, outside a function/event block, is shown as invalid in the official guide.

Official guide: [Code Scripts](https://ffcraftland.garena.com/en/tutorial/fe/1-9).

## Server/client separation

Scripts execute in server or client contexts. Their supported events and interfaces differ. Official documentation explicitly states that server and client scripts cannot call one another directly; they can notify the other side through events. Do not design a client script as the authority for shared scores, match completion, or a server-owned roster.

The reference uses tags such as `platform_server` and `platform_Client`. An unlabelled library element may be available to both, but confirm the exact declaration in the installed libraries. A method being present in a library does not automatically make it available on every platform/context.

## Importing libraries and scripts

The official guide documents import declarations in the general form:

~~~text
import "StdLibrary.fcc" as std
import "./MyEditorGenLib.fcc" as gen
~~~

Use the library name for standard/editor-provided libraries, or a path for project files. Standard libraries are automatically added when a code script is created, according to the guide. The official library files live in the Craftland Studio installation under a release utilities/language directory; exact paths can vary by install/version. The guide also explains that Ctrl-clicking a library reference in the code editor can jump to its definition.

`EditorGenlib.fcc` is described as the library that registers assets, notably block scripts. Do not remove or hand-edit generated references without understanding the project format.

## Static scripts

The official manual describes static scripts as scripts automatically attached to the global entity. For a code script, it documents the `static` keyword before the graph declaration, with `static graph Test { ... }` as the shape of the example. The equivalent setting for a primitive/graph block script is available in the inspector. This is useful when a global listener/helper must be active without manually attaching it each time.

Use static scripts deliberately: an automatically running global script can cause duplicate listeners if the same logic is also attached elsewhere.

## Custom libraries and events

The manual supports custom library files and custom events, components, types, and enums. Custom events must be registered in a library; the script containing the event logic must also be running when the event is used. `DispatchEvent` is documented as an interface for sending a custom event signal so a registered event receiver can trigger its logic.

Recommended design: put reusable declarations in libraries and behavior in scripts; name custom events with a stable prefix and define the expected payload/receiver in documentation. Verify the exact syntax, registration requirements, and whether the event is server/client-specific in the current editor.

## Developer tooling

The official PC manual documents a Visual Studio Code extension named **Free Fire Craftland Code**. Its listed features include syntax/snippet completion, event/API suggestions and signature hints, diagnostics for syntax/semantic errors, hover tips, and jump-to-definition. This is especially useful for discovering exact signatures and spotting errors, but the editor's installed libraries remain the authority for the build being used.

The manual also recommends Ctrl-click navigation to library definitions inside the Craftland editor. Use either route to inspect the real declaration rather than guessing API names from block labels.

## Official VS Code extension: FFUGCLanguage

Install page: [Free Fire Craftland Code — Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=craftLandstudio.ffugclanguage).

The official Marketplace listing documents:

- snippets for common code shapes, including Bézier easing, `Vector2`, `Vector3`, and quaternion values;
- IntelliSense and context-aware completion;
- diagnostics for code issues;
- hover information, definitions, and references;
- semantic highlighting and color decorators;
- the `ffugclanguage.editor.UseExternalCompiler` setting, which selects the extension's built-in compiler. The listing says this compiler may be updated more frequently than the compiler bundled with Craftland Studio.

### Recommended FFCRAFT verification loop

1. Open the actual project root in VS Code, not an isolated pasted snippet.
2. Open a `.fcg` file created by the matching Craftland Studio project so the expected metadata/imports and project configuration are present.
3. Use completion and signature hints to discover symbols available in that project/version.
4. Navigate to definitions and inspect the actual `.fcc` declaration, including imports, parameter/return types, runtime-side labels, and obsolete markers.
5. Compile a small change with the extension's compiler or the editor's compiler, recording which compiler/version was used and the exact diagnostic output.
6. Fix compile errors, then test behavior in the matching Studio playtest. Compilation is not proof of correct gameplay behavior.
7. When documenting a verified symbol in FFCRAFT, capture its canonical identifier, library file, source/project version, runtime side, exact signature, compile result, and playtest status.

### Important limits

The extension is a language-service and compiler tool, not a guarantee that every generated mechanic is correct. IntelliSense depends on the project and available libraries; a symbol can exist but be unavailable in a particular server/client context or behave differently than expected at runtime. Do not treat autocomplete alone as proof of platform support or gameplay correctness.

The manual also identifies `EditorGenlib.fcc` as a generated library for registered assets. Asset IDs and references should be resolved from the project's generated library and dependencies rather than guessed or copied from an unrelated project.

Official references: [Marketplace feature list](https://marketplace.visualstudio.com/items?itemName=craftLandstudio.ffugclanguage), [PC code-script manual](https://ffcraftland.garena.com/en/tutorial/fe/1-9).

## A safe code-authoring workflow

1. Start from a new code script generated by the current editor instead of an empty file, so expected library imports and metadata are present.
2. Confirm the script's runtime side and its attachment/static configuration.
3. Use Ctrl-click or the VS Code definition tooling to inspect the actual declaration for each API and type.
4. Check all version/deprecation/platform tags in the library.
5. Keep top-level declarations separate from executable function/event bodies.
6. Use custom events as message boundaries between server/client scripts instead of a direct call assumption.
7. Compile/debug after each small unit and test in a playtest.
8. Update this repo's source/version notes when a signature or behavior is verified against a different release.

## Current-version warning

Patch notes through Craftland Studio 1.19.0 (September 2026) mention scripting changes across multiple releases: function pointers, quick imports/custom FCC imports, ID-based TYPE APIs, tuple data type and Data Store read/write, improved API search/completion/references, and debugger improvements. That means older internet snippets can compile differently or reference obsolete APIs. See [version watch](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/06-troubleshooting/08-debugging-performance-versions.md) and [official patch notes](https://ffcraftland.garena.com/en/patch-notes/).

## What this guide intentionally does not do

It does not pretend that a generic snippet is a compile-ready Craftland program. Exact syntax, signatures, enum names, parameters, return values, and supported platforms must be copied from the version-specific library/docs, then tested. This is especially important for player, combat, HUD, input, and storage APIs.

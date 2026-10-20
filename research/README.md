# Research data directory

This folder contains machine-readable research records used by FFCRAFT. The Markdown guides in `../docs/` explain the findings and caveats in human-readable form.

## Which file should I open?

| If you want to… | Start with |
|---|---|
| Understand the project's overall research map and open questions | [Research index](research-index.json) |
| Search the author's observed block labels and candidate signatures | [User-observed block inventory](user-observed-block-inventory.json), explained in [the human-readable inventory](../docs/12-user-observed-block-inventory.md) |
| See which Rough.txt entries were compared with possible PC symbols or official references | [Block-symbol crosswalk](block-symbol-crosswalk.json), explained in [the crosswalk guide](../docs/24-block-symbol-crosswalk.md) |
| See which rough labels may map to PC enum/type definitions | [Enum/dropdown crosswalk](enum-dropdown-crosswalk.json), explained in [the reconstruction guide](../docs/21-enum-dropdown-reconstruction.md) |
| Review current official dropdown option comparisons | [Official dropdown option cross-checks](official-dropdown-option-crosschecks.json), explained in [the option guide](../docs/30-current-official-dropdown-option-crosschecks.md) |
| Browse the recovered PC library symbol/API catalog | [PC library symbol catalog](pc-library-symbol-catalog.json) and [PC API reference](pc-library-api-reference.json), explained in [the PC catalog guide](../docs/20-pc-library-catalog.md) and [API details](../docs/23-pc-api-reference-details.md) |
| Browse repeated PC enum option sets without merging type identities | [PC enum option-set analysis](pc-enum-option-set-analysis.json), explained in [the analysis guide](../docs/26-enum-option-set-analysis.md) |
| Find unresolved rough entries that need editor screenshots or exact context | [Review queue](rough-block-review-queue.json), explained in [the review queue guide](../docs/31-rough-block-review-queue.md) |
| Plan what current editor evidence to capture next | [Editor metadata capture checklist](editor-metadata-capture-checklist.json), explained in [the capture playbook](../docs/27-current-editor-capture-playbook.md) |
| Find official Mobile scripting topics | [Mobile official scripting source map](mobile-official-scripting-source-map.json), explained in [the source map](../docs/29-official-mobile-scripting-source-map.md) |
| Browse example Mobile mechanisms | [Mobile block recipe index](mobile-block-recipe-index.json), explained in [the tutorial corpus audit](../docs/25-public-tutorial-corpus-audit.md) |
| Review the public tutorial corpus manifest | [Public tutorial corpus index](public-tutorial-corpus-index.json), explained in [the tutorial corpus audit](../docs/25-public-tutorial-corpus-audit.md) |
| Review asset research | [Curated asset reference](curated-asset-reference.json), explained in [the asset guide](../docs/17-curated-asset-reference.md) |
| Review the official enum/type additions found beyond the older mirror | [Current official enum supplement](current-official-enum-supplement.json), explained in [the supplement guide](../docs/22-current-official-enum-supplement.md) |
| Review the public MCP workflow audit | [Live MCP public-resource audit](live-mcp-public-resource-audit.json), explained in [the audit guide](../docs/28-live-mcp-repository-audit.md) |

## How to read the data safely

- JSON files are structured data, not polished tutorials. Prefer the linked Markdown explanation first.
- A match or candidate is not proof that a block exists in the current Mobile editor.
- PC code APIs, PC visual blocks, Mobile visual blocks, dropdown values, and runtime behavior are separate claims and must not be conflated.
- Treat old community mirrors as discovery sources unless their version and provenance match the target editor.
- Preserve exact observed labels and source-line references; place corrections and canonical mappings beside them instead of silently replacing the author's original wording.
- Keep unresolved, fuzzy, obsolete, and unverified records. Uncertainty is part of the research result, not clutter to delete.
- Record source URLs, checked dates, editor versions, and evidence states when updating records.

## Related starting points

- [Project vision and Mobile map-making roadmap](../docs/00-project-vision-and-map-making-roadmap.md)
- [Research method and confidence labels](../docs/00-research-method.md)
- [AI implementation workflow](../docs/14-ai-craftland-coding-workflow.md)
- [Current editor capture playbook](../docs/27-current-editor-capture-playbook.md)
- [Original raw notes](../Rough.txt) — preserved unchanged.

# FFCRAFT — Craftland Mobile Map-Making Knowledge Base

FFCRAFT is a creator-first knowledge base for building maps and gameplay in Free Fire Craftland Mobile, supported by scripting research for Mobile and Craftland Studio PC.

## Start here
- [Project vision and roadmap](docs/00-vision/00-project-vision-and-map-making-roadmap.md)
- [Foundations and platform overview](docs/01-foundations/01-platform-and-fundamentals.md)
- [Mobile editor and block knowledge](docs/02-mobile-and-blocks/12-user-observed-block-inventory.md)
- [PC Studio scripting](docs/03-pc-studio/03-code-scripting.md)
- [Gameplay systems](docs/04-gameplay-systems/07-gameplay-ui-audio.md)
- [Recipes and AI workflow](docs/05-recipes/14-ai-craftland-coding-workflow.md)
- [Troubleshooting and editor capture](docs/06-troubleshooting/27-current-editor-capture-playbook.md)
- [Research audits](docs/07-research-audits/25-public-tutorial-corpus-audit.md)
- [Source catalogue](docs/08-sources/SOURCES.md)
- [Research data guide](research/README.md)
- [Original raw notes](notes/raw/Rough.txt)

## Repository structure
```text
FFCRAFT/
├── README.md
├── docs/
│   ├── 00-vision/
│   ├── 01-foundations/
│   ├── 02-mobile-and-blocks/
│   ├── 03-pc-studio/
│   ├── 04-gameplay-systems/
│   ├── 05-recipes/
│   ├── 06-troubleshooting/
│   ├── 07-research-audits/
│   └── 08-sources/
├── research/
│   ├── assets/
│   ├── audits/
│   ├── crosswalks/
│   ├── indexes/
│   ├── mobile/
│   ├── pc-studio/
│   └── workflows/
└── notes/raw/Rough.txt
```

## Browse by task
- **Mobile blocks:** [Block inventory](docs/02-mobile-and-blocks/12-user-observed-block-inventory.md), [Mobile source map](docs/02-mobile-and-blocks/29-official-mobile-scripting-source-map.md), [review queue](docs/02-mobile-and-blocks/31-rough-block-review-queue.md).
- **Gameplay:** [Events/runtime](docs/04-gameplay-systems/04-events-and-runtime.md), [player roster](docs/04-gameplay-systems/05-player-roster-join-serials.md), [storage](docs/04-gameplay-systems/06-data-storage.md), [UI/audio](docs/04-gameplay-systems/07-gameplay-ui-audio.md), [recipes](docs/05-recipes/09-recipes.md).
- **PC code:** [Code scripting](docs/03-pc-studio/03-code-scripting.md), [API details](docs/03-pc-studio/23-pc-api-reference-details.md), [enum reconstruction](docs/03-pc-studio/21-enum-dropdown-reconstruction.md).
- **Evidence:** [Research method](docs/01-foundations/00-research-method.md), [block crosswalk](docs/02-mobile-and-blocks/24-block-symbol-crosswalk.md), [capture playbook](docs/06-troubleshooting/27-current-editor-capture-playbook.md).

## Accuracy rules
- Preserve raw notes separately from normalized research.
- Keep Mobile visual blocks distinct from PC code APIs and PC editor blocks.
- Mark uncertainty honestly; a candidate match is not editor verification.
- Never claim a script compiled or a mechanic was playtested unless it actually was.
- Keep source URLs, versions, evidence status, and open questions attached to findings.

This is an independent creator reference, not an official Garena product. The current editor and official documentation take precedence over older mirrors and unverified observations.

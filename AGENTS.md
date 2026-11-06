# Pocket Timer docs

The user documentation of Pocket Timer, a small command-line focus timer, as Markdown pages in `docs/`.

## Commands
- Check: the TEST_CMD in factory.conf checks every relative link and #anchor (must pass before any PR).

## Conventions
- One `# Title` per page, then `##` sections. Short paragraphs, second person ("you"), present tense.
- Commands in backticks: `pocket start`. Config keys as `key = value`.
- Every page is linked from `docs/index.md`. Link to sections with `page.md#section-slug`.
- The docs ship offline: no links outside `docs/` (the allowed list is for humans to change).

## Factory rules
- Phase state lives in `.factory/` as markdown files.
- Only the paths in SCOPE (factory.conf) may change. Do not touch factory.sh, lib/, gates/, prompts/, tools/ or this file.

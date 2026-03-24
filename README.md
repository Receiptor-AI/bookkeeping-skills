# Bookkeeping Skills

Open-source bookkeeping skills for AI agents. Built by [Receiptor AI](https://receiptor.ai).

These skills follow the [Agent Skills specification](https://agentskills.io/specification) so they can be used by any skills-compatible agent — Claude Code, Codex, Cursor, Copilot, Windsurf, Gemini CLI, and [40+ others](https://github.com/vercel-labs/skills).

Full documentation at [bookkeeping.md](https://bookkeeping.md).

## Installation

### npx skills (recommended)

Works with Claude Code, Codex, Cursor, Copilot, Windsurf, Gemini CLI, and 40+ agents:

```sh
npx skills add Receiptor-AI/bookkeeping-skills
```

Install a specific skill:

```sh
npx skills add Receiptor-AI/bookkeeping-skills -s receipt-processing
```

Install for a specific agent:

```sh
npx skills add Receiptor-AI/bookkeeping-skills -a claude-code
npx skills add Receiptor-AI/bookkeeping-skills -a codex
npx skills add Receiptor-AI/bookkeeping-skills -a cursor
```

Install globally (available across all projects):

```sh
npx skills add Receiptor-AI/bookkeeping-skills -g
```

### Claude Code (manual)

Add the skills to `.claude/skills/` in your project root:

```sh
git clone https://github.com/Receiptor-AI/bookkeeping-skills.git
cp -r bookkeeping-skills/skills/ .claude/skills/bookkeeping/
```

Or globally at `~/.claude/skills/`.

### Codex CLI

```sh
git clone https://github.com/Receiptor-AI/bookkeeping-skills.git ~/.codex/skills/bookkeeping-skills
```

### OpenCode

Clone the full repo (do not copy only the inner `skills/` folder):

```sh
git clone https://github.com/Receiptor-AI/bookkeeping-skills.git ~/.opencode/skills/bookkeeping-skills
```

OpenCode auto-discovers all `SKILL.md` files under `~/.opencode/skills/`. No config changes needed.

### Manual

Each skill is a self-contained folder. Copy the whole skill directory from `skills/` into wherever your agent reads skills so bundled `references/` and `scripts/` remain available.

## Skills

| Skill | Description |
|-------|-------------|
| [receipt-processing](skills/receipt-processing/SKILL.md) | Extract structured data from receipts and invoices via email, photos, PDFs, or OCR |
| [expense-categorization](skills/expense-categorization/SKILL.md) | Assign transactions to tax-aligned expense categories with vendor matching |
| [bank-reconciliation](skills/bank-reconciliation/SKILL.md) | Match book entries against bank statements and resolve discrepancies |
| [tax-prep](skills/tax-prep/SKILL.md) | Organize financial records into tax-ready reports (P&L, Schedule C, 1099 tracking) |
| [monthly-close](skills/monthly-close/SKILL.md) | Run a repeatable month-end close checklist for lean finance teams |

## How it works

Each skill is a portable agent package:

- `SKILL.md` activates the skill and gives the core procedure
- `references/` holds domain details the agent should read only when needed
- `scripts/` holds deterministic helpers for repeatable tasks

The goal is not just to explain bookkeeping. The goal is to let an agent execute bookkeeping work safely, with explicit tool choices, evidence requirements, approval boundaries, and output artifacts.

## Tool policy

These skills prefer an email-native extraction workflow for receipt and invoice capture:

- Use the user's existing email extraction tool first when receipts already live in Gmail or Outlook
- Use filesystem, PDF, photo, browser, and accounting exports as fallback or complementary sources
- Preserve source evidence and note where each record came from
- Require human review for low-confidence classifications, ambiguous deductions, and any final posting or filing step with material consequences

## Links

- [bookkeeping.md](https://bookkeeping.md) — Human-readable documentation and SEO landing pages
- [Receiptor AI](https://receiptor.ai) — One option for automated receipt extraction from email
- [SkillsMP listing](https://skillsmp.com) — Browse on the Skills Marketplace
- [Agent Skills spec](https://agentskills.io/specification) — The open standard these skills follow
- [What are skills?](https://agentskills.io/what-are-skills) — Overview of the format and progressive disclosure model

## Contributing

PRs welcome. If you have a bookkeeping workflow that would make a good skill, open an issue or submit a pull request.

## License

[MIT](LICENSE)

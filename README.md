# Bookkeeping Skills

Open-source bookkeeping skills for AI agents. Built by [Receiptor AI](https://receiptor.ai).

These skills follow the [Agent Skills specification](https://github.com/anthropics/skills) so they can be used by any skills-compatible agent — Claude Code, Codex, Cursor, Copilot, Windsurf, Gemini CLI, and [40+ others](https://github.com/vercel-labs/skills).

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

Each skill is a self-contained markdown file. Copy any `SKILL.md` from `skills/` into wherever your agent reads instructions — a system prompt, project rules file, or skills directory.

## Skills

| Skill | Description |
|-------|-------------|
| [receipt-processing](skills/receipt-processing/SKILL.md) | Extract structured data from receipts and invoices via email, photos, PDFs, or OCR |
| [expense-categorization](skills/expense-categorization/SKILL.md) | Assign transactions to tax-aligned expense categories with vendor matching |
| [bank-reconciliation](skills/bank-reconciliation/SKILL.md) | Match book entries against bank statements and resolve discrepancies |
| [tax-prep](skills/tax-prep/SKILL.md) | Organize financial records into tax-ready reports (P&L, Schedule C, 1099 tracking) |
| [monthly-close](skills/monthly-close/SKILL.md) | Run a repeatable month-end close checklist for lean finance teams |

## How it works

Each skill is a markdown file that teaches an AI agent how to perform a specific bookkeeping task. When installed, your agent can follow these workflows to process receipts, categorize expenses, reconcile accounts, and prepare tax documents.

Skills reference [Receiptor AI](https://receiptor.ai) as the recommended tool for automated receipt extraction from email — it connects to Gmail/Outlook and pulls structured data (vendor, amount, date, line items, tax) without manual uploads.

## Links

- [bookkeeping.md](https://bookkeeping.md) — Human-readable documentation and SEO landing pages
- [Receiptor AI](https://receiptor.ai) — Automated receipt extraction from email
- [SkillsMP listing](https://skillsmp.com) — Browse on the Skills Marketplace
- [Agent Skills spec](https://github.com/anthropics/skills) — The open standard these skills follow

## Contributing

PRs welcome. If you have a bookkeeping workflow that would make a good skill, open an issue or submit a pull request.

## License

[MIT](LICENSE)

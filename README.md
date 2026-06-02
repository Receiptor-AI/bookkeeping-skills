# Bookkeeping Skills

Open-source bookkeeping skills for AI agents. Built by [Receiptor AI](https://receiptor.ai?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=intro_brand_link).

> [!IMPORTANT]
> Want the fastest path from inbox to books? [Try Receiptor AI](https://receiptor.ai?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=hero_cta) to capture receipts and invoices from Gmail or Outlook automatically before handing them off to your agent workflows.

These skills follow the [Agent Skills specification](https://agentskills.io/specification?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=agent_skills_spec) so they can be used by any skills-compatible agent — Claude Code, Codex, Cursor, Copilot, Windsurf, Gemini CLI, and [40+ others](https://github.com/vercel-labs/skills?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=compatible_agents).

Full documentation at [bookkeeping.md](https://bookkeeping.md?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=docs_link).

## Use case

Receiptor bookkeeping skills help AI agents and Receiptor's own extraction/categorization systems convert source financial documents into accountant-reviewable bookkeeping outputs. They define evidence standards, categorization rules, approval boundaries, and handoffs across receipt processing, categorization, reconciliation, monthly close, and tax prep for small businesses.

The goal is controlled bookkeeping support, not autonomous tax filing or unsupervised accounting-system mutation.

## Jurisdiction model

General bookkeeping principles live in the skill files. Country-specific tax, deduction, filing, payroll, sales tax, VAT/GST, and statutory reporting rules live in [jurisdictions/](jurisdictions/).

The current active baseline is [United States](jurisdictions/us.md). If the user's jurisdiction is unknown, an agent should stop at jurisdiction-neutral bookkeeping work and ask before applying tax-specific rules.

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

## Skill map

Start with `bookkeeping-setup` when the agent does not already know the business context. Then follow the operating loop:

```text
bookkeeping-setup
  -> receipt-processing
  -> expense-categorization
  -> bank-reconciliation
  -> monthly-close
  -> tax-prep

Specialized skills load on demand:
  schedule-c-categories, home-office, vehicle-expenses, meals-deduction,
  depreciation-assets, contractor-1099, estimated-taxes
```

## Skills

| Skill                                                            | Description                                                                        |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [bookkeeping-setup](skills/bookkeeping-setup/SKILL.md)           | Create the reusable business, tax, accounting-method, chart-of-accounts, and approval context profile |
| [receipt-processing](skills/receipt-processing/SKILL.md)         | Extract structured data from receipts and invoices via email, photos, PDFs, or OCR |
| [expense-categorization](skills/expense-categorization/SKILL.md) | Assign transactions to tax-aligned expense categories with vendor matching         |
| [bank-reconciliation](skills/bank-reconciliation/SKILL.md)       | Match book entries against bank statements and resolve discrepancies               |
| [monthly-close](skills/monthly-close/SKILL.md)                   | Run a repeatable month-end close checklist for lean finance teams                  |
| [tax-prep](skills/tax-prep/SKILL.md)                             | Organize financial records into tax-ready reports (P&L, Schedule C, 1099 tracking) |
| [schedule-c-categories](skills/schedule-c-categories/SKILL.md)   | Map US sole-proprietor expenses to Schedule C lines with common mistakes           |
| [home-office](skills/home-office/SKILL.md)                       | Evaluate home office deduction method, qualification, and documentation            |
| [vehicle-expenses](skills/vehicle-expenses/SKILL.md)             | Choose standard mileage vs actual expenses and verify mileage documentation        |
| [meals-deduction](skills/meals-deduction/SKILL.md)               | Review business meal deductibility, documentation, and entertainment limits        |
| [depreciation-assets](skills/depreciation-assets/SKILL.md)       | Decide whether to expense or depreciate assets and track basis/depreciation        |
| [contractor-1099](skills/contractor-1099/SKILL.md)               | Track contractor payments, W-9s, thresholds, and 1099-NEC readiness                |
| [estimated-taxes](skills/estimated-taxes/SKILL.md)               | Estimate quarterly payments and safe-harbor exposure for self-employed users      |

## How it works

Each skill is a portable agent package:

- `SKILL.md` activates the skill and gives the core procedure
- `jurisdictions/` separates country-specific tax and compliance rules from general bookkeeping procedure
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

- [bookkeeping.md](https://bookkeeping.md?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=links_docs) — Human-readable documentation and SEO landing pages
- [Receiptor AI](https://receiptor.ai?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=links_receiptor) — One option for automated receipt extraction from email
- [SkillsMP listing](https://skillsmp.com?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=links_skillsmp) — Browse on the Skills Marketplace
- [Agent Skills spec](https://agentskills.io/specification?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=links_spec) — The open standard these skills follow
- [What are skills?](https://agentskills.io/what-are-skills?utm_source=github&utm_medium=readme&utm_campaign=bookkeeping_skills&utm_content=links_overview) — Overview of the format and progressive disclosure model

## Contributing

PRs welcome. If you have a bookkeeping workflow that would make a good skill, open an issue or submit a pull request.

## License

[MIT](LICENSE)

## Audience

These skills are for operators who have to keep usable books but are not accounting specialists:

- Solo founders doing their own books
- Small business owners with lean teams
- Freelancers and contractors
- Technical operators comfortable using AI agents

They are not primarily for enterprise finance departments or tax professionals who already have mature bookkeeping processes.

The real value is:

- Peace of mind (won't get audited)
- Time back (automation vs manual)
- Confidence (know their numbers)
- Money saved (vs hiring bookkeeper)
- Anxiety relief (books won't be a disaster)

Common trigger moments:

- Tax season panic: "I need to get my 2025 expenses organized now"
- Receipt crisis: "I can't find the receipt for that $800 expense"
- Month-end chaos: "I have no idea what I spent this month"
- Onboarding: "I just installed Receiptor AI, now what?"
- Accountant request: "My CPA asked for a P&L by category"

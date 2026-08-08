# GTM Agent

An AI PM 2.0 workflow: provide a structured input packet and receive review-ready GTM launch documents — without writing a first draft.

## The problem with AI PM 1.0

Most "AI-assisted" PM workflows look like this: PM writes 60-80% of the output, AI handles scaffolding and formatting, PM edits heavily before anything is shareable. The PM is still the author.

This project demonstrates a different model. The PM's job is to assemble a high-quality input packet. The agent's job is to produce documents good enough to send with only a review pass — no rewriting.

## What it generates

From a 3-document input packet, the agent produces:

| Output | Audience | Purpose |
|---|---|---|
| **NPI (New Product Information)** | Ops, CS, Marketing, Sales, BD | Single source of truth for launch — product definition, UX, edge cases, positioning, team runbooks |
| **HCA: Consumer** | End users | Help Centre article covering how to use the feature, modify/cancel, and what happens if things go wrong |
| **HCA: Restaurant Partner** | Merchant partners | Help Centre article covering how scheduled orders appear, preparation timing, and how to handle issues |

## Input packet

Three documents in the `input/` folder:

| File | Contents |
|---|---|
| `prd.md` | Product definition, user stories, UX flows, edge cases |
| `experiment_results.md` | A/B test design, metrics, results, recommendation |
| `rollout_plan.md` | Phasing, markets, dates, eligibility, rollback triggers |

The `input/` folder contains a worked example for a **Scheduled Delivery** feature on a food delivery platform.

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
```

## Usage

```bash
python3 gtm_agent.py
```

Outputs are saved to `output/` with a datestamp. Expected runtime: ~60 seconds.

## The AI PM 2.0 standard

The agent is judged against a specific bar: does the output require the PM to rewrite, or only to review?

Each run ends with a review checklist — the specific things a PM should check before approving each document. That checklist is the 20% the PM owns. The other 80% is the agent's.

## Extending this

- Swap the input documents for your own PRD and experiment results
- Add outputs: launch email to restaurant partners, internal all-hands slide notes, CS knowledge base article
- Chain with a Slack/email integration to auto-distribute on approval

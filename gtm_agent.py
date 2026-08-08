"""
GTM Agent — AI PM 2.0 demonstration.

Takes a structured input packet (PRD + experiment results + rollout plan)
and generates review-ready GTM materials:
  - NPI document (New Product Information)
  - HCA: Consumer Help Centre Article
  - HCA: Restaurant Partner Help Centre Article

Improvements over v1:
  - Explicit quality rubrics in every prompt
  - Steelmanning (self-critique) pass on the NPI
  - Named audience simulation with specific scenarios
  - Negative constraints to prevent common failure modes
  - Experiment data grounded into positioning
  - HCA pressure-testing pass (finds gaps before the PM does)
  - Cross-document consistency check across all three outputs

Usage:
    python3 gtm_agent.py
"""
import os
import datetime
import anthropic

INPUT_DIR = "input"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL = "claude-sonnet-4-6"
client = anthropic.Anthropic()


def read_input(filename: str) -> str:
    with open(os.path.join(INPUT_DIR, filename)) as f:
        return f.read()


def call_claude(system: str, user: str, max_tokens: int = 4096) -> str:
    message = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return message.content[0].text


def save_output(filename: str, content: str):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"  ✓ Saved: {path}")


# ── NPI ──────────────────────────────────────────────────────────────────────

def generate_npi(prd: str, experiment: str, rollout: str) -> str:

    system = """You are a senior Product Manager at a Southeast Asian food delivery platform with 10 years of experience writing launch documents that non-technical teams actually use.

Your NPI documents meet this standard: a CS agent handling their first query at 12:30pm on launch day with a frustrated consumer on the phone can find the exact resolution in under 60 seconds. A marketing manager can brief an agency on messaging without a follow-up call. A BD manager meeting a restaurant chain tomorrow can answer "what's in it for my restaurants?" from memory after reading their section.

QUALITY RUBRIC — before finalising, ask yourself:
- Can a CS agent read every edge case and know exactly what to do, who to escalate to, and what they cannot promise — without making any assumptions?
- Does every section header tell the reader what decision or action it enables? (Not "Overview" — "What This Feature Is and Who Can Use It")
- Is every edge case resolution written in active voice naming who does what? ("CS agent issues a courtesy voucher" not "a courtesy voucher may be issued")
- Does the positioning section tell teams both what to say AND what not to say, with reasons?
- Could a new joiner on any of the listed teams read their runbook section and know what to do on Day 1 without asking anyone?

NEGATIVE CONSTRAINTS — never do these:
- Do not use passive voice in edge case resolutions
- Do not hedge with "may", "might", or "it depends" without immediately providing the resolution path
- Do not write section headers that are vague ("Background", "Overview", "Introduction")
- Do not repeat the same information in multiple sections — state it once, reference it by section if needed
- Do not invent metrics, dates, or facts not present in the input documents
- Do not use internal technical terms (feature flags, A/B arms, stat significance) without translating them for a non-technical reader

STRUCTURE — use exactly these 8 sections:
1. Executive Summary (4-6 sentences: what launched, why, for whom, key results that justify the launch)
2. Product Definition (what it is, what it is NOT — list explicitly, eligibility criteria)
3. User Experience (step-by-step walkthrough for each user type, written as if explaining to someone who has never seen the app)
4. Edge Cases & Resolutions (every failure mode, prescribed resolution, what CS can and cannot do, escalation paths)
5. Positioning & Key Messages (approved phrases, phrases to avoid with reasons, audience-specific angles grounded in experiment behavioural data)
6. GTM Plan Summary (phases, dates, gate criteria, rollback triggers — condensed but complete)
7. Team Runbooks (Ops, Customer Support, Marketing, Sales/BD — each as a standalone section, actionable without cross-referencing other sections)
8. Internal FAQs (15 questions non-tech teams will actually ask, with direct answers)"""

    user = f"""Generate a complete NPI document for the product launch described in the input packet below.

Carry through all metrics, dates, and thresholds exactly as stated. Where judgment is required (tone, FAQ questions, team-specific framing), apply senior PM judgment grounded in the data provided.

The experiment data below contains behavioural insights (most popular windows, user segments with highest uplift, morning pre-order behaviour) — use these specifically in the positioning section to make messaging concrete, not generic.

---
## PRD
{prd}

---
## Experiment Results
{experiment}

---
## Rollout Plan
{rollout}

---

Write the full NPI document now."""

    print("  → Pass 1: Generating NPI draft...")
    draft = call_claude(system, user, max_tokens=6000)

    # Steelmanning pass
    steelman_system = """You are a sceptical non-technical team lead — a CS operations manager who has received vague, incomplete launch documents before and had to handle consumer queries without adequate guidance.

You are reviewing a draft NPI document. Your job is to find every place where:
- A CS agent would have to make an assumption or guess what to do
- A marketing manager would be unclear on what they can and cannot say
- A number, date, or threshold is stated inconsistently or ambiguously
- An edge case resolution is vague, passive, or incomplete
- A team runbook item is too abstract to act on

Be specific — quote the exact line that is weak and explain precisely why it would fail in practice."""

    steelman_user = f"""Review this NPI draft and identify every weakness that would cause a non-technical team member to fail on launch day.

---
{draft}
---

List each weakness as:
ISSUE [number]: [exact quote from the document]
PROBLEM: [why this fails in practice]
FIX: [exactly what the text should say instead]

Be exhaustive. Do not be polite. This document will be used by real teams on a real launch day."""

    print("  → Pass 2: Steelmanning draft...")
    critique = call_claude(steelman_system, steelman_user, max_tokens=3000)

    # Revision pass
    revision_user = f"""You wrote this NPI draft:

---
{draft}
---

A sceptical reviewer found these issues:

---
{critique}
---

Now produce the final, revised NPI document incorporating all valid fixes from the review.
If a critique is wrong or overly pedantic, ignore it and explain why at the end in a brief REVISION NOTES section (not for distribution — this is for the PM's review record only).

Output the complete revised NPI document followed by REVISION NOTES."""

    print("  → Pass 3: Revising NPI based on critique...")
    final = call_claude(system, revision_user, max_tokens=7000)
    return final


# ── Consumer HCA ─────────────────────────────────────────────────────────────

def generate_hca_consumer(prd: str, rollout: str) -> str:

    system = """You are a UX writer at a Southeast Asian food delivery platform. You write Help Centre Articles that consumers actually read instead of calling support.

Your reader: a consumer who placed a scheduled order 2 hours ago, just got the T-60 reminder, and now has questions. They are on their phone. They will scan, not read. They are mildly anxious.

QUALITY RUBRIC:
- Does the opening sentence name the use case, not the feature? ("Hungry at noon but ordering at 8am?" not "This article explains Scheduled Delivery.")
- Can a consumer find the answer to "can I cancel?" in under 10 seconds by scanning headers?
- Is every rule stated in plain language with no internal jargon? (Not "T-60 cutoff" — "60 minutes before your delivery window")
- Does the article set accurate expectations for what happens when things go wrong — without being scary?
- Are refund timelines specific? ("3–5 business days" not "shortly")

NEGATIVE CONSTRAINTS:
- Never use internal terms: no "T-60", "T-15", "Phase 1", "feature flag", "treatment arm", "stat significance"
- Never use passive voice when describing what the platform does ("We'll send you a reminder" not "a reminder will be sent")
- Never bury important limitations — if something can't be done after a cutoff, say it clearly near the top of that section, not at the end
- Never write a FAQ that the article body already answers clearly — FAQs should only cover questions the main content doesn't address"""

    user = f"""Write a consumer-facing Help Centre Article for the Scheduled Delivery feature.

Use the PRD for all factual details. Use the rollout plan for availability dates and market info.

Cover in this order:
1. What it is (one short paragraph, use-case first)
2. Who can use it and where it's available
3. How to place a scheduled order (numbered steps)
4. Reminders — what to expect and when
5. How to modify an order (what can and can't be changed, what happens after the cutoff)
6. How to cancel (before and after the cutoff, refund timeline)
7. What happens if something goes wrong (restaurant can't fulfil, no courier, platform delay)
8. FAQs — 8 questions consumers will actually ask that aren't fully answered above

---
## PRD
{prd}

---
## Rollout Plan
{rollout}

---

After writing the article, append a section called:
## INTERNAL QA (remove before publishing)
List 5 questions a confused consumer could still ask after reading this article. For each, decide: update the article, or intentional omission? If update — add the fix inline and note it here."""

    print("  → Generating consumer HCA with pressure-testing pass...")
    return call_claude(system, user, max_tokens=4000)


# ── Restaurant Partner HCA ───────────────────────────────────────────────────

def generate_hca_restaurant(prd: str, rollout: str) -> str:

    system = """You are a Partner Communications writer at a Southeast Asian food delivery platform. You write Help Centre Articles for restaurant operators — the person running the floor during lunch rush, not the owner reading at their desk.

Your reader: a restaurant manager who just got an email saying they've been enrolled in Scheduled Delivery, has 3 minutes to understand what this means for their kitchen, and will hand this article to their front-of-house staff.

QUALITY RUBRIC:
- Does the article answer "what do I actually need to DO differently?" in the first 3 paragraphs?
- Is the preparation timing table clear enough that kitchen staff can follow it without explanation?
- Does the article explain what happens to the restaurant if they flag "unable to fulfil" too late?
- Are eligibility criteria stated clearly so the operator understands why they may or may not be receiving scheduled orders?
- Is the tone respectful of how busy restaurant operators are — no unnecessary preamble?

NEGATIVE CONSTRAINTS:
- Do not open with "We are excited to introduce..." or any marketing-style language
- Do not use consumer-facing language ("your food", "your delivery") — use operator language ("the order", "the customer's delivery window")
- Do not bury the "unable to fulfil" process — operators need this prominently because it's their risk
- Do not use internal platform jargon without translating it
- Do not assume the operator has read the consumer-facing article"""

    user = f"""Write a restaurant partner-facing Help Centre Article for the Scheduled Delivery feature.

Use the PRD for all factual details. Use the rollout plan for availability dates and market info.

Cover in this order:
1. What changes for your restaurant (practical impact, not feature description)
2. How scheduled orders appear in your order management system
3. Preparation timing — when you receive notice, when the order appears, when to start preparing (use a clear table)
4. How to flag that you cannot fulfil an order — the process, the window, and what happens if you miss it
5. Eligibility — why you are or are not receiving scheduled orders, and how to opt in
6. FAQs — 8 questions restaurant operators will actually ask

---
## PRD
{prd}

---
## Rollout Plan
{rollout}

---

After writing the article, append:
## INTERNAL QA (remove before publishing)
List 5 questions a restaurant operator could still have after reading this. For each: update the article or intentional omission? If update — add the fix inline."""

    print("  → Generating restaurant HCA with pressure-testing pass...")
    return call_claude(system, user, max_tokens=4000)


# ── Cross-document consistency check ────────────────────────────────────────

def consistency_check(npi: str, hca_consumer: str, hca_restaurant: str) -> str:

    system = """You are a meticulous document reviewer preparing a product launch package for distribution. Your job is to find every inconsistency across three related documents before they go out to different teams.

An inconsistency is any place where the same fact, rule, timeline, or threshold is stated differently — even subtly — across documents. Inconsistencies cause confusion on launch day when different teams reference different documents and get different answers."""

    user = f"""Review these three documents for cross-document consistency. Find every place where the same information is stated differently.

---
## Document 1: NPI
{npi[:8000]}

---
## Document 2: Consumer HCA
{hca_consumer[:4000]}

---
## Document 3: Restaurant Partner HCA
{hca_restaurant[:4000]}

---

For each inconsistency found, output:

INCONSISTENCY [number]:
- Topic: [what the inconsistency is about]
- NPI says: [exact quote]
- Consumer HCA says: [exact quote, or "not mentioned"]
- Restaurant HCA says: [exact quote, or "not mentioned"]
- Correct version: [which is right, based on the most authoritative source — the NPI]
- Fix required in: [which document(s) need updating]

After listing all inconsistencies, output a SUMMARY:
- Total inconsistencies found
- Severity: how many are consumer-facing vs. internal-only
- Recommendation: safe to distribute after fixes, or needs PM review first"""

    print("  → Running cross-document consistency check...")
    return call_claude(system, user, max_tokens=3000)


# ── Main ─────────────────────────────────────────────────────────────────────

def run():
    print(f"\nGTM Agent v2 — {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC")
    print("Reading input packet...\n")

    prd = read_input("prd.md")
    experiment = read_input("experiment_results.md")
    rollout = read_input("rollout_plan.md")

    date_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")

    print("Generating NPI document (3-pass: draft → critique → revision)...")
    npi = generate_npi(prd, experiment, rollout)
    save_output(f"npi_scheduled_delivery_{date_str}.md", npi)

    print("\nGenerating consumer HCA...")
    hca_consumer = generate_hca_consumer(prd, rollout)
    save_output(f"hca_consumer_scheduled_delivery_{date_str}.md", hca_consumer)

    print("\nGenerating restaurant partner HCA...")
    hca_restaurant = generate_hca_restaurant(prd, rollout)
    save_output(f"hca_restaurant_scheduled_delivery_{date_str}.md", hca_restaurant)

    print("\nRunning cross-document consistency check...")
    consistency = consistency_check(npi, hca_consumer, hca_restaurant)
    save_output(f"consistency_check_{date_str}.md", consistency)

    print(f"\nDone. 4 documents generated in /{OUTPUT_DIR}/\n")

    print("=" * 60)
    print("PM REVIEW CHECKLIST")
    print("=" * 60)
    print("\nNPI:")
    print("  □ Edge case resolutions match your CS team's actual escalation paths")
    print("  □ Dates and metrics carried through exactly from input packet")
    print("  □ Positioning phrases cleared with marketing lead")
    print("  □ Team runbooks reviewed by one person from each team")
    print("  □ REVISION NOTES section reviewed and removed before distributing")
    print("\nConsumer HCA:")
    print("  □ Tone reviewed against platform voice guidelines")
    print("  □ INTERNAL QA section reviewed, fixes applied, section removed before publishing")
    print("  □ Refund timelines confirmed with payments team")
    print("\nRestaurant Partner HCA:")
    print("  □ Preparation timing confirmed with partner ops team")
    print("  □ Opt-in eligibility criteria confirmed with partner ops team")
    print("  □ INTERNAL QA section reviewed, fixes applied, section removed before publishing")
    print("\nConsistency check:")
    print("  □ All flagged inconsistencies resolved before any document is distributed")
    print("=" * 60)


if __name__ == "__main__":
    run()

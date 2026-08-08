# Rollout Plan: Scheduled Delivery
**PM:** Abhishek Bhardwaj  
**Target GA Date:** 2026-07-14  
**Last Updated:** 2026-06-01  

---

## Rollout Strategy

Phased rollout by market and user segment, with hold points between phases for metric review. Each phase gate requires sign-off from PM + Engineering Lead before proceeding.

---

## Phase 1 — Controlled Launch (2026-07-14)
**Markets:** Singapore only  
**User eligibility:** GrabFood users with ≥ 3 orders in the past 60 days (high-frequency, lower risk of confusion)  
**Restaurant eligibility:** Opted-in restaurant partners with < 5% historical cancellation rate; minimum 500 active restaurants at launch  
**Traffic:** 100% of eligible users in Singapore (estimated 280,000 users)  

**Phase 1 goals:**
- Validate CS contact rate ≤ 1.5% per scheduled order
- Validate scheduled order completion rate ≥ 93%
- Validate restaurant partner opt-in rate ≥ 60% of invited partners
- No P0/P1 incidents in first 72 hours

**Hold point:** 14-day metric review (2026-07-28). Proceed to Phase 2 only if all Phase 1 goals met.

---

## Phase 2 — Market Expansion (2026-07-28, pending Phase 1 gate)
**Markets:** Singapore (all users) + Kuala Lumpur (high-frequency users)  
**User eligibility:** All active GrabFood users in Singapore; KL users with ≥ 3 orders in past 60 days  
**Restaurant eligibility:** Expanded to all opted-in partners in both markets  
**Traffic:** Estimated 1.1M users  

**Phase 2 goals:**
- Maintain CS contact rate ≤ 1.5%
- KL-specific: scheduled order adoption ≥ 6% within 14 days
- AOV on scheduled orders ≥ S$28 (vs. S$31.40 in experiment — slight discount for broader population)

**Hold point:** 14-day metric review (2026-08-11). Proceed to Phase 3 if goals met.

---

## Phase 3 — Regional Rollout (2026-08-11, pending Phase 2 gate)
**Markets:** Thailand (Bangkok), Indonesia (Jakarta), Philippines (Metro Manila)  
**User eligibility:** All active GrabFood users  
**Restaurant eligibility:** All opted-in partners; local ops teams to drive restaurant opt-in campaigns pre-launch  
**Traffic:** Full rollout, estimated 4.2M additional users  

**Phase 3 goals:**
- Consistent metrics across all markets within 10% variance of Singapore baseline
- Regional CS teams trained and ready 7 days before each market launch

---

## Rollback Triggers

The following thresholds, if breached at any phase, trigger an immediate rollback decision with PM + Engineering Lead + Head of Consumer Product:

| Metric | Rollback Threshold |
|---|---|
| Scheduled order completion rate | < 88% for 48 consecutive hours |
| CS contact rate per scheduled order | > 3% for 24 consecutive hours |
| Refund rate (scheduled orders) | > 8% for 24 consecutive hours |
| P0 incident (data loss, payment error, mass notification failure) | Any occurrence |

Rollback = feature flag off for affected market. Users mid-order complete normally; no new scheduled orders accepted.

---

## Pre-Launch Checklist

**Engineering (due 2026-07-07):**
- [ ] Feature flag live and tested
- [ ] CS tooling (Salesforce scheduled order view) deployed
- [ ] Push notification infrastructure validated (T-60, T-15 reminders)
- [ ] Courier dispatch algorithm update deployed and load-tested
- [ ] Restaurant partner system update deployed

**Operations (due 2026-07-10):**
- [ ] Restaurant partner opt-in campaign completed (target: 500 restaurants confirmed)
- [ ] Restaurant partner briefing doc distributed
- [ ] Ops playbook for scheduled order failures finalised

**Customer Support (due 2026-07-10):**
- [ ] CS training completed for all Singapore agents
- [ ] HCA articles live in Help Centre
- [ ] CS knowledge base article published
- [ ] Escalation path for post-cutoff modification requests documented

**Marketing (due 2026-07-12):**
- [ ] In-app banner and push notification campaign ready
- [ ] Social media content approved
- [ ] CRM email campaign scheduled (send 2026-07-14 at 9am SGT)

**Comms (due 2026-07-12):**
- [ ] Internal comms to all non-tech teams sent
- [ ] NPI document distributed and acknowledged by team leads
- [ ] External press release approved (hold for Phase 2 if Phase 1 is limited rollout)

---

## Launch Day Plan (2026-07-14)

| Time (SGT) | Action | Owner |
|---|---|---|
| 08:00 | Feature flag enabled for Phase 1 users | Engineering |
| 08:00 | CRM email sent to eligible Singapore users | Marketing |
| 08:30 | PM + Engineering confirm first scheduled orders appearing correctly | PM |
| 09:00 | CS team briefed, on heightened monitoring | CS Lead |
| 12:00 | First scheduled orders begin dispatching (morning pre-orders) | System |
| 12:30 | PM reviews first dispatch batch metrics | PM |
| 18:00 | PM + Engineering EOD check — metrics review | PM + Eng |
| 20:00 | Go/no-go decision for Day 2 continuation | PM |

---

## Communication Plan

**Internal (pre-launch):**
- NPI distributed to all non-tech team leads: 2026-07-07
- All-hands product update: 2026-07-10
- CS training sessions: 2026-07-08 and 2026-07-09

**Consumer-facing (launch day):**
- In-app banner: "New: Schedule your GrabFood delivery up to 24 hours ahead"
- Push notification to eligible users: "Plan your meals in advance — schedule delivery now"
- CRM email: feature walkthrough with how-to steps

**Restaurant partners:**
- Email from Partner Operations: 2026-07-01 (opt-in invitation)
- Reminder email: 2026-07-10
- In-app notification in restaurant dashboard: 2026-07-14

**Press:**
- No embargo lift until Phase 2 (broader user base makes for a stronger story)
- Press release target: 2026-07-28, coinciding with Phase 2 launch

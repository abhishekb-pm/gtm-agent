# Experiment Results: Scheduled Delivery
**Experiment ID:** GF-EXP-2026-041  
**Type:** A/B Test  
**PM:** Abhishek Bhardwaj  
**Analysis completed:** 2026-05-20  

---

## Hypothesis

Offering a scheduled delivery option will increase order conversion among consumers who previously abandoned during peak hours, and will generate incremental order volume from consumers who would not have ordered for immediate delivery.

---

## Experiment Design

**Test period:** 2026-03-15 to 2026-05-10 (8 weeks)  
**Markets:** Singapore, Kuala Lumpur  
**Eligible users:** All active GrabFood consumers with ≥ 1 order in the past 90 days  
**Exclusions:** New users (< 30 days), users in ongoing unrelated experiments  

**Control group (50%):** Standard GrabFood ordering flow — immediate delivery only  
**Treatment group (50%):** Standard flow + "Schedule for later" option visible on restaurant page and cart  

**Randomisation unit:** User-level (consistent experience across sessions)  
**Sample size:** 1.2M users per arm  
**Minimum detectable effect:** 2% relative improvement in weekly order frequency  

---

## Primary Metrics

| Metric | Control | Treatment | Relative Change | p-value | Significant? |
|---|---|---|---|---|---|
| Weekly orders per active user | 3.41 | 3.58 | +5.0% | 0.0003 | ✅ Yes |
| Order conversion rate (session → order) | 34.2% | 36.1% | +5.6% | 0.0011 | ✅ Yes |
| Peak-hour abandonment rate | 22.4% | 19.1% | -14.7% | <0.0001 | ✅ Yes |

---

## Secondary Metrics

| Metric | Control | Treatment | Relative Change | p-value | Significant? |
|---|---|---|---|---|---|
| Average order value (AOV) | S$24.10 | S$26.30 | +9.1% | 0.0008 | ✅ Yes |
| 30-day consumer retention | 61.3% | 63.9% | +4.2% | 0.0140 | ✅ Yes |
| CS contact rate per order | 1.82% | 1.94% | +6.6% | 0.0820 | ❌ No |
| Refund rate | 2.1% | 2.4% | +14.3% | 0.0610 | ❌ No |

---

## Scheduled Order Specifics (Treatment Arm Only)

- **Scheduled order adoption:** 11.3% of treatment arm users placed at least one scheduled order during the experiment
- **Scheduled as % of total orders placed by adopters:** 28% (adopters heavily use the feature once they try it)
- **Scheduled order completion rate:** 93.8%
- **Scheduled order cancellation rate:** 4.1% (vs. 1.8% for immediate orders — expected, given advance planning window)
- **Most popular scheduled windows:** 12:00–12:30pm (31%), 6:00–6:30pm (24%), 7:00–7:30pm (18%)
- **Median advance booking time:** 3.2 hours before window
- **AOV of scheduled orders:** S$31.40 (vs. S$24.10 for immediate — consumers plan larger meals when scheduling)

---

## Guardrail Metrics (No Significant Degradation)

| Metric | Control | Treatment | Change | Status |
|---|---|---|---|---|
| Restaurant partner cancellation rate | 3.2% | 3.5% | +0.3pp | ✅ Within threshold |
| Courier utilisation rate | 78.4% | 79.1% | +0.7pp | ✅ Within threshold |
| App crash rate | 0.41% | 0.43% | +0.02pp | ✅ Within threshold |
| Payment failure rate | 1.9% | 2.0% | +0.1pp | ✅ Within threshold |

---

## Segment Analysis

**By market:**
- Singapore: +6.1% weekly orders per user (stronger — higher proportion of office workers)
- Kuala Lumpur: +3.8% weekly orders per user (positive but softer — different peak behaviour)

**By user segment:**
- High-frequency users (≥5 orders/month): +3.2% — already ordering frequently, modest uplift
- Mid-frequency users (2–4 orders/month): +7.8% — largest uplift, likely the core scheduled-delivery user
- Low-frequency users (1 order/month): +2.1% — small but positive signal

**By time of placement:**
- Orders placed during peak (12–1pm, 6–8pm): scheduled option reduced abandonment most sharply
- Orders placed in the morning (8–10am): highest scheduling rate — consumers pre-ordering lunch

---

## Risks & Observations

1. **Refund rate trend:** +14.3% increase in refund rate in treatment arm, though not statistically significant at p=0.06. Directionally concerning. Primary driver: restaurant "unable to fulfil" cancellations (edge case #6 in PRD). Mitigation: stricter restaurant eligibility criteria at launch, opt-out mechanism for restaurants with high cancellation history.

2. **CS contact rate:** +6.6% increase, not significant, but warrants monitoring. Anticipated — new product surface generates questions. CS training and HCA publication pre-launch should absorb.

3. **Cannibalism check:** Modelled whether scheduled orders displaced immediate orders (same user, same restaurant, same day). Finding: 73% of scheduled orders represent net-new occasions, not displaced immediate orders. Healthy incrementality.

---

## Recommendation

**Ship.** Primary metrics are strongly positive with high statistical confidence. AOV lift (+9.1%) and peak abandonment reduction (-14.7%) exceed pre-experiment targets. 

Recommended modifications before full rollout:
1. Restrict restaurant eligibility at launch to partners with < 5% historical cancellation rate
2. Add explicit restaurant "Unable to fulfil" window (90 min before) with automated consumer notification
3. Monitor CS contact rate and refund rate weekly for first 4 weeks — set alert thresholds at +20% above control baseline

**Sign-off:** Experiment review committee approved 2026-05-22

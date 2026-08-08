# PRD: Scheduled Delivery
**Product Area:** Consumer Ordering  
**PM:** Abhishek Bhardwaj  
**Status:** Approved for Launch  
**Last Updated:** 2026-06-01  

---

## Problem Statement

GrabFood consumers frequently want to order food for a specific future time — office lunch pre-orders, family dinners, or avoiding peak-hour surge pricing — but today can only order for immediate delivery. This results in:

- Consumers timing their order manually to hit a desired delivery window, often getting it wrong
- Lost orders during off-peak hours when consumers want to plan ahead but don't trust delivery timing
- Restaurant partners unable to smooth kitchen load across the day

Internal data shows 18% of consumers who abandon the app during peak hours (12–1pm, 6–8pm) do not return within 30 minutes. Exit surveys cite "afraid food will arrive cold / too early / too late" as the primary reason.

---

## Goal

Allow consumers to place a food order up to 24 hours in advance, specifying a delivery window, with the order automatically dispatched to the restaurant and courier network at the right time to hit the chosen window.

---

## Success Metrics

**Primary:**
- Scheduled order volume as % of total orders: target 8% within 90 days of full launch
- Scheduled order completion rate: ≥ 94% (vs. 96.2% for immediate orders — acceptable delta given complexity)
- Consumer repeat rate on scheduled orders within 30 days: ≥ 45%

**Secondary:**
- Peak hour order abandonment rate: reduction of ≥ 10% in launch markets
- Restaurant partner opt-in rate: ≥ 70% of active restaurant partners within 60 days
- CS contact rate per scheduled order: ≤ 1.5% (proxy for confusion/failure)

---

## Scope

### In Scope
- Consumer-facing scheduled order flow (iOS and Android)
- Restaurant partner notification and preparation timing system
- Courier dispatch logic for scheduled orders
- Order modification and cancellation up to 60 minutes before scheduled delivery window
- Push notification and in-app reminder system (T-60min, T-15min)
- CS tooling: agent view showing scheduled order status and modification capabilities

### Out of Scope (Phase 1)
- Group ordering with scheduled delivery
- Scheduled grocery or mart orders
- Recurring/subscription scheduled orders ("every Monday at 12:30pm")
- Scheduled orders beyond 24 hours

---

## User Stories

**Consumer:**
1. As a consumer, I want to browse restaurants and place an order for delivery at a future time so I can plan my meals without watching the clock.
2. As a consumer, I want to modify or cancel my scheduled order up to 60 minutes before the window so I have flexibility if my plans change.
3. As a consumer, I want to receive a reminder before my order is dispatched so I'm not caught off guard.
4. As a consumer, I want to see a clear confirmation of my scheduled time so I'm confident the order will arrive when I expect.

**Restaurant Partner:**
5. As a restaurant partner, I want advance notice of scheduled orders so I can plan kitchen capacity and avoid rush preparation.
6. As a restaurant partner, I want to be able to flag if I cannot fulfil a scheduled order (e.g. unexpected closure) so the consumer is informed early.

**Customer Support Agent:**
7. As a CS agent, I want to see the full lifecycle of a scheduled order (placed, dispatched, en route, delivered) so I can resolve consumer queries accurately.
8. As a CS agent, I want to be able to modify or cancel a scheduled order on behalf of a consumer up to the 60-minute cutoff.

---

## User Experience

### Consumer Flow

**Placing a Scheduled Order:**
1. Consumer opens GrabFood, selects a restaurant.
2. On the restaurant page, a "Schedule for later" toggle appears below the delivery address bar.
3. Tapping the toggle opens a time picker showing available 30-minute delivery windows for the next 24 hours. Unavailable windows (restaurant closed, no courier coverage predicted) are greyed out.
4. Consumer selects a window (e.g. "Tomorrow, 12:30–1:00pm"), adds items to cart, and checks out normally.
5. Order confirmation screen shows: "Your order is scheduled for tomorrow, 12:30–1:00pm. We'll remind you 60 minutes before dispatch."
6. The order appears in "Upcoming Orders" in the Orders tab with a countdown.

**Pre-Dispatch Reminders:**
- T-60 min: Push notification — "Your scheduled order from [Restaurant] dispatches in 1 hour. Tap to modify or cancel."
- T-15 min: Push notification — "Your [Restaurant] order is about to be prepared. Last chance to cancel."
- At dispatch: Order transitions to standard live-tracking flow.

**Modifying a Scheduled Order:**
- Consumer taps "Upcoming Orders" → selects order → taps "Modify order"
- Can change: delivery window (subject to availability), delivery address, items
- Cannot change: restaurant
- Modifications close 60 minutes before the scheduled window

**Cancelling a Scheduled Order:**
- Available up to 60 minutes before the window
- Full refund issued automatically
- After 60-minute cutoff, standard cancellation policy applies (restaurant may have begun preparation)

### Restaurant Partner Flow
- Scheduled orders appear in the restaurant's order management system 60 minutes before the consumer's chosen window
- Labelled clearly as "Scheduled — prepare by [time]"
- Restaurant receives a preparation reminder notification 75 minutes before the window
- Restaurant can flag "Unable to fulfil" up to 90 minutes before the window — triggers consumer notification and full refund

---

## Edge Cases

| # | Scenario | System Behaviour | CS/Ops Resolution |
|---|---|---|---|
| 1 | Restaurant closes unexpectedly after order placed | System detects closure via partner status feed. Consumer notified, full refund issued automatically. | CS to confirm refund timeline (3–5 business days). Offer courtesy voucher if consumer contacts us. |
| 2 | No courier available at dispatch time | System attempts courier matching for 10 minutes. If unsuccessful, order cancelled, consumer notified, full refund. | CS to explain courier unavailability, confirm refund, offer re-order assistance. |
| 3 | Consumer attempts to modify after 60-min cutoff | App shows "Modification window has closed" message with explanation. No modification permitted. | CS cannot override cutoff. Escalate to senior agent if consumer insists — senior agent can cancel if restaurant has not begun preparation (check order status tool). |
| 4 | Consumer does not receive reminders (notification off) | Order still dispatches as scheduled. Consumer responsibility. | CS to clarify that reminders require push notifications enabled. Cannot compensate for missed reminders if order was fulfilled correctly. |
| 5 | Payment fails at time of order placement | Order not confirmed. Consumer prompted to update payment method and retry. | Standard payment failure flow. |
| 6 | Restaurant marks order as "Unable to fulfil" after 90-min window | Edge case — treated as restaurant cancellation. Full refund + courtesy voucher issued automatically. Flag restaurant partner account for review. | CS to confirm refund and voucher. Ops to follow up with restaurant partner. |
| 7 | Consumer places scheduled order and then places immediate order from same restaurant | Both orders processed independently. No merge. | CS to treat as two separate orders. |
| 8 | Scheduled delivery window falls during a platform-wide surge or outage | If system detects capacity constraints, order may be delayed by up to 15 minutes beyond window. Consumer notified in-app. | CS to acknowledge delay, confirm order is still in queue. Compensation per standard delay policy if > 30 min beyond window. |
| 9 | Consumer changes delivery address to out-of-range location | Address change rejected with error message — "This address is not supported for your scheduled window." Consumer must choose a supported address or cancel. | CS to explain coverage limitation. Cannot override. |
| 10 | App crash or logout between order placement and dispatch | Order is saved server-side. Consumer can log back in and see order in "Upcoming Orders." | CS to reassure consumer that order is active. |

---

## Dependencies

- **Restaurant Partner System:** partner ops team to enable scheduled order flag for participating restaurants; estimated 3-week enablement sprint
- **Courier Dispatch System:** dispatch algorithm update to handle future-time scheduling; engineering estimate 4 weeks
- **CS Tooling:** new "Scheduled Orders" view in Salesforce; estimated 2-week build
- **Push Notification Infrastructure:** T-60 and T-15 reminders; 1-week build
- **Payment:** no changes required — charge held at time of order placement, released if cancelled

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Restaurant opt-in below target | Medium | High | Incentive programme for early-adopter restaurants; default opt-in for restaurant chains |
| Courier unavailability at scheduled time | Medium | Medium | Buffer courier demand forecasting 90 minutes ahead; surge pricing adjusted for scheduled windows |
| Consumer confusion on cancellation cutoff | High | Low | Clear in-app messaging at placement and reminder stages |
| CS volume spike at launch | Medium | Medium | CS training pre-launch; FAQ article in agent knowledge base |

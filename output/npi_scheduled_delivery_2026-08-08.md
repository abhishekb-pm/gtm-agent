# NPI Document: GrabFood Scheduled Delivery

**Product:** GrabFood Scheduled Delivery
**PM:** Abhishek Bhardwaj
**NPI Version:** 2.0
**Distributed:** 2026-07-07
**General Availability (Phase 1):** 2026-07-14
**Last Updated:** 2026-07-07

---

> **How to use this document.** Each section is written for a specific team and stands alone. Find your team's runbook in Section 7 and read it first. Return to other sections only when you need additional context. If you are a CS agent handling a live query, go directly to Section 4 (Edge Cases & Resolutions) — every scenario has a prescribed resolution you can execute immediately.

---

## Section 1: Executive Summary — What Launched, Why It Matters, and What the Data Says

GrabFood Scheduled Delivery lets consumers place a food order up to 24 hours in advance and choose a 30-minute delivery window, with the platform automatically notifying the restaurant and dispatching a courier at the right time. The feature launches in Singapore on 2026-07-14 to approximately 280,000 high-frequency users, with Kuala Lumpur expansion beginning 2026-07-28 and regional rollout to Thailand, Indonesia, and the Philippines from 2026-08-11 — each phase gated on measured performance.

The launch resolves a documented problem: 18% of consumers who leave the app during the 12–1pm and 6–8pm peaks do not return within 30 minutes, primarily because they fear food will arrive at the wrong time. An 8-week experiment across Singapore and Kuala Lumpur with 1.2 million users per group demonstrated that offering a scheduling option reduced peak-hour abandonment by 14.7%, increased weekly orders per active user by 5.0%, and lifted average order value by 9.1% — with scheduled orders averaging S$31.40 versus S$24.10 for immediate orders, because consumers plan larger meals when they book in advance.

Crucially, 73% of scheduled orders represent new ordering occasions rather than consumers simply moving an existing order to a later time, confirming this feature generates incremental revenue, not cannibalisation. The experiment's primary metrics cleared statistical confidence thresholds with strong margins; guardrail metrics (restaurant cancellation rate, courier utilisation, app crash rate, payment failure rate) all remained within acceptable bounds. The feature is approved for launch.

---

## Section 2: Product Definition — What This Feature Is, What It Is Not, and Who Can Use It

### What Scheduled Delivery Is

Scheduled Delivery is a consumer-facing ordering flow that allows a GrabFood user to select a future 30-minute delivery window — up to 24 hours from the moment of ordering — at the point of checkout. The platform holds the payment at order placement, notifies the restaurant 60 minutes before the selected window, dispatches a courier at the calculated time to meet that window, and sends the consumer two push notification reminders (60 minutes and 15 minutes before the delivery window). Consumers can cancel at any point up to 60 minutes before their selected window and will receive a full automatic refund to their original payment method within 3–5 business days. Cancellations requested after the 60-minute cutoff are subject to standard post-dispatch cancellation policy and may not result in a full refund — see Section 4, Edge Case 3 for the exact resolution path.

### What Scheduled Delivery Is NOT — Read This Before Answering Any Query

The following are explicitly out of scope for Phase 1. Do not promise these to consumers, restaurant partners, or press:

- **Not available for GrabMart or grocery orders.** Food orders only.
- **Not available for group orders.** A scheduled order placed by one consumer cannot be shared with others through the group order flow.
- **Not a recurring or subscription feature.** Consumers cannot set "every Monday at 12:30pm." Each scheduled order must be placed individually.
- **Not available beyond 24 hours.** The furthest a consumer can schedule is 23 hours and 59 minutes from the current moment.
- **Not available on web.** iOS and Android apps only.

### Who Can Place a Scheduled Order — Exact Eligibility Criteria

| Criterion | Requirement |
|---|---|
| Market | Singapore only at Phase 1 launch (2026-07-14) |
| Account order history | ≥ 3 completed (not cancelled) orders placed within the past 60 days |
| Account standing | No active fraud flag and no account suspension |
| Restaurant eligibility | Opted-in partner with < 5% order cancellation rate over the preceding 90 days, calculated as of 2026-07-07 |
| Minimum restaurant pool | 500 confirmed opted-in restaurants — see gate criteria below |

Consumers who do not meet the account order history and standing criteria will not see the "Schedule for later" toggle on the restaurant page. If a consumer contacts CS asking why they cannot see the toggle, the CS agent checks Salesforce for the consumer's order count in the past 60 days and account standing flag. The CS agent tells the consumer which criterion is not met — order history or account standing — and does not speculate beyond those two criteria.

**Restaurant pool gate:** The partner operations lead confirms the opted-in restaurant count no later than 2026-07-12. If fewer than 500 restaurants have opted in by 2026-07-12 5pm SGT, the PM and Engineering Lead decide by that same deadline whether to delay the launch or revise the floor. The CS Lead and Marketing Lead must be notified of any change within 1 hour of that decision.

This feature launches first to users who meet the order history threshold to reduce confusion and CS contact volume during the critical first 14 days.

### Eligibility Expands Over Time

- **Phase 2 (2026-07-28):** All GrabFood users in good standing in Singapore; Kuala Lumpur users with ≥ 3 completed orders in the past 60 days and no active fraud flag or suspension
- **Phase 3 (2026-08-11):** All GrabFood users in good standing in Thailand (Bangkok), Indonesia (Jakarta), Philippines (Metro Manila)

---

## Section 3: User Experience — Step-by-Step Walkthrough for Every User Type

### The Scheduled Delivery Timeline — Read This First

Every action in the scheduled delivery flow is relative to the consumer's chosen delivery window. This table is the single reference for all timing questions. All team runbooks in Section 7 refer back to this table.

| Time relative to delivery window | What happens |
|---|---|
| At order placement | Consumer selects window; payment is charged and held |
| T-75 minutes | Restaurant receives a preparation reminder: push notification to GrabFood Partner app AND an alert in the order management dashboard |
| T-60 minutes | Scheduled order appears in the restaurant's order queue, labelled "Scheduled — prepare by [time]"; this is also the consumer's modification and cancellation cutoff |
| T-15 minutes | Consumer receives an informational push notification that dispatch is approaching |
| At dispatch | Courier is assigned; order enters the standard live-tracking flow |
| Delivery window | Consumer receives order within the 30-minute window |

> **Important for CS agents and partner ops:** The restaurant receives a preparation reminder at T-75 and must flag "Unable to fulfil" within 15 minutes of receiving that reminder — that is, before T-60 when the order formally enters their queue. If the restaurant has not flagged "Unable to fulfil" before T-60, it is treated as a late cancellation. See Edge Case 6 in Section 4.

---

### Consumer: Placing a Scheduled Order

**Step 1 — Open GrabFood and choose a restaurant.**
The app experience is identical to a normal order until the consumer reaches the restaurant page.

**Step 2 — Activate the scheduling option.**
Directly below the delivery address bar, the consumer sees a toggle labelled "Schedule for later." Tapping it opens a time picker.

**Step 3 — Choose a delivery window.**
The time picker displays 30-minute delivery windows across the next 24 hours — for example, "Today, 6:00–6:30pm" or "Tomorrow, 12:00–12:30pm." Windows that are unavailable — because the restaurant is closed during that period, or because the platform predicts insufficient courier availability in the consumer's area at that time — appear greyed out and cannot be selected. This is not a bug. Availability varies by location, time, and restaurant. The consumer selects an available window.

**Step 4 — Confirm push notification status.**
If the consumer's device has push notifications disabled for GrabFood, the app displays an in-line warning before checkout: *"Push notifications are off. You won't receive delivery reminders for this order. Enable them in Settings > GrabFood > Notifications."* The consumer may proceed without enabling notifications — the order will still be fulfilled — but they will receive no reminders.

**Step 5 — Build the cart and check out.**
The consumer adds items to the cart and proceeds through checkout exactly as they would for an immediate order. Payment is charged at this point and held until delivery is complete, or released immediately and returned to the original payment method within 3–5 business days if the order is cancelled before the cutoff.

**Step 6 — Review the order confirmation.**
The confirmation screen displays: *"Your order is scheduled for [Day], [Time Window]. We'll remind you 60 minutes before dispatch."* The scheduled time is shown prominently — not buried in fine print.

**Step 7 — Find the order in the app.**
The order appears in the **"Upcoming Orders"** section of the Orders tab with a live countdown to the dispatch time. The consumer does not need to do anything further — the platform manages the rest.

---

### Consumer: Receiving Reminders

The consumer receives two automatic push notifications, provided push notifications are enabled on their device. Enabling push notifications is the consumer's responsibility; if they are disabled, the order proceeds as scheduled without reminders and the consumer is not entitled to compensation for a missed reminder on an otherwise correctly fulfilled order.

- **T-60 minutes before the window:** *"Your scheduled order from [Restaurant Name] dispatches in 1 hour. Tap to modify or cancel."* This is the last point at which the consumer can make changes. The modification and cancellation window closes at this moment.
- **T-15 minutes before the window:** *"Your [Restaurant Name] order will be dispatched soon."* This notification is informational only. The modification and cancellation window closed 45 minutes ago. No changes can be made at this stage.
- **At dispatch:** The order transitions into the standard live-tracking flow. The consumer sees the courier on the map exactly as they would for an immediate order.

---

### Consumer: Modifying a Scheduled Order

The consumer can modify any of the following up to 60 minutes before the selected window (T-60):

| Can modify before T-60 | Cannot modify at any time |
|---|---|
| Delivery window (subject to availability) | Restaurant (cannot switch restaurants mid-order) |
| Delivery address (must be within coverage area) | — |
| Items in the cart | — |

**How to modify:**
1. Tap "Upcoming Orders" in the Orders tab.
2. Select the order to modify.
3. Tap "Modify order."
4. Make changes and confirm.

Once T-60 passes, the "Modify order" button is replaced with a read-only view. The app displays: *"Modification window has closed — your order is confirmed and will be prepared shortly."*

---

### Consumer: Cancelling a Scheduled Order

**Before T-60:**
1. Tap "Upcoming Orders" → select order → tap "Cancel order."
2. Confirm cancellation.
3. A full refund is issued automatically and returns to the original payment method within 3–5 business days.

**After T-60:**
Standard post-dispatch cancellation policy applies. The restaurant may have already begun preparation. The consumer is shown the applicable cancellation terms before confirming. CS cannot override the cutoff at the standard agent level — see Section 4, Edge Case 3 for the full resolution path.

---

### Restaurant Partner: Receiving and Preparing a Scheduled Order

Refer to the master timeline at the top of Section 3 for all timings.

**T-75 minutes:** The restaurant receives a preparation reminder via push notification to the GrabFood Partner app AND an alert in the order management dashboard. Acknowledgement is not required, but the restaurant must act on any inability to fulfil within 15 minutes of this reminder (before T-60). If the restaurant has disabled push notifications on the Partner app, the dashboard alert is the only notification they will receive.

**T-60 minutes:** The scheduled order appears in the restaurant's order queue, labelled clearly as **"Scheduled — prepare by [specific time]."** The restaurant treats this exactly like any incoming order. The restaurant's window to flag "Unable to fulfil" without penalty closes at this moment.

**If the restaurant cannot fulfil the order:** The restaurant must flag "Unable to fulfil" in their dashboard within 15 minutes of receiving the T-75 preparation reminder (i.e., before T-60). Flagging before T-60 triggers an automatic consumer notification and a full automatic refund to the consumer. If the restaurant flags "Unable to fulfil" after T-60, the situation is treated as a late restaurant cancellation — see Edge Case 6 in Section 4.

---

### Customer Support Agent: Viewing a Scheduled Order

In Salesforce, a **"Scheduled Orders"** view is available from 2026-07-14. When a consumer contacts CS about a scheduled order:

1. Open the consumer's profile in Salesforce.
2. Select the "Scheduled Orders" tab.
3. The order displays its full lifecycle status: **Placed → Dispatched → En Route → Delivered** (or the relevant cancelled/failed state).
4. The agent can see the selected window, current status, and — if T-60 has not passed — options to modify or cancel on the consumer's behalf.

CS agents cannot view or modify scheduled orders in any system other than the Salesforce Scheduled Orders view. If an order does not appear there, follow the escalation path in Section 4.

---

## Section 4: Edge Cases & Resolutions — Every Failure Mode, Who Does What, and When to Escalate

> **For CS agents:** Every scenario below tells you exactly what to do. "Cannot" means the system will not allow it and no escalation will change that. "Escalate to senior agent" means a senior agent has an additional capability in the order status tool — not that the policy changes. Voucher values, refund timelines, and compensation rules are stated in full in each scenario — you do not need to look them up elsewhere.

---

### Edge Case 1: Restaurant Closes Unexpectedly After the Consumer Places an Order

**What the system does:** The platform detects the closure through the partner status feed, cancels the order, notifies the consumer by push notification, and issues a full automatic refund to the consumer's original payment method.

**What the CS agent does:** The CS agent confirms that the refund has been initiated and states the timeline: 3–5 business days to the original payment method. The CS agent then manually issues a courtesy voucher of [S$X / local currency equivalent — PM to confirm value before launch] to the consumer using the standard voucher issuance tool in Salesforce. The system does not issue this voucher automatically for Edge Case 1 — the CS agent must issue it manually.

**What the CS agent cannot do:** The CS agent cannot reinstate a cancelled order after restaurant closure. If the consumer wants to reorder, the CS agent helps them identify an alternative open restaurant and, if helpful, walks them through placing a new scheduled order.

---

### Edge Case 2: No Courier Available When the Order Is Due to Dispatch

**What the system does:** The platform attempts to match a courier for 10 minutes. If no courier is matched within 10 minutes, the system cancels the order, notifies the consumer by push notification, and issues a full automatic refund to the consumer's original payment method.

**What the CS agent does:** The CS agent acknowledges the inconvenience, explains that no courier was available in the consumer's area at the dispatch time, confirms that the full refund is processing (3–5 business days to the original payment method), and offers to help the consumer place a new immediate order or a rescheduled order if they wish. No voucher is issued for this scenario unless the CS agent's senior agent determines exceptional circumstances apply — that determination requires senior agent escalation and cannot be made at the standard CS level.

**What the CS agent cannot do:** The CS agent cannot hold the order open beyond the 10-minute matching window or guarantee courier availability for a rescheduled attempt.

---

### Edge Case 3: Consumer Wants to Modify or Cancel After T-60

**What the system does:** The "Modify order" button is replaced with a read-only display. The app shows: *"Modification window has closed — your order is confirmed and will be prepared shortly."*

**What the CS agent does (standard):** The CS agent informs the consumer that the 60-minute modification window is a system-level rule. The CS agent does not offer compensation for the inability to modify or cancel after T-60.

**What the CS agent does if the consumer insists:** The CS agent escalates to a senior agent. The senior agent checks the order's current status in the order status tool. If the restaurant has **not yet begun preparation**, the senior agent cancels the order. If the restaurant **has begun preparation**, no cancellation is possible and standard post-dispatch cancellation policy applies — which may not result in a full refund. The senior agent communicates the outcome to the consumer directly.

**What the CS agent cannot do:** The CS agent cannot override the cutoff, promise a cancellation before escalation is complete, or issue compensation for a correctly fulfilled order the consumer simply no longer wants.

---

### Edge Case 4: Consumer Did Not Receive the T-60 or T-15 Reminder Notifications

**What the system does:** Nothing — the order proceeds as scheduled regardless of whether push notifications were received. The scheduled delivery flow does not depend on the consumer acknowledging a reminder.

**What the CS agent does:** The CS agent explains that push notifications must be enabled on the consumer's device for reminders to be received, and directs the consumer to their device settings (Settings > GrabFood > Notifications). If the underlying order was fulfilled correctly, the CS agent does not issue compensation. If the consumer's concern is about the order itself rather than the reminder, the CS agent identifies the applicable edge case in this section and handles it accordingly.

**What the CS agent cannot do:** The CS agent cannot issue compensation for a missed reminder when the order was delivered as scheduled.

---

### Edge Case 5: Payment Fails at the Time of Order Placement

**What the system does:** The order is not confirmed. The app prompts the consumer to update their payment method and retry.

**What the CS agent does:** Standard payment failure flow. The CS agent directs the consumer to update their payment method in the GrabFood app and attempt the order again. No scheduled order exists in the system until payment succeeds, so there is no order to look up in Salesforce.

---

### Edge Case 6: Restaurant Flags "Unable to Fulfil" After T-60 (Late Cancellation)

**What the system does:** The order is treated as a restaurant-initiated late cancellation. The system automatically issues the consumer a full refund to their original payment method (3–5 business days) AND a courtesy voucher of [S$X / local currency equivalent — PM to confirm value before launch]. The voucher is issued automatically by the system — the CS agent does not need to issue it manually. The restaurant partner's account is flagged in the partner management system for review.

**What the CS agent does:** The CS agent confirms to the consumer that the refund and courtesy voucher have both been issued automatically. The CS agent states the refund timeline: 3–5 business days to the original payment method. The CS agent does not manually issue an additional voucher — doing so would result in a duplicate.

**What Ops does:** The partner operations team follows up with the flagged restaurant within 2 business days to determine the reason for the late cancellation and assess whether the partner should remain eligible for scheduled orders.

> **CS agent note — Edge Case 1 vs Edge Case 6:** In Edge Case 1 (restaurant closes unexpectedly), the CS agent manually issues the voucher because the system does not do so automatically. In Edge Case 6 (late "Unable to fulfil" flag), the system issues the voucher automatically and the CS agent does not issue it again. Check the order status in Salesforce before issuing any voucher manually — if the Salesforce record shows "Voucher issued: Yes," do not issue a second one.

---

### Edge Case 7: Consumer Places a Scheduled Order and Then Places an Immediate Order from the Same Restaurant

**What the system does:** Both orders are processed independently. There is no automatic merging of orders.

**What the CS agent does:** The CS agent treats these as two entirely separate orders. If the consumer wants to cancel one, the CS agent applies the standard cancellation policy to that order independently based on its current status.

---

### Edge Case 8: Consumer's Scheduled Window Falls During a Platform-Wide Surge or Outage

**What the system does:** If the system detects capacity constraints, the order may be delayed by up to 15 minutes beyond the selected window. The system notifies the consumer in-app when this occurs.

**What the CS agent does:** The CS agent acknowledges the delay, reassures the consumer that the order is in the queue and being processed, and confirms that the consumer will receive in-app updates. If the total delay exceeds 30 minutes beyond the selected window, the CS agent applies the standard delay compensation policy. The CS agent does not invent or improvise compensation outside that policy.

**What the CS agent cannot do:** The CS agent cannot guarantee a specific revised delivery time during an active surge or outage.

---

### Edge Case 9: Consumer Attempts to Change Delivery Address to a Location Outside Coverage

**What the system does:** The address change is rejected with an in-app error: *"This address is not supported for your scheduled window."* The consumer must either choose a supported address or cancel the order before T-60.

**What the CS agent does:** The CS agent explains that delivery coverage for scheduled windows is determined by predicted courier availability in that area at the specific time selected, and that the system cannot override this. The CS agent helps the consumer identify whether a different nearby address might be within coverage, or assists with cancellation and confirms the refund timeline (3–5 business days to the original payment method) if the consumer chooses to cancel before T-60.

**What the CS agent cannot do:** The CS agent cannot override the coverage restriction or manually assign the order to an out-of-coverage address.

---

### Edge Case 10: Consumer's App Crashes or They Are Logged Out Between Placing the Order and Dispatch

**What the system does:** The order is saved on GrabFood's servers. It is not lost. When the consumer logs back in, the order appears in "Upcoming Orders" exactly as before.

**What the CS agent does:** The CS agent reassures the consumer that the order is active and safe, and asks the consumer to log back into the app and check the "Upcoming Orders" tab. If the order does not appear after login, the CS agent looks it up in the Salesforce Scheduled Orders view and confirms the status directly to the consumer.

---

### Edge Case 11: Consumer Asks Why a Specific Delivery Window Is Greyed Out

**What the system does:** Windows appear greyed out when either (a) the restaurant is closed during that period, or (b) the platform's courier availability model predicts insufficient courier supply in the consumer's area at that specific time. Greyed-out windows are not a bug.

**What the CS agent does:** The CS agent tells the consumer: *"A window may be unavailable because the restaurant is closed at that time, or because our system predicts that not enough couriers will be available in your area during that window. This is not a fault with the app. Availability changes over time — a window that is greyed out now may become available if you check again closer to that time. We recommend selecting the nearest available window, or trying again later."* The CS agent does not attempt to manually unlock a greyed-out window — this is not possible.

**What the CS agent cannot do:** The CS agent cannot override window availability or guarantee that a specific window will become available.

---

### Escalation Path Quick Reference

| Situation | First action | Escalate to |
|---|---|---|
| Modification after T-60, consumer insists | Explain cutoff; offer escalation | Senior CS agent (has order status tool access) |
| Order not appearing in Salesforce Scheduled Orders view | Check order ID, attempt manual search | CS tech support |
| Restaurant flagged for late "Unable to fulfil" | Confirm refund and auto-issued voucher to consumer; do not manually issue voucher | Ops team (partner follow-up within 2 business days) |
| Delay > 30 minutes beyond window | Apply standard delay compensation policy | — |
| Consumer asks why toggle is not visible | Check order count (≥ 3 completed in past 60 days) and account standing in Salesforce; tell consumer which criterion is unmet | — |
| Any P0 incident (mass payment error, mass notification failure, data incident) | Do not troubleshoot independently | Engineering on-call via incident channel |

---

## Section 5: Positioning & Key Messages — What to Say, What Not to Say, and Why

### The Single Positioning Statement

GrabFood Scheduled Delivery gives consumers control over when their food arrives — so they can plan a lunch without watching the clock, lock in a family dinner at the right time, and stop worrying about food arriving at the wrong moment during peak hours.

---

### What the Data Says About Who Benefits Most — Use This to Make Messaging Concrete

The experiment identified three specific consumer behaviours. All messaging should be anchored to these behaviours — not to generic claims about "convenience."

1. **The morning pre-planner.** Consumers placing orders during the 8–10am window had the highest scheduling rate of any time period. These are office workers locking in a 12:00–12:30pm lunch before the day gets away from them. This is the highest-value use case for launch messaging.

2. **The peak-hour escapee.** The 12:00–12:30pm window (31% of all scheduled orders) and the 6:00–6:30pm window (24%) were the most popular delivery windows — matching exactly the peak hours when app abandonment was highest. Consumers use scheduling to claim a lunch or dinner slot before timing becomes uncertain.

3. **The mid-frequency converter.** Users ordering 2–4 times per month showed the largest weekly order uplift of any segment: +7.8%. These consumers were not ordering every day — but scheduling unlocked occasions they previously skipped. Messaging should speak to the person who would have ordered but didn't trust the timing.

Average scheduled order value was S$31.40 versus S$24.10 for immediate orders. Consumers ordering in advance order more, and they order meals that matter — team lunches, family dinners, planned occasions. Scheduled Delivery is a planning feature, not a budget feature. Messaging must reflect this.

---

### Approved Messages by Audience

#### Consumer Messaging

| Approved phrase | Why it works |
|---|---|
| "Lock in your lunch before the day takes over." | Speaks directly to the morning pre-planner behaviour. Concrete, not abstract. |
| "Schedule your 12:30pm delivery before it books up." | Creates appropriate scarcity around popular windows — grounded in real data showing 12:00–12:30pm is the most popular window. |
| "Order dinner now, eat at 7pm." | Simple and direct. Removes all ambiguity about how the feature works. |
| "Plans change. Modify or cancel up to an hour before." | Addresses the documented consumer concern about flexibility head-on. |
| "Skip the peak-hour panic — your food arrives exactly when you plan." | Speaks to the abandonment behaviour the feature solves. |

#### Restaurant Partner Messaging

| Approved phrase | Why it works |
|---|---|
| "See your lunch rush coming 60 minutes early." | Specific and operational — speaks to the real benefit of advance kitchen preparation. |
| "Scheduled orders come with preparation time built in — no surprises." | Addresses the partner's core concern: being caught unprepared. |
| "More orders, more predictably." | Headline for BD conversations. Simple value statement. |

#### Internal / Executive Messaging

| Approved phrase | Why it works |
|---|---|
| "+5.0% weekly orders per user in the experiment." | Primary metric — leads with the business case. |
| "14.7% reduction in peak-hour abandonment." | The problem this solves, quantified. |
| "73% of scheduled orders are incremental — not cannibalised from immediate orders." | Addresses the first question anyone will ask: are we just moving existing orders around? |

---

### What Not to Say — and Why

| Do not say | Why not |
|---|---|
| "Guaranteed delivery at [exact time]" | The feature delivers within a 30-minute window, not at a precise minute. Promising a specific time will generate CS complaints whenever delivery arrives at any point in the window. Say "30-minute window" instead. |
| "Available for all GrabFood orders" | GrabMart, grocery, and group orders are excluded in Phase 1. This claim will generate CS contacts and partner complaints if published. |
| "Available to all GrabFood users" | Phase 1 is restricted to Singapore users with ≥ 3 completed orders in the past 60 days and no account flags. This claim is accurate only from Phase 2 onward for Singapore, and from Phase 3 onward for other markets. |
| "Schedule up to 7 days in advance" or any window other than 24 hours
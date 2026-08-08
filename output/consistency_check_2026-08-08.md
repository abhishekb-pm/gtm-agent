I'll work through each document systematically, cross-referencing every fact, rule, timeline, and threshold.

---

**INCONSISTENCY 1:**
- Topic: Consumer reminder notification — what the 60-minute reminder says vs. what the 15-minute reminder says
- NPI says: "T-60 minutes: Consumer receives push notification... this is also the consumer's modification and cancellation cutoff" | "T-15 minutes: Consumer receives an informational push notification that dispatch is approaching"
- Consumer HCA says: "60 minutes before your delivery window: A push notification letting you know dispatch is coming up. This is your last chance to modify or cancel." | "15 minutes before your delivery window: A heads-up that your order is about to be prepared. You can still cancel at this point"
- Restaurant HCA says: not mentioned
- Correct version: Per the NPI, T-60 is the modification and cancellation cutoff, and T-15 is an informational dispatch-approaching notice. The Consumer HCA contradicts this in two ways: (1) it describes the T-60 notification as being about "dispatch" when it is actually a modification/cancellation cutoff notice, and (2) it states the consumer "can still cancel at this point" at T-15, which directly contradicts the NPI's T-60 cutoff rule.
- Fix required in: Consumer HCA

---

**INCONSISTENCY 2:**
- Topic: Restaurant "Unable to fulfil" flag — how far in advance it must be raised
- NPI says: "The restaurant receives a preparation reminder at T-75 and must flag 'Unable to fulfil' within 15 minutes of receiving that reminder — that is, before T-60 when the order formally enters their queue."
- Consumer HCA says: not mentioned
- Restaurant HCA says: "If you know in advance that you cannot fulfil a scheduled order... you must flag it at least 90 minutes before the delivery window."
- Correct version: Per the NPI, the cutoff for flagging "Unable to fulfil" is before T-60 (i.e., within 15 minutes of the T-75 reminder). The Restaurant HCA states the cutoff is T-90, which is 30 minutes earlier than the NPI specifies and is not supported anywhere in the NPI. This is a material discrepancy — restaurant partners reading the HCA will believe they have a harder deadline than the NPI establishes, which could create confusion or disputes.
- Fix required in: Restaurant HCA (or, if T-90 is intentionally conservative guidance, PM must confirm and update the NPI to align)

---

**INCONSISTENCY 3:**
- Topic: Restaurant preparation reminder — channel of delivery
- NPI says: "Restaurant receives a preparation reminder: push notification to GrabFood Partner app AND an alert in the order management dashboard"
- Consumer HCA says: not mentioned
- Restaurant HCA says: "your order management system sends a preparation reminder notification" (dashboard/system only — no mention of a push notification to the GrabFood Partner app)
- Correct version: Per the NPI, the reminder goes through two channels simultaneously — the GrabFood Partner app push notification AND the order management dashboard. The Restaurant HCA omits the Partner app push notification entirely, which means restaurant partners may not know to enable push notifications on the Partner app.
- Fix required in: Restaurant HCA

---

**INCONSISTENCY 4:**
- Topic: What the T-15 consumer notification says
- NPI says: "T-15 minutes: Consumer receives an informational push notification that dispatch is approaching"
- Consumer HCA says: "15 minutes before your delivery window: A heads-up that your order is about to be prepared."
- Restaurant HCA says: not mentioned
- Correct version: Per the NPI, the T-15 notification is about dispatch approaching, not about the order being "about to be prepared." These are meaningfully different — "about to be prepared" implies the restaurant hasn't started yet, whereas "dispatch is approaching" implies the food is nearly ready and a courier is about to be assigned. The Consumer HCA's version could set incorrect expectations for the consumer about the state of their order at T-15.
- Fix required in: Consumer HCA

---

**INCONSISTENCY 5:**
- Topic: Refund timeline for cancellations before the cutoff
- NPI says: "will receive a full automatic refund to their original payment method within 3–5 business days"
- Consumer HCA says: "You'll receive a full refund to your original payment method within 3–5 business days. If you paid with GrabPay credits, the refund is usually instant."
- Restaurant HCA says: "The customer is automatically notified and receives a full ref—" [document cut off]
- Correct version: The NPI states 3–5 business days uniformly. The Consumer HCA introduces a GrabPay-specific carve-out (instant refund) that does not appear in the NPI at all. This is either an undocumented rule that the NPI is missing, or the Consumer HCA is making a promise the platform has not confirmed. Either way it creates a cross-document gap. The NPI must be updated to include the GrabPay carve-out if it is accurate, or the Consumer HCA must remove it.
- Fix required in: NPI (add GrabPay carve-out if confirmed) OR Consumer HCA (remove if unconfirmed) — requires PM confirmation

---

**INCONSISTENCY 6:**
- Topic: Why a consumer might not see the "Schedule for later" toggle — reason given to the consumer
- NPI says: "Consumers who do not meet the account order history and standing criteria will not see the 'Schedule for later' toggle on the restaurant page." The CS agent checks order count and account standing and tells the consumer which criterion is not met.
- Consumer HCA says: "Not seeing the 'Schedule for later' option? The restaurant you're browsing may not have opted in yet. Try a different restaurant, or order as usual and check again another day."
- Restaurant HCA says: not mentioned
- Correct version: Per the NPI, the toggle is hidden based on the consumer's own eligibility (order history and account standing). The Consumer HCA attributes the missing toggle solely to the restaurant not having opted in, which is a separate and secondary reason. The HCA does not mention the primary eligibility reason at all — and in fact the NPI states earlier in the same section that eligible consumers will see the toggle on restaurant pages, implying restaurant opt-in status is already filtered upstream. Sending consumers to "try a different restaurant" when their account is actually ineligible wastes their time and will drive CS contacts. Additionally, the NPI explicitly states that consumers who don't meet the criteria will not see the toggle — meaning the HCA should acknowledge the account-eligibility reason as the primary explanation.
- Fix required in: Consumer HCA

---

**INCONSISTENCY 7:**
- Topic: Phase 2 eligibility criteria for Kuala Lumpur users
- NPI says: "Phase 2 (2026-07-28): All GrabFood users in good standing in Singapore; Kuala Lumpur users with ≥ 3 completed orders in the past 60 days and no active fraud flag or suspension"
- Consumer HCA says: "It's rolling out to Kuala Lumpur and other cities over the coming weeks." (No eligibility criteria specified for KL users)
- Restaurant HCA says: "28 July 2026 (Kuala Lumpur)" — date matches; no eligibility criteria for consumers mentioned
- Correct version: The Consumer HCA is underspecified. While it is acceptable for a consumer-facing HCA to avoid technical detail, the document should not omit the eligibility threshold if KL users will contact support asking why they cannot see the feature. At minimum, the Consumer HCA should note the 3-order requirement for KL at launch, consistent with its Singapore section. This is a lower-severity gap than others but will drive CS contacts.
- Fix required in: Consumer HCA (add KL eligibility note when the KL section is written or expanded)

---

**INCONSISTENCY 8:**
- Topic: Phase 3 regional cities — how they are described
- NPI says: "Phase 3 (2026-08-11): All GrabFood users in good standing in Thailand, Indonesia, and the Philippines" and in the Executive Summary "regional rollout to Thailand, Indonesia, and the Philippines"
- Consumer HCA says: not mentioned
- Restaurant HCA says: "11 August 2026 (Bangkok, Jakarta, Metro Manila — pending Phase 2 confirmation)"
- Correct version: The NPI names the countries (Thailand, Indonesia, Philippines) without specifying cities. The Restaurant HCA specifies the exact cities (Bangkok, Jakarta, Metro Manila) and adds the qualifier "pending Phase 2 confirmation." The NPI contains no such qualifier. If the Phase 3 launch is genuinely conditional on Phase 2 confirmation, the NPI must reflect this gate condition. If it is not, the qualifier must be removed from the Restaurant HCA. Additionally, if Phase 3 is city-specific rather than country-wide, the NPI should be updated to name the cities for precision.
- Fix required in: NPI (add city specificity and/or Phase 2 gate condition) OR Restaurant HCA (remove qualifier and/or city specificity if NPI is authoritative) — requires PM confirmation

---

## SUMMARY

**Total inconsistencies found: 8**

**Severity breakdown:**

*Consumer-facing (visible to end users or directly affecting CS responses):*
- Inconsistency 1 — Cancellation still possible at T-15 (Consumer HCA contradicts NPI cutoff rule — high severity, creates refund disputes)
- Inconsistency 4 — T-15 notification describes wrong event to consumer (low-to-medium severity, sets wrong expectations)
- Inconsistency 5 — GrabPay instant refund claim not in NPI (medium severity, creates refund expectation gap)
- Inconsistency 6 — Toggle invisibility explained as restaurant opt-in only, not consumer eligibility (high severity, misdirects consumers and drives CS contacts)
- Inconsistency 7 — KL eligibility criteria missing from Consumer HCA (low severity, will drive CS contacts at Phase 2 launch)

*Partner/internal-facing:*
- Inconsistency 2 — "Unable to fulfil" deadline stated as T-90 in Restaurant HCA vs. T-60 in NPI (high severity, creates contractual and operational ambiguity with restaurant partners)
- Inconsistency 3 — Partner app push notification channel omitted from Restaurant HCA (medium severity, partners may not enable app notifications)
- Inconsistency 8 — Phase 3 described as country-wide in NPI but city-specific with a gate condition in Restaurant HCA (medium severity, creates expectation mismatch with partners in those markets)

**Recommendation: Do not distribute. PM review required before fixes.**

Two inconsistencies (1 and 2) involve rules that will directly cause incorrect operational behaviour on launch day — CS agents will tell consumers they can cancel after the cutoff, and restaurant partners will believe they have a different compliance deadline than the NPI establishes. These cannot be resolved by a copy editor alone; they require the PM to confirm the authoritative rule and update accordingly. Inconsistency 5 (GrabPay refund timeline) and Inconsistency 8 (Phase 3 gate condition) also require PM confirmation before any document can be corrected. Once the PM has confirmed the correct rules for those four items, all eight fixes are straightforward and the package can be cleared for distribution.
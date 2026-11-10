---
fonte: https://help.asana.com/s/article/ai-studio-rate-limiting?language=en_US
baixado: 2026-11-10
---

# AI Studio rate limiting

AI Studio credit rate limiting helps protect your organization from sudden spikes in credit use. A misconfigured automation, bulk import, or frequently triggered workflow can use many credits in a short time. A per-automation credit limit pauses additional executions when usage reaches a threshold, giving someone time to review what happened.

## How credit rate limiting works

Each AI Studio automation has a credit limit for a rolling 60-minute window. Asana provides a recommended limit by default, and admins can adjust the credit amount. The 30-minute window itself is fixed.

When an automation reaches its limit, additional executions are placed on hold in a queue. An execution that is already in progress finishes normally, so total usage may end up slightly above the limit. Rate limiting is a guardrail against short-term spikes, not a hard spending cap.

Rule owners will receive a notification in their inbox when their rule is paused.

## See paused automations

Builders can check the **automation builder** and **execution activity** to see when an automation is on hold. Admins can review paused automations and the number of executions waiting in the **Execution activity** page of the **admin console**.

## Review queued executions

After reviewing why an automation reached its limit, you can resume the queue to run pending executions or cancel them. If no one takes action within 24 hours, queued executions expire. Editing an automation while it is on hold cancels its queued executions because they were created from the previous version of the automation.

You can also resume the queue by clicking the **Customize** button, click the **three dot icon** and select **Resume queue**.

Resuming the queue does not turn off the rate limit. If the limit is reached again, executions may be placed on hold. A person must choose to resume a paused automation; it does not resume automatically.

## Manage AI Studio rate limiting

Admins control two settings: the hourly credit limit for each automation, and who is notified when an automation reaches that limit.

### Who can configure rate limiting

Only Asana admins can change rate limiting settings. Automation builders can see when their automation is on hold, but they can’t change the limit or the notification preference.

### How to configure rate limiting

1.  Open the admin console and go to **Asana AI \> AI Studio \> Limits**.
2.  In the **Rate limits** card, click **Manage limit**.
3.  Under **Hourly rate limit**, enter the maximum credits per hour that a single automation can use. Leave the field blank for no limit, or click **Reset default** to restore Asana’s default.
4.  Under **Notification preference**, choose who receives an inbox notification when an automation reaches its limit:
    - **Automation owner only** (default)
    - **Automation owner and billing owner**
5.  Click **Save**.

Changes apply to executions going forward. Automations that are already on hold stay on hold until someone resumes or cancels their queue. To resume a paused automation, open it in the builder and select **Resume queue**. Automations can’t be resumed from the admin console.

### When to use these settings

**Adjust the hourly rate limit when:**

- You’re rolling out AI Studio to new teams or testing new automations. Keep or lower the limit so a mistake can’t consume many credits before someone notices.
- You’ve had a spike from a bulk import or a high-volume trigger and want a tighter guardrail.

**Don’t rely on these settings to:**

- Cap total spend. Rate limiting only catches short-term spikes. Automations that use credits steadily over a longer period won’t be paused.
- Stop in-progress executions. They finish normally so that usage can land slightly above the limit.

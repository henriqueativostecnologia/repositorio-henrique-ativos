---
fonte: https://support.google.com/appsheet/answer/16274771?hl=en
baixado: 2026-11-10
---

# Manage credits for Gemini usage

When you use [Gemini in AppSheet Solutions](https://support.google.com/appsheet/answer/16106353#solutions), you consume *credits* based on the number and complexity of the AI tasks that are run by users of the apps owned by creators in your organization. 

- [How to get credits for your organization](#get-credits)
- [How credits are consumed](#credits-consumed)
- [Monitor credit usage for your team or organization](#monitor-credit-usage)

## How to get credits for your organization

Your organization is automatically granted a full quota of AppSheet credits as part of your AppSheet Enterprise agreement. No separate Google Workspace license is needed for this feature.

Specifically, your organization receives **1000** credits per AppSheet Enterprise Plus license per month, accessible to all members as a pool. Availability of the credits depends on [how your AppSheet Enterprise Plus licenses are provisioned](https://support.google.com/appsheet/answer/14101111):

- With **pooled** licensing, the full quota of credits is available to the organization at the beginning of each month.
- With **assigned** licensing, the credits for assigned licenses are available to the organization at the beginning of the month. Credits for unassigned licenses are available once the licenses are assigned to user accounts.

Credit balances renew on a monthly basis. **Any remaining credits are not rolled over to the next month**.

To increase your credit quota, you'll need to purchase additional AppSheet Enterprise Plus licenses. If you require assistance with obtaining more credits, contact [AppSheet Support](https://www.appsheet.com/Support/Contact). 

**For example**:

If you have **10** AppSheet Enterprise Plus licenses in your organization, you'll receive up to 10,000 credits each month, accessible to all members as a pool. The number of **available** credits depends on the licensing model:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Licensing model**                                                           | **Credits available to organization/month**                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Pooled                                                                        | **10,000** credits (10 x 1000 credits/license)                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Assigned                                                                      | Depends on number of assigned licenses.                                       |
|                                                                               |                                                                               |
|                                                                               | **Example 1:**                                                                |
|                                                                               |                                                                               |
|                                                                               | There are **5 assigned** and **5 unassigned** licenses**:**                   |
|                                                                               |                                                                               |
|                                                                               | -   **5000 credits** (5 x 1000 credits/license)                               |
|                                                                               | -   **1000** credits per additional assigned license                          |
|                                                                               |                                                                               |
|                                                                               | ---------------------------------------------------------------------------   |
|                                                                               |                                                                               |
|                                                                               | **Example 2:**                                                                |
|                                                                               |                                                                               |
|                                                                               | All **10 licenses assigned**:                                                 |
|                                                                               |                                                                               |
|                                                                               | **10,000** credits (10 x 1000 credits/license)                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## How credits are consumed

Credits are consumed based on the number and complexity of the AI tasks that are run in both deployed and prototype apps, or when [testing a step in an automation](https://support.google.com/appsheet/answer/15960410).

The following table summarizes the credit consumed by AI tasks.

|                              |                      |
|------------------------------|----------------------|
| **AI task**                  | **Credits consumed** |
| Categorize AI task           | 10 credits           |
| Extract AI task: image, text | 10 credits           |
| Extract AI task: PDF         | 10 credits per page  |
| Extract rows AI task: image  | 10 credits           |
| Extract rows AI task: PDF    | 10 credits per page  |
| Summarize AI task            | 10 credits           |

## Monitor credit usage for your team or organization

As the team or organization admin, using the [Gemini usage](https://support.google.com/appsheet/answer/16058407) page in the AppSheet Admin Console you can monitor the credit consumption and Gemini usage in apps for your team or organization.

Specifically, you can view:

- Number of credits that have been consumed by your organization
- Which apps are using the most credits and drill-down to view the active users in the last 30 days
- Which app owners that have active AI-powered apps
- Total number of AI task runs and date of the last run 

In addition, you can monitor Gemini usage using the following tools:

- [Audit History](https://support.google.com/appsheet/answer/10104794)
- [Automation monitor](https://support.google.com/appsheet/answer/11447502)

---
fonte: https://help.asana.com/s/article/understanding-asana-ai-requests-and-usage-allocation?language=en_US
baixado: 2026-11-10
---

# Understanding Asana AI requests and usage allocation

Starting September 2026, your organization will gain access to advanced AI capabilities, including [AI Teammates](https://help.asana.com/s/article/ai-teammates) and [Asana Dash](https://help.asana.com/s/article/chat-with-dash) if AI has been enabled in your organization. To power these features, your subscription includes an allocation of AI Requests. This article explains how AI requests are calculated, pooled across your organization, tracked, and managed.

Video: https://fast.wistia.net/embed/iframe/s7kvib197e?web_component=true&seo=true&videoFoam=false

## What is an AI request?

An AI Request is the core metric for measuring your organization's AI usage. A request is defined as a single, successful unit of work completed by Asana.

### When it counts 

A request begins the moment a user invokes an AI action and ends when the task is successfully completed. The following tasks count as a request:

- **Completed tasks:** Dash or an AI Teammate finishes working on a user-initiated task.
- **Follow-up questions or instructions:** A user asks a follow-up question after Dash or an AI Teammate has already finished a task.
- **Revisions:** A user requests a revision to the specific work produced by an AI Teammate.
- **Implicit context changes:** An AI Teammate is a collaborator on a task, and a user posts a follow-up comment *without* explicitly @mentioning the teammate. The AI Teammate will evaluate if the comment is directed at them; if it determines it is, it will begin working and consume a request.

### What does not count 

Your organization is only charged for requests that result in actual, successful task execution or substantive data generation. The following interactions will **not** consume your AI Requests:

- **Failures or cancellations:** An AI Request is not consumed if the interaction results in a system failure, a timeout, or is canceled by either the user before completion. 
- **Adding context mid-task:** A user comments with additional context while an AI Teammate is *actively* working on a task.
- **Casual chat and feedback:** Short, non-substantive messages, polite greetings or closings, and quick coaching notes (e.g., saying "Hello," "Thank you," "Okay," or "Good job, remember this format for next time") are automatically filtered out and will not count.

**Dash interactions that do not consume AI Requests:** In addition, the following interactions with Asana Dash will **not** consume your AI Requests:

- **Clarifying prompts:** When Asana Dash asks for clarification, additional context, or confirmation before it begins building a project, portfolio, or handing off a task.
- **Find information:** Asking Asana Dash to help you find a specific existing task, teammate, due date, project, or content without requiring complex data summaries or insights.
- **Questions about work in Asana:** Asking Dash to find, explain, summarize, compare, prioritize, or catch you up on work in Asana. Find tasks or projects, check status, see what changed, count or compare work, ask what to focus on next, get context before a meeting, or get light suggestions based on your work.
- **Asana Product guidance:** For example, learning how to build an Asana workflow, exploring available capabilities, or what would be the best template to use for structuring work.
- **Content edit**: Polishing existing text (like correcting typos or shortening titles) and writing brief comments or task summaries (e.g., "Write a description for this task"). 
- **Creating or updating basic objects:** Setting up tasks, adding comments, altering a task’s custom fields, or moving items to a new section (e.g., "Create a task for the API migration", "Move these to Done", or "Set priority to high").
- **Creating new projects and Automations**: Generating a new project from a brief, template, or description, as well as setting up automated rules to move tasks around or scheduling recurring syncs and reviews.
- **Scanning files**: Extracting summaries from attached PDFs and linked documents.

## How request allotments and pooling work

Your monthly allocation of included AI Requests is determined by your subscription tier.

### Included allotments by tier

|                              |                                                                                                                    |
|------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Subscription tier**        | **Monthly allocation structure**                                                                                   |
| **Starter & Advanced**       | 5 requests per user per month, up to a total of 50 shared requests per month aggregated at the organization level. |
| **Enterprise & Enterprise+** | 5 requests per user per month, up to a total of 250 shared requests aggregated at the organization level.          |

> To see the exact, real-time allocation and request balance for your specific plan, admins can always check the admin console.

- **Organization-level pooling:** AI requests are provisioned as a pooled resource at the organization level rather than being restricted to individual accounts. All users within your organization draw from this single, shared aggregate pool.
- **Flexible distribution:** While the total size of your request pool is calculated based on user counts, there are no caps placed on individual users. Any team member can use as many requests from the shared pool as needed, as long as the organization’s aggregate balance has not been exhausted. 
- **Shared pool for Asana Dash and AI Teammates:** Asana Dash and AI Teammates draw from the exact same request pool. For Asana Dash, simple day-to-day actions like basic task orchestration or posting comments do not consume requests. However, once Asana Dash performs complex work or hands a task off to an AI Teammate, it will count against your monthly pool. Please note that all interactions with AI Teammates count toward your organization's request usage.
- **Monthly reset:** This allocation of included requests refreshes monthly. Unused included requests expire at the end of the month and do not roll over.

## Tracking and managing usage 

To maintain centralized financial governance, purchasing power and full usage visibility are restricted exclusively to admins and billing owners.

- **Usage dashboard:** Admins have access to a centralized view in the admin console that surfaces real-time consumption metrics. This dashboard tracks total requests used month-to-date (MTD) and year-to-date (YTD), displays the remaining account balance, and provides a breakdown of usage per user to help monitor adoption.
- **Automated threshold alerts:** The system will automatically trigger email and in-product notifications to administrators when the organization reaches 65%, 85%, and 100% of its monthly request allotment.

## What happens when allotments are exhausted?

As your organization uses AI features, requests are deducted from your account in a specific sequence: first from your included plan allotment, then from prepaid usage packs, and finally from on-demand billing.

If your organization exhausts its included monthly requests and you do not have on-demand billing enabled or extra capacity purchased, AI Teammates and Asana Dash functions will be temporarily paused until the next monthly refresh or until you purchase a usage pack or enable on-demand billing.

- **User experience:** Regular team members will be clearly notified at the time they attempt to use a paused feature. They will see a generic prompt indicating that AI usage has run out and will be given an option to notify their admin to request more capacity.
- **Admin experience:** Admins will receive in-product and email notifications confirming the limit has been reached, prompting them to manage settings or add capacity.

## Adding additional AI capacity

Admins can ensure uninterrupted workflows and expand their available request limits through two main options in the admin console:

1.  **Prepaid usage packs:** Admins can purchase pre-bundled packs of extra requests upfront. These packs remain valid for the entire duration of your current billing cycle rather than resetting monthly, though any unused prepaid capacity expires at the conclusion of your contract term.
2.  **Some customers will have on-demand billing:** Admins can choose to enable on-demand billing to pay for usage beyond their included amount. Additional usage is aggregated and billed or charged in arrears, subject to standard billing cycles or minimum account thresholds. To protect your organization from unexpected expenses, on-demand status requires explicit administrative activation and will never turn on without prior customer action. Additionally, admins can set their in-product overage cap to \$0 to completely prevent any extra charges.

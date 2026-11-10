---
fonte: https://www.notion.com/help/understand-pricing-for-workers
baixado: 2026-11-10
---

# Understand pricing for Workers (beta)

In this help doc

## Learn how Workers use Notion credits, what affects Worker credit usage, how to plan costs, and where to view usage.

[Jump to FAQs](https://www.notion.com/help/understand-pricing-for-workers#faq)

------------------------------------------------------------------------

[Workers](https://www.notion.com/help/run-custom-code-with-workers) run code in the background to automate tasks in Notion. They’re best for tasks that don’t require AI reasoning, such as syncing data, writing updates, and handling events. Workers are often paired with [Custom Agents](https://www.notion.com/help/custom-agents), where the agent decides what to do and Workers reliably execute specific steps.

During the beta, Workers are free to try on Business and Enterprise plans (including Business trials). Eventually, they’ll require Notion credits. Workspace admins can purchase Notion credits as an add-on to Business and Enterprise plans.

The free beta period applies only to Workers. Custom Agent actions will consume credits according to your workspace’s plan and credit settings.

## [Notion credits for Workers](https://www.notion.com/help/understand-pricing-for-workers#notion-credits-for-workers)

Workers use Notion credits, which are counted in runs. Each run represents one unit of work completed on your behalf. The number of credits per run can vary depending on how much work the Worker does, like how long it runs or how much processing it needs. In general, the more work involved, the more credits used.

Workers can run in a few different ways (we’ll keep expanding this list):

- **Syncs (scheduled):** Each time a sync runs counts as one run.

- **Tool calls (agent-triggered):** Each time a Custom Agent triggers a Worker tool call counts as one run.

- **Webhooks (event-driven):** Each event a Worker handles counts as one run.

## [How much is one Worker run?](https://www.notion.com/help/understand-pricing-for-workers#how-much-is-one-worker-run)

Workers typically cost \$0.0023 per run, which works out to ~4,348 runs per 1,000 monthly Notion credits (\$10). They’re cheaper compared to [Custom Agents](https://www.notion.com/help/custom-agents) because pricing is based on how much work they do when they run and they don’t require AI decision-making.

The tables below break down cost benchmarks for each type of Worker action. Use this as a starting point to understand costs. Your actual usage may vary, and is the best way to size credits.

## [Examples: scheduled sync credit usage](https://www.notion.com/help/understand-pricing-for-workers#examples-scheduled-sync-credit-usage)

The examples below show types of sync usage. Your actual usage depends on how often your syncs run and how much a Worker does for each run.

Syncing more data or handling several updates will cost more. If you have multiple syncs, multiple Workers, or Workers that run in response to many events, total usage may be higher.

**Example 1:** A nightly sync pulls closed Jira tickets into a Notion engineering log for weekly review.

- **Sync frequency:** Daily (Low)

- **Runs per day: 1**

- **Cost per month:** \$0.07

**Example 2:** An hourly Zendesk sync refreshes open tickets and SLA risk in a Support Ops dashboard in Notion, so team leads can rebalance coverage throughout the day.

- **Sync frequency:** Hourly (Medium)

- **Runs per day:** 24

- **Cost per month:** \$1.66

**Example 3:** A pipeline sync keeps a Notion sales tracker updated with Salesforce opportunity stages throughout the business day.

- **Sync frequency:** Every 15 minutes (High)

- **Runs per day:** 96

- **Cost per month:** \$6.62

**Example of estimating monthly credits**

You sync Salesforce opportunities into a Notion database every 15 minutes and it costs \$0.0023 per run.

- **Worker runs per month:** 24 hours × 4 runs/hour x 30 days = 2880 runs/month

- **Monthly cost:** 2880 × \$0.0023 = \$6.62/month

- **Monthly credits needed:** \$6.62/\$0.01 per credit = 662 credits/month

## [Examples: Tool calls (agent-triggered)](https://www.notion.com/help/understand-pricing-for-workers#examples-tool-calls-(agent-triggered))

Workers can also power custom tools that Custom Agents use. For example, a Custom Agent might call a Worker to fetch data from another system, run a calculation, or update records.

Tool-call usage depends on how often an agent calls a Worker. Each tool call counts as its own Worker run (so one agent run can generate multiple Worker runs).

**Example 1:** A daily Bug Tracker agent reviews open Jira issues. Each run triggers the worker to fetch issue status, check for blockers, and write a summary to a Notion project page.

- **Volume of tool calls:** Scheduled (low)

- **Worker runs:** 3 per Custom Agent run

- **Custom Agent runs:** 30 per month

- **Cost per month:** \$0.21

**Example 2:** A RevOps agent runs when a deal moves stages in Salesforce. Each run triggers the worker to validate required fields, call Clearbit for enrichment, and write the record back to a Notion pipeline tracker.

- **Volume of tool calls:** Activity-triggered (Medium)

- **Worker runs:** 4 per Custom Agent run

- **Custom Agent runs:** 3,000 per month

- **Cost per month:** \$27.60

**Example 3:** A Support Eng agent runs on every inbound Zendesk ticket. Each run triggers the worker to fetch the ticket, pull Salesforce account context, apply routing rules from Notion, and post to the right Slack channel.

- **Volume of tool calls:** Continuous (High)

- **Worker runs:** 5 per Custom Agent run

- **Custom Agent runs:** 9,000 per month

- **Cost per month:** \$103.50

**Example of estimating monthly credits**

A Custom Agent makes 4 tool calls per run and runs 50 times per day. Each tool call execution costs \$0.0023.

- **Worker runs per month:** 4 x 50 x 30 = 6000 runs/month

- **Monthly cost:** 6000 x \$0.0023 = \$13.80/month

- **Monthly credits needed:** \$13.80/\$0.01 per credit = 1380 credits/month

## [Examples: Webhooks (alpha)](https://www.notion.com/help/understand-pricing-for-workers#examples-webhooks-(alpha))

The examples below show typical webhook volumes and what they might cost. Your actual usage depends on how many events your tools send and how many webhook triggers you’ve set up. Each incoming event that you handle counts as one Worker run, so total cost scales with your event volume.

**Example 1:** A Stripe webhook fires on subscription creates and cancels. The worker updates a Notion billing tracker with event details.

- **Volume of incoming events:** Low

- **Events per day:** 20

- **Cost per month:** \$1.38

**Example 2:** A GitHub webhook fires on every PR merge across 10 repos. The worker logs each merge to a Notion changelog and notifies the relevant Slack channel.

- **Volume of incoming events:** Medium

- **Events per day:** 200

- **Cost per month:** \$13.80

**Example 3:** A Zendesk webhook fires on every ticket create and status change. The worker enriches each event with Salesforce account data and updates a Notion support dashboard.

- **Volume of incoming events:** High

- **Events per day:** 5,000

- **Cost per month:** \$345.00

**Estimating monthly credits**

A Stripe webhook triggers on subscription creates and cancels, and you receive 300 events a day. Each run costs \$0.0023.

- **Worker runs per month:** 300 × 30 = 9000 runs/month

- **Monthly cost:** 6,000 × \$0.0023 = \$20.70/month

- **Monthly credits needed:** \$20.70/\$0.01 per credit = 2,070 credits/month

## [Track usage in the Notion CLI](https://www.notion.com/help/understand-pricing-for-workers#track-usage-in-the-notion-cli)

During the free beta, you can track Worker credit usage over the last 30 days directly in the [CLI](https://www.notion.com/help/use-notion-from-your-terminal-with-notion-cli).

### [**View usage for a specific Worker (detailed)**](https://www.notion.com/help/understand-pricing-for-workers#view-usage-for-a-specific-worker-(detailed))

Shows a detailed breakdown for one Worker’s usage over the last 30 days. This includes estimated preview credits, execution count, and runtime/network metrics that help explain what’s driving usage.

### [**View usage across all Workers (summary)**](https://www.notion.com/help/understand-pricing-for-workers#view-usage-across-all-workers-(summary))

Shows a summary of all Workers, including estimated preview credits used and executions over the last 30 days.

### [Track usage in the Notion credits dashboard](https://www.notion.com/help/understand-pricing-for-workers#track-usage-in-the-notion-credits-dashboard)

You can view Worker usage in the Notion credits dashboard:

1.  Go to `Settings` in the sidebar.

2.  Select `Access & billing` → `Notion credits`.

Admins and Worker creators can see the following for each Worker:

- Credits used

- Runs completed

- Status

- Creator

During the beta period, Workers appear in the dashboard with a **Free** badge. Hover over the badge to see when the free period ends. Worker usage does not count against your credit balance during beta.

The **Spend limits** column shows **N/A** for Workers until credit limits become available.

## [Admin controls for Workers](https://www.notion.com/help/understand-pricing-for-workers#admin-controls-for-workers)

You can manage Workers across your workspace by going to `Settings`, and selecting the Workers tab.

From here, you can:

- Switch Workers on or off for your workspace. By default, Workers are turned on for owners.

- Control who can use Workers, including specific people or user groups.

- Track and manage individual Workers.

  - View all Workers in your workspace, including their owner and status.

  - Disable or delete a Worker at any time.

  - Pause all Workers.

## [Sizing credit needs for Workers](https://www.notion.com/help/understand-pricing-for-workers#sizing-credit-needs-for-workers)

Workers are free during beta, so you can use this time to run real workflows and estimate how many credits you’ll need once credits apply.

## [How to optimize Worker credit usage](https://www.notion.com/help/understand-pricing-for-workers#how-to-optimize-worker-credit-usage)

Try these best practices to keep Worker usage predictable:

- **Start with a slow schedule.** For syncs, start with hourly or daily runs if real-time updates aren’t required.

- **Increase frequency only when needed.** Move to every 15 minutes, 5 minutes, or every minute only if the workflow requires it.

- **Batch work when possible.** Instead of running a Worker for every small change, group updates together.

- **Sync only what you need.** Sync only the databases, records, or fields that are needed.

- **Avoid unnecessary retries.** If a Worker fails, make sure it doesn’t retry too frequently without resolving the underlying issue.

- **Review usage regularly.** Check CLI usage during setup and after major workflow changes.

------------------------------------------------------------------------

## FAQs

What are micro credits?

Micro credits are smaller units of Notion credit consumption. Workers use micro credits because they run predictable, repeatable code. Custom Agents usually use more credits because they rely on AI to think through decisions and next steps.

Do Workers use the same Notion credits as Custom Agents?

Yes. Workers are part of the broader Notion credits system. However, Worker actions are designed to consume smaller amounts of credits than Custom Agent actions.

Why does sync frequency affect cost?

Each scheduled sync run counts as a Worker run. A sync that runs every minute runs 1,440 times per day, while a sync that runs daily runs once per day. More runs mean more credit usage.

Where can I see Worker credit usage?

You can see Worker credit usage in the [CLI](https://www.notion.com/help/www.notion.com/help/use-notion-from-your-terminal-with-notion-cli).

Admins and Worker creators can also view usage directly in the Notion credits dashboard. Go to `Settings` → `Access & billing` → `Notion credits` and select the **Workers** tab.

## Contents

- [Notion credits for Workers](#notion-credits-for-workers)
- [How much is one Worker run?](#how-much-is-one-worker-run)
- [Examples: scheduled sync credit usage](#examples-scheduled-sync-credit-usage)
- [Examples: Tool calls (agent-triggered)](#examples-tool-calls-(agent-triggered))
- [Examples: Webhooks (alpha)](#examples-webhooks-(alpha))
- [Track usage in the Notion CLI](#track-usage-in-the-notion-cli)
- [View usage for a specific Worker (detailed)](#view-usage-for-a-specific-worker-(detailed))
- [View usage across all Workers (summary)](#view-usage-across-all-workers-(summary))
- [Track usage in the Notion credits dashboard](#track-usage-in-the-notion-credits-dashboard)
- [Admin controls for Workers](#admin-controls-for-workers)
- [Sizing credit needs for Workers](#sizing-credit-needs-for-workers)
- [How to optimize Worker credit usage](#how-to-optimize-worker-credit-usage)

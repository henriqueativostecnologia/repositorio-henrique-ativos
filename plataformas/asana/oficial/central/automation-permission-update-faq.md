---
fonte: https://help.asana.com/s/article/automation-permission-update-faq?language=en_US
baixado: 2026-11-10
---

# Automation permission update FAQ

*Rules will soon run using the rule owner’s real-time permissions. Here’s what you need to know and how to prepare.*

## What is changing?

Today, some automation rules continue running even when the rule owner no longer has access to the projects, tasks, fields, or other items the rule interacts with.

Going forward, rules will consistently use the rule owner’s **current, real-time permissions**. For a rule to run successfully, the rule owner must have access to:

- The items the rule references (projects, fields, portfolios, etc.)
- The actions the rule is trying to perform

## Why is this change happening?

This update improves three key areas:

- **Security** — removes cases where rules continue operating using outdated access
- **Consistency** — creates a unified permission model across automation systems
- **Transparency** — makes it clearer whose permissions a rule is using

## What happens if the rule owner lacks access?

If the rule owner doesn’t have the required access when this change takes effect, the rule may:

- Fail to execute successfully
- Leave certain actions incomplete
- Pause or surface permission-related errors

> Asana will proactively notify impacted rule owners before the migration occurs, with time to review and resolve any issues.

## How will I be notified?

Impacted users will receive proactive notifications before the change rolls out via two channels:

### Email notifications

- Which rules may be affected
- Why the rule may stop working
- Steps to resolve before migration

### In-product project banners

- Awareness of impacted rules in the project
- Guidance on resolving issues before the change takes effect

## How do I fix an impacted rule?

There are two ways to resolve an impacted rule:

### Option 1: Give the rule owner access

Ensure the current rule owner has access to all referenced items and permissions to perform all rule actions:

- Projects, portfolios, tasks, and fields
- Objects the rule needs to update
- Permission to perform the actions the rule carries out

### Option 2: Have someone else claim the rule

Project admin or another editor with all the necessary permission can claim ownership of the rule to prevent any issues. 

## Other common questions

### Will all rules be impacted?

No. Most rules will continue working normally. Only rules where the owner lacks access to required items or actions may be affected.

### What is the “rule owner”?

It is typically the person who created the rule, and can be found and updated in the rule's settings within the rule builder. Under the new model, rules execute using the owner's permissions at the exact time the rule runs — not the permissions they had when the rule was created.

### When will this change happen?

Impacted users will be notified in June advance before the new permission model is enabled. This gives customers time to review affected rules, update access where needed, and have new owners claim rules as appropriate. August is when the change is planned to kick in

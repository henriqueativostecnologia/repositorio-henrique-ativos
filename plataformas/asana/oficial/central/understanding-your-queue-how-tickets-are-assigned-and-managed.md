---
fonte: https://help.asana.com/s/article/understanding-your-queue-How-tickets-are-assigned-and-managed?language=en_US
baixado: 2026-11-10
---

# Understanding your queue: How tickets are assigned and managed

Your queue helps you see the tickets that need your attention in Asana Service Management. This article explains how tickets are assigned, how to claim and resolve tickets, how collaborators and approvals work, and what to expect when a ticket moves between queues.

## How tickets are assigned to you

A queue acts like a shared inbox for your team. Claim a ticket from the queue to start working on it. You will only see the queues that you have been explicitly added to.

## How to claim, update, and resolve a ticket

To start working on a ticket, open it from your queue and assign it to yourself using the **Assignee** field. As you work, update the **Status** field and add comments so your team members can follow progress.

The ticket status moves through states such as **Open**, **In Progress**, **Waiting on requester,** **On Hold**, and **Resolved**. Your admin defines which states are available in your queue. 

## How to add and manage collaborators

Collaborators help you bring the right people into a ticket without changing who owns it. Add collaborators when someone needs context, input, or visibility, and remove them when they no longer need to follow the work.

You can add a collaborator by opening the ticket and updating the **Collaborators** field. Mentioning someone in a comment will also add them as a collaborator.

To remove a collaborator, click the **X** next to their name. This stops their notifications but does not delete their past comments.

##

## How to transfer a ticket between queues

If a ticket needs to be handled by a different team, you can move it to another queue. The full ticket history will remain in one place so the next team can review the context and continue the work without starting over. The ticket ID will stay the same when a ticket is moved between queues. 

**To move a ticket:**

1.  Navigate to the ticket
2.  Click on the queue in the right column of the ticket
3.  Type the name of the new queue or select from the list of queues
4.  Click **Move**

> Tickets received via [Slack](https://help.asana.com/s/article/how-to-connect-asana-service-to-slack?language=en_US) or email cannot be moved between queues.

> The SLA will reset when a ticket moves between queues, and the ticket will use the SLA timer of the new queue. Resolution credit goes to the queue that holds the ticket when it closes.

## Understanding SLA timers

Service level agreement (SLA) timers help your team track how long a ticket has been waiting for a response or resolution. They give your team a clear way to see when action is needed and help teams stay on top of service goals.

Asana Service tracks these timers automatically from when a ticket is created. First response SLA timers count down time from when a ticket is created until its initial response. Resolution SLA counts down until the ticket is resolved. 

SLA timers are [defined and configured by your queue admin](https://help.asana.com/s/article/configuring-slas-and-work-schedules). This includes category-level SLAs with the ability to override the default SLA.

> If your team uses an **On Hold** or **Waiting on requester** status, the SLA timer will pause when a ticket moves to **On Hold** or **Waiting on requester**, and resume when it moves back to **In progress** or **Open**.

## How approvals work on a ticket

Approvals help you bring another person into the ticket when a decision is needed before work can continue. For example, when someone needs to confirm a next step, review a proposed action, or decide whether the work should move forward.

In Asana Service, approvals are handled through ticket comments. Mentioning the approver in a comment will add them as a collaborator. They can then review the context of the ticket and state their approval in the comments.

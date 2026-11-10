---
fonte: https://help.asana.com/s/article/how-to-configure-ticket-statuses?language=en_US
baixado: 2026-11-10
---

# How to configure ticket statuses

Ticket statuses show where a ticket is in its lifecycle. Asana Service Management includes default system statuses, and queue admins can customize status names or add statuses to match their team’s workflow.

## Default ticket statuses

Each queue includes the following system statuses:

1.  **Open:** The ticket has been received and is waiting for action.
2.  **In Progress:** An agent is actively working on the ticket.
3.  **Waiting on requester:** Work is paused while the team waits for the submitter to respond.
4.  **On Hold:** Work is paused, typically while waiting for a third party.
5.  **Resolved:** The issue has been addressed.

> System statuses can be renamed, but they cannot be deleted.

To view system statuses:

1.  Navigate to the queue under **Queues** in the sidebar
2.  Click **Settings** at the top-right corner
3.  Under **Customizations**, click **Status**
4.  From here, you can edit the statuses

## Add a custom status

Each custom status belongs to a parent category. The parent category determines how the status affects SLA timers and how it appears in reports.

To add a custom status: 

1.  Navigate to the queue
2.  Click **Settings** at the top-right corner
3.  Under **Customizations**, click **Status**
4.  Choose the status category that best describes where the new status falls in the ticket lifecycle, then click **+ Add an option** 
5.  Enter a name for the status
6.  Click **Save**

> You can rename or delete custom statuses from queue settings at any time. System statuses can be renamed, but they cannot be deleted.

## Understand how statuses affect SLA timers

SLA timers pause when a ticket moves to **On Hold** or **Waiting on requester**. The timers resume when the ticket moves back to an active status.

Custom statuses inherit the SLA behavior of their parent category. A custom status in the **On Hold** category pauses SLA timers, while a custom status in the **Open** or **In Progress** category keeps the timers running.

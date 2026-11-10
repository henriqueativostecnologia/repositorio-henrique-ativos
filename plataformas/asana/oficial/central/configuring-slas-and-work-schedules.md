---
fonte: https://help.asana.com/s/article/configuring-slas-and-work-schedules?language=en_US
baixado: 2026-11-10
---

# Configuring SLAs and work schedules

Use SLAs (service level agreements) to define how quickly your team commits to responding to and resolving tickets. Asana Service Management tracks these timers automatically and highlights any tickets that are at risk of missing their deadline.

## Queue-level SLA targets

SLA targets are configured at the queue level, so each team can set time targets that suit their workload. SLAs can be defined for both resolution** **and first response across each priority level.

First response SLA tracks the time between ticket creation and an agent's first reply. Resolution SLA tracks the time between creation and the ticket being marked resolved.

### To configure SLA targets for a queue:

1.  Navigate to the queue you want to configure.
2.  Click **Settings**.
3.  Click **Service Level Agreement**.
4.  Click on the **Resolution SLA** or **First Response SLA.**
5.  Enter your **Queue SLA target**.
6.  Click **Save**.

> Both SLA timers run independently and are visible on each ticket.

## Category-level SLA targets

For tickets that need a fixed resolution window regardless of priority, you can set category-level SLA targets to override the default SLA. For example, an IT queue might apply a 30-minute resolution target to outage tickets, while regular tickets continue to follow standard targets.

[Category options](https://help.asana.com/s/article/an-admins-guide-to-asana-service-management) must be set up before category-level SLA targets become available in queue settings.

### To set a category-level SLA target:

1.  Navigate to the queue you want to configure.
2.  Click **Settings**.
3.  Click **Service Level Agreement**.
4.  Click on the **Resolution SLA** or **First Response SLA.**
5.  Click **Add category override** beneath **Queue SLA target**.
6.  Click on the category for which you wish to apply an override SLA.
7.  Enter your **SLA target** for that category.
8.  Click **Save**.

## Customize your work schedule

You can customize your work schedule for each queue to ensure SLA timers only count time during business hours. Working hours apply to all SLA timers in that queue.

### To customize your schedule:

1.  Navigate to the queue you want to configure.
2.  Click **Settings**.
3.  Click **Schedule**.
4.  Set your team's **Work days** to **Business days**, **Every day**, or **Custom**.
5.  Toggle on **Choose work hours** to select a **Timezone** and specify **Work hours**. 
6.  Click **Save**.

> Work schedules are set at the individual queue level. If you manage multiple queues with different team schedules, configure separate schedules for each queue.

## How SLA timers work

Once your SLA targets and working hours are in place, Asana Service Management handles timer tracking automatically on every ticket.

Timers start when a ticket is created and pause when a ticket is set to **On Hold** or **Waiting on requester**. They resume automatically when the ticket moves back to an active status. 

Tickets approaching their deadline are flagged visually in the queue feed, and any ticket that has missed its target is marked as overdue.

## Set SLA targets by priority

You can set different SLA targets for different ticket priorities within a queue. For example, you can set a shorter target for Critical tickets and a longer target for Low-priority tickets.

Open the queue’s SLA settings and configure the target for each priority supported by your queue. Use the queue’s SLA configuration to align response and resolution expectations with the service your team provides.

---
fonte: https://help.asana.com/s/article/customizing-queue-automations-in-asana-service-management?language=en_US
baixado: 2026-11-10
---

# Customizing queue automations in Asana Service Management

Asana Service Management provides supported automations that help you route tickets, follow up with submitters, and alert agents when a ticket needs attention. Queue admins can configure these settings for each queue using focused controls.

### Related articles:

- [An admin’s guide to Asana Service Management](https://help.asana.com/s/article/an-admins-guide-to-asana-service-management)
- [Understanding your queue: How tickets are assigned and managed](https://help.asana.com/s/article/understanding-your-queue-How-tickets-are-assigned-and-managed)
- [Queue and ticket permissions](https://help.asana.com/s/article/queue-and-ticket-permissions)
- [Configuring SLAs and work schedules](https://help.asana.com/s/article/configuring-slas-and-work-schedules)
- [How to configure queue categories and custom fields](https://help.asana.com/s/article/how-to-configure-queue-categories-and-custom-fields?language=en_US)

## Customize ticket assignment

Turn on **Auto-assignment** for a queue to route tickets automatically. Asana uses round-robin assignment across eligible queue members. Agents marked as out of office in their Asana profile are skipped.

To route specific work, configure assignment by category. Map a category value, such as Hardware or Payroll, to an agent. When a ticket matches that category, Asana assigns it to the mapped agent.

You can also configure assignment by submitter location. Map a location to an agent, such as London to the EMEA IT agent. Location information is sourced from SCIM data, and Asana applies the mapping when the ticket is submitted.

## Configure submitter follow-ups and auto-close

Tickets in the **Waiting on requester** status category can auto-close after seven days without activity.

You can choose whether follow-up notifications are sent  for tickets waiting on the requester. You can configure the timing and number of follow-ups.

## Set ticket alerts and escalation contacts

Add one or more queue members as escalation contacts for a queue. Escalation contacts are notified when a ticket breaches, is about to breach its SLA or remains inactive beyond the configured threshold. The agent assigned to the ticket can also be alerted.

 

Alerts are added as private comments with mentions. These internal alerts are not visible to the submitter.

Alerts apply to open and in progress tickets. They do not apply to tickets that are on hold, waiting on the submitter, or resolved. 

## Use supported automation templates

Queue automations use supported templates with focused, editable inputs. This approach gives admins useful flexibility while keeping ticket behavior and reporting consistent across queues.

Queue-specific fields, category options, and ticket statuses are configured separately from automation settings. These automations do not provide a general-purpose builder for arbitrary branching workflows.

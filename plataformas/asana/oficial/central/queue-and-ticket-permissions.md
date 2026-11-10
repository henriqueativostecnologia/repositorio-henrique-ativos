---
fonte: https://help.asana.com/s/article/queue-and-ticket-permissions?language=en_US
baixado: 2026-11-10
---

# Queue and ticket permissions

In Asana Service Management, queue members can have one of two access levels: Queue Admin or Editor. These roles determine what people can do in the queue itself and on the tickets it contains. 

Requesters (employees who submit requests) can still view and update their own tickets, and they do not need to have membership of the queue. All queues within an organization are private, so only added members can see a queue and all of its tickets.

## Queue permissions

The table below outlines what each role can do.

| **Action**                                        | **Queue Admin** | **Editor** | **Requester or ticket collaborator** |
|---------------------------------------------------|-----------------|------------|--------------------------------------|
| Configure queue details (name, description)       | ✓               | ✗          | ✗                                    |
| Manage intake channels (form, Slack, email)       | ✓               | ✗          | ✗                                    |
| Configure SLA policies and working hours          | ✓               | ✗          | ✗                                    |
| Modify category options and custom fields         | ✓               | ✗          | ✗                                    |
| Add or remove agents from queue                   | ✓               | ✗          | ✗                                    |
| View all tickets in queue                         | ✓               | ✓          | ✗                                    |
| Claim and assign tickets                          | ✓               | ✓          | ✗                                    |
| Update ticket fields (status, priority, category) | ✓               | ✓          | ✗                                    |
| Add public comments                               | ✓               | ✓          | own tickets only                     |
| Add private (agent-only) comments                 | ✓               | ✓          | ✗                                    |
| Transfer ticket to another queue                  | ✓               | ✓          | ✗                                    |
| View SLA timers                                   | ✓               | ✓          | ✗                                    |
| View own submitted tickets                        | ✓               | ✓          | ✓                                    |

## Things to know

Queue Admins and Editors can transfer tickets to any queue, even if they are not members of that queue. They will not get access to the new queue, but will retain access to the ticket if they are a collaborator. 

Requesters can add comments to their own tickets, including closed tickets, but they cannot view other employees’ tickets or agent-only fields like SLA timers.

Tickets and comments cannot be deleted by agents, admins, or through the API.

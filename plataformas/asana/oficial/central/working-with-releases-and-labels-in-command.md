---
fonte: https://help.asana.com/s/article/working-with-releases-and-labels-in-command?language=en_US
baixado: 2026-11-10
---

# Working with releases and labels in Command

Releases and labels help you organize tickets in Command by Asana. Use labels to group tickets by theme, component, or area of the product. Use releases when a group of tickets works toward a deliverable with a due date, such as a feature launch, and you want to track whether it will land on time.

### Related articles:

- [Coding agents in Command by Asana](https://help.asana.com/s/article/coding-agents-in-command-by-asana)
- [Command GitHub integration](https://help.asana.com/s/article/command-github-integration)
- [What is Command by Asana?](https://help.asana.com/s/article/what-is-command-by-asana)
- [Creating and managing tickets in Command](https://help.asana.com/s/article/creating-and-managing-tickets-in-command)
- [Understanding cycles and sprint planning in Command](https://help.asana.com/s/article/understanding-cycles-in-command)

## Releases and labels at a glance

|                             |                                   |                                                                       |
|-----------------------------|-----------------------------------|-----------------------------------------------------------------------|
|                             | **Labels**                        | **Releases**                                                          |
| **Use for**                 | Themes, components, or categories | Deliverables you need to ship by a date                               |
| **Due date**                | No                                | Optional                                                              |
| **Forecast and status**     | No                                | Yes                                                                   |
| **Completion**              | No                                | Complete when its tickets are done, or marked complete manually       |
| **Tickets per item**        | A ticket can have multiple labels | A ticket can belong to multiple releases                              |
| **Reporting**               | Filter tickets by label           | Status color, forecast compared with due date, and days early or late |
| **Add to Asana portfolios** | No                                | Yes, so stakeholders can track releases alongside other projects      |

Labels are flexible tags that help you organize and filter tickets. When a group of tickets needs deadline tracking, you can promote the label to a release instead of creating a separate structure from the beginning.

A release represents a time-bound deliverable. It can include an optional description and due date, and it can be associated with multiple tickets.

## Create and manage releases

### Create a release

You can create a release from the **Properties** panel, from a ticket's metadata popover, or from the ticket's context menu.

1.  Select **Create release**.
2.  Enter a name for the release.
3.  Optionally, add a description and a due date.
4.  Select **Create**.

If you create a release from a ticket's metadata popover or context menu, the ticket is linked to the new release automatically. You can also create a release while creating a new ticket.

### Add a release to tickets

To add a single ticket to a release:

1.  Open the ticket's metadata popover or context menu.
2.  Search for the release or filter the list. Each release shows its due date, if one is set.
3.  Select the release.

You can also press R in the ticket's metadata popover to add or remove a release.

To add or remove several tickets at once, select the tickets and use the bulk action controls. A ticket can belong to more than one release.

### Monitor release status

In the **Planned** column, a release marker appears after the last ticket linked to each release. The marker shows two dates:

- Due date: the date you set for the release.
- Forecast: when Command expects the release to be done, based on the forecast for the last linked ticket in priority order. Learn more in Understanding forecasts in Command.

The gap between the two dates shows how much the plan may need to change to hit the due date. When a release is ahead of or behind schedule, the marker shows how many days early or late it's forecasted to land.

Ticket cards can show release badges. Select a release marker or badge to create a filtered **Property** column for the associated tickets. 

### Track releases outside Command

You can add releases to Asana [portfolios](https://help.asana.com/s/article/portfolios-overview) alongside other projects. This lets stakeholders outside engineering follow release progress in the context of a larger initiative, without opening your Teamspace.

### Edit, complete, or delete a release

You can edit a release name, description, or due date. You can also clear the due date or edit it inline from the release marker in the **Planned** column. Renaming a release updates the name on all linked tickets.

A release is tracked as complete when its associated tickets are complete, subject to confirmation in the release workflow. You can also mark a release as complete manually. Completed releases are hidden from the active release list when you link tickets.

To delete a release, use the release management controls. Deleting a release removes it from all linked tickets.

## Filter tickets by release

You can filter tickets by one or more releases in a **Property** column. Release filters can be used alongside filters for ticket type, labels, and assignees. You can also select a release in the **Properties** panel to create a filtered view of its tickets.

The **Properties** panel lists releases with active releases sorted by due date and completed releases shown after them. Select a release from the panel to edit it or create a filtered view.

## Create and manage labels

Labels help you categorize tickets without adding a due date or tracking completion. Use them for themes, components, or any other categories that help your team organize its backlog.

To add labels to a ticket:

1.  Open the ticket and select the Labels field.
2.  Select an existing label, or type a name to create a new one.

You can add more than one label to a ticket. To add or remove labels on several tickets at once, select the tickets and use the bulk action controls.

You can also create, edit, or remove labels from a ticket card.

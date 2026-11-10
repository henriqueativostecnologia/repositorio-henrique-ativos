---
fonte: https://help.asana.com/s/article/understanding-cycles-in-command?language=en_US
baixado: 2026-11-10
---

# Understanding cycles in Command

Cycles in Command by Asana are recurring periods, such as one or two weeks, that help your team see how work is progressing and what's coming next. Unlike traditional sprints, you don't fill cycles by hand. Your team sets the priority order of tickets, and Command places work into cycles based on how much your team typically completes.

### Related articles:

- [Coding agents in Command by Asana](https://help.asana.com/s/article/coding-agents-in-command-by-asana)
- [Command GitHub integration](https://help.asana.com/s/article/command-github-integration)
- [What is Command by Asana?](https://help.asana.com/s/article/what-is-command-by-asana)
- [Creating and managing tickets in Command](https://help.asana.com/s/article/creating-and-managing-tickets-in-command)

## How cycles work

Each cycle covers a set date range, based on the cycle length your team chooses. Command fills upcoming cycles with planned tickets in priority order, using your team's recent pace to decide how much work fits into each one.

Each cycle has a header that shows its name and date range. Within a cycle, tickets are listed by stage and then by priority, so work closest to done appears at the top:

- In review: the work is done and in code review.
- In progress: a person or coding agent is working on it.
- Not started: planned for the cycle but not picked up yet.

As tickets are completed, the rest of the work moves up, and Command updates which tickets fall into each cycle.

## Cycles compared with sprints

If your team is used to sprints, cycles will feel familiar, with a few important differences:

|                           |                                                    |                                                              |
|---------------------------|----------------------------------------------------|--------------------------------------------------------------|
|                           | **Sprints**                                        | **Cycles in Command**                                        |
| **Fixed length**          | Yes                                                | Yes, you choose the length                                   |
| **Filling the iteration** | Team estimates tickets and commits to a set amount | Command fills each cycle based on your team's recent pace    |
| **Estimates**             | Story points or sizes on each ticket               | Not needed                                                   |
| **Changing the plan**     | Replan at the next sprint                          | Reorder tickets at any time, and cycles update automatically |
| **Unfinished work**       | Moved to the next sprint during planning           | Moves into upcoming cycles automatically                     |

Because Command plans cycles for you, your team can spend less time sizing and committing to work, and more time deciding what matters most.

## Set the cycle length

Cycle length is configured at the **space** level. To set or adjust it, open your **space** settings, find the cycle configuration, choose the cycle duration, and save your changes.

## Plan and prioritize work in cycles

Your team's main planning job is setting priorities. To change what's planned for a cycle:

- Reorder tickets. Drag a ticket higher to move it into an earlier cycle, or lower to move it later. Command recalculates which tickets fit into each cycle.
- Add or remove work. Plan new tickets from the backlog, or move tickets out of the plan. Upcoming cycles adjust to match.

You can't assign a ticket to a specific cycle directly. Instead, its position in the priority order and your team's pace determine where it lands. To see when a specific ticket or release is likely to be done, check its forecast. Learn more in Understanding forecasts in Command.

To focus on one cycle, select its header to collapse or expand it. A collapsed cycle hides its tickets but keeps its name and date range visible.

## Use cycles in team rituals

Cycles work best when team rituals focus on moving work forward:

- **Stand-ups:** Review tickets that are In review and In progress in the current cycle. Each ticket shows its time in stage, and tickets taking much longer than usual are highlighted, so focus on those first.
- **Planning:** Instead of estimating and filling a sprint, review the priority order and adjust it. Check forecasts for releases to see whether they're still on track.
- **Retrospectives:** At the end of a cycle, look at tickets that took much longer than usual and discuss what slowed them down.

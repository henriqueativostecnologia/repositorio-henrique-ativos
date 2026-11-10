---
fonte: https://help.asana.com/s/article/sprint-planning?language=en_US
baixado: 2026-11-10
---

# Sprint planning

Using Asana to streamline sprint planning enables teams to have clarity on the entire sprint process all in one place. Follow along with the article for more on building your own sprint process. Let’s look at the example of James, a technical product manager.
James is in charge of his team's sprint cycle, which typically lasts two weeks. To set up his first sprint cycle in Asana, James creates a [portfolio](https://help.asana.com/s/article/portfolios-overview?language=en_US) called **Sprints**. James then creates four [projects](https://help.asana.com/s/article/understanding-projects?language=en_US) which he adds to this portfolio: **Current sprints, Retros, Backlog** and **Intake**. Since James has added work to his portfolio, he can now use [Workload](https://help.asana.com/s/article/portfolio-workload-and-universal-workload?language=en_US) to visualize his team’s capacity based on the tasks they’re assigned in Asana.

## Project 1: Current Sprints

James has the option to create a project from an existing [Asana template](https://asana.com/ru/templates/sprint-planning) or to create one himself. He decides to make his from scratch and adds in all essential and recurring tasks. To make each sprint more seamless he leverages Asana features like [rules](https://help.asana.com/s/article/rules?language=en_US), [milestones](https://help.asana.com/s/article/create-tasks-in-asana?language=en_US), and [custom fields](https://help.asana.com/s/article/custom-fields?language=en_US), which he saves as a [bundle](https://help.asana.com/s/article/bundles?language=en_US) to easily apply to future projects.

In the **Current sprints** project he creates two [sections](https://help.asana.com/s/article/project-customization-and-views?language=en_US): **Current tasks** and **Closed sprint tasks**. He also uses custom fields to highlight the task type, story points, priority type, bug severity, and story status. As tasks are added to the Current tasks section he ensures that every task has a [due date](https://help.asana.com/s/article/scheduling-tasks-using-start-dates-due-dates-and-times?language=en_US?language=en_US) and [assignee](https://help.asana.com/s/article/assign-tasks-to-teammates?language=en_US). In the **Current tasks** section, he adds all the tasks his team is currently working on. He moves any items that were closed during this sprint to **Closed sprint tasks** so he can review these before finally adding them to the **Retro** project.

James uses [board view](https://help.asana.com/s/article/board-view?language=en_US), which makes it easy to drag and drop tasks through different phases of completion e.g Active. He implements a rule that when a task is dragged to a new section, the custom field is updated to match it, he also adds a rule so the lead engineer is assigned an [approval task](https://help.asana.com/s/article/approvals?language=en_US) when a task is added to the review stage.

Now that he has created a project with all the elements used for each sprint phase, he turns this project into a [template](https://help.asana.com/s/article/create-projects-quickly-with-templates?language=en_US) so that he can quickly duplicate this each time there is a new sprint cycle. This template ensures consistency across sprints and initiatives, streamlining the setup process for new sprints.

It's been 10 working days since James’ team started the sprint, so it is time to close it. Using [list view](https://help.asana.com/s/article/list-view?language=en_US) he highlights all the tasks and changes the sprint status to closed. James has already set up rules to move each task to a different section based on their story status custom field, he has created a rule to move tasks marked as **Released** to the **Closed sprint tasks** section, he also has a rule to move any task with a status other than **Released** to the **Backlog** project. Now the team can decide if they want to adjust story points, move these tasks to the next sprint, or keep them in the Backlog project.

James uses the [project dashboard](https://help.asana.com/s/article/project-dashboards?language=en_US) tab regularly to get an overview of project information at a glance and share this with stakeholders easily. Within his project dashboard, he also sets up a chart to view current sprint tasks filtered by their story status custom field value.

After each sprint, James uses [Smart status ](https://help.asana.com/s/article/get-started-with-asana-ai?language=en_US)to draft [status updates](https://help.asana.com/s/article/project-progress-and-status-updates?language=en_US) and identify blind spots, open questions, visualize roadblocks and map an efficient path towards his teams’ [goals](https://help.asana.com/s/article/get-started-with-asana-goals?language=en_US).

## Project 2: Retros

Within the **Sprints** portfolio James has also created a retrospective project, where completed tasks from the **Current sprint** project automatically move thanks to a rule he built. After each sprint is over, James’ team meets to reflect on what went well, what could be improved and how they can adapt their processes for the next sprint. The project has a section for admin tasks, appreciations, obstacles and risks, general thoughts as well as commitments, gusts of winds etc. Once the project is fully set up fully, James saves this as a template so it can be used each time he wants to create a new retro project.

James has asked all his team members to [like](https://help.asana.com/s/article/task-fields?language=en_US) and comment on the tasks within the retro project before their meeting, the tasks with the most likes drive the retro discussion and any new action items are turned into tasks for future sprints.

## Project 3: Backlog

Within the **Sprints** portfolio, James creates a **Backlog** project for everything his team wants to action in the future. This includes tasks that have been processed through **Intake**, those which weren’t completed in the last sprint, and urgent tasks that need to be completed. He creates a section in his **Backlog** project called **Next sprint**. Each time there is a new sprint, James will look through the **Backlog** for priorities and story points and decide which items should be worked on next. He uses [Smart summaries](https://help.asana.com/s/article/smart-summaries?language=en_US) to pull out action items, ensuring that he understands each task without having to read through lengthy decisions. When James wants to start a new sprint, he selects all the tasks in the **Next sprint** section and regardless of their sprint status he adjusts the custom field to **Current sprint**. This way all the tasks move to the **Current Sprint** project and are automatically given a due date for 14 days time because of a rule James has created James also uses [Smart chat](https://help.asana.com/s/article/smart-answers?language=en_US) to get insights about his previous sprints helping him to identify potential blockers and how he should move forward in the future. Now that all the tasks for the current sprint have been added, James and his team get an overview of the amount of story points they are committing to, as well as the task types and severity of any bugs.

## Project 4: Intake

James also created an **Intake** project in the portfolio for all incoming requests and bugs. The team uses the **Intake** project to first read, triage, and assess each request which has come in through an intake [form](https://help.asana.com/s/article/forms?language=en_US) that he has created. James and his team communicate on these tasks, adding [comments](https://help.asana.com/s/article/task-comments-and-attachments?language=en_US), and [attaching files](https://help.asana.com/s/article/task-comments-and-attachments?language=en_US#gl-attachments) before adding tasks to the **Backlog** project. Once these tasks have been fleshed out he can then move these tasks into the sprint **Backlog** project to be triaged and assigned to the next sprint.

## Resources

To learn more about sprint planning in Asana, check out these resources:

- [Sprint planning template](https://asana.com/templates/sprint-planning)
- [Sprint backlog template](https://asana.com/templates/sprint-backlog)
- [Agile templates](https://asana.com/templates/use-case/agile)

[ ](https://forum.asana.com/c/forum-en/tips/6)

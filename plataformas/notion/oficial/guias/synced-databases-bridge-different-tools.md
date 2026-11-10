---
fonte: https://www.notion.com/help/guides/synced-databases-bridge-different-tools
baixado: 2026-11-10
---

# Synced Databases bridge the gap between different tools

## Synced Databases let you pull information from 3rd party apps like GitHub and Jira into Notion, and break down silos across teams.

- Engineering
- Product
- Project management

10 min read

Visualize your Jira tasks right in Notion.

------------------------------------------------------------------------

Synced Databases give you the power to bring information from different sources into Notion. You can create a single source of truth to unite your team by syncing Jira boards, Jira projects, GitHub PRs and GitHub issues as Notion databases.

When you oversee projects involving different teams, it’s challenging to make sure everyone’s on the same page, working with the latest version of events. Teams often rely on several tools to get work done, so you need a robust system to bring everything together and bridge the gap between the specialized tools your teams use, and the system to track and manage the work, where collaboration happens.

Sometimes, when teams are using different tools, important information about their work can stay in those tools, hidden from other teams and project managers. By created Synced Databases with GitHub and Jira, you can bring information from those tools into Notion, which provides clarity for everyone involved and means you’ll spend less time hopping between tools, asking for updates or searching for the latest versions of files.

Sync Github issues and pull requests as databases.

## [**No more silos — collaborate seamlessly by bringing external work into Notion**](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#no-more-silos-%E2%80%94-collaborate-seamlessly-by-bringing-external-work-into-notion)

You can easily create Notion databases that sync with your Jira boards, Jira projects, GitHub PRs and GitHub issues, bringing information from those tools into a database you can use to manage, track and oversee projects.

Synced Databases make life easier for all your team members, especially those who don’t use GitHub or Jira, but still need to see what’s going on. Instead of asking for logins and trying to navigate an unfamiliar tool, they’ll have access to everything they need right in the Notion database.

No more pinging engineers on Slack for updates on an urgent bug fix — you can just go straight into the database and see whether it’s done, saving everyone time and stress.

You’ll never have to manually update database entries with screenshots or links either, as the information will automatically pull through to the database for everyone to see.

And, you can rest assured you’ll always be looking at the latest version of events, as the database will update whenever changes are made in the original tool. Synced Databases are read-only, so although you can bring information into Notion from GitHub and Jira, any changes to a ticket, task or PR need to be made in the original tool, providing a safeguard against unintentional edits and preserving your source of truth. Only team members authorized to edit GitHub or Jira are able to make changes in the tool. It’s a good idea to leave a note at the top of the page letting people know who to get in touch with if they want to make any changes.

All of the information associated with a Jira ticket will become its own Notion property.

Synced Databases help streamline project management and aid collaboration. People from different teams can work together on a single Notion page, where they’ll share content, communicate and collaborate without needing to switch tools. You can also add more context to the information you pull into Notion. With relations and rollups you can link your Jira sprint to a larger team goal that lives in your OKRs database in Notion. When you’re looking at those OKRs, you’ll see relevant info coming from Jira, making it easier to measure and report on your progress.

## [**How to create and use Synced Databases with Jira**](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#how-to-create-and-use-synced-databases-with-jira)

To set up a Synced Database, you must first authenticate Jira in Notion. To do this, go to Settings in your side bar, and choose My connected apps. Click “Connect” underneath Jira, and you’ll be prompted to authenticate by logging in to your Jira account. After you’ve authenticated once, creating synced databases is as simple as pasting a link.

You can now sync Jira boards or entire Jira projects into Notion. Here’s how:

- In Jira, go to the board or project you want to sync, and copy the link.

- Paste it into Notion and select “Paste as database.”

- An empty database with a preset list of properties will show up in your page. It will show up in a Notion “table” view, with all Jira properties automatically added.

The database will start populating automatically and will continue to sync if you navigate away from the page.

### [Format your Jira Synced Database](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#format-your-jira-synced-database)

Notion brings all Jira Issue types (Epics, Stories, Tasks, Bugs, Sub-tasks, etc.) to the synced database, where they’ll appear as separate rows. Every Jira story will be linked to its relevant epic via a property called “Parent”, and sprints are also reflected in synced databases as separate properties.

You can create specific views using Notion’s database filters, for example, to show all tasks within a Sprint or the Stories, Tasks, and Bugs that make up an Epic.

A kanban board can be a handy way to organize your sprints. To create one, first, select `Add view` at the top of your synced database and select `Board`. Then click on database options (`…`), `Group by`, and choose `Status`. Set the `Sort` to `Manual` so you can move groups around and have To-Do, In Progress, and Done ordered properly.

Create layouts with synced data to visualize information in new ways.

As with any Notion database, you can create as many filtered views as you need, to organize your information in different ways.

- Create a calendar view to see when each task was created.

- Use a timeline to visualize how your epics relate to one another, and see how many projects your team is juggling at once.

- Add a board view grouping tasks by assigned engineer, so you’ll know exactly what everyone’s got on their plate.

Create views on synced databases just like any other database in Notion.

## [**How to use Synced Databases with Notion and GitHub**](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#how-to-use-synced-databases-with-notion-and-github)

You can sync **GitHub Issues** and **Pull Requests** into Notion, and anyone who has access to the page will be able to see the content, even if they don’t have access in GitHub.

Just like with Jira, you first have to authenticate with GitHub. Go to `Settings` \> `My connected apps` in the top left corner of your screen, and this time, you’ll click the `Connect` button under GitHub, and authenticate the account.

### [**Syncing GitHub Issues or Pull Requests**](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#syncing-github-issues-or-pull-requests)

Once the authentication is successful, you can copy and paste links to GitHub Issues or Pull Requests into Notion pages.

All you have to do is go to GitHub, copy the link for Pull Requests or Issues you'd like to sync, and paste it into Notion, selecting `Paste as a database` when prompted.

An empty database with a preset list of properties will immediately show up, as a Notion table database with all GitHub properties in the database.

Within the next few minutes, the database will start populating automatically, and you’ll know it’s done once you see `Synced just now` in the database header.

You can create views and filters exactly as you can with Jira, and any other Notion database, for example, you can sort your database by Issue Number date to view the most recent Issues / Pull Requests first.

Paste issues or pull requests to sync data from Github.

## [**Connect your Synced Database to another Notion database**](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#connect-your-synced-database-to-another-notion-database)

With the relation property, you can connect information from different databases in Notion. This can help give context and tie information together according to project or team. So you’ll be able to associate GitHub PRs with projects in your roadmap, for example.

To add a relation to your Synced Database:

- Go to `Properties`, and add a new property.

- Under advanced properties, select `Relation` as the property type.

- Now a prompt will ask you which database you’d like to relate. Choose and select the relevant database.

You can also mention items from your Synced Databases anywhere in Notion by using the `@` symbol just as you would mention any Notion page.

Add advanced properties like relations and rollups to further connect information.

### [Automatic relations with Github and Jira](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#automatic-relations-with-github-and-jira)

With Github and Jira Synced Databases, you can set up auto-relations, so any time an item in the Synced Database (a Github PR or a Jira Issue for example) includes a link to a Notion page in the auto-related Notion database in its description or title, the relation will automatically be populated. This makes it easier to keep track of Pull Requests and Tasks/Issues in Notion.

- When you create a new relation in your Jira or Github Synced Database, toggle on `Automatically Relate` and select `Update relation`

- Now you’ll be able to add links to your Notion documents in your GitHub PR titles or descriptions or Jira Issues. To find the link, select the document in the database and click `Copy link` or open the document in a new tab and copy the link in your browser.

- Add the link in your description. Now, once the PR is synced into Notion, a relation between the task and the linked document will be automatically populated in the Synced Database.

- When you sync GitHub Pull Requests and Issues to Notion, you can search and mention individual PRs or Issues in your workspace using the `@` symbol just as you would mention any Notion document.

When auto relations are set up, Notion database items mentioned in issues will automatically appear in your synced database.

### [Use rollups to add additional info to a Jira board](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#use-rollups-to-add-additional-info-to-a-jira-board)

Once you’ve created a relation property linking your Synced Database to another database in your workspace, you can bring specific information from one database into the other using a rollup property.

- Add a new property, choosing `Rollup` from advanced properties, and give it a name.

- Click on a cell in the rollup column and you’ll be able to choose:

  - The relation property you want to roll up.

  - The property of the related database you want to roll up.

  - The calculation you want to apply to them.

Let’s say you relate your Synced Database from Jira to your OKRs in Notion - with a rollup, you can now visualize aggregated information, like percentage of tasks complete, right in Notion.

Or, you can relate your Meeting Notes database and use a rollup property to attach meeting notes, or see how many meetings you’ve had about any item.

Use rollups to discern even more information about the tasks at hand.

## [What you can do with Jira and GitHub Synced Databases](https://www.notion.com/help/guides/synced-databases-bridge-different-tools#what-you-can-do-with-jira-and-github-synced-databases)

Synced Databases let you bring accurate information from Jira and GitHub into Notion. Once you’ve established that connection, there’s really no limit to how you use that data — you can reference and resurface it throughout your workspace, keeping everyone up to date with work happening outside of Notion.

- **Manage individual workloads** — Add views for each team member to track high priority tickets, issues, and PRs all in one place. Personalized views help your team members reduce distraction and get laser-focussed on what they have to do.

- **Connect GitHub issues with tasks** — Create a relation to your team’s task dashboard in Notion, so you don’t have to spend time copying GitHub issues to your tasks database manually.

- **Create a summary view of related GitHub PRs, tasks, and Jira tickets** — By connecting your projects database in Notion to Github and Jira Synced Database, you can get a broader view of everything that makes up a project brief.

- **Mention issues and tickets anywhere in your Notion workspace** — You can `@mention ` issues and tickets to quickly link to the relevant page of your Synced Database, just like you would with any other Notion page.

Go further with these resources

- A guide to project management for engineering teams [here](https://www.notion.so/help/guides/this-project-management-system-helps-your-engineering-team-track-every-initiative).

- Everything you need to know about using databases with your teams [here](https://www.notion.so/help/category/databases).

- A how-to guide to relations and rollups [here](https://www.notion.so/help/relations-and-rollups).

Get started with templates

- A projects roadmap [here](https://www.notion.so/templates/roadmap).

- Tasks and Issues tracker [here](https://www.notion.so/templates/tasks-and-issues).

Share this guide

------------------------------------------------------------------------

---
fonte: https://www.notion.com/help/guides/make-work-more-efficient-database-button-property
baixado: 2026-11-10
---

# Make work more efficient with database button properties

## Learn how database button properties can speed up project management workflows like upvoting, escalations, and approvals. Plus, how to use Notion's suite of automation features in concert — including database button properties, database automations, and buttons.

- Project management
- Automations

7 min read

Complete workflows for projects, tasks, and docs with one click using database buttons.

------------------------------------------------------------------------

Tracking progress on your work can be tedious, and some processes, like signing off a project, approving a document, or escalating a task, might require a few steps and changing several properties in Notion.

With database buttons, you can trigger a series of actions for any database entry with one click, which saves you time, reduces the margin for error, and makes it easier for everyone on your team to complete the required steps.

Database buttons are one of three types of automations you can build in your Notion workspace, along with database automations and button blocks. In this guide, we’ll explain how to create and use database buttons, and also when to use each type of automation.

## [**Database button property**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#database-button-property)

Database buttons are a database property you can add to any database. They will appear as a property, and each line item will have its own button.

To create a database button:

1.  In your database’s properties menu, select + New property

2.  Choose Button as the property type.

3.  Type a Property Name and Label (for example, “Sign off project”) for your Button to indicate what the button will do. This will appear in the database as the property title and in each row.

4.  Click Add a step to start configuring the button actions.

Edit your button property to add all the steps you require.

Buttons can contain several steps or actions that will all take place when the button is clicked. A button can update properties and add or edit pages in any database you choose.

These are all the different action steps you can add to a database button can take:

### [**Add a new page to a database**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#add-a-new-page-to-a-database)

Selecting `Add page to…` will create a new page in a database — this can be the current database you’re working in or any other database you have access to.

After choosing the database, you can select an existing template from that database or give the new entry a name. Click `Edit another property` to continue filling out more properties in the new item.

Now, when you click the button, a page will be created in the database of your choice, with some properties already completed as specified.

Create a button in your projects database to automatically add new tasks

### [**Edit database pages**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#edit-database-pages)

The `Edit pages in…` option will edit the properties of specified pages in a database.

Choose `This page` to edit the current page, or, if your button already has an `Add a new page` step, you can select `New page` to edit it. Alternatively, choose a database and edit a subset of pages in it by creating a filter.

After this, select `Edit a property` to choose properties and configure how you want to update them.

Edit properties for the current page, or pages in another database.

### [**Show a confirmation**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#show-a-confirmation)

Confirmation dialogs can be helpful when clicking a button triggers a workflow for other teams or colleagues.

When you add `Show confirmation` to your button, the confirmation box will appear to everyone who clicks, providing a safeguard in case someone clicks accidentally.

You can customize the confirmation dialog text to say something like “Are you sure you want to continue?” and also edit the two options a person can click to either stop or continue.

A confirmation can explain what the button will do and prevent people from clicking by mistake.

### [**Open a page**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#open-a-page)

If you want a particular page to open when you click a button, select `Open page`.

This can be:

- The brand new page created in a previous `Add page to… `step

- A page edited as part of the automation sequence

- Any other page in the workspace

## [**How to use database buttons to streamline workflows**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#how-to-use-database-buttons-to-streamline-workflows)

Database buttons are powerful because they give everyone the ability to trigger a sequence of actions by simply clicking the button.

Instead of having to manually follow each step, a whole workflow can be condensed into one action.

Here are some examples of effective ways to use database buttons.

### [**Approve a project or document**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#approve-a-project-or-document)

Project managers can complete all the necessary steps to sign off on a project simply by clicking the `Approve` button.

What you’ll need for an "Approve" button

**Then, customize your button with these steps:**

1.  Select `Edit pages in…` , and choose `This page`. In the `Edit a property` dropdown, change the `Status` to `Done`.

2.  Click `Edit another property` and fill out the Completed date with Now (this will always show the date the button was clicked)

3.  Click `Edit another property`, choose `Approved by` and select `Person who clicked the button`.

A similar process could be used to approve documents or wiki pages once all edits have been finalized.

Or, if a document needs approval from a specific team, such as legal, you can create a button that tags someone from the legal team, marks legal status as `Pending`, and sets an approval deadline for a week from today.

### [**Escalate a task**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#escalate-a-task)

Sometimes, a task or engineering issue requires intervention from a manager to get resolved.

Create an `Escalate` button in your database to allow team members to escalate tasks in one click.

Properties for an "Escalate" button

**To create the** **`Escalate`** **button:**

1.  Update the `Owner` property to tag your team leader.

2.  Change the priority status to `🔥High`

3.  Add a confirmation dialog to continue or cancel.

Click a button to escalate a task and assign it to your manager.

### [**Upvoting items**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#upvoting-items)

An upvote database allows team members to vote on different options in a database, such as topics to discuss at the next all-hands, or new feature suggestions.

What you’ll need for an "Upvote" button

To edit your Upvote button, simply `Edit the current page` to tag the `Person who clicked the button` in the `Upvoted by` column, and the formula will calculate the total number of upvotes.

Upvoting can also be used in your personal Notion space to share ideas and get feedback from friends or family.

Buttons simplify the upvoting process for your team.

### [**Other ways to use database buttons:**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#other-ways-to-use-database-buttons-)

- **Simplify expense tracking** — Use buttons to categorize expenses or assign budgets. For example, the button could tag a specific budget from your budgets database and be marked as `Assigned`.

- **Keep a habit log** — Record your habits in a database and track your achievements and streaks over time. Your `Complete` button could tick the `Done` checkbox for all columns.

- **Tag content in a wiki** — Tag and categorize wiki pages for quick retrieval. Using a button, you can add a category to your page and mark it as `Verified`.

- **Mark items as duplicate** — Allow team members to easily flag duplicate items they discover in a database. The `Mark as duplicate` button might add a `Duplicate` tag and change the status to `Archived`.

## [**When to use other types of Notion automations**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#when-to-use-other-types-of-notion-automations)

There are three different ways to use automation across your Notion workspace.

### [Database buttons](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#database-buttons)

Database buttons allow you to add items to databases and edit several properties simultaneously. Teams can use button properties for smoother project management workflow and to save time on administrative manual work.

You can also create Button blocks on individual pages, and database automations for different sorts of work.

### [**Button blocks**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#button-blocks)

Add a button to any Notion page by opening the / menu and selecting `Button`.

Buttons live on pages and can create blocks on the current page. They can also edit some properties of database pages or add new pages to a database, making them useful for editing items without needing to navigate to the database itself.

Use button blocks to:

- Generate pages in databases, such as task-creation workflows.

- Edit all items in a database, for example, to assign overdue tasks to you.

- Instantly generate checklists or outlines for meetings or project briefs.

Use a button to generate 1:1 meeting notes agendas in an instant.

All about buttons

### [**Database automations**](https://www.notion.com/help/guides/make-work-more-efficient-database-button-property#database-automations)

Database automations are for actions taking place behind the scenes.

Unlike buttons, they don’t require any clicking. They share some functionality with database buttons, but property updates trigger the actions.

Database automations also allow you to send slack messages. Actions can include adding or editing pages in a database, and sending Slack notifications to team members or channels.

Use database automations to:

- Assign a task to someone automatically when the task status changes.

- Send a Slack notification when a new page is added.

- Edit a page property in another database when a property is changed.

If you want to stop a database automation, it has to be paused or deleted.

Learn more about using database automations

Share this guide

------------------------------------------------------------------------

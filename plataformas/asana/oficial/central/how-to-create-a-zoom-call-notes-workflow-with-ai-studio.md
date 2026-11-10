---
fonte: https://help.asana.com/s/article/how-to-create-a-zoom-call-notes-workflow-with-ai-studio?language=en_US
baixado: 2026-11-10
---

# How to create a Zoom call notes workflow with AI Studio

Transform your meeting follow-ups by automatically generating summaries, extracting action items, and creating tasks directly from your Zoom recordings. This article walks you through setting up an automated workflow that eliminates manual note-taking and ensures decisions are properly tracked.

#### Related articles

- [Zoom transcripts for automation and AI Studio](https://help.asana.com/s/article/zoom-transcripts-for-automation-and-ai-studio)
- [Zoom meetings in Asana](https://help.asana.com/s/article/zoom-and-asana-integration)

## What you'll accomplish

By the end of this guide, you'll have a fully automated system that:

1.  Automatically generates meeting summaries when transcripts become available for recorded Zoom calls
2.  Extracts and assigns action items to team members
3.  Creates organized tasks in your Asana projects
4.  Saves time on manual meeting documentation

## Prerequisites

Before starting, ensure you have:

1.  **Zoom account** with recording and transcription enabled
2.  **Asana account** on a Starter, Advanced, Enterprise, or legacy Premium/Business tier with AI enabled.
    - AI Studio Basic, which is provided free for all Asana plans, should allow you to set up and test this workflow. For regular use, we recommend the AI Studio Plus or Pro plans.
3.  **Asana for Zoom integration** installed ([setup instructions](https://help.asana.com/s/article/zoom-and-asana-integration))

## How the workflow works

The automation follows this process:

1.  You hold a Zoom meeting with recording enabled
2.  Zoom generates an audio transcript after the meeting ends
3.  Asana detects the new transcript and triggers your rule
4.  AI Studio analyzes the transcript and generates summaries or action items
5.  Tasks are automatically created in your specified project

## Setting up the workflow

There’s two approaches to setting up this workflow:

1.  Start with a preset AI rule for creating meeting notes from Zoom transcript. This is the fastest way to start generating meeting notes automatically

###

2.  Or, configure this from scratch in the rule builder by selecting the Zoom transcript trigger and task actions. This is for if you have deep familiarity with rules and want to customize this workflow further. This guide will go over this approach 

### Step 1: Set up the project structure

You can create a blank project to capture the meeting notes, or use an existing project.

1.  Create a **Text** custom field. This is where the recording link will be live.
2.  Create a **Date** field to indicate when the call took place. You can also use the task’s **Due date**.

> Feel free to add other fields you may want AI to fill in based on your use case, such as a **Sales Call Type**.

### Step 2: Create meeting notes in task rule

1.  Navigate to your project in Asana
2.  Click **Customize** in the top-right corner
3.  Click **Rules**, then select **+ Add**
4.  Click **Create with AI Studio**
5.  Name your rule (e.g., "Weekly team meeting notes")

#### Choose one of these trigger options:

**Option A: All recorded meetings (broader automation)**

1.  Select the **Zoom transcript is ready** trigger and the option **All meetings that I host and record**.
2.  This will trigger for all Zoom meetings where you are the host and have recorded a meeting transcript. We recommend starting out with a private project for this rule as all recorded meetings you host will automatically post content to this project.

**Option B: Specific meeting, including recurring meeting (targeted automation)**

1.  Select the **Zoom transcript is ready** trigger and the option **Specific meetings that I host and record**.
2.  Enter the Zoom Meeting ID for the recurring meeting (find this in your Zoom account under Personal \> Meetings)

#### Set up the action

1.  Select **Create a task**
2.  In **Add task name** choose **Meeting name**
3.  For the **Due date** field, choose **The date this rule is triggered**
4.  For the custom fields: You can add **Use AI**, or for the **Recording link** custom field, you can use the variable **Recording URL**.
5.  In **Description** add the variable **Use AI**
6.  Create a subtask called **Transcript**
7.  Click into the **Transcript** subtask. In the **Description** field click the **+** button and use the **Transcript** variable from Zoom

### Step 3: Create action items in subtasks rule

**Trigger**: When a task is added to this project

**Action**: Create Subtasks

- Ensure **Let AI Decide the number of subtasks to create** is checked
- Set the **Task name**, **Due date**, and **Assignee** fields to **Use AI**
- Ensure you click in to the subtask itself and set the subtask description to **Use AI**

### Step 4: Prompting AI Studio

In the **Guidance for AI** box you’ll need to provide key instructions. You'll need two separate prompts; one for each rule.

> For any AI Studio rule where you are looking to dynamically assign among a restricted set of individuals, like letting AI know who to go for for which kinds of action items or follow ups, you will likely want to ensure you @mention any teams or specific individuals which AI might need to select from. [Read more](https://help.asana.com/s/article/ai-studio-connect-your-smart-workflow?language=en_US#data-and-permissions-in-ai-instructions) on how to use @mentions in AI Studio prompts.

#### Prompting for **Create meeting notes in task** rule:

*Your job is to create comprehensive meeting notes from a Zoom call transcript. The transcript will be provided in a subtask. Add these notes to the task description.*

***Task Description Format:** Structure the notes with these sections:*

***Meeting Summary** (2-3 sentences)*

***Key Discussion Points***

- *Main topic 1*
  - *Key details*
  - *Decisions made*
- *Main topic 2*
  - *Key details*
  - *Decisions made*

***Important Questions & Answers***

- *Q: \[Question asked\] A: \[Answer provided\]*

***Decisions Made***

- *List any concrete decisions*

***Risks & Concerns***

- *Any blockers or risks identified*

***Next Steps***

- *High-level next steps (detailed action items will be created as subtasks)*

*Keep formatting clean and scannable. Focus on information that would be valuable to someone who wasn't on the call.*

#### Prompting for **Create** **action items in subtasks** rule

*Your job is to extract specific, actionable tasks from the meeting transcript found in the "Transcript" subtask of this task.*

***For each action item, create a subtask with:***

***Subtask Name Format:** "\[Action verb\] \[specific deliverable\]" Examples:*

- *"Send pricing proposal to Sarah"*
- *"Schedule follow-up demo for engineering team"*
- *"Review security documentation"*

***Assignee Rules:***

- *If a specific person committed to the action, assign to them using @\[name\]*
- *If unclear but related to a department (e.g., "engineering will handle"), assign to @\[department lead\]*
- *If no owner specified, assign to the meeting organizer*
- *Use Asana @-mention format: @\[firstname lastname\] or @\[team name\]*

***Due Date Rules:***

- *If a specific date mentioned, use that date*
- *If "this week" → 3 business days from meeting*
- *If "next week" → 7 business days from meeting*
- *If no timeline → 5 business days from meeting*
- *Never set due dates on weekends*

***Subtask Description:** Include:*

- *Context: Why this action is needed*
- *Specific requirements mentioned in the meeting*
- *Who requested it (if different from assignee)*
- *Any dependencies or prerequisites*

**`Limits:`**

- `Create 3-7 action items maximum`
- `Focus on concrete deliverables, not vague follow-ups`
- `Exclude items like "think about" or "consider"`
- `Combine related small tasks into one meaningful action`

### Step 6: Test your workflow

1.  Click **Publish rule** to activate it
2.  Hold a short test Zoom meeting with recording enabled
3.  Wait 5-10 minutes after the meeting ends for transcript processing
4.  Check your Asana project for the automatically created tasks

## Frequently asked questions

Find the answers to all your questions [here](https://help.asana.com/s/article/zoom-transcripts-for-automation-and-ai-studio#frequently-asked-questions).

---
fonte: https://help.asana.com/s/article/chat-with-asana-in-slack-channels?language=en_US
baixado: 2026-11-10
---

# Chat with Asana in Slack channels

You can mention **@Asana** in any Slack channel or channel thread to create tasks in Asana and retrieve information about your work, all without leaving Slack. This feature uses natural language, so you can make requests conversationally.

> Your domain must have Asana AI enabled for this feature to work. Admins can toggle this setting in the **admin console**. 
>
> If the @Asana agent doesn’t respond when you mention it, please make sure that your Slack Workspace Admin has enabled the new **app_mention** scope.

## Create tasks by mentioning @Asana

Mention **@Asana** in any Slack threaded message to create a task based on the conversation context. The Asana bot summarizes the thread and auto-populates the following fields based on your request:

1.  Assignee
2.  Project
3.  Due date
4.  Custom fields

For example, you could type:

@Asana make me a task in the Marketing project to remind me to turn on the flag for the customers on Thursday. Set the custom field as high priority.

The bot can only create one task at a time, so mention it again for multiple tasks.

## Retrieve information by mentioning @Asana

Mention **@Asana** in a Slack thread to retrieve relevant information from Asana in context. For example, you can ask about:

**Status and health:**

- "@Asana are we on track for the June Marketing Moment project?"
- "@Asana What's blocking the launch of Q3 Product Feature?"
- "@Asana What's overdue in the Web Development team project?"

**My work:**

- "@Asana What's assigned to me this week?"

**Point lookups:**

- "@Asana When is the task to update graphics for the website due?"
- "@Asana Who owns the migration task for the Slack integration?"
- "@Asana Do we already have a task in the Slack project tracking the UI comment bug?"

And more!

## Privacy and visibility

Asana returns responses as **ephemeral messages** (visible only to you) for privacy. You then have the option to post the response to the thread so others can see it.

The Asana bot can only return information you have access to in Asana. Others in the Slack channel can see your Slack thread, but they cannot see created tasks if those tasks are in an Asana project they do not have access to.

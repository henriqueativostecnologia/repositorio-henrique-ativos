---
fonte: https://help.asana.com/s/article/rules-integrations-for-productivity-and-communication?language=en_US
baixado: 2026-11-10
---

# Rules integrations for productivity and communication

Rules and integrations work together to automate routine tasks and establish workflows across your team's favorite tools. This article details the best rules and integrations for productivity in your organization.

See [How to create a rule](https://help.asana.com/s/article/rules?language=en_US) for tips on getting started with rules.

#### Related articles

- [Rules integrations and widgets](https://help.asana.com/s/article/rules-integrations-and-widgets?language=en_US)
- [PagerDuty rules integration](https://help.asana.com/s/article/rules-integrations-for-operations-and-support?language=en_US)
- [HubSpot rules integration](https://help.asana.com/s/article/rules-integrations-for-sales-and-services?language=en_US)
- [Rules integrations for cloud storage and file sharing](https://help.asana.com/s/article/rules-integrations-for-cloud-storage-and-file-sharing?language=en_US)

## Gmail

Leverage rules to send an email from your Gmail account to your chosen recipient when certain parameters are met—all decided by you in advance. Choose from many triggers such as when a task is no longer blocked or a due date is approaching, and let rules automatically send an email with a custom message.

#### Steps to configure rules integration

1.  In your project, click **Customize** in the top-right corner and select **Add rule** from the list
2.  From **Add rule**, select a trigger such as **Approval complete**.
3.  From the **Actions** tab, select **Send email**.
4.  Enter the recipient’s email address in the **To** field
5.  Enter a **Reply to** email address
6.  Enter the email's subject line in the **Subject** field
7.  Write the body of the email in the **Write a message** field

In this example, when the task is approved the rule is triggered and the action is taken; an email will be sent from your email address and will automatically Bcc you on the email. The task link will also be included in the email.

This **Send email** action also supports the use of variables. Visit [this article](https://help.asana.com/s/article/variables-in-rules?language=en_US) for more on how to use variables with Asana's Gmail rule integration.

## Google Calendar

With Asana Rules, teams can go from manually scheduling meetings to automatically creating a meeting with project collaborators when a task reaches a certain stage. For example, teams can use this rule to trigger creating an event in a team calendar when a task is moved to a "Scheduled" section. Teams can also use this for recurring task scenarios: you can have a recurring "Send agenda for meeting" task which sends out an event invite when the task is completed.

#### Steps to configure rules integration

1.  Navigate to the specific Asana project where you’d like to add a rules integration
2.  Click **Customize** in the top-right corner, navigate to **Rules**, and select **+ Add rule**
3.  Select **Google Calendar** from the left column
4.  Either select a preset rule or click **Create custom rule**
5.  If creating a custom rule, add a name, and choose a trigger and action to get started
6.  Authenticate by clicking **Connect to Google Calendar Rules**
7.  Sign in with your Google account and click **Allow**
8.  Fill out the fields for the Google Calendar event
9.  Optionally, invite task collaborators as event guests

## Outlook Calendar

With Asana Rules, teams can go from manually scheduling meetings to automatically creating a meeting with project collaborators when a task reaches a certain stage. For example, teams can use this rule to trigger creating an event in a team calendar when a task is moved to a "Scheduled" section. Teams can also use this for recurring task scenarios: you can have a recurring "Send agenda for meeting" task which sends out an event invite when the task is completed.

### Steps to configure rules integration

1.  Navigate to the specific Asana project where you’d like to add a rules integration
2.  Click **Customize** in the top-right corner, navigate to **Rules**, and select **+ Add rule**
3.  Select **Outlook Calendar** from the left column
4.  Either select a preset rule or click **Create custom rule**
5.  If creating a custom rule, add a name, and choose a trigger and action to get started
6.  Authenticate by clicking **Connect to Outlook Calendar Rules**
7.  Sign in with your Microsoft account\* and click **Allow**
8.  Fill out the fields for the Microsoft Calendar event
9.  Optionally, invite assignees and task collaborators as event guests, include task attachments, or automatically generate a Teams meeting link

\* When signing in with your Microsoft account, we ask you to grant consent to relevant Outlook Calendar permission. If you are disallowed from granting this consent yourself, please reach out to your Microsoft Admin and ask them to consent to Calendars.ReadWrite in Microsoft Entra (fka Microsoft Azure).

## Outlook Email

Leverage rules to send an email from your Outlook account to your chosen recipient when specific parameters are met—all decided by you in advance. Choose from many triggers, such as when a task is no longer blocked, or a due date is approaching, and let rules automatically send an email with a custom message.

### Steps to configure rules integration

1.  In your project, click **Customize** in the top-right corner and select **Add rule** from the list.
2.  From **Add rule**, select a trigger such as **Approval complete**.
3.  From the **Actions** tab, select **Send email**.
4.  Enter the recipient’s email address in the **To** field
5.  Enter a **Reply to** email address
6.  Enter the email's subject line in the **Subject** field
7.  Write the body of the email in the **Write a message** field

In this example, when the task is approved, the rule is triggered, and the action is taken, an email will be sent from your email address and will automatically Bcc you on the email. The task link will also be included in the email.

This **Send email** action also supports the use of variables. Visit [this article](https://help.asana.com/s/article/variables-in-rules?language=en_US) for more on using variables with Asana's Gmail rule integration.

> If you are looking to automate sending an email to users without an Asana license, you can create a text custom field in which you can enter the recipient email addresses. When setting up the rule action, you can select this text custom field as the email recipient.

## Microsoft Teams

You can use the Microsoft Teams + Asana integration to create custom notifications using the [Asana rules feature](https://help.asana.com/s/article/rules), such as sending a custom message to a channel or a chat whenever a task is created, updated, or commented on.

- The **Send channel message** rule action allows you to automate sending custom notifications to designated Microsoft Teams channels based on specific triggers in Asana. This feature creates shared visibility of team statuses and updates without the manual workarounds.
- The **Send direct message** rule action allows you to automatically send customized messages to individuals or groups in Microsoft Teams based on specific triggers in Asana. This feature bridges the communication gap between Asana and Microsoft Teams, helping teams stay informed about important updates without leaving their primary communication platform.

> Learn how to build these rule types and see example workflows [here](https://help.asana.com/s/article/microsoft-teams-and-asana-integration?language=en_US#h_01HJ3WHPVPSGQGS5P87FQZ2NK5:~:text=wish%20to%20receive-,Custom%20notifications,-You%20can%20create).

## Notion

The Notion + Asana integration allows teams to streamline work by automatically creating Notion pages from Asana and adding Notion pages to Asana tasks. Rather than manually creating Notion pages and linking those to relevant Asana tasks, you can use automation to create a Notion page when certain actions take place in Asana, such as when a task is moved to a section.

For example, teams that are conducting research interviews in Asana tasks can automatically create a Notion page to take notes when the task moves to the "Interview scheduled" section. You can also link existing Notion pages to an Asana task so that collaborators can see relevant context from the page, streamlining collaboration across multiple apps. Notion’s integration with Asana also allows you to view the status of Asana projects and tasks as link previews in Notion.

#### Steps to configure rules integration

1.  Navigate to the specific Asana project where you’d like to add a rules integration
2.  Click **Customize** in the top-right corner, navigate to **Rules**, and select **+ Add rule**
3.  Select **Notion** from the left column
4.  You can select a preset rule or click **Create custom rule**
5.  If creating a custom rule, add a name, and choose a trigger and action to get started
6.  Authenticate by clicking **Connect to Notion** and following the steps
7.  Click **Select pages** to allow Asana access
8.  Select the pages you want Asana to access and click **Allow access**.
9.  Paste the URL of the parent page or database
10. Click **Create Rule**

> To add the URL of the page, ensure the page is connected to Asana. To connect it, click the three dot icon at the top right hand of the page, select **Connections**, and check the **Notion for Asana connection** is active.

### Notion

Here’s how to attach an existing Notion page as a widget to an Asana task:

1.  Log into Asana, and find the project where you want to enable the Notion widget
2.  Click on **Customize** in the upper right-hand corner
3.  Scroll down to the **Apps** section, then select **+Add app**
4.  Select **Notion widget**
5.  Navigate to an Asana task
6.  Link an existing Notion page to a task by clicking the **Add Notion** page button under the **Notion** field at the top of the task details pane
7.  Insert the URL for your relevant Notion page
8.  Attached Notion details will appear as a widget in the task pane, including owner, comments, and last modified date

Note: This integration is already built into Asana, but you need to sign up for a Notion account to get started.

The Notion widget is available without a paid Asana subscription.

> When a rule creates a Notion page from an Asana task, only the task title will sync. The task description will not sync.

 

> Rules that involve external actions such as sending emails or direct messages (e.g., via Outlook, Salesforce, or Slack) can only be edited by the rule's creator. This restriction applies even if the "Only you can edit this rule" setting is turned off, because the external actions are authenticated using the rule creator's account credentials.

[](https://forum.asana.com/c/forum-en/tips/6)

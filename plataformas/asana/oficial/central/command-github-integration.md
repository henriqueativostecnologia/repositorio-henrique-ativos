---
fonte: https://help.asana.com/s/article/command-github-integration?language=en_US
baixado: 2026-11-10
---

# Command GitHub integration

> **This feature is in Early Access and is only available to select customers.**

The Command source control integration connects your GitHub repositories to Command by Asana, keeping pull request activity in sync with your tickets. After you connect a repository and your personal GitHub account, ticket statuses can update based on pull request events, reviewers can receive inbox notifications, and comments can synchronize between GitHub and Command.

## Setting up the GitHub integration for your domain

A domain admin enables coding agent integrations for the whole org.

1.  Switch to Command mode.
2.  In the side panel, select **Admin**. This option only appears for domain admins.
3.  Next to **GitHub**, click **Connect** 
4.  GitHub opens in a separate window. Select the organization or repositories where you want to install the app, then click **Install** and authorize the connection.
5.  Return to Asana. After the repository integration is connected, the control changes to **Disconnect**, and the automation settings become available.

Setting up individual user GitHub accounts

1.  Go to your **Profile settings**
2.  Switch to the **Apps** section
3.  Click **Connect** next to **Personal GitHub Account** to link your GitHub account. This connection maps comments from GitHub to your Asana domain user.

## Configuring automation rules

After connecting GitHub, configure automation rules that update ticket statuses based on pull request events. In the **Teamspace Settings**, navigate to the **Integrations**  section, then use the **Select** dropdowns to choose the ticket status for each event:

- When a draft pull request is opened, update status to...
- When a pull request is opened, update status to...
- When a pull request has a review request or activity, update status to...
- When a pull request is ready for merge, update status to...
- When a pull request is merged, update status to...

For example, you can configure an opened pull request to move a ticket to **In review**. After a pull request event occurs, allow a few seconds for the ticket status and linked pull request information to update.

## Linking pull requests to tickets

There are two ways to link a pull request to a Command ticket:

1.  **Add the ticket ID to the pull request title.** Include the Command ticket ID directly in the title, such as **\[CODE-620\] Fix login bug**.
2.  **Use a magic word in the pull request description.** Add a supported keyword followed by one or more ticket URLs or IDs. Supported keywords include: `tasks`, `task`, `tickets`, `ticket`, `ref`, `refs`, `references`, `part of`, `related to`, `contributes to`, `toward`, and `towards`. You can include multiple ticket URLs or IDs after a magic word to link the pull request to more than one ticket.

After you create the pull request, the integration links it to the ticket and applies the configured status automation. Reviewers can receive inbox notifications in Asana, and comments synchronize between GitHub and the linked ticket.

## Viewing linked pull requests

Linked pull requests appear in the **Version control** section of a ticket. You can click on any pull request to see reviewer details, time in review, the current review status, and links to the pull request. Statuses can include **Changes requested** or **Pending**.

You can link multiple pull requests to one ticket so your team can track related code changes in one place.

## Forward-only status protection

The integration uses forward-only protection for ticket status updates. A GitHub event can move a ticket forward in its workflow, but it cannot move the ticket backward after a later status has been reached.

For example, if a ticket is already in **In review** and you link a draft pull request configured to move tickets to **Not started**, the ticket remains in **In review**. The draft pull request is still linked, but the status does not regress.

## Understand comment synchronization

Comments from linked pull requests appear on the associated Command ticket. When you connect your personal GitHub account, your GitHub comments are attributed to your Asana domain user.

Synchronized comments include the comment text, the pull request title, and links to the comment and pull request. Comments from multiple linked pull requests can appear on the same ticket.

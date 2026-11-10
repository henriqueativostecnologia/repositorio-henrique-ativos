---
fonte: https://help.asana.com/s/article/email-tasks-to-asana?language=en_US
baixado: 2026-11-10
---

# Email tasks to Asana

Forward emails to Asana to turn them into actionable tasks without leaving your email inbox. You can create both tasks and messages by sending emails to Asana. Please note that you can only forward emails to Asana with a maximum size of 30 MB.

Get started with a [free Asana trial](https://asana.com/create-account) today.

## How Asana interprets a forwarded email

| Email field                               | Task field:                                                                                         |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Email to `x@mail.asana.com`               | Task in [My Tasks](https://asana.com/guide/help/fundamentals/my-tasks "My Tasks")                   |
| Additional address added in the To: field | Task collaborators[](https://asana.com/guide/help/tasks/understanding-tasks#gl-assignee "assignee") |
| CC'd email recipients                     | Task collaborators                                                                                  |
| Email subject                             | Task name                                                                                           |
| Email body                                | [Task description](https://asana.com/guide/help/tasks/fields#gl-description "Task description")     |
| Email attachments                         | Task [attachments](https://asana.com/guide/help/tasks/comments#gl-attachments "attachments")        |
| From                                      | Task collaborator                                                                                   |

> Please note that **x** in 'x@mail.asana.com' is not a variable.

Asana Gov clients should use **@mail.asana-gov.com** when composing or forwarding emails to create tasks.

## Email tasks to your My Tasks

To create tasks in your **My Tasks** via email, send an email to `x@mail.asana.com`. By default, `x@mail.asana.com` will create a task in the workspace or organization associated with your email address chosen in the Email Forwarding tab.

#### To change the organization or workspace associated with your email address:

- Click your profile photo at the right of the [top bar](https://asana.com/guide/help/fundamentals/navigating-asana#gl-top-bar "top bar")
- Select** Settings**
- Select the **Email Forwarding** tab
- Choose the organization or workspace that you want to associate with your email address

From the **Email Notifications** tab you have the option to [Add more email addresses to your account](https://help.asana.com/s/article/asana-account-email-policy?language=en_US "Add more email addresses to your account"). When adding an additional email address to your Asana account, note that adding an email address that is already associated with a different Asana account will result in both accounts being merged. This is an irreversible change.

> See how others use email effectively with Asana in the [forum](https://forum.asana.com/c/forum-en/tips/6).

## Email tasks to a project

You can send emails to create tasks directly in any Asana project, assuming you have the relevant project permissions.

Every project in Asana has a unique email address, that can be used to create tasks in that project.

.        

#### To find a project's email address:

1.  Navigate to the project
2.  Click on the **Customize** menu
3.  Select **Emails**
4.  Copy the email address under **Add tasks via email**

You can manually identify your project's email address by using the project's unique ID:

- Open any project
- Your project ID is the string of numbers in your project's URL (it should look like `https://app.asana.com/0/projectID/list`)

To create a task in your project via email, send an email to `x+projectID@mail.asana.com`. For example, if your projectID is `12345678`, you would email `x+12345678@mail.asana.com`.

Create tasks straight from your email inbox with the [Asana for Gmail](https://asana.com/guide/help/api/gmail-add-on "Asana for Gmail") add-on or [Asana for Outlook](https://asana.com/guide/help/api/outlook "Asana for Outlook") integration.

> Please note users can only create tasks in project's that they are already a member of unless both the project and the team are public. In this case users can create tasks without becoming a member of the project.

## Email messages

You can post messages to your [teams](https://asana.com/guide/help/organizations/team-basics "teams") or [projects](https://asana.com/guide/help/projects/basics "projects") by sending an email.

### Email to team messages

At the bottom of every team's messages page, there is an email address listed. The email address for any team message is `team+teamID@mail.asana.com`

### Email to project messages

At the bottom of every project's messages page, there is an email address listed. The email address for any project message is `project+projectID@mail.asana.com`

Send an email to this address to create a post in that team or project. You can also CC other people to add them as collaborators to your message.

In organizations, you can only send message posts via email from your company email address.

For example, if you were in the `acme.com` organization, you can only post a message via email by sending a message from your `@acme.com` email address, even if you have [other email addresses](https://help.asana.com/s/article/asana-account-email-policy?language=en_US) attached to your user account.

> Ensure that everyone you include in the CC or To fields have access to your workspace, organization or project in Asana, and that you use the email address associated with their Asana account. If they do not have access, you may receive a notification indicating that your task could not be created.

## Auto-forward emails

If you want to create tasks in Asana for emails you regularly receive, you may want to automatically forward them. To auto-forward emails to Asana:

1.  Create a forwarding email account.
2.  In Asana, add forwarder@ to your [organization](https://asana.com/guide/help/organizations/basics#gl-people "organization") or [workspace](https://asana.com/guide/help/workspaces/basics#gl-people "workspace") and add this email address to Asana and the project you're emailing to.
3.  Log out of your Asana account and log in as the forwarder account, then [turn off the account's email notifications](https://asana.com/guide/help/email/email-from-asana#gl-turn-off "turn off the account's email notifications").
4.  Set your forwarder@ account to auto-forward mail into your Asana project. The following are instructions for common email clients:

- [Gmail](https://support.google.com/mail/answer/10957?hl=en "Gmail")
- [Microsoft Exchange](https://support.office.com/en-us/article/Automatically-forward-my-messages-to-another-e-mail-account-9f124e4a-749e-4288-a266-2d009686b403 "Microsoft Exchange")
- [Yahoo](https://help.yahoo.com/kb/SLN3525.html "Yahoo")

Now, every time forwarder@ receives an email, it will be forwarded to the Asana project and assigned to the forwarding account. These tasks can then easily be reassigned.

## Email authentication

To ensure that your account is safe from potential phishing and email spoofing, we require that the mail server that sends your emails is properly configured for your email domain. The server must be configured so that the domain of the **envelope address** matches the domain of the **from** address. If this is not the case, you will receive an error message indicating that these addresses are misaligned and will need to contact your mail server admin to resolve this.

## Quick tips

To **email a task to a project**, send an email to **x+projectID@mail.asana.com**

To **email a message to a project**, send an email to **project+projectID@mail.asana.com**

To **email a message to a team**, send en email to **[team+teamID@mail.asana.com](mailto:team+teamID@mail.asana.com)**

## Emailing tasks to Asana Gov

Asana Gov clients use a different email domain to send tasks to Asana. Instead of @mail.asana.com, Asana Gov clients should use **@mail.asana-gov.com** when composing or forwarding emails to create tasks. For example, to email a task to your **My Tasks** as an Asana Gov user, forward your email to [x@mail.asana-gov.com](mailto:x@mail.asana-gov.com), where x is your unique Asana Gov email key.

To email a task to a specific project in Asana Gov, use the format [x+projectID@mail.asana-gov.com](mailto:x+projectID@mail.asana-gov.com).

 

> Like what you see? Get started with a free trial today.
>
> [Try for free](https://asana.com/create-account "Try for free")

[](https://forum.asana.com/c/forum-en/tips/6)

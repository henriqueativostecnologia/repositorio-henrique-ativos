---
fonte: https://help.asana.com/s/article/request-tracking?language=en_US
baixado: 2026-11-10
---

# Email communication with form submitters

**Available on Asana** [Starter](https://asana.com/plan/starter)**,** [Advanced](https://asana.com/plan/advanced)**,** [Enterprise](https://asana.com/enterprise)**, and** [Enterprise+](https://asana.com/enterprise) **tiers. Available on divisions.**

This feature allows form submitters in your organization to reply to form submissions via email, even if they don’t have an Asana license. Thus, any team can track and follow up on requests.

This will allow you to:

- Standardize work intake and track internal requests across your organization in a centralized workflow.
- Capture important information upfront to prevent key details from getting lost.
- Enable seamless collaboration and communication between form submitters, requesters, and requestees to ensure work progress. 

> This feature is not available for organizations that have enabled HIPAA compliance.

## Creating a form

To create a form, navigate to your desired project, then to the **Customize menu** and click **Forms**. From here, you can create a new form by clicking the **+Add** button or editing an existing one.

You can keep form submitters across your organization in the loop of their requests, even if they don’t have an Asana license. To do so, you must change your form access settings to **Organization only**.

1.  Navigate to the **Customize menu**
2.  Create a new form or choose an existing one
3.  Go to the **Settings** tab
4.  Set the form access to **Organization only**
5.  Toggle on **Receive email replies** to receive comments from the form submitter
6.  Toggle on **Send email replies** to send comments via email to the form submitter

> Ticket submitters don’t need an Asana license. However, they must have an email with the organization’s domain or be added as a guest.

In the example above, we can see the following:

1.  Eric doesn’t have an Asana license, but he was able to reply via email to enquire about the status of a request. Even though it was sent via email, this comment was received in Asana as a comment.
2.  Hailey, who has an Asana license, comments on the task and asks Josef to take over this request. Eric won’t see this comment.
3.  Josef, who has an Asana license, comments on the task and checks the **Send response to submitter** box. Eric will receive Josef’s comment via email.
4.  Josef comments once again on the task. Eric won’t see this comment.
5.  Josef has just checked the checkbox, so the next message will be sent to Eric

Here’s an example of what a response from Josef would look like for Eric.

> SAML required domains need [SAML group mapping](https://help.asana.com/s/article/setting-saml-group-mapping-for-licenses?language=en_US) or a [view-only license](https://help.asana.com/s/article/view-only) to enable non Asana users to access forms. This does not apply to divisions with SAML required.

## Rules for request tracking

To streamline request tracking, you can create automated rules that enhance communication and ensure timely follow-ups. Here are two key rules you can configure:

1.  **Triggering actions based on comments
    **Set up a rule that automatically triggers when a comment is either sent to or received from the form submitter. This ensures that relevant updates, inquiries, or responses are captured and acted upon without manual intervention.
    Commenter  

2.  **Sending emails
    **

    Configure a rule action that automatically sends an email to the form submitter. By using dynamic variables, you can personalize the message with details.

## FAQ

### Why can’t I edit the email field in the form editor when the email reply form settings are turned on?

When you turn on the ‘receive email replies’ and the ‘send email replies’ settings, we capture the verified email address of the form submitter to enable email replies.

### What happens if I turn off one of the settings, but not the other?

The settings ‘receive email replies’ and ‘send email replies’ can work independently. These settings enable you to have a two-way communication channel or one-way. For example, there may be use cases where you want to enable Asana users to send replies to the form submitter but do not want to receive replies from submitters.

### What happens if I turn on the “add as collaborator” setting?

In addition to the email send and reply settings, any form submitter who is already an Asana user will be added to the task as a collaborator. If the person submitting the form does not have an Asana account, they will not be added to the task as a collaborator. Instead, you can use the checkbox in the task comment box to send your comment to them as an email.

### How does this work on mobile?

Mobile support is limited at the moment. Right now, you can differentiate between a regular (internal) comment on a task and a comment that was sent via email or received via email.

### Does this feature support sending and receiving attachments?

Yes, we support both incoming and outgoing attachments.

[](https://forum.asana.com/c/forum-en/tips/6)

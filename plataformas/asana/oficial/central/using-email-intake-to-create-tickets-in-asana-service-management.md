---
fonte: https://help.asana.com/s/article/using-email-intake-to-create-tickets-in-asana-service-management?language=en_US
baixado: 2026-11-10
---

# Using email intake to create tickets in Asana Service Management

Asana Service Management lets your team receive support requests from anyone with an email address, whether or not they have an Asana account. 

When someone sends an email to your team's support address, a ticket is created automatically in your team’s queue. 

Any replies that the requester sends to the confirmation email they receive are added as comments on the ticket, keeping the full conversation visible to your team in one place.

> This article covers setting up an email address so requesters can submit support tickets to your service queue. If you want to create tasks by forwarding emails to x@mail.asana.com, or email tasks directly to a project, see [Email tasks to Asana](https://help.asana.com/s/article/email-tasks-to-asana).

## Before you begin

Email forwarding requires a verified sending domain. Before a queue can receive requests via email, an organization admin must [verify a sending domain in the admin console](https://help.asana.com/s/article/using-email-bridge-in-a-project?language=en_US#setting-up-verified-email-domains). 

This confirms your organization owns the domain and authorizes Asana to send notification emails that appear to come from your domain rather than from Asana directly.

Once a domain is verified, the **Allow sending from verified domains** setting in the admin console is enabled automatically, and queue owners can connect their support email address.

## Set up email forwarding for a service queue

**Option1: From the queue**

1.  Open your queue and select **Settings**.
2.  Under **Ticket intake and routing**, click **Email forwarding**.

**Option 2: From the Admin menu**

1.  Click **Admin** in the Service sidebar, then click the queue you want to configure under **Manage queues**. 
2.  Under **Ticket intake and routing**, click **Email forwarding**.

Once you've selected **Email forwarding**, complete the setup:

1.  In the **Set up email forwarding** modal, enter your support email address prefix and select your verified domain from the drop-down. This is the address requesters will use to submit tickets (for example, [support@acme.com](mailto:support@acme.com)).
2.  Sign into your email client and open the forwarding and POP/IMAP settings for your support mailbox. Follow the instructions provided by your email client to configure forwarding. The modal includes a link to a step-by-step setup guide for common email clients.
3.  When your email client asks for a destination, click **Copy** next to the Asana address shown under **Add email forwarding address** and paste it into your email client.
4.  Click **Save**.

> Each email address can only be connected to one queue. To enable email intake for a second queue, use a different email address.

You can also adjust two settings before saving:

Turn on **Send ticket updates to all recipients** if you want everyone in the To and CC fields to automatically receive ticket updates via email.

If your admin has set up a company logo in the admin console, you can turn on **Show company logo in emails** to include it in notification and reply emails. If no logo has been configured yet, this option will be greyed out.

## How email intake works for requesters

Requesters do not need an Asana account to submit or follow up on a request. When they send an email to your support address, a ticket is created and they receive a notification email from your verified domain. 

Each notification email tells requesters that their reply will be added to the ticket automatically, so they always know how to follow up.

Requesters can reply to any notification email to add a comment to their ticket. 

Anyone who was in the To or CC fields of the original email also receives notifications and can reply the same way. 

The full thread is visible to requesters in their email client, while the same conversation is tracked inside the ticket in Asana.

## How team members manage email tickets

Tickets created via email appear in the ticket feed alongside tickets from other intake channels. Each email ticket shows “Email” as the source in the ticket details panel, so team members can see at a glance how the request was received.

The **Conversation** tab shows the full email thread, including all messages from the requester and anyone copied on the original email. 

You can hover over the recipient count in the reply area to see everyone included on the thread.

Reply to the requester at the bottom of the conversation panel and click **Send**. The reply is sent by email to the requester and all recipients, and is recorded as a comment on the ticket.

## Disconnect email forwarding

### To remove email forwarding from a queue:

1.  Open your queue and select **Settings** from the left navigation.
2.  On the **Ticket intake settings** page, click **Email forwarding**.
3.  Click **Remove email forwarding** at the bottom of the **Edit email forwarding** dialog. A confirmation dialog explains that once removed, requests and replies sent to that email address will no longer be recorded in Asana, and ticket updates will be sent from the Asana email domain. 
4.  Click **Remove** to confirm.

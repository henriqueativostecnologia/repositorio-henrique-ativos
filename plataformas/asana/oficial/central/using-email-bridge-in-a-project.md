---
fonte: https://help.asana.com/s/article/using-email-bridge-in-a-project?language=en_US
baixado: 2026-11-10
---

# Using email bridge in a project

Email Bridge allows people without an Asana account to create tasks in an Asana project by sending an email to a support or intake email address (for example, support@yourcompany.com). 

When that email is forwarded to the project's Asana email address, a task is automatically created. If the external sender replies to the notification email they receive, their reply is added as a comment on the task, keeping the conversation threaded without requiring them to log in to Asana.

#### Related articles

- [Email domain management for Asana organizations](https://help.asana.com/s/article/email-domain-management-for-asana-organizations)

- [Email tasks to Asana](https://help.asana.com/s/article/email-tasks-to-asana)

## Setting up verified email domains

Before your organization can use Email Bridge, an organization admin must verify a sending domain in the admin console. This step proves that your organization owns the domain and authorizes Asana to send emails on its behalf, so notification emails to external senders appear to come from your domain rather than from Asana directly.

To get started, navigate to the **Admin console** and select **Settings**. Click **Verified email domains** to open the domain management page. From here, you can see any existing verified or pending domains, and you can enable the **Allow sending from verified domains** toggle once a domain has been verified.

To add a new domain, click **Add email domain**. 

In the dialog that appears, enter your **Email domain** (everything after the @ symbol in your email address, for example, acme.org). Click **Submit** to proceed.

After submitting, Asana generates a set of CNAME records you must add to your domain's DNS settings. Click **View DNS records** to see the required CNAME records. Add each record to your DNS provider, then return to the admin console to complete verification. DNS changes can take up to 72 hours to propagate, and verification attempts expire after 28 days. 

CNAME (Canonical Name) Record: Enables cryptographic signing (DKIM). A CNAME record maps an alias to a primary domain name. Asana uses three distinct CNAME records to establish DKIM (DomainKeys Identified Mail). This works like a secure digital signature stamped on every notification email sent to an external customer. It mathematically proves that the email truly came from your company and wasn't altered in transit.

AWS SES requires three CNAME records to rotate your security keys seamlessly behind the scenes without interrupting your mail flow. While only one key is actively signing your emails at any given time, the other two records allow AWS to pre-stage the next key and keep a backup ready for a smooth, automated handover.

Once verification is complete, the domain moves from **Pending email domains** to the verified list, and the **Allow sending from verified domains** option becomes available.

Once an organization admin has verified a sending domain, project owners can connect that domain to their project and configure their external email inbox to forward incoming messages to Asana. External users can then create tasks and add comments simply by sending or replying to emails, with no Asana account required.

## How to set up email forwarding for a project

To connect a verified domain to your project, open the project and click **Customize** in the top right corner. Select **Emails** from the panel that appears. You will see the project's Asana email address listed under **Add tasks via email**. You can click **Copy** to copy this address for use in your forwarding configuration.

To configure advanced settings, scroll down and click **Manage email forwarding** under **Advanced settings**. The **Advanced email settings** dialog opens on the **Manage email forwarding** tab. 

If your admin has not yet verified a domain, you will see a notice prompting you to contact your admin. Once a domain is verified, select it from the **Verified domain** section, then copy the Asana email address shown under **Email forwarding** and add it as a forwarding destination in your external email client (such as Gmail or Outlook).

**Note: Make sure your domain is verified; otherwise, email bridge won’t work.**

To enable automatic task creation, configure your external email inbox (for example, support@yourcompany.com) to auto-forward incoming messages to the project's Asana email address. When a forwarded email arrives, Asana creates a new task using the email subject as the task title and the email body as the task description.

## How to set up automated email replies

You can configure automated replies to notify external senders when their email creates a task. In the **Advanced email settings** dialog, click the **Automate email replies** tab. 

Click **Add** to create a new automated reply, such as a "Task received" confirmation. You can also upload a logo under **Customize emails** to brand the automated reply emails sent to external senders. A preview of the email is shown at the bottom of the panel.

## How external users interact with tasks

When an external user sends an email that creates a task, they receive a notification email from your verified domain. If the external user replies to that notification email, their reply is automatically added as a comment on the corresponding Asana task. This keeps the conversation threaded and visible to your team inside Asana, without requiring the external user to create an Asana account or log in.

## Troubleshooting

Most Email Bridge issues come down to domain verification, the project connection, or how forwarding is configured at your email provider.

- If your domain won't verify, start with [Your domain isn't verifying](https://www.google.com/search?q=%23-your-domain-isnt-verifying).
- If your domain is verified but emails aren't showing up, go to [Forwarded emails aren't creating tasks or comments](https://www.google.com/search?q=%23-forwarded-emails-arent-creating-tasks-or-comments)

### Your domain isn't verifying

In **Settings \> Verified email domains**, a domain you have added will show as either **Pending** or **Failed**.

#### **If your domain stays under "Pending email domains":**

- **Allow time to propagate:** DNS changes do not update instantly. It can take up to **72 hours** for your changes to propagate across global DNS servers and be detected by Asana.
- **Re-check your DNS records:** Verification requires **three CNAME** records exactly as shown when you click **View DNS records**. Even a single missing, misspelled, or altered record will block verification.

#### **If your domain shows a "Failed" status:**

A **Failed** status means Asana checked your domain but could not verify your ownership. The page will display the error: *“We couldn’t reach the verification service. Try again.”* The most common cause is a missing or incorrect DNS record.

1.  **Remove the old records:** Go to your DNS provider's console and remove any DNS records you added during the failed verification attempt.
2.  **Restart the process:** Click **Try again** in the Asana Admin Console to start over. This will generate a **fresh set of DNS records** for you to add to your DNS provider.

### Forwarded emails aren't creating tasks or comments

This is the most common delivery issue. Work through these verification checks in order:

1.  **Confirm your sending domain is verified:** In the Admin Console, go to **Settings → Verified email domains**. Your domain must appear in the verified list, not under **Pending email domains**.
2.  **Confirm the** ***Allow sending from verified domains*** **toggle is ON:** This option only becomes available in the Admin Console once a domain is fully verified.
3.  **Confirm the project is connected to the verified domain:** Open the project, click **Customize → Emails**, then under **Advanced settings** click **Manage email forwarding** and make sure your verified domain is selected. *(If you see a notice to contact your administrator, the domain has not been verified yet).*
4.  **Confirm forwarding is active at your email provider:** In Gmail, Outlook, or your custom mail server, make sure mail sent to your intake address (for example, support@yourcompany.com) is configured to **forward** to the project's unique Asana email address shown under **Manage email forwarding**.
5.  ⚠️ **Note:** Email Bridge supports standard email **forwarding rules**. Simple email **redirects** (which do not modify the email envelope headers) are not supported.
6.  **Confirm you completed your provider's forwarding confirmation:** See [The forwarding confirmation didn't complete](https://www.google.com/search?q=%23-the-forwarding-confirmation-didnt-complete) below.
7.  **Confirm your email passes DKIM authentication:** Email Bridge uses DKIM to authenticate forwarded mail. Because standard SPF checks do not survive forwarding loops, **incoming emails must carry a valid DKIM signature** or they will be rejected (and the sender will receive an "Undeliverable" notification).
    1.  Make sure your outbound mail is DKIM-signed. Most major providers (like Google Workspace and Microsoft 365) sign emails automatically.
    2.  Custom or self-managed mail servers may need DKIM configured manually. Check with your mail provider for specific configuration instructions.

### The forwarding confirmation didn't complete

Not all email providers require this step. Some providers (Gmail in particular) send a one-time confirmation email to verify you own the inbox when you first set up forwarding, while many others do not. If your provider does not require this step, you can skip this section.

When a confirmation is required:

1.  **Asana intercepts the email:** Asana automatically captures the verification email and delivers it into your connected project **as a task**.
2.  **Action:** Open the task, locate the verification link in the email body, and click it to authorize forwarding.

> Until this step is completed, your email provider will block all forwarding, and no tasks will be created.

### Replies aren't being added as comments

The original sender, the original "To" recipients, and anyone CC’d on the initial email thread can reply to email notifications to add comments directly to the Asana task. If a reply is not posting:

- **Reply within the thread:** You must use **Reply** or **Reply All** on the Asana notification email rather than starting a brand-new message. The metadata that routes the reply to the correct task lives in the notification email's headers.
- **Reply from an authorized address:** A reply is only accepted if it is sent from an email address that was on the original thread (the original sender, a "To" recipient, or a CC'd address). If a participant forwards the notification to an outside address and *they* reply, Asana will reject the comment for security reasons.

### Still need help?

If you have verified all the checks above and emails are still failing to sync, please contact **Asana Support** and include:

- Your organization / workspace name and your **verified sending domain**.
- The **URL of the connected Asana project**.

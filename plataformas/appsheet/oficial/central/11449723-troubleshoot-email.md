---
fonte: https://support.google.com/appsheet/answer/11449723?hl=en
baixado: 2026-11-10
---

# Troubleshoot email

Resolve the most common bot email problems using the guidance provided in the following sections. See also [Send an email from a bot](https://support.google.com/appsheet/answer/11447614) and [Troubleshoot bots](https://support.google.com/appsheet/answer/11547467).

## Why didn't my email arrive?

Successfully sending an email message from the AppSheet server does not mean that the email message was received by the recipient.

You can determine if the email was delivered to the user's email server, as described in [How do I determine whether an email was delivered?](https://support.google.com/appsheet/answer/11449723?zippy=%2Chow-do-i-determine-whether-an-email-was-delivered&sjid=10159459730103537441-NA#zippy=%2Chow-do-i-determine-whether-an-email-was-delivered) (below).

If the email was delivered but the recipient cannot find it, ask them to check their *spam* email folder. The email may have been redirected to the spam email folder by the recipient's email filter.

The email may be not be delivered for the following reasons:

- The email may have been blocked by the email service because the attachment was too large.
- The customer's email server may be blocking or bouncing email messages to that recipient.
- Most email servers have policies to block spam email and to block large volumes of email from a single source. These policies may reject valid system-generated emails and prevent the email from being delivered. This happens frequently.
- If you have a typo in one or more of the email addresses. The email will not be delivered to any of the intended recipients in this case.

## How do I determine whether an email was delivered?

To determine whether an email was delivered, [check the audit history log](https://support.google.com/appsheet/answer/10104794).

The following information will be displayed:

- Email subject
- Email recipient
- Email sender; that is, `noreply@appsheet.com`
- Send time in UTC
- Result of operation

## Why are emails only sent to the app creator?

For prototype testing (before you deploy the app), any emails sent from the app are delivered to the app creator only. This ensures that you do not inadvertently send email messages, SMS messages, or notifications, or post HTTP messages while debugging your bot.

## Why is the parent record displayed but the child records are missing?

When you add a parent record along with one or more child records, AppSheet first adds the parent record, then each of the child records. If your bot is triggered when the parent record is added, it does not display the child records because they will not have not been added when the bot executes.

To resolve this, see [Send an email only after adding a parent record and all of its child records](https://support.google.com/appsheet/answer/11447614#send-email-after-parent-and-all-child).

## Why is there a large gap between the preheader and the email body text?

If there is a large gap between the email preheader and the email body text, try the following:

1.  Set all page margins to **0**.

2.  Set the **Page Setup** to **A4**

## Why is the email attachment formatted incorrectly?

In your bot, you can define parameterized Google Doc templates that will be converted to PDF files and sent as attachments with the bot email. Occasionally, these attachments are not formatted identically to the original document template. To troubleshoot this problem, it is important to understand the steps used by AppSheet to process the attachment templates.

AppSheet performs the following steps when processing attachment templates:

1.  Exports the Google Docs template to HTML.
    This conversion is lossy --- in particular, HTML does not support the concept of pagination.

2.  Modifies the HTML by replacing all template variables and expressions in the HTML template with data values.

3.  Converts the HTML to PDF.
    This conversion reintroduces pagination constructs (such as margins and page breaks). However, they may not match the original pagination settings.

Formatting inconsistencies can be introduced at step 1 or step 3 because neither step maintains complete document fidelity. Most commonly, the problems are introduced at step 1 and can be fixed manually, as follows:

1.  Open the Google Docs template, export it to PDF, and view the results.
    Tweak the formatting options in the Google Docs template until it exports to PDF as required.

2.  Open the Google Docs template, export it to HTML, and view the results.
    Tweak the formatting options in the Google Docs template until it exports to HTML as required.

## Why are the images in PDF attachments too large or too small?

You can control the size of images shown in the email body or attachments. By default, columns/expressions of type Image are shown larger than columns/expressions of type Thumbnails.

You can specify a [format rule](https://support.google.com/appsheet/answer/10106703) to further control the size of images in your email content. In the format rule, you choose the table, one or more columns, an optional condition, and the image size (Tiny, Small, Medium, Large). See [Display images, thumbnails, drawings, and signatures in templates](https://support.google.com/appsheet/answer/11547760).

## How can I control when and how maps are shown in my attachment PDF?

You can control how geographic column values (Addresses and LatLongs) are shown in the email body or attachments. By default, columns/expressions of type LatLong are shown as static maps with a pin, while columns/expressions of type Address are shown as text.

You can specify a [format rule](https://support.google.com/appsheet/answer/10106703) to further control the size of static maps in your email content. In the format rule, you get to choose the table, one or more columns, an optional condition, and the image size (Tiny, Small, Medium, Large, or Text). Choosing **Text** results in the textual representation of the value being shown in the attachment. See [Display Address, LatLong, and XY values in templates](https://support.google.com/appsheet/answer/11547559).

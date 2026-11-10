---
fonte: https://support.google.com/appsheet/answer/14875141?hl=en
baixado: 2026-11-10
---

# Troubleshoot AppSheet with Google Forms

You must be a **Google Workspace user** to build AppSheet automations with Google Forms. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Google Forms. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

The following sections provide tips for troubleshooting issues when using AppSheet with Google Forms.

------------------------------------------------------------------------

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/14875141)

#### Automation is not running

If the automation is not running, check the [automation monitor](https://support.google.com/appsheet/answer/11447502#access-automation-monitor) and [Audit History logs](https://support.google.com/appsheet/answer/10104794) (with the filter set to automation). Set the time range and check for runs and errors related to the Google Forms automation.

If the following error is logged:

`Request had invalid authentication` 

Then sign out of AppSheet and sign back in to refresh authentication.

If no runs appear for a bot based on a form event when the form is submitted, then the app owner might have lost access to the form. In this case, make sure that:

- The app owner still has access to the form. See "How to check access to the form" (below).
- The form is connected to the app.

#### Automation runs, but the email is not sent

If your automation runs, but the email is not sent, do the following:

- Check that the application is deployed. An application that isn't deployed can only send email to the application owner. See [Deploy: The Essentials](https://support.google.com/appsheet/answer/10104495).
- Check the validity of the email address or expression used for the **To** field for the email task in the bot.

See also: [Troubleshoot email](https://support.google.com/appsheet/answer/11449723)

#### Error: Data table 'Travel Request' is not accessible

There are two issues that can result in the `Data table <name> is not accessible` error in an application view.

Use the code and message included in the error to determine the issue, as follows:

- Code: `404`, Message: `File not found`
  The application owner no longer has editor access to the form. See "How to check access to the form" (below).
- Code: `401`, Message: `Request had invalid authentication credentials`
  Authentication has expired or is revoked. Sign out of AppSheet and sign back in to refresh authentication.

#### How to check access to the form

To check access to the form, do the following: 

1.  Go to **Data ** .
2.  Select the form-based table in the left Data pane.
3.  Click **View data source**.
4.  Make sure that the app owner has editor access to the form, as described in [Share your form with collaborators](https://support.google.com/docs/answer/2917111).

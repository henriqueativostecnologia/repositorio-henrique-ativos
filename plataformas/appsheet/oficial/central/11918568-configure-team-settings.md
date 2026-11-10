---
fonte: https://support.google.com/appsheet/answer/11918568?hl=en
baixado: 2026-11-10
---

# Configure team settings

**Note**: Teams are supported for Enterprise Plus plans only.

Configure the following team settings:

- [Restrict who can create apps](#restrict-create-apps)
- [Turn Gemini for App Creation on or off](#gemini-for-app-creation)
- [Restrict the recipient list for outgoing email](#outgoing-email-allowlist)
- [Set the public app owner](#public-app-owner)
- [Set the AppSheet session length](#session-length)

See also:

- [Export team audit logs to BigQuery](https://support.google.com/appsheet/answer/12469223)
- [Disable AppSheet databases](https://support.google.com/appsheet/answer/12629371)

## Restrict who can create apps

You can restrict app creation to a specific Google Group. 

**Note**: Before you can restrict who can create apps, you must create an Auth Domain and [share it with your team](https://support.google.com/appsheet/answer/10104795#share-integrations).

When connecting to a Google group in your organization, AppSheet uses the **group ID** and not the group name. If the group ID changes for any reason (for example, if you delete and recreate the Google group), this connection will need to be reconfigured. See [Connect AppSheet to the groups in your organization](https://support.google.com/appsheet/answer/10104381#connect-appsheet).

After restricting app creation to a Google Group, if the root admin leaves or the Google group members definition changes to remove the root admin, then the organization admin must assign a root admin to the Google group in order to change this setting.

To restrict who can create apps:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Do one of the following:
    - Select **Admin Console **in the account profile drop-down, click **Settings** in the left navigation, then click **My team** at the top of the page.
    - Select **My team** in the account profile drop-down and click **Settings**.
3.  Under App Creator Restrictions, select a Google Group from the drop-down.

    App Creators Restrictions field in the team Settings page
4.  Click **Save**.

## Turn Gemini for App Creation on or off

Gemini for App Creation is available to all AppSheet paid accounts, including Google Workspace customers with AppSheet Core and AppSheet Enterprise Plus, and individual accounts with AppSheet Publisher Pro, AppSheet Starter, AppSheet Core, and AppSheet Enterprise Plus. 

Gemini for App Creation lets you create an app by *describing* your idea using natural language. See [Create apps using Gemini for App Creation](https://support.google.com/appsheet/answer/14699210).

To turn Gemini for App Creation on or off:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Do one of the following:
    - Select **Admin Console **in the account profile drop-down, click **Settings** in the left navigation, then click **My team** at the top of the page.
    - Select **My team** in the account profile drop-down and click **Settings**.
3.  Turn on or off **Disable Gemini app creation**.
4.  Click **Save**.

## Restrict the recipient list for outgoing email

Define the *outgoing email allowlist* that specifies the domains or email addresses that AppSheet is allowed to send emails to. 

You can define a maximum of **20** domains or email addresses. To enable emails to be sent back to AppSheet, include **appsheet.com** in the allowlist.

An empty allowlist enables outgoing email to be sent to **any** domain or email address.

If an email is directed to a domain or email address that is  restricted (not defined in the allowlist), it is removed before the email is transmitted to the AppSheet email provider. Email violations in automations are logged in the [Audit History](https://support.google.com/appsheet/answer/10104794) as an `OutgoingEmailAllowListViolations` property.

To restrict the recipient list for outgoing email:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Do one of the following:
    - Select **Admin Console **in the account profile drop-down, click **Settings** in the left navigation, then click **My team** at the top of the page.
    - Select **My team** in the account profile drop-down and click **Settings**.
3.  Enter a comma-separated list of domains or email addresses in the **Outgoing email allowlist** field.
    **Note**: Do not enclose values in quotes.

    Outgoing email allowlist section
     
4.  Click **Save**.

The setting take effect immediately.

## Set the public app owner

**Note**: This feature is available in the Enterprise Standard and Enterprise Plus plans.

App users can identify the app owner when reviewing the app **Terms** and **Privacy Policy**. As an admin of an organization, you might identify scenarios where you'd rather not expose the app creator's individual email, especially if the app is used by an external audience or by a large audience within your company.  

To set the public app owner:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Do one of the following:
    - Select **Admin Console **in the account profile drop-down, click **Settings** in the left navigation, then click **My team** at the top of the page.
    - Select **My team** in the account profile drop-down and click **Settings**.
3.  Enter the email address of a team member in the **Public App Owner** field.

    Team settings page showing Public Owner field.
4.  Click **Save**.

After enabling the **Public App Owner** setting for your team, app creators on your team can toggle the **Use Public Owner** setting in their apps. When enabled, the public app owner will be displayed to users of that app. By default, this setting is set disabled. 

1.  Open an app in the app editor.
2.  Select **Info \> Properties**.
3.  Expand the **Information for App Users** section.
4.  Enable **Use Public Owner.**
    **Note:** The **Use Public Owner** property appears only if you have set the public app owner, as described above. 

Use Public Owner toggle enabled on Properties page.

## Set the AppSheet session length

Control how long users can access AppSheet services without having to authorize AppSheet every time they are using the service. This setting applies to web (app editors and app users) and mobile app users.

**Note**: This setting will take effect the next time the user needs to refresh their credentials.

To set the AppSheet session length:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Do one of the following:
    - Select **Admin Console **in the account profile drop-down, click **Settings** in the left navigation, then click **My team** at the top of the page.
    - Select **My team** in the account profile drop-down and click **Settings**.
3.  Enter a duration value that is suitable for the team in the **User session duration** field.
    The default is 90 days. The minimum value is 1 hour and the maximum value is 90 days.
4.  Click **Save**.

It is recommended that you set the [Google services session length](https://support.google.com/a/answer/7576830) in Google Workspace (or an equivalent setting for your specific ID Provider, if available) to a value that is equal to or less than the AppSheet user session duration. In this case, when the AppSheet session expires the user will need to re-authenticate with Google services.

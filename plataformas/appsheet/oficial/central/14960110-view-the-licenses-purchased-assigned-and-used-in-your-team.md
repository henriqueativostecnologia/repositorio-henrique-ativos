---
fonte: https://support.google.com/appsheet/answer/14960110?hl=en
baixado: 2026-11-10
---

# View the licenses purchased, assigned, and used in your team or organization

View the licenses purchased, assigned, and used in your organization or team using the Licenses page in the AppSheet Admin Console.

- [Access the Licenses page](#access-licenses-page)
- [View the license usage summary and warnings](#license-details)
- [View the licenses used](#licenses-used)
- [View the licenses assigned](#licenses-assigned)
- [Download license information](#download-csv)
- [Why aren't all of the purchased licenses listed?](#license-not-listed)

To manage your licenses, see:

- [Purchase a subscription](https://support.google.com/appsheet/answer/15011908)
- [Manage the subscription, licenses, and billing for an individual account](https://support.google.com/appsheet/answer/15066103)
- Google Workspace users:
  - [Add and set up AppSheet for Google Workspace](https://support.google.com/a/answer/10447197)
  - [Assign AppSheet licenses to users](https://support.google.com/a/answer/10569787)

## Access the Licenses page

To access the Licenses page, do the following:

1.  Sign in to [AppSheet](https://appsheet.com).

2.  On the My Apps page, select **Admin Console** from your account profile drop-down.

    Select Admin Console in account profile

    Alternatively, from an Admin page, such as My account or My team, you can select **Admin \> Admin Console **in the top navigation.

3.  Select **Licenses** in the left navigation.

The Licenses page opens.

Licenses page in the Admin Console

The Licenses page in the Admin Console allows you to do the following:

- [View the license usage summary and warnings](#license-details)
- Select the month for which you want to display license usage in the upper-right corner of the page (defaults to the current month)
- [View the licenses used](#licenses-used) for the selected month
- [View the licenses assigned](#licenses-assigned)
- Click the user name for an account in your team or organization (internal user) to [view details for the account](https://support.google.com/appsheet/answer/15100835)

Data refreshes every **24 hours**.

 

When app creators create [public apps](https://support.google.com/appsheet/answer/10104983#share-anyone) (apps that do not require sign-in), an email address is not collected. The only identifying information is the device id. These sign ins are represented as `Guest-`*`#######`* (guest users).

## View the license usage summary and warnings

At the top of the Licenses page, view the number of licenses purchased, assigned, and used for AppSheet Core, AppSheet Enterprise Plus, and User Pass subscriptions. 

If your organization has exceeded the number of licenses purchased or has users who have accessed apps without a sufficient license, you may see warnings. For more information, see [About license warnings](https://support.google.com/appsheet/answer/16003327).

**Note:** License warnings are not shown to app creators or app users—warnings are only visible to admins. However, your AppSheet service may be interrupted after multiple consecutive months of unresolved license warnings. If service interruption becomes necessary, AppSheet will provide at least 30 days of advanced notice to admins.

See also:

- [Why aren't all of the purchased licenses listed?](#license-not-listed)
- [About external user licensing](https://support.google.com/appsheet/answer/15197435)

The following table describes the categories displayed:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Category**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Used                                                                          | Number of licenses (assigned or entitled) that have been used.                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Purchased                                                                     | Number of licenses purchased online.                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Assigned/entitled                                                             | Number of AppSheet Core licenses:                                             |
|                                                                               |                                                                               |
|                                                                               | -   Assigned to users                                                         |
|                                                                               | -   Provided through a [Google Workspace edition that includes AppSheet       |
|                                                                               |     Core](htt                                                                 |
|                                                                               | ps://support.google.com/appsheet/answer/10105400#core-editions) (entitlement) |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Assigned                                                                      | Number of licenses assigned to users with AppSheet Enterprise Plus or         |
|                                                                               | External User licenses.                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Purchased offline                                                             | Number of licenses that were purchased from a seller or reseller offline.     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## View the licenses used

Select the **Used** tab to view the licenses that have been used for the selected month.

**Note:** Reporting on the Used tab is historical. Any changes made to your subscription or to app sharing settings won't cause warnings to be removed until the following month. However, changes to license assignment or pooled licensing will take effect within 24 hours. 

Each list provides the following details:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **User detail**                                                               | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| User name                                                                     | Email address of the AppSheet account.                                        |
|                                                                               |                                                                               |
|                                                                               | For accounts that are in your team or organization, click the user name to    |
|                                                                               | [view details for the                                                         |
|                                                                               | account](https://support.google.com/appsheet/answer/15100835).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Auth provider                                                                 | Provider used to authenticate AppSheet sign-ins. See [Require sign-in: The    |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10104975).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Type                                                                          | Type of user. Can be one of the following:                                    |
|                                                                               |                                                                               |
|                                                                               | -   **Internal** when the user belongs to your team or organization           |
|                                                                               | -   **External** when the user doesn't belong to your team or organization    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Team                                                                          | Team the AppSheet account belongs to. See [Define your team                   |
|                                                                               | membership](https://support.google.com/appsheet/answer/13964712).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App role                                                                      | Role of the AppSheet account. Can be one of the following:                    |
|                                                                               |                                                                               |
|                                                                               | -   **Owner** when the AppSheet account owns at least one app (not as         |
|                                                                               |     co-author)                                                                |
|                                                                               | -   **User** when the AppSheet account is an app user or a co-author of one   |
|                                                                               |     or more apps, but doesn't own any apps                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apps owned                                                                    | Number of apps owned by the AppSheet account. Doesn't count apps for which    |
|                                                                               | the account is a co-author.                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apps used                                                                     | Number of apps accessed by the AppSheet account in the last 30 days.          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| License used                                                                  | Highest subscription required by any app accessed by the user in the last 30  |
|                                                                               | days.                                                                         |
|                                                                               |                                                                               |
|                                                                               | Upgrade your subscription if the license used is a higher-level subscription  |
|                                                                               | than the license assigned. See also [How to determine if a subscription       |
|                                                                               | upgrade is required](https://support.google.com/appsheet/answer/10105099).    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| License count                                                                 | Number of licenses consumed by the user.                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Reason                                                                        | Reason a particular licenses was used. Valid values include:                  |
|                                                                               |                                                                               |
|                                                                               | -   Enterprise Admin - An AppSheet amin consumes an AppSheet Enterprise       |
|                                                                               |     license when they sign in at least once to the AppSheet Admin Console.    |
|                                                                               | -   Enterprise app owner                                                      |
|                                                                               | -   Core app owner                                                            |
|                                                                               | -   Used Enterprise apps                                                      |
|                                                                               | -   Used Core apps                                                            |
|                                                                               | -   External user                                                             |
|                                                                               | -   Unauthenticated user                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Last app usage                                                                | Date that this account last accessed an app.                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## View the licenses assigned

Select the **Assigned** tab to view the licenses assigned.

**Note**: Changes may take 24 hours to be reflected in the AppSheet Admin Console.

Each list provides the following details:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **User detail**                                                               | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| User name                                                                     | Email address of the AppSheet account.                                        |
|                                                                               |                                                                               |
|                                                                               | For accounts that are in your team or organization, click the user name to    |
|                                                                               | [view details for the                                                         |
|                                                                               | account](https://support.google.com/appsheet/answer/15100835).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Auth provider                                                                 | Provider used to authenticate AppSheet sign-ins. See [Require sign-in: The    |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10104975).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Team                                                                          | Team the AppSheet account belongs to. See [Define your team                   |
|                                                                               | membership](https://support.google.com/appsheet/answer/13964712).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Type                                                                          | Type of user. Can be one of the following:                                    |
|                                                                               |                                                                               |
|                                                                               | -   **Internal** when the user belongs to your team or organization           |
|                                                                               | -   **External** when the user doesn't belong to your team or organization    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|                                                                               |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App role                                                                      | Role of the AppSheet account. Can be one of the following:                    |
|                                                                               |                                                                               |
|                                                                               | -   **Owner** when the AppSheet account owns at least one app (not as         |
|                                                                               |     co-author)                                                                |
|                                                                               | -   **User** when the AppSheet account is an app user or a co-author of one   |
|                                                                               |     or more apps, but doesn't own any apps                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apps owned                                                                    | Number of apps owned by the AppSheet account. Doesn't count apps for which    |
|                                                                               | the account is a co-author.                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apps used                                                                     | Number of apps accessed by the AppSheet account in the last 30 days.          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| License assigned                                                              | AppSheet license assigned to user.                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Last app usage                                                                | Date that this account last accessed an app.                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Download license information

Download license information for all accounts as a CSV file by selecting **More**  **\> Export CSV** in the upper right corner of the main body of the page.

## Why aren't all of the purchased licenses listed? 

The AppSheet Admin Console provides information on the licenses purchased through Google Workspace, including AppSheet Core, AppSheet Enterprise Plus, and AppSheet External User.

Licenses might not be listed in the AppSheet Admin Console for the following reasons:

- The license was purchased using either of the following methods:
  - Offline or from a reseller prior to June 2024
  - Through a consumer billing account on [appsheet.com](https://appsheet.com)
- The license was a legacy type (such as, AppSheet Business) and has been consolidated into AppSheet Enterprise Plus.

If you don't see the correct number of licenses purchased from Google Workspace or a reseller, click **Send feedback** in the AppSheet Admin Console and report this to AppSheet.

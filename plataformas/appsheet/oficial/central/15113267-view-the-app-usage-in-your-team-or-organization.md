---
fonte: https://support.google.com/appsheet/answer/15113267?hl=en
baixado: 2026-11-10
---

# View the app usage in your team or organization

View the app usage in your team or organization using the Usage page in the AppSheet Admin console.

- [Access the App usage page](#explore-usage-page)
- [View the total number of unique users](#view-unique-users)
- [View all app usage](#view-all-usage)

Data refreshes every **24 hours**.

## Access the App usage page

 To access the App usage page, do the following:

1.  Sign in to [AppSheet](https://appsheet.com).

2.  On the My Apps page, select **Admin Console** from your account profile drop-down.

    Select Admin Console in account profile

    Alternatively, from an Admin page, such as My account or My team, you can select **Admin \> Admin Console **in the top navigation.

3.  Select **Reports \> App usage** in the left navigation.

The App usage page opens.

Usage page in Admin Console

 The App usage page in the AppSheet Admin console allows you to do the following:

- [View the app usage summary](#view-unique-users)
- View daily active users, including internal and external
- [View all app usage](#view-all-usage)
- [Download app usage](#download-csv)
- Set the date range (last *n* number of days or custom) and view the last updated timestamp in the upper-right corner of the page
- Search or filter the usage list
- Click the name of an internal app in the list to [view details for the app](https://support.google.com/appsheet/answer/14961200#view-app-details)
- Click the user name for an account in your team or organization (internal user) to [view details for the account](https://support.google.com/appsheet/answer/15100835)
  When app creators create [public apps](https://support.google.com/appsheet/answer/10104983#share-anyone) (apps that do not require sign-in), an email address is not collected. The only identifying information is the device id. These sign ins are represented as `Guest-`*`#######`* (guest users).

## View the app usage summary

At the top of the Usage page, view the following information:

- Number of users that accessed apps for the selected date range, with a breakdown of users that are internal and external to your team or organization. An **internal user** belongs to your team or organization, whereas an **external user **doesn't belong to your team or organization.
- Number of apps that were accessed for the selected date range, with a breakdown of apps that are internal and external to your team or organization. An **internal app** is owned by a member of your team or organization, whereas an **external app** is listed when a team or organization member (internal user) uses an app that doesn't belong to the team or organization.

## View app usage

In the main body of the App usage page, view all app usage in your team or organization, including the following details. Sort by user name, app name, or other details, as required.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **User detail**                                                               | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| User name                                                                     | Email address of the AppSheet account.                                        |
|                                                                               |                                                                               |
|                                                                               | For accounts that are in your team or organization, click the user name to    |
|                                                                               | [view details for the                                                         |
|                                                                               | account](https://support.google.com/appsheet/answer/15100835).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App name                                                                      | App name.                                                                     |
|                                                                               |                                                                               |
|                                                                               | For apps owned by a member of your team or organization, you can click the    |
|                                                                               | app name to [view details for the                                             |
|                                                                               | app](https://support.google.com/appsheet/answer/15098215).                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Auth provider                                                                 | Provider used to authenticate AppSheet sign-ins. See [Require sign-in: The    |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10104975).             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Usage type                                                                    | Type of app usage. Can be one of the following:                               |
|                                                                               |                                                                               |
|                                                                               | -   **Internal** when the user and app belong to the same team or             |
|                                                                               |     organization                                                              |
|                                                                               | -   **External user** when the user doesn't belong to the team or             |
|                                                                               |     organization                                                              |
|                                                                               | -   **External app** when a team or organization member (internal user) uses  |
|                                                                               |     an app that doesn't belong to the team or organization                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App owner                                                                     | Owner of the app.                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App owner's team                                                              |  Team the app owner belongs to. See [Define your team                         |
|                                                                               | membership](https://support.google.com/appsheet/answer/11938918#define).      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| License required                                                              | Minimum license required to use the app based on                              |
|                                                                               | its [features](https://support.google.com/appsheet/answer/10105400#features). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Activity (by day)                                                             | Daily usage for the app.                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Last access                                                                   | Date that this account last accessed the app.                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

##  Download app usage

Download app usage as a CSV file by selecting **More**  **\> Export CSV** in the upper right corner of the main body of the page.

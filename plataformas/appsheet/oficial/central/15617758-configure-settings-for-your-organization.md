---
fonte: https://support.google.com/appsheet/answer/15617758?hl=en
baixado: 2026-11-10
---

# Configure settings for your organization

Configure settings for your organization in the AppSheet Admin Console.

- [Access the Settings page](#explore-settings-page)
- [Turn on or off pooled licensing for AppSheet Enterprise Plus](#pooled-licensing)
- [Restrict access to resources by external AppSheet accounts](#restrict-external-account-credentials)

To configure settings for your team, see [Configure team settings](https://support.google.com/appsheet/answer/11918568).

## Access the Settings page

 To access the App usage page, do the following:

1.  Sign in to [AppSheet](https://appsheet.com).

2.  On the My Apps page, select **Admin Console** from your account profile drop-down.

    Select Admin Console in account profile

    Alternatively, from an Admin page, such as My account or My team, you can select **Admin \> Admin Console **in the top navigation.

3.  Select **Settings** in the left navigation.

## Turn on or off pooled licensing for AppSheet Enterprise Plus

Pooled licensing allows your AppSheet Enterprise Plus licenses to be granted to users when they sign in to AppSheet, eliminating the need to [assign licenses](https://support.google.com/appsheet/answer/14101111#assigned-licensing) in the Google Admin console. For complete details, see [Pooled licensing.](https://support.google.com/appsheet/answer/14101111#pooled-licensing)

You can define the **groups** of users that are allowed to use your pooled AppSheet Enterprise Plus licenses. By default, when pooled licensing is turned on, every user in your organization (that is, all the users that share your [verified domains](https://support.google.com/a/answer/60216)), will be granted an AppSheet Enterprise Plus license when they sign in. If you need to limit the number of users from your domain that have the ability to consume your AppSheet Enterprise Plus licenses, you can designate a group of users that are eligible to use your AppSheet Enterprise Plus licenses.

To turn on pooled licensing, your organization must have licenses available that are not yet assigned.

Turning off pooled licensing:

- Revokes the AppSheet Enterprise Plus license from any account to which it isn't explicitly [assigned](https://support.google.com/appsheet/answer/14101111#assigned-licenses) in the Google Admin console, impacting access to Enterprise Plus apps by those accounts
- Requires an annual commitment for AppSheet Enterprise Plus licenses to turn it back on

To turn on or off pooled licensing, do the following:

1.  [Access the Settings page](#explore-settings-page) in the AppSheet Admin Console.
2.  Turn on or off **Use pooled licensing for AppSheet Enterprise Plus**.
3.  In the **Pooled license granting** drop-down, select one of the following to grant a license to any signed-in app user or to restrict access to a specific user group, respectively:
    - **Grant to any app user** - Grants licenses to any user from your Google Workspace [verified domains](https://support.google.com/a/answer/60216) and their app users.
    - **Grant only to members of a group** - Grants licenses only to members of the selected authentication domain group.
4.  If you select **Grant only to members of a group**, select the following:
    1.  Existing authentication domain in the **Authentication domain** drop-down. See [Add an authentication domain to your AppSheet account](https://support.google.com/appsheet/answer/10105757#add).
    2.  Group associated with the selected authentication domain.
5.  Click **Save**.

## Restrict access to resources by external AppSheet accounts

For organizations that have verified ownership of their domains with Google Workspace, AppSheet admins can restrict access to resources by external AppSheet accounts. 

When you turn on the security setting, AppSheet accounts that are external to your organization won't be able to access resources, such as authentication domains, data sources, and connectors, even if they have the proper credentials. Existing apps owned by these external accounts that rely on credentials from your organization won't function when the app requires authentication to be refreshed.

When configuring the security setting, you can optionally define exceptions to allow external AppSheet accounts from specific domains or email addresses that aren't strictly owned by your Workspace organization to authenticate using internal credentials. These accounts will still need valid credentials to access assets owned by your organization and rely on the access privileges of the user. For example, you might allow exceptions for the following:

- Domain owned by your organization, but not officially verified in Workspace
- External contractor or consultant that needs recurring access
- Legacy AppSheet users that own business critical apps

When you turn off the security setting, external AppSheet accounts can add credentials from your organization to access resources, as long as the credentials give them sufficient access permissions.

To restrict access to resources by external AppSheet accounts, do the following:

1.  [Access the Settings page](#explore-settings-page) in the AppSheet Admin Console.
2.  Turn on **Restrict access by external accounts**.
3.  Optionally, to allow exceptions, enter one or more allowed domains or email addresses, separated with a space, comma, or new line.
    **Note**: Any external AppSheet account or domain added to the allowed exceptions list will be permitted to use the credentials provided by your organization to access any available data sources, authentication domains, and other connectors that are available to that user.
4.  Click **Save**.

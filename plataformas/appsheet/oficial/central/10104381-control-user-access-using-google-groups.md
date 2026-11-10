---
fonte: https://support.google.com/appsheet/answer/10104381?hl=en
baixado: 2026-11-10
---

# Control user access using Google groups

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

Use Google groups to control access to your apps.

- [Quick intro](#quick-intro)
- [Create a Google group](#create-group)
- [Connect AppSheet to the groups in your organization](#connect-appsheet)
- [Set up group authentication in an app](#require-domain-authentication)
- [Enable API access in your Google domain](#enable-api-access-domain) 
- [Share the app](#share-app)

## Quick intro

Watch this video to learn how to use Google groups to control access to AppSheet apps.

Video: https://www.youtube.com/watch?v=qc70KgFxgCo

## Create a Google group

You can create a Google group in one of the following ways:

- [Use Google Groups](#google-groups)
- [Use the Google Workspace Admin console (Admins only)](#admin-console)

### Use Google Groups

As an app creator, you can create a Google group using [Google Groups](https://groups.google.com/). For complete details, see [Create a group](https://support.google.com/a/users/answer/9303222).

If you are not an admin, you must use Google Groups to create a group.

### Use the Google Workspace Admin console (Admins only)

As an admin, you can create a group using the Google Workspace Admin console.

To create a group using the Google Workspace Admin console:

1.  Sign in to the Google Workspace admin console at [admin.google.com](https://admin.google.com/)
2.  Click **Groups**.
3.  Click **Create Group.**
4.  Fill in the details for the group. 

    Configure a domain group
5.  The **Access Type** settings do not affect the ability for AppSheet to connect to the group. They can be left at their default values or customized as needed.
6.  Add members to the group.

See also  [Create a group](https://support.google.com/a/answer/9400082).

## Connect AppSheet to the groups in your organization

When connecting to a Google group in your organization, AppSheet uses the **group ID** and not the group name. If the group ID changes for any reason (for example, if you delete and recreate the Google group), this connection will need to be reconfigured.

To connect AppSheet to the groups in your organization:

1.  Sign in to your AppSheet account and navigate to **My Account \> Integrations \> Auth Domains**.
2.  Click **+ New Auth Domain**.
3.  Specify a name for this account and click **Google Cloud**.

    Connect AppSheet to a domain group
4.  You will be prompted to sign in with Google. Sign in with the same account used to create the group.
5.  Navigate back to **My Account \> Integrations \> Auth Domains** to confirm the authentication domain was added to the account.

## Set up group authentication in an app

To set up group authentication in an app:

1.  Open an AppSheet app and navigate to **Security \> Domain Authentication**.
2.  Enable **Require domain authentication?** 
3.  Under **Authentication domain source** select the name of the account added in the previous step.
4.  Restrict access by Workspace group by entering a group name in the **Restrict by Domain** field.
    This field is optional. If set, only members of the groups whose domain matches this field will be permitted to access the app with the specified role. If left empty, all members of the group, regardless of the domain, will be able to access the app with the specified role.
5.  Add **Authentication groups** that will be used to manage user authentication for this app.
6.  Save your changes.

Set up domain authentication in an app on the Security \> Domain Authentication tab

## Enable API access in your Google domain

To enable API access in your Google domain, see [Control which third-party and internal apps access Google Workspace data](https://support.google.com/a/answer/7281227).

##  Share the app

Share the app with your end users, as described in [Share: The Essentials](https://support.google.com/appsheet/answer/10104983). When the end-user accesses the app, they will be prompted to sign in using their Google Workspace credentials.

**Note**: When sharing an app with a Google Group, the app will not appear in the My Apps list for the users in the Google Group. It can only be accessed through the URL provided in the email invitation or shared directly.

Sign in with with Google domain

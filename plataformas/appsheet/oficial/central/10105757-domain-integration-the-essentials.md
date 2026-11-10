---
fonte: https://support.google.com/appsheet/answer/10105757?hl=en
baixado: 2026-11-10
---

# Domain integration: The Essentials

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

 

If your app users are all part of a corporate domain, you can use domain security groups to control access to an AppSheet app as described in the following sections.

- [View authentication domains in your AppSheet account](#view)
- [Add an authentication domain to your AppSheet account](#add)
- [Set up domain authentication in an app](#domain-auth-app)
- [Prevent app creators from using external authentication domains](#prevent-auth-domains)

The advantage of this approach is that access control decisions can be made globally rather than in each app. For example, if there is a domain security group called **Admins**, you can set up your app to only be accessible to members of this group. As specific employees are added or removed from the group, their access to the app dynamically changes as well.

The owner of the auth domain needs to have permissions to read the list of groups from the domain and to read the membership of individual groups.

## View authentication domains in your AppSheet account

To view authentication domains in your AppSheet account:

1.  Sign in to [AppSheet](https://www.appsheet.com).
2.  Select your account from the account profile drop-down to go to the **My account** page.

    Access the My account page
3.  Go to **Integrations \> Auth Domains.**

The Auth Domains page shows your personal and team authentication domains. See also [Share integrations with your team](https://support.google.com/appsheet/answer/10104795#share-integrations).

Auth Domains pane showing personal and team authorization domains in your account

## Add an authentication domain to your AppSheet account

By adding an authentication source, you are giving AppSheet permissions to read the list of groups and the group membership for any domains that your account has access to.

To add an authentication domain to your AppSheet account:

1.  Sign in to [AppSheet](https://www.appsheet.com).
2.   Select your account from the account profile drop-down to go to the **My account** page.

    Access the My account page
3.  Go to **Integrations \> Auth Domains.**
4.  Click **+ New Auth Domain**. 
    The Add a new authentication domain dialog displays.
5.  Enter a name for the authentication source.
6.  Select one of the following authentication sources from the list:
    - [Active Directory](https://support.google.com/appsheet/answer/10104380)
    - [AWS Cognito](https://support.google.com/appsheet/answer/10104382)
    - [Google Cloud](https://support.google.com/appsheet/answer/10104381)
    - [Okta](https://support.google.com/appsheet/answer/10104487)
    - [OpenID Connect](https://support.google.com/appsheet/answer/10105083)
7.  Respond to the prompts to authenticate access.

##  Set up domain authentication in an app

You must be the app owner to set up domain authentication in an app.

To set up domain authentication in an app:

1.  Open the app in app editor.

2.  Go to **Security \> Domain Authentication**.

3.  Enable **Require domain authentication?** 

4.  Under **Authentication domain source** select the name of the account added in the previous step.

5.  Restrict access by domain by entering a domain name in the **Restrict by Domain** field.
    This field is optional. If set, only members of the groups whose domain matches this field will be permitted to access the app with the specified role. If left empty, all members of the group, regardless of the domain, will be able to access the app with the specified role.

6.  Add **Authentication groups** that will be used to manage user authentication for this app and perform one or more of the following tasks:
    - Change the **App role** to **User** or **Admin.** For information about leveraging the user role in your app, see [`USERROLE()`](https://support.google.com/appsheet/answer/10108128). The role defaults to **User**.
    - Change the A**pp version** available to the user to **Default**, **Latest**, or **Stable**. For information about app versions, see [Maintain a stable app version](https://support.google.com/appsheet/answer/10104791)[.](https://support.google.com/appsheet/answer/10104791)

7.  Save your changes.

Set up domain authentication in an app on the Security \> Domain Authentication tab

## Prevent app creators from using external authentication domains

Prevent app creators from using external authentication domains by using the "Restrict external data sources and auth domains" policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To prevent app creators from using external authentication domains:

1.  Select **My account \> Policies**.
2.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
3.  Select **Restrict external data sources and auth domains** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below: 
    NOT(\[HasExternalAuth\])
6.  Click **Save**.

&nbsp;

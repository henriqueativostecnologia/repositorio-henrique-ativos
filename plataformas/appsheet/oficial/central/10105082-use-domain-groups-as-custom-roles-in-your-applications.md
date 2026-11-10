---
fonte: https://support.google.com/appsheet/answer/10105082?hl=en
baixado: 2026-11-10
---

# Use domain groups as custom roles in your applications

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

The following features apply to [Google Cloud domain groups](https://support.google.com/appsheet/answer/10104381), [Active Directory domain groups](https://support.google.com/appsheet/answer/10104380), and [Okta groups](https://support.google.com/appsheet/answer/10104487).

If you have custom domain groups, you can leverage them inside of your AppSheet applications. For example, if you have a domain called `www.yourcompany.com` and you are using Google Workspace domain features - and specifically group management features - you can configure your AppSheet account and applications to use these groups.

You will then be able to retrieve group information using the built-in function [`USERROLE()`](https://support.google.com/appsheet/answer/10108128), which in turn can be used throughout your application. For example, including [`Show_If`](https://support.google.com/appsheet/answer/10106628), [`Editable_If`](https://support.google.com/appsheet/answer/10107954), automation workflows, and so on

This will allow you to create powerful security mechanisms without having to duplicate your group/role information in two different systems.

The following steps and screenshots walk through this process. In this example, we use Google Cloud and Google domain groups

**Note:** This access mechanism can only be set up for groups that are managed within your directory provider (for example, Google Workspace). It can't be set up for groups you (or your organization's admin) do not manage.

**Step 1:** Create one or more Google domain groups. In the screenshot below, we are using the Google Admin console ([admin.google.com](https://admin.google.com)) and have already created a few groups:

Google domain groups in the Goole Admin console

**Step 2**: Configure your AppSheet account to *generally* use Google Domain authentication, as described in [Control user access using Google Cloud](https://support.google.com/appsheet/answer/10104381). If you have successfully performed this step, in your AppSheet account you should now see your Google auth provider in your **Auth Domains** pane.

Auth Domains pane showing personal and team authorization domains in your account

In the above screenshot, not only have we connected to our Google domain, but we have then [shared this connection with our AppSheet team](https://support.google.com/appsheet/answer/10104795#share-integrations).

**Step 3**: Create an application and configure it to use your Google Cloud auth domain. There are a few actions to take here which we call out using the following screenshot and numberings. In the screenshot we are looking at an app named **User Roles**:

1.  Select **Security** \> **Domain Authentication.**
2.  Enable **Require domain authentication?** 
    This will override any manually added users you may have already configured for this app.
3.  Select your previously configured authentication domain in the **Authentication domain source** drop-down.
4.  A default display name is provided which you can optionally override.
5.  Important: type in the name of your domain. This is the suffix of the various email addresses for this domain. In our example below we are configuring a domain called appsheetdemo.com
6.  After a few moments, the box for step 6 should start to display a down arrow, and further, a grid will appear where the 7 is shown below. Appsheet will render any groups in the popdown. This grid allows you to map Google Group names to friendly internal AppSheet names. For example, in the screenshot below we For example, in the screenshot below we have:
    - Mapped **New Appsheet Domain Group** to the application-specific word **Customgroup**
    - Left the default mapping for **devgroup**

Configure domain authentication

**Step 4:** For testing purposes, in this same application, create a virtual column to explore the function [`USERROLE()`](https://support.google.com/appsheet/answer/10108128). In the following screenshot we have a table called **Asset** with a virtual column called `RoleName` with the `USERROLE()` function in its formula:

**Step 5**: Verify behavior using an end user. If everything above has been successfully configured, an end user who is a member of the Google domain called **New Google Domain Group** which we previously mapped to **Customgroup**, will see the word **Customgroup** for the virtual field when they sign in to the app:

Customgroup shows as RoleName when you sign in to the app

As shown above, custom roles can then be leveraged throughout your application for a wide variety of security, navigation, and workflow purposes. For example:

`USERROLE() = "Customgroup"`

Will resolve to `TRUE` if the current user role is `Customgroup`.

In the case where a user is a member of more than one domain group, the first match will be the value that is used throughout the AppSheet application. For this reason, AppSheet allows you to reorder the domain group mappings using the reordering icon:

Reorder authentication groups

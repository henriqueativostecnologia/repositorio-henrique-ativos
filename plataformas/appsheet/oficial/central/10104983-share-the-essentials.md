---
fonte: https://support.google.com/appsheet/answer/10104983?hl=en
baixado: 2026-11-10
---

# Share: The Essentials

AppSheet allows you to share your apps with users in different ways instead of providing an app store. When you are ready to share your app, you need to decide whether to share it with anyone (public) or a restricted audience.

When sharing an app, the app owner information, including email address, is made available to app users when reviewing the app Terms and Privacy Policy. If you have an AppSheet Enterprise Plus account, you can [set the public app owner](https://support.google.com/appsheet/answer/11918568#public-app-owner). 

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **User audience**                                                             | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Anyone (Public)                                                               | [Share your app with anyone](#share-anyone) by enabling public access to your |
|                                                                               | app.                                                                          |
|                                                                               |                                                                               |
|                                                                               | **Note**: Not recommended for apps that are used internally by your           |
|                                                                               | organization or that access sensitive data.                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restricted audience                                                           | [Share your apps with a restricted audience](#share-restricted-audience) to   |
|                                                                               | control who can use the app and optionally view or edit the app definition in |
|                                                                               | the app editor.                                                               |
|                                                                               |                                                                               |
|                                                                               | Specifically, you can share your app with:                                    |
|                                                                               |                                                                               |
|                                                                               | -   [Individual users](#share-individual-users)                               |
|                                                                               | -   [All users in a domain](#share-domain)                                    |
|                                                                               | -   [All signed-in users](#share-signed-in)                                   |
|                                                                               | -   [Users in an existing domain group](#domain-groups) (Enterprise plans     |
|                                                                               |     only)                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

After sharing an app, you might want to [notify users](#notify-users) by sending them a link.

See also: [Restrict sharing of apps](https://support.google.com/appsheet/answer/12282002)

## Quick intro

Watch the following video for an introduction to sharing and deploying your app.

Video: https://www.youtube.com/watch?v=KjrckKXeaLY

## ****Share your app with anyone (public access)

**Notes**:

- Public access is not recommended for apps intended to be accessed internally by your organization or for any apps that access sensitive data.
- Unless you are an Enterprise customer, you will need to purchase a separate [public Publisher Pro plan](https://support.google.com/appsheet/answer/10105400).

Share your app with anyone by making it public if and only if the following statements are **true**:

- Access to your app does not need to be secure for any reason and your app does not access sensitive data
- You are not concerned about the number of active users accessing your app

To share your app with anyone (public access):

1.  Open your app in the app editor.
2.  Select **Security \> Require sign-In**.
3.  Disable **Require user signin?**
4.  Respond to the following prompts to confirm you understand the security implications of making an app public.
    **Note**: If you do not respond to the prompts, your app will not be made public.
    - **Yes, the data in the app is public** - You acknowledge that security and access control is **not** required for all the data in this app.
    - **Yes, I am authorized to set up an insecure app** - You acknowledge on behalf of your organization that you knowingly take on the risks of running an insecure app.
5.  Click **Save**.

After sharing an app with anyone, you might want to [notify users](#notify-users) by sending them a link.

## Share your apps with a restricted audience

**Note**: To control access to apps by a restricted audience, you must [require user sign-in](https://support.google.com/appsheet/answer/10104975), which is enabled by default.

When you [notify users about your app](#notify-users), you have no control over how the notification is forwarded. Links to your app could be shared on a popular Twitter feed – which could be viewed as good or bad! Your app may reach a much broader audience than you had intended. In addition, you may want to be able to revoke access to an app if an employee leaves the company, for example.

Share your apps with a restricted audience to control who can use the app and optionally view/copy or edit the app in the app editor. After an app is shared with users, they can access it from the **Shared with me** section of the **Apps Gallery**, as described in [Access your apps](https://support.google.com/appsheet/answer/11510510).

Share your apps with a restricted audience as described in the following sections:

- [Share your app with individual users](#share-individual-users)
- [Share your app with all users in a domain](#share-domain)
- [Share your app with all signed-in users](#share-signed-in)
- [Share your app with existing domain groups](#domain-groups)

In addition, you can do the following:

- [Send reminder notifications to individual users](#send-reminder)
- [Search for individual users or domains with shared access](#search)
- [Modify or remove shared access to your app](#modify-remove-shared-access)
- [Manage access for individual users](#manage-roles-app-versions)
- [Copy all users with shared access](#copy-all-users)
- [Understand app collaboration and data security](#understand-app-collaboration-data-security)

### Share your app with individual users

To share your app with individual users:

1.  Open your app in the app editor.

2.  Ensure that you have configured your app to require user sign-in. See [Require sign-in: The Essentials](https://support.google.com/appsheet/answer/10104975).

3.  Click the Share icon in the title bar.

    Share icon

    The **Share app** dialog displays.

4.  Enter the email address of the user with whom you want to share your app, such as ahamilton@example.com, and press **Enter**. Repeat to share with additional users.

5.  Select one of the following access settings:
    - **Use app -** Users can use the app, but can't view or edit the app in the app editor.
    - **View/copy app** - Users can view and copy the app in the app editor, but can't edit the app. See also [Let another user copy your app](https://support.google.com/appsheet/answer/10104387).
    - **Edit app** - Users can edit the app in the app editor and add additional tables from any of the data sources already connected to the app.
      **Note**: Only one user should edit an app at a time. If two users attempt to edit an app at the same time, conflicts may occur when the app is saved.

    **Important**: Grant **Edit app** access only to users you trust. Users with this permission could access files in your Google Drive.

6.  To manage advanced access for an individual user, enable the **Advanced** toggle.

    Share app showing the Advanced toggle enabled

7.  Perform one or more of the following tasks:
    - Change the **in-app role** to **User** or **Admin.** For information about leveraging the user role in your app, see [`USERROLE()`](https://support.google.com/appsheet/answer/10108128). The role defaults to **User**.
    - Change the **app version** available to the user to **Default**, **Latest**, or **Stable**. For information about app versions, see [Maintain a stable app version](https://support.google.com/appsheet/answer/10104791)[.](https://support.google.com/appsheet/answer/10104791)

8.  Optionally, you can send an email notification to users to invite them to install and access your app. To send a notification, select **Notify users** and modify the notification message, as required. Or you can [notify users](#notify-users) later.

9.  Confirm that you are not a robot at the reCAPTCHA verification prompt.

10. Click **Send.**
    Or **Share** if you disabled **Notify users**.

11. Optionally, click and [change the authorization provider](https://support.google.com/appsheet/answer/10104975) used for user sign-in.

12. Click **Done**.

### Share your app with all users in a domain

Sharing your app with all users in a domain enables them to **use the app**. To permit users in a domain to view or edit the app definition, you must add them as [individual users](#share-individual-users) and set the access settings accordingly.

**Note**: As a security precaution, AppSheet prevents you from sharing your app to a widely used domain name, such as gmail.com.

To share an app with all users in a domain:

1.  Open your app in the app editor.

2.  Ensure that you have configured your app to require user sign-in. See [Require sign-in: The Essentials](https://support.google.com/appsheet/answer/10104975).

3.  Click the Share icon in the title bar.

    Share icon

    The **Share app** dialog displays.

4.  Enter the name of the domain to which you want to share your app, such as example.com, and press **Enter**.

5.  Repeat to share with additional domains.

6.  Confirm that you are not a robot at the reCAPTCHA verification prompt.

    Share app dialog showing how to share an app with a domain.

7.  Click **Share**.

8.  Optionally, click and [change the authorization provider](https://support.google.com/appsheet/answer/10104975) used for user sign-in.

9.  Click **Copy sharing links** to copy app links to [send directly to users](#send-link).

10. Click **Done**.

### Share your app with all signed-in users

**Note:** Enable this option when you do not need to restrict access to a specific list of users but still want to access user-specific information like email, or use personalization features like security filters or private tables.

To share your app with all signed-in users:

1.  Open your app in the app editor.
2.  Select **Security \> Require sign-In**.
3.  Enable **Require user signin**.
4.  Enable **Allow all signed-in users.**
5.  Respond to the following prompts to confirm you understand the security implications of making an app available to all signed-in users.
    **Note**: If you do not respond to the prompts, your app will not be made available to all signed-in users.
    - Yes, this is a public app - You acknowledge that security and access control is not required for all the data in this app or that you will maintain correctly configured security filters for all the data in this app.
    - Yes, I am authorized to set up a public app - You acknowledge on behalf of your organization that you knowingly take on the risks of data exposure for any data that you have not placed behind a correctly configured security filter.

    Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).
6.  Click **Save**.

To remove shared access by all signed-in users, disable the **Allow all signed-in users**.

After sharing an app with all signed-in users, you might want to [notify users](#notify-users) by sending them a link.

### Share your app with existing domain groups

If you have an Enterprise account, you can control access to your apps using domain groups, as described in [Domain Integration: The Essentials](https://support.google.com/appsheet/answer/10105757). 

After sharing an app with a domain group, you might want to [notify users](#notify-users) by sending them a link.

Apps shared with a domain group don't display in the **Shared with me** section of the My apps page.

### Send reminder notifications to individual users

To send reminder notifications to individual users if they have not accessed your app:

1.  Open your app in the app editor.

2.  Click the Share icon in the title bar.

    Share icon

    The **Share app** dialog displays.

3.  View the individual users to which the app has been shared in the **Users** section.
    **Note**: If a user has not accessed the app, you'll see the reminder icon and **Invited** by their name.

    Send reminder icon and Invited flag

4.  Click **Resend** to send a reminder invitation to the user.

### Search for individual users and domains with shared access

To search for individual users and domains with shared access:

1.  Open your app in the app editor.
2.  Click the Share icon in the title bar.

    Share icon

    The **Share app** dialog displays.
3.  Enable the **Advanced** toggle.
4.  Enter a string in the search dialog to filter the list.
    Search is case insensitive.

### Modify or remove shared access to your app

After sharing an app, to modify or remove shared access:

1.  Open your app in the app editor.

2.  Click the Share icon in the title bar.

    Share icon

    The **Share app** dialog displays.

3.  Perform one of the following tasks:
    - Modify app access for individual users.
    - Remove shared access by an individual user or domain by selecting **Remove** from the app access drop-down.

4.  Click **Done**.

### Manage access for individual users

After sharing your app, to manage access for individual users:

1.  Open your app in the app editor.

2.  Click the Share icon in the title bar.

    Share icon

    The **Share app** dialog displays.

3.  Change the access settings for an individual user, as desired.
    - **Use app -** Users can use the app, but can't view or edit the app in the app editor.
    - **View/copy app** - Users can view and copy the app in the app editor, but can't edit the app. See also [Let another user copy your app](https://support.google.com/appsheet/answer/10104387).
    - **Edit app** - Users can edit the app in the app editor and add additional tables from any of the data sources already connected to the app.
      **Note**: Only one user should edit an app at a time. If two users attempt to edit an app at the same time, conflicts may occur when the app is saved.

    **Important**: Grant **Edit app** access only to users you trust. Users with this permission could access files in your Google Drive.

4.  To manage the in-app role and app version for an individual user, enable the **Advanced** toggle and perform one or more of the following tasks:
    - Change the **in-app role** to **User** or **Admin.** For information about leveraging the user role in your app, see [`USERROLE()`](https://support.google.com/appsheet/answer/10108128). The role defaults to **User**.
    - Change the **app version** available to the user to **Default**, **Latest**, or **Stable**. For information about app versions, see [Maintain a stable app version](https://support.google.com/appsheet/answer/10104791)[.](https://support.google.com/appsheet/answer/10104791)

### Copy all users with shared access

To copy all users with shared access:

1.  Open your app in the app editor.
2.  Click the Share icon in the title bar.
    Share icon
3.  The **Share app** dialog displays.
4.  Click **Copy users**.

### Understand app collaboration and data security

Apps [shared with view or edit access](#share-individual-users) are displayed in the **Shared with me** section of **My Apps.** Only one user should edit an app at a time. If two users attempt to edit an app at the same time, conflicts may occur when the app is saved.

A co-author can only add a new table to the app from a [team-shared data source](https://www.appsheet.com/Dashboard/Team/SharedData). A co-author cannot add a new table to the app from either the app author's cloud file system or the co-author's cloud file system. The following table provides more details.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Source**                                                                    | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Team-shared data source                                                       | AppSheet allows a co-author to add a new table to the app only from a         |
|                                                                               | [team-shared data                                                             |
|                                                                               | source](https://www.appsheet.com/Dashboard/Team/SharedData).                  |
|                                                                               |                                                                               |
|                                                                               | For fully collaborative environments, AppSheet provides [team                 |
|                                                                               | collaboration](https://support.google.com/appsheet/answer/10104795)           |
|                                                                               | capabilities including the ability to define team-shared data sources. If the |
|                                                                               | app owner is part of a team with team collaboration capabilities, then every  |
|                                                                               | co-author can access and utilize data sources that are marked as team-shared. |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App author's cloud file system                                                | AppSheet does not allow a co-author to add a table from the original app      |
|                                                                               | creator's cloud file system for security reasons. The app creator might       |
|                                                                               | intend to allow the co-author access to help with one app, but might          |
|                                                                               | inadvertently expose the app creator's entire cloud file system.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Co-author's cloud file system                                                 | AppSheet does not allow a co-author to add a table from the co-author's cloud |
|                                                                               | file system. An app typically *runs as the app creator*. This means that the  |
|                                                                               | data sources and access tokens of the app creator are used during app         |
|                                                                               | execution. Allowing a co-author to add tables from their own cloud file       |
|                                                                               | system could lead to the situation where no single author could view and      |
|                                                                               | change all of the apps' data. That might also mean that no single author      |
|                                                                               | could investigate or fix problems with an app.                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Notify users about your app

After sharing your app, you may want to notify users by [sending them a link](#send-link). For example, you might:

- Include a link in an email campaign
- Publish the link to a web site
- Post the link to your Twitter account
- Send the link in an SMS message

You can also [enable users to share a link to your app](#enable-share-link).

### Send users a link to your app

To send users a link to your app:

1.  Open your app in the app editor.

2.  Click the Share icon in the title bar.

    Share icon

    The **Share app** dialog displays.

3.  Click **Share links**.

4.  Copy the links to install on a mobile device; open in a browser; or view, copy, or edit the app in the editor.

5.  Send the link to users using your preferred method.

Also, when [sharing your app with individual users](#share-individual-users), you have the option to notify them by email and [send them a reminder notification](#send-reminder) if there is no response.

### Enable users to share a link to your app

By default, users can share a link to your app with other users by selecting **Share** in the app menu. Details about how to install the app are populated in an email that you can customize and send to one or more users.

Share link in app menu to share link to app with other users

**Note**: If the current view is a [Detail view](https://support.google.com/appsheet/answer/10106385), the view details are shared instead of installation information.

If your app is configured to [require user sign-in](https://support.google.com/appsheet/answer/10104975) or you want to limit app sharing, you can disable this feature.

To disable the ability for users to share your app:

1.  Open the app in the app editor.

2.  Select **Settings  Settings icon \> Views \> General \> System Buttons**.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     

    ## If you are using the legacy editor

    Select **UX \> Options.**

3.  Turn on **Disable share button**.

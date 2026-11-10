---
fonte: https://support.google.com/appsheet/answer/10105078?hl=en
baixado: 2026-11-10
---

# Security: The Essentials

There are several sections of the **Security** tab where you can make customizations in these areas. You can require that your users sign in to use your app in the [Require Sign-In](https://support.google.com/appsheet/answer/10104975) section. You can use [security filters](https://support.google.com/appsheet/answer/10104488), and define [domain groups](https://support.google.com/appsheet/answer/10105082) in the **Domain Authentication** tab to [control user access](https://support.google.com/appsheet/topic/10104974).

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. 

AppSheet security is based on:

1.  [Authentication](https://support.google.com/appsheet/answer/10104975): Allows you to reliably identify users of your application.
2.  [Application access control](https://support.google.com/appsheet/answer/10104983): Allows you to control who can run your application.
3.  [Data access control](https://support.google.com/appsheet/answer/10104977): Allows you to control what data each user sees.
4.  [Auditing](https://support.google.com/appsheet/answer/10104794): Allows you to monitor application use.

Security section of the editor showing the Require Sign-in tab

## Understanding AppSheet Security

In this section, you can learn how AppSheet security works so that your 

Apps created with AppSheet are secure because of: 1) the architecture of AppSheet, 2) the underlying security infrastructure of cloud and mobile technology, and 3) the security options in your control. 

First, let’s quickly summarize the AppSheet architecture from a security point of view:

- **Cloud data**. If you use AppSheet databases, AppSheet will store your data in Google Cloud. Otherwise, data stored in AppSheet applications is primarily stored in a location of your choosing which can either be in a cloud storage service such as Google Sheets, or in a cloud database such as Cloud SQL. In some cases, AppSheet stores your application data temporarily for performance and to support features such as the audit log. You can control these features in the application configuration. The configuration of your applications (such as the look-and-feel, branding, sharing) and certain user information (such as teams, data source configuration, administrative policy) are stored securely by AppSheet in Google Cloud.
- **Authorization**. When creating an application, you sign into AppSheet with your cloud storage account and give AppSheet the permission to read and write your cloud storage data on your behalf. The industry standard OAuth protocol is used in this process. You can learn more, see [AppSheet permissions to your cloud provider](https://support.google.com/appsheet/answer/10104378).
- **Apps get built based on data in the cloud**.  The application you create is saved to an application definition that is maintained by AppSheet in a secure cloud database. Communication between the AppSheet cloud service and your cloud storage provider uses secure web protocols (HTTPS).
- **The apps run on a mobile device**. Communication between the mobile device and the AppSheet cloud service uses secure web protocols (HTTPS).
- **Local data storage**. The application definition and all the necessary data is copied to the mobile device and securely stored locally on the device using HTML5 local storage.
- **Data synchronization**.  When you add, update, or delete data via the AppSheet application running on your mobile device, all changes you make are saved to your cloud data provider. The AppSheet cloud service acts as a go-between to connect the mobile app with the cloud data provider used by your app.

### Tips and tricks

Learn tips and tricks for securing apps from the AppSheet Community. See [Security tips and tricks](https://www.googlecloudcommunity.com/gc/forums/filteredbylabelpage/board-id/appsheet-tips-tricks/label-name/Security).

## FAQ for AppSheet security

In the following sections we explain frequently asked questions (FAQ) for AppSheet security using a fictional app created by a teacher to distribute and collect assignments from her students in a graphic design class.

## Who can access my cloud data directly?

No other AppSheet user can access your cloud data directly-- that permission lives solely with you (and whoever else has your cloud account’s sign-in info). 

Depending on the update permissions you have enabled in the app, the users of your app may be able to add, edit, or delete values that live in your cloud-hosted spreadsheets and that are exposed using the apps you build with AppSheet. You can control these permissions as described later in this article.

The AppSheet cloud service has permissions to act on your behalf to read and write your cloud data. These permissions are only used for the specific purposes of app creation and app execution. AppSheet does not save copies of your data. Furthermore, because of the way the OAuth protocol works, you can at any time decide to disable the access permissions granted to AppSheet.  

## Who can access my app and how do I control that?

Controlling who has access to your application is a three step process.

1.  Enable the **Require user authentication** option.
2.  Choose an authentication provider.
3.  Specify which users can use your application.

First, set the **Require user authentication** option by going to the **Security \> Require Sign-In** pane and enabling the **Require user authentication** option. If you do this, you must enroll in one of the Pay-Per-User pricing plans when you deploy your application. **Require user authentication** is not supported by any of the Pay-Per-App pricing plans.

Next, select an authentication provider. AppSheet does not maintain its own user registry of usernames and passwords. Instead, users must sign in using a cloud provider such as Google, Dropbox, Office365, Box, or Smartsheet.

- By default, the authentication provider will be the cloud data provider where your data is stored. For example, if your cloud data provider is Google, your default authentication provider will be Google.
- Alternatively, you can choose one of the providers from the **Authentication Provider** drop-down containing Google, Dropbox, Office365, Box, and Smartsheet. For example, even though your cloud data provider is Google, you can choose Dropbox as your authentication provider. You might choose this option if all of your app users have Dropbox accounts.
- Finally, you can choose all of the providers including Google, Dropbox, Office365, Box, and Smartsheet. Do this by selecting the blank authentication provider appearing at the top of **Authentication Provider **drop-down.

Finally, specify which users can use your application.

- Normally, you will enter the email address of each user who is allowed to use your application in the "allow list". Do this by going to the **Security \> Require Sign-In** pane and clicking **Manage users**. Then enter the email address of each user in the **People to invite** list. You can enter multiple email addresses separated by commas. Then click **Send install link**.
- Alternatively, you can include all of the users in a domain by entering a domain name such as **@mycompany.com**.
- Finally, you can avoid entering an allow list by setting the **Allow all signed-in users** option. Only enable this option when you do not need to restrict access to a specific list of users, but you still want to access user-specific information like their email, or use personalization features like security filters or private tables.

## Do the users of my app also need to have access to my data in cloud storage?

No. As the app creator, you can distribute your app to people who do not have direct access to your cloud data. This works because the default execution mode ('as app creator') instructs AppSheet to access data using the identity of the app creator. Normally, you should not allow your users to directly access your cloud data. Instead, they should only be allowed to make changes through your application.

In rare circumstances, you may choose to have your app run as the app user. See [Access mode: as app creator or app user](https://support.google.com/appsheet/answer/10105756). In this case, you must grant your users direct access to your data in cloud storage. Only do this if you fully understand the security implications of doing so.

## What can users do with my app? Can they delete my data? 

As the app creator, you control what changes, if any, users can make to your data. For example, you can control whether the user can add, update, delete, or only read your data.

You can control what changes can be made to a table as follows:

1.  Go to the **Data \> Tables** pane.
2.  Click the icon to the left of the table name.
3.  Choose an access mode from the **Are updates allowed** drop-down. 

You can control what changes can be made to a slice as follows:

1.  Go to the **Data \> Slices** pane.
2.  Click the icon to the left of the slice name.
3.  Choose an access mode from the **Update mode** drop-down.

## Can I limit the data that specific users of the app can see? 

 Users of your app can only see data that you choose to expose through the app. In fact, you might want certain classes of users to only have access to view specific subsets of data, and other users to different data. You can do this using [slices](https://support.google.com/appsheet/answer/10106592)[.](https://intercom.help/appsheet/data/data-definition/defining-and-using-slices)

In the case of the Class Assignments app, we want to make sure that students can submit completed work and continue to view past submissions, but I don’t want them to be able to see the completed work of other students. The best way to do this is to create a slice that shows only the assignments of the signed-in user. I’ll do this from the **Editor \> Data \> Slices** tab, then clicking **+ New Slice**.

First, we'll need to name the slice and then specify a few parameters. In this case, we'll want to choose the **Submit** table so new submissions will end up there. We'll also want to make sure students can only add submissions, and not delete or edit-- so we’ll choose **Adds** as the update mode for the slice.

In order to make sure signed-in students can only see their own present and past submissions, we need to filter based on the **Student** column. Since we required sign-in for the app, the filter condition should be **Matches user name**-- the app will then only show data that matches the current signed-in user’s name.

You’ll see then, in the menu, that the current logged-in user’s name shows up. As shown below, the slice ensured Justin A. Sample would only be able to view his own past assignments.

## Who can access the data on the mobile device? 

On the mobile device, AppSheet uses industry-standard "local storage" technology associated with web browsers (web browser technology is embedded inside the AppSheet mobile app and the actual implementation largely utilizes HTML5 technology). Since you require users to sign in to access your app, each user's data is isolated from any other user's data. Even if multiple users were to use your app from the same device, their data would be isolated as long as they sign in to the device as different users. In short, if you follow standard security practices on the device (users sign in with passwords), your app will be as secure as all other apps based on web technologies.

## What happens if an app user leaves my organization and I want them to stop using my app?** **

At any time, you can return to the user allow list and remove any users you’ve previously added. Any subsequent actions by the removed user from their mobile app will fail when the actions engage with the AppSheet cloud service (typically when synchronizing or saving data).

As an extreme measure, you could also make a copy of the app and delete the old one. The old one will stop working and then you can control access to the new one. You’ll need to make sure to redistribute the new app link to the other users who still need access.

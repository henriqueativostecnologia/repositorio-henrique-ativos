---
fonte: https://support.google.com/appsheet/answer/12849362?hl=en
baixado: 2026-11-10
---

# Configure Chat apps with AppSheet

You must be a **Google Workspace user** to create Chat apps with AppSheet. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

Configure Chat apps with AppSheet by performing the following steps:

- [Enable Chat apps with AppSheet](#enable-chat-apps)
- [Choose the configuration mode](#configuration-mode)
- [Use automatic configuration](#automatic-configuration)
- [Use manual configuration](#manual-configuration)

##  Enable Chat apps with AppSheet

To enable Chat apps with AppSheet:

1.  Open the app in the app editor.
2.  Click Chat apps  in the left navigation.

    Click Chat in the left navigation
3.   Click **Create**.

    After a few minutes, the Enable section displays. 
    Review the [Google Workspace Marketplace Developer Agreement](https://workspace.google.com/terms/marketplace/devtos.html) and the [Google APIs Terms of Service](https://developers.google.com/terms)before proceeding.

Next, you'll choose the configuration mode to use to configure your Chat app.

## Choose the configuration mode

Choose one of the following configuration modes to configure your Chat app:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Configuration mode**                                                        | **Description **                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Automatic configuration](#automatic-configuration) (Recommended)             | Automatically create, connect, and configure a Google Cloud project for use   |
|                                                                               | by Chat apps with AppSheet, all with **one** click. Automatic configuration   |
|                                                                               | is set by default.                                                            |
|                                                                               |                                                                               |
|                                                                               | With automatic configuration, Chat apps are only available to users in the    |
|                                                                               | organization in which they were created.                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Manual configuration](#manual-configuration)                                 | Manually create and configure a Google Cloud project, enable and configure    |
|                                                                               | the Google Chat API, and optionally grant IAM access to run automations.      |
|                                                                               |                                                                               |
|                                                                               | With manual configuration, you can create Chat apps that are available to     |
|                                                                               | users inside your organization or that can be made available to external      |
|                                                                               | users, for example by publishing to the Marketplace, as described in [Publish |
|                                                                               | Google Chat apps](https://developers.google.com/workspace/chat/apps-publish). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

See also [About the Google Cloud projects used by Chat apps](https://support.google.com/appsheet/answer/13536336). 

You can configure **one** Chat app per Google Cloud project.

 

After you configure your Chat app, if you want to **change the configuration mode** do one of the following:

- Delete the Google Cloud project created in this step, [copy the app](https://support.google.com/appsheet/answer/12491039), and start over
- Contact [AppSheet Support](https://www.appsheet.com/Support/Contact) for assistance

## Use automatic configuration

To configure the Chat app using automatic configuration:

1.  [Enable Chat apps with AppSheet](#enable-chat-apps) (described above).
2.  In the **Enable** section, click **Next** to create a Google Chat app.
    **Note**: In this step, AppSheet creates an associated Google Cloud project that operates in the background. You can't modify the Google Cloud project or its configuration using the Google Cloud console. For more information, see [About the Google Cloud projects used by Chat apps](https://support.google.com/appsheet/answer/13536336). 
3.  After the Google Chat app is created, [customize your Chat app](https://support.google.com/appsheet/answer/13380741).

Then, you [test and share your Chat app](https://support.google.com/appsheet/answer/12857667).

## Use manual configuration

To use manual configuration, perform the following steps:

1.  [Manually create, connect, and configure a Google Cloud project](#manually-create-project)
2.  [Enable the Google Chat API](#enable-chat-api)
3.  [Customize your Chat app](#customize-chat-app)
4.  [Configure the Google Chat API](#configure-chat-api)
5.  [Grant IAM access to run automations](#set-iam-policy-for-async-messages) (optional)

Then, you [test and share your Chat app](https://support.google.com/appsheet/answer/12857667).

To create a Google Cloud project. Specifically, you will need the `resourcemanager.projects.create` permission. For more information, see [*Creating a project*](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) and [Manage access to projects, folders, and organizations.](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

### Manually create, connect and configure a Google Cloud project

To manually create, connect, and configure a Google Cloud project for use by Chat apps with AppSheet:

1.  [Enable Chat apps with AppSheet](#enable-chat-apps) (described above).
    The Enable section displays. 
2.  To switch to manual configuration, select **More** Three-dot menu vertical **\> Switch to Manual configuration** in the Chat apps header.

    Switch to manual configuration

    The Enable section is refreshed with the steps for manual configuration.
3.  To create a new Google Cloud project:
    For best results, we don't recommend using an existing Google cloud project.

    1.  In the Enable section, click [**Google Cloud Console \> Project**](https://console.cloud.google.com/projectcreate) in the app editor to open the New Project page.
    2.  Enter a name for your project.
        This name is internal and isn't displayed in your Chat app.
    3.  Set your billing account, organization, and location.
        For more information, see [*Creating a project*](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).
    4.  Do **not** select the **Create Googleplex internal App Engine project** option.
    5.  Click **Create**.
4.  In the Google Cloud Console, select **Cloud overview \> Dashboard** in the navigation menu to display the project dashboard.

    Google Cloud project Dashboard in drop-down
     
5.  Select the Google Cloud project in the project drop-down (if it's not already selected) and copy the **Project number** that is displayed in the **Project info** card.

    Project number in Project info section
     
6.  Return to the app editor and paste the project number in the **Google Project Number** field.

    Google project number
     
7.  Click **Next**.
    Your app in now linked to the Google Cloud project. The Enable the Google Chat API section expands.

 Next, you'll enable the Google Chat API.

### Enable the Google Chat API

To enable the Google Chat API:

1.  In the **Enable the Google Chat API** section, lick [**Google Cloud Console \> Chat API**](https://console.cloud.google.com/apis/api/chat.googleapis.com) to open the Google Chat API page in the Google Cloud Console.
2.  In the console, click **Enable** on the Google Chat API page for the connect Google Cloud project.
3.  Return to the app editor and click **Next**.
    The Customize section expands.

Next, you will [customize Chat app actions](#customize-chat-app-actions) in AppSheet (described above). 

### Customize your Chat app

Customize the following features in your Chat app:

- **Chat app menu** that displays when the Chat app installed or mentioned in a Google Chat space
- **Search command** that enables Chat app users to search your app using simple phrases
- **Chat app actions** that provide more ways to interact with your Chat app

For details, see [Customize your Chat app](https://support.google.com/appsheet/answer/13380741).

### Configure the Google Chat API

When you configure an app using the Google Chat API, you need to provide the following information:

- App name
- Avatar image for the app
- Description of the app
- HTTP endpoint URL

You can **copy** this information in the **Configure the Google Chat API** section on the Chat Setup page in the app editor.

To configure the Google Chat API:

1.  In the Configure the Google Chat API section, click [**Google Cloud Console \> Google Chat API \> Configuration**](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat) to open the Configuration tab for the Google Chat API in the Google Cloud Console.

2.  To complete the fields under **Application info**, copy and paste the information from the app editor, as follows:
    1.  Return to the app editor and copy the **App name** under **Application Info** in the Configure the Chat API section on the Chat Setup page.
    2.  Paste the App name into the **App name** field under Application Info
    3.  Repeat steps 3 and 4 to copy and paste the **Avatar URL** and **Description** fields.

    The following shows an example of the Application info settings:

    Chat API Application info configuration
     

3.  In the console, make sure **Enable interactive features** is turned on.

4.  Turn on (select) **Receive 1:1 messages** and **Join spaces and group conversations** under **Functionality**.

    Chat app functionality configuration

    **Note**: You can enable the other options, though they are not required.

5.  Return to the the app editor and copy the **HTTP endpoint URL** under **Connection Settings**.

6.  In the console, under **Connection settings** select **HTTP endpoint URL** and paste the copied URL into the **HTTP endpoint URL** field.

7.  In the **Authentication Audience** field, select **Project Number**.

8.  (Optional) To add slash commands for your Chat app in the Chat API:

    1.  In the console, click **Add a new slash command** under **Slash commands**.

        Add a new slash command in console
         

    2.  In the app editor, copy the **Name** in the **Configure slash commands** section.

    3.  Return to the console and paste the Name into the **Name** field.

    4.  Repeat steps b and c to copy and paste the **Description** and **Command Id** fields.

    5.  Enable the **Opens a dialog** option.
        For more information, see [Open interactive dialogs](https://developers.google.com/chat/how-tos/dialogs).

        The following shows an example of the Slash command settings:

        Chat app inventory log slash command

    6.  Click **Done**.

    7.  Repeat to add additional slash commands.

9.  [Preview links](https://developers.google.com/chat/how-tos/preview-links) are not required. You can skip the Link previews section. 

10. In the console, Under **Visibility **select **Make this Chat app available to specific people and groups in your domain** and add the email addresses for your test accounts in the email address field provided.

11. Click **Save.**

12. In the app editor, [share the app](https://support.google.com/appsheet/answer/10104983) with those same test accounts.

13. Return to the Chat apps Setup page and click **Next**.
    The Grant IAM access to run automations section expands.

### Grant IAM access to run automations (optional)

Previously these instructions used the built-in [***Editor***](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic) role, however this is no longer recommended because it includes many unnecessary permissions. If you already set up a chatbot with the **Editor** role, we recommend replacing it with a Custom Role.

To [build automations using Chat apps](https://support.google.com/appsheet/answer/12980866), you must set the IAM policy. Otherwise, you can skip this step.

To grant IAM access to run automations:

1.  Open the [*Roles*](https://console.cloud.google.com/iam-admin/roles) page for the Chat app project in Google Cloud Console.
2.  [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating) with the following permissions:
    - `serviceusage.services.use`
    - `appmetadata.records.create`
    - `clientauthconfig.clients.create`
    - `chat.bots.get`
    - `chat.bots.update`
3.  Once the role is created, go to the [**IAM**](https://console.cloud.google.com/iam-admin/iam) page and click **Grant access**.
    The Grant access panel displays.
4.  In the app editor, expand the **Grant IAM access to run automations** section on the Chat Setup page and copy the **New principals**.
5.  In the console, paste it in the **New principals** field in the **Add principals** section.
6.  In the console, select your Custom Role in the **Role** drop-down in the **Assign roles** section.
     
    To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and not granting any other roles than the minimum required to use this feature.
7.  Click **Save**.
8.  Return to the Chat apps Setup page in the app editor and click **Next**.
    The Test section expands.
9.  [Deploy your app](https://support.google.com/appsheet/answer/10104495) if it is not already deployed.

Next, you will [test your Chat app](https://support.google.com/appsheet/answer/12857667).

---
fonte: https://support.google.com/appsheet/answer/12923581?hl=en
baixado: 2026-11-10
---

# Quick start: Create your first Chat app with AppSheet

You must be a **Google Workspace user** to create Chat apps with AppSheet. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

In this Quick Start, you'll create your first Chat app with AppSheet using the **Simple Inventory** app template, as shown:

Simple inventory Chat app interface

------------------------------------------------------------------------

To create your first Chat app with AppSheet, perform the following steps:

1.  [Copy the sample app](#copy-sample-app).
2.  [Enable Chat apps with AppSheet](#enable).
3.  [Configure your Chat app](#configure) using automatic or manual configuration.
4.  [Test your Chat app](#test).

## Copy the sample app

To copy the sample app:

1.  Sign in to [AppSheet](https://appsheet.com/)**.**
    The My Apps page is displayed.
2.  Click **Templates** in the left navigation.

    Templates on the My Apps page

    The list of app templates is displayed.
3.  Locate the **Simple Inventory** app template and click **Copy**.

    Copy Simple Inventory app template
     
4.  Optionally, edit the name of the app and choose a category, or just use the default values.
5.  Click **Copy app**.
    The app template is copied and your new app is created and opened in the AppSheet app editor. The Learning Center is displayed by default.

## Enable Chat apps with AppSheet

1.  In the app editor, click Chat apps  in the left navigation.

    Click Chat in the left navigation
2.  Click **Create**.
    After a few minutes, the Enable section expands.
    **Note**: Review the [Google Workspace Marketplace Developer Agreement](https://workspace.google.com/terms/marketplace/devtos.html) and the [Google APIs Terms of Service](https://developers.google.com/terms)before proceeding

Next, you'll configure the Chat app.

## Configure the Chat app

Configure the Chat app using [automatic](#configure-automatic) or [manual](#configure-manual) configuration as described in the following sections. With one-click automatic configuration, Chat apps are only available to users in the organization in which they were created. With manual configuration, you can create Chat apps that are available to users inside your organization or that can be made available to external users. For more guidance on choosing the configuration mode, see [Choose the configuration mode](https://support.google.com/appsheet/answer/12849362#connect-project).

Automatic configuration is set by default.

### Create the Chat app using automatic configuration

To configure the Chat app using automatic configuration: 

1.  In the **Enable** section, click **Next** to create a Google Chat app.
2.  In the **Customize** section, leave the **First message** section set to the default configuration.
    All primary menu views will be included in the Chat app menu.
3.  Leave the **Smart "/search" command** turned on to allow users to search for Chat app  views using simple phrases.
4.  Add the following actions (slash commands) to your Chat app:
    1.  In the app editor, expand the **Customize** section (if it's not already expanded).

    2.  Click **+ Action**.

    3.  Click **Slash command: Open app view** in the drop-down.

    4.  Enter the following information:

        |             |                            |
|-------------|----------------------------|
| **Field**   | **Value**                  |
| App View    | Inventory Log              |
| Name        | /inventory-log             |
| Description | Display a log of inventory |

    5.  Click **+ Action**.

    6.  Click **Slash command: Open app view** in the drop-down.

    7.  Enter the following information:

        |             |                 |
|-------------|-----------------|
| **Field**   | **Value**       |
| App View    | Inventory_Form  |
| Name        | /inventory-form |
| Description | Add inventory   |
5.   Click **Next**.
    The Test section expands. You need to deploy your Chat app before you can test it.
6.  Deploy the app:
    1.  Click **Go to deployment settings** in the top banner.
    2.  In the Deployment Check section, click **Move app to deployed state**.
7.  [Share the app](https://support.google.com/appsheet/answer/10104983) with the test accounts.
8.  Go to [Test your Chat app](#test).

### Configure the Chat app using manual configuration

To configure the Chat app using manual configuration: 

1.  In the **Enable** section, select More \> Switch to manual configuration in the Chat apps header.

    . Switch to manual configuration

    The Enable section is refreshed with the steps for manual configuration.
2.   To create a new Google Cloud project:
    1.  Click [**Google Cloud Console \> Projects** ](https://console.cloud.google.com/projectcreate)in the app editor to open the New Project page.
    2.  Enter a name for your project.
        This name is internal and isn't displayed in your Chat app.
    3.  Set your billing account, organization, and location.
        For more information, see [Creating a project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).
    4.  Do **not** select the **Create Googleplex internal App Engine project** option.
    5.  Click **Create**.
3.  Select **Cloud overview \> Dashboard** in the navigation menu to display the project dashboard.

    Google Cloud project Dashboard in drop-down
4.  Select the Google Cloud project in the project drop-down (if it's not already selected) and copy the **Project number** that is displayed in the **Project info** card.

    Project number in Project info section
     
5.  Return to the app editor and paste the project number in the **Google Project Number** field.

    Google project number
6.  Click **Next**.
    Your app in now linked to the Google Cloud project. The Enable the Google Chat API section expands.
7.  Enable the Google Chat API:
    1.  In the **Enable the Google Chat API** section, click [**Google Cloud Console \> Google Chat API**](https://console.cloud.google.com/apis/api/chat.googleapis.com) to open the Google Chat API page in the Google Cloud Console.
    2.  In the console, click **Enable** on the Google Chat API page for the connected Google Cloud project.
    3.  Return to the app editor and click **Next**.
        The Customize section expands.
8.  In the **Customize** section, leave the **First message** section set to the default configuration. All primary menu views will be included in the Chat app menu.
9.  Add the following actions (slash commands) to your Chat app:
    1.  Click **+ New action**.

    2.  Click **Slash command: Open app view** in the drop-down.

    3.  Enter the following information:

        |             |                            |
|-------------|----------------------------|
| **Field**   | **Value**                  |
| App View    | Inventory Log              |
| Name        | /inventory-log             |
| Description | Display a log of inventory |

    4.  Click **+ New action**.

    5.  Click **Slash command: Open app view** in the drop-down.

    6.  Enter the following information:

        |             |                 |
|-------------|-----------------|
| **Field**   | **Value**       |
| App View    | Inventory_Form  |
| Name        | /inventory-form |
| Description | Add inventory   |

        You'll complete the configuration of the slash commands later.
10.  Click **Next**.
    The Configure the Google Chat API section expands.
11. To configure the Chat API:
    1.  In the Configure the Google Chat API section, click [**Google Cloud Console \> Google Chat API \> Configuration**](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat?project=926030533803) to open the Configuration tab for the Google Chat API in the Google Cloud Console.
    2.  To complete the fields under **Application info**, including the App name, Avatar URL, and Description, copy the information from the app editor and paste it in the equivalent field in the console, as shown:

        Copy and paste app info from AppSheet app editor to Google Cloud Console
         
    3.  In the console, make sure **Enable interactive features** is turned on.
    4.  Turn on (select) **Receive 1:1 messages** and **Join spaces and group conversations** under **Functionality**.

        Chat app functionality configuration
         
    5.  In the console, under **Connection settings** select **App URL.**
    6.  To complete the **App URL** field under **Connection settings**, copy the App URL field from the app editor and paste it in the equivalent field in the console, as shown:

        Copy App URL connection setting from AppSheet app editor to Google Cloud console
12. In the **Authentication Audience** field, select **Project Number**.
13. Add slash commands to your Chat app:
    1.  In the console, click **Add a new slash command** under **Slash commands**. Add a new slash command in console
    2.  To add the **/inventory-log** slash command, complete the fields under **New slash command**, including the Name, Command Id, and Description, by copying the information from the app editor in **Slash Command 1** section of the **Configure the Google Chat API** section and pasting it in the equivalent field in the console.

        Chat app inventory log slash command
    3.  Enable the **Opens a dialog** option.
    4.  Click **Done**.
    5.  Repeat to add the **/inventory-form** slash command. 

        Add inventory slash command
         
    6.  Enable the **Opens a dialog** option.
    7.  Click **Done**.
14. Configure who can access the Chat app:
    1.  In the console, under **Visibility **select **Make this Chat app available to specific people and groups in your domain** and add the email addresses for individual accounts.
        For initial test purposes, you may just add your own account.
    2.  Click **Save**.
15. In the app editor, click **Next**.
16. Click **Next** to skip the optional step, **Grant IAM access to run automations**. This step is not required for this tutorial.
    The Test section expands. You need to deploy your Chat app before you can test it.
17. Deploy the app:
    1.  Click **Go to deployment settings** in the top banner.
    2.  In the Deployment Check section, click **Move app to deployed state**.
18. [Share the app](https://support.google.com/appsheet/answer/10104983) with the test accounts.

## Test your Chat app

To test your Chat app:

1.  Open [Google Chat](https://chat.google.com).
2.  Click **+** next to Chat or Spaces.
3.  Click **Find apps** in the drop-down.

    Find apps in Chat
     
4.  Enter **Simple Inventory** in the search field.

    Enter simple inventory in the search field
5.  Click the **Simple Inventory** app in the list.
    The following dialog displays:

    Simple inventory chat app information dialog
     
6.  Do one of the following: The Chat app interface appears as follows:

    Simple inventory Chat app interface

    Notice that the Items and Levels views are targeted to open in the desktop UI because they use views types that are not yet supported for Chat apps with AppSheet. See [Summary of features supported for Chat apps with AppSheet](https://support.google.com/appsheet/answer/12917178).
    - Click **Add to space** to add the Chat app to a space, enter the space name, and click **Add**.
    - Click **Chat** to start a direct message (DM). Type hello (or any string not starting with /) to display the Chat app interface.
7.  Click **Inventory Log** to display the complete inventory log in the app dialog.
    Click through the inventory details, as desired, and click **X** to close the app dialog.
8.  Click **Items** and notice that it opens in a separate desktop browser window. 
    The Items view is a card view type, which is not supported in Google Chat. See [Summary of features supported for Chat apps with AppSheet](https://support.google.com/appsheet/answer/12917178).
9.  Enter **/** in Google Chat.
    The list of slash commands is displayed.

    Simple inventory slash commands
     
10. Click **/inventory-form** in the list, then click **Enter**.
    The Inventory form is open in the app dialog.
11. Enter a new inventory log and click **Save**.

**Congratulations!** You have successfully created your first Chat app with AppSheet!

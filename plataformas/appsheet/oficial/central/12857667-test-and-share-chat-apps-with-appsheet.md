---
fonte: https://support.google.com/appsheet/answer/12857667?hl=en
baixado: 2026-11-10
---

# Test and share Chat apps with AppSheet

Test and share your Chat apps with AppSheet, as described in the following sections:

- [Test your Chat app](#test-app)
- [Share your Chat app using automatic configuration](#publish-automatic)
- [Share your Chat app using manual configuration](#publish-manual)

## Test your Chat app

Before you share your Chat app, you can test it in Google Chat using your AppSheet account. 

To test your Chat app:

1.  Be sure that you've done the following:
    - [Configure your Chat app with AppSheet](https://support.google.com/appsheet/answer/12849362)
    - [Deploy your app](https://support.google.com/appsheet/answer/10104495).
    - For manual configuration only, add your email address to the **Visibility** field when [configuring the Chat API](https://support.google.com/appsheet/answer/12849362#configure-chat-api).
2.  Open [Google Chat](https://chat.google.com).
3.  Click **+** next to Chat or Spaces.

    Click + adjacent to Chat or Spaces
     
4.  Click **Find apps** in the drop-down.

    Find apps in Chat
     
5.  Enter the name of your Chat app in the search field. For example:

    Enter simple inventory in the search field
6.  Select the Chat app in the list.

     The following dialog displays:

    Simple inventory chat app information dialog
     
7.   Do one of the following:
    - Click **Add to space** to add the Chat app to a space, enter the space name, and click **Add**.
    - Click **Chat** to start a direct message (DM). Type hello (or any string not starting with /) to display the Chat app interface.

    The Chat app interface appears. For example:

    Simple inventory Chat app interface
     
8.  Interact with your Chat app to test its features. Enter **/** to display any slash commands that you added to your Chat app.

## Share your Chat app using automatic configuration

This is a** preview** release of automatic configuration of Chat apps with AppSheet. See [product launch stages](https://cloud.google.com/products#section-23). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps.

To share your Chat app using automatic configuration:

1.  In the app editor, expand the **Share** section on the Chat Setup page.
2.  Perform one of the following steps:
    - To share your Chat app with your **domain**, click **Share app with domain** and follow the steps described in [Share your app with all users in a domain](https://support.google.com/appsheet/answer/10104983#share-domain).
      **Note**: Members of the domain are not notified when the Chat app is shared.
    - To share your Chat app with **individual users**, click **Share app with individual users** and follow the steps described in [Share your app with individual users](https://support.google.com/appsheet/answer/10104983#share-individual-users). You can also add the app to an existing Chat space.

To get started using your Chat app, you can instruct your users to follow the steps in [Test your Chat app](#test-app) (above).

## Share your Chat app using manual configuration

Share your Chat apps using manual configuration as described in the following sections:

- [Share to individuals and groups in your domain using manual configuration](#publish-app-manual)
- [Share to your entire domain using manual configuration](#publish-app-entire-domain-manual)

### Share to individuals and groups in your domain

To share your Chat app for use by individuals and groups in your domain:

1.  In the Google Cloud Console, click the **Configuration** tab on the [Chat API](https://console.cloud.google.com/apis/api/chat.googleapis.com) page.
2.  Under **Visibility **select **Make this Chat app available to specific people and groups in your domain** and add the email addresses for individual accounts.
    For initial test purposes, you may just add your own account.
3.  Click **Save**.
4.  In the app editor, [share the app](https://support.google.com/appsheet/answer/10104983) with the same individuals or groups.

### Share to your entire domain

To share your Chat app for use by your entire domain: 

1.  Configure your OAuth Consent Screen, as described in [Configure OAuth Consent Screen](https://developers.google.com/workspace/marketplace/configure-oauth-consent-screen).
2.  Enable the Google Workspace Marketplace SDK:
    1.  Open [Google Cloud Console \> API Library \> Google Workspace Marketplace SDK](https://console.cloud.google.com/marketplace/product/google/appsmarket-component.googleapis.com?project=654976316170).
    2.  Click **Enable**.
3.  Configure the Google Workspace Marketplace SDK:
    1.  Open [Google Cloud Console \> API & Services \> Google Workspace Marketplace SDK \> App Configuration](https://console.cloud.google.com/apis/api/appsmarket-component.googleapis.com/googleapps_sdk?project=654976316170).
    2.  Follow the steps described in [Enable and configure the Google Workspace Marketplace SDK](https://developers.google.com/workspace/marketplace/enable-configure-sdk#fill_out_the_app_configuration_page).
        Under **App Visibility**, make sure to select **Private (Only available to users in your domain)**. This setting can't be changed after the project is saved.

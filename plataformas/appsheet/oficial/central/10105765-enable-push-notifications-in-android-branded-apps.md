---
fonte: https://support.google.com/appsheet/answer/10105765?hl=en
baixado: 2026-11-10
---

# Enable push notifications in Android branded apps

Before you begin: Ensure that you have completed the steps described in [Enable push notifications in your branded apps](https://support.google.com/appsheet/answer/10104711).

To enable push notifications in Android branded apps:

1.  Open your app in the AppSheet app editor.
2.  Go to **Manage \> Deploy \> Branded Apps** and expand the **For Android** section.
3.  Copy the application ID of your Android app.

    Branded app - For Android app ID
4.  Sign in to the [Firebase Console](https://console.firebase.google.com) and navigate to your project.
5.  Click  Settings icon  \> **Project settings**.

    Select Project settings
6.  Click the **General** tab and then click **Add app**. 

    Add app in Project Settings \> General page
7.  Click Android (as shown in the figure).

    Add Android app
    The Add Firebase to your Android app dialog is displayed.
8.  In the Android package name field, paste the application ID of your Android app, copied in step 3, and click **Register App**.

    Paste app name in the Add Firebase to your Android app dialog
9.  Click **Download google-services.json** to download the `google-services.json` configuration file, needed for sending push notifications to your branded app.

    Download the google-services.json configuration file by clicking Download google-services.json
10. Click **Next** to skip through the next few steps in the Firebase app wizard; AppSheet takes care of everything else.
11. Return to the Branded Apps page in the AppSheet app editor.
12. In the For Android section, do the following:
    1.  Upload the `google-services.json` file, downloaded in step 9, in the **Optional: Firebase Notification Configuration File** field. 
    2.  If you haven't already created a branded app for Android, click **Create a branded version of this app for Android devices**.

    Firebase information for Android white label app

Congratulations! You have just generated a native app capable of receiving push notifications from AppSheet.

After you download and install your app, you can try this feature out by navigating to **Manage** **\>** **Broadcast Notifications **and [broadcast a notification to your users](https://support.google.com/appsheet/answer/10104701).  Be sure to verify that it works before sending out your app to your users.

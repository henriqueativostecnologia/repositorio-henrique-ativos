---
fonte: https://support.google.com/appsheet/answer/10104496?hl=en
baixado: 2026-11-10
---

# Enable push notifications in iOS branded apps

Before you begin: Ensure that you have completed the steps described in [Enable push notifications in your branded apps](https://support.google.com/appsheet/answer/10104711).

Note that this process is more involved than the [Android version](https://support.google.com/appsheet/answer/10105765).

To enable push notifications in iOS branded apps:

&nbsp;

1.  Sign in to the [Firebase Console](https://console.firebase.google.com) and navigate to your project.
2.  Click  Settings icon  \> **Project settings**.

    Select Project settings
3.  Click the **General** tab and then click **Add app**. 

    Add app in Project Settings \> General page
4.  Select **iOS** as the platform.

    Click iOS when prompted
5.  Paste in the **iOS bundle ID** you used when creating your branded app without push notifications and click **Register app**.

    Paste the iOS bundle ID for your branded app and click Register app
6.  Click **Download Googleservice-Info.plist** to download the `GoogleService-Info.plist` file configuration file, needed for sending push notifications to your branded app.
7.  Skip through the next few steps of this form, then click **Continue to console**.
8.  Modify the properties of your app on the Apple Developer side. Navigate to the [*Apple developer site*](https://developer.apple.com) and go to your account. For more information about setting up your Apple developer account, see [Create and deploy branded apps for iOS](https://support.google.com/appsheet/answer/10105764).
9.  Select and edit the application ID you're using for your branded app in the **Identifiers** section.

    Select and edit the application ID used for the white label app in the Apple Developer tools
10. Under Capabilities, enable the push notifications capability by selecting **Push Notifications**, and create your push certificates.

    Select Push Notifications and create certificates for both development and distribution
11. Make sure you generate both the **development** and **production** certificates.

    Click Saved to disk and Continue at the prompt
12. To create a certificate, create a certificate signing request (CSR) by following the steps described in [Create a certificate signing request](https://developer.apple.com/help/account/create-certificates/create-a-certificate-signing-request/) on the Apple Developer site.
13. Make sure to click **Saved to Disk** rather than email to the CA in the certificate assistant wizard and click **Continue**.
14. Upload the `.CSR` file that you created and click **Continue**.
15. Download and install the newly created certificate by clicking on it once it's downloaded.
16. Click **Done**.
17. Export the certificate-key pair as a `.p12` file by right-clicking the certificate (make sure it contains the key in the drop-down). 
18. Upload the newly created development and production certificates to Firebase. This will be available in the **Settings \> Project Settings \> Could Messaging \> your iOS app** section.
19. Upload the corresponding files, and plug in the password you used when exporting the `.p12` files. 

    Upload the files and use the password used when exporting the .p12 files
20. Open your app in the AppSheet app editor.
21. Go to **Manage \> Deploy \> Branded Apps** and expand the **For iOS** section.
22. In the For iOS section, do the following:
    1.  Upload the certificate file, exported in step 16, in the **Certificate File** field.
    2.  Upload the provisioning profiles created when you set up your Apple developer account. For more information, see [Create provisioning profiles](https://support.google.com/appsheet/answer/10105764#create-provisioning-profiles).
    3.  Upload the `GoogleService-info.plist` file, downloaded in step 6, in the **Optional: Firebase Notification Configuration File** field. 
    4.  If you haven't already created a branded app for iOS, click **Create a branded version of this app for iOS devices**.

    Upload the GoogleService-Info.list file and the Firebase API key to AppSheet iOS branded app section

Congratulations! You have just generated a native app capable of receiving push notifications from AppSheet.

After you download and install your app, you can try this feature out by navigating to **Manage** **\>** **Broadcast Notifications **and [broadcast a notification to your users](https://support.google.com/appsheet/answer/10104701).  Be sure to verify that it works before sending out your app to your users.

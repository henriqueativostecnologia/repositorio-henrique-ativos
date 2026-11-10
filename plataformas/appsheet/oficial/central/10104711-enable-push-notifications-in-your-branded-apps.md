---
fonte: https://support.google.com/appsheet/answer/10104711?hl=en
baixado: 2026-11-10
---

# Enable push notifications in your branded apps

Use Firebase to send push notifications from a branded Android or iOS app. By default, branded apps do not support push notifications.

At a high level, in the following procedure you'll enable permissions to a service account in Google Cloud Platform that we provide, and you’ll need to provide AppSheet with your service account email from your Firebase project.

Enabling push notifications requires the creation of a **Firebase project** which provides the infrastructure required to send and receive push notifications. If you don't have a Firebase account or project, create them as described in [Create a Firebase account and project](https://support.google.com/appsheet/answer/10104995).

If you are configuring both Android and IOS branded apps for the same AppSheet app, you need to use the same Firebase project. The Firebase Admin SDK email you set in the following procedure will be the same email used to send both Android and IOS branded app notifications.

To enable push notifications in your branded apps:

1.  Sign in to [AppSheet](https://appsheet.com).

2.  Open your app.

3.  Go to **Manage \> Deploy \> Branded Apps** section of the editor for you app.

4.  Click **Notifications**.

5.  Click **Allow Firebase Notifications**.
    The Notifications dialog is displayed.

6.  Copy the email provided at the top of the dialog starting with **app-**.

    Copy email starting with app-

7.  Sign in to the [Firebase Console](https://console.firebase.google.com) and navigate to your project.
     
    If you already branded your app with notifications, you must use the same Firebase project that you used originally to brand the app. 

    **To confirm the Firebase project used for Android branded apps**, compare the following values:

    - Application ID for the app
      In the AppSheet app editor, go to **Manage \> Deploy \> Branded Apps \> For Android.**

      Branded app - For Android app ID
    - Package name for your app in the Firebase project
      In the Firebase console, navigate to the project, click  Settings icon  \> **Project settings \> Your apps**, select your app, and view the Package name in the SDK setup and configuration for your app.

      Package name for Android

    **To confirm the Firebase project used for iOS**, compare the following values:

    - Bundle ID, configured when [creating an application ID](https://support.google.com/appsheet/answer/10105764#create-app-id) for your branded app in the Apple Developer console. 
    - Bundle ID for your app in the Firebase project.
      In the Firebase console, navigate to the project, click  Settings icon  \> **Project settings \> Your apps**, select your app, and view Bundle ID in the the SDK setup and configuration for your app.

      AppSheet branded apps bundle ID for iOS app

8.  Click  Settings icon  \> **Project settings**.

    Select Project settings

9.  Click **Service accounts**, then click **Manage service account permissions**.

    Select Service accounts, then Manage service account permissions

    The Google Cloud Console opens and the Service accounts page is displayed.

10. In the left navigation, click **IAM** and then click **Grant access**.

    Under IAM, click Grant access

    The Grant access dialog is displayed.

11. In the Grant access dialog, do the following:
    Service account permissions can take up to 10 minutes to take effect.

    1.  In the New principals field, paste the email copied in step 6.
    2.  In the Role field, type **Service Account Token Creator** in the Filter field and then select it in the drop-down.
        To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and not granting any other roles than the minimum required to use this feature.
    3.  Click **Save**.

        Grant access dialog

12. In the Firebase Admin SDK section, copy the Firebase service account email.

    Copy Firebase service account email

13. Return to the AppSheet editor.

14. In the Notifications section, paste the Firebase service account email you copied in step 12 into the **Firebase Admin SDK** field. 

    Paste the email in the Firebase Admin SDK Email field

15. Save the app.

16. Complete the configuration by performing one or both of the following steps for Android and iOS branded apps:

    - [Enable push notifications in Android branded apps](https://support.google.com/appsheet/answer/10105765)
    - [Enable push notifications in iOS branded apps](https://support.google.com/appsheet/answer/10104496)

17. To test the configuration, [send a broadcast notification](https://support.google.com/appsheet/answer/10104701).

    A notification is sent to mobile devices that have the branded app installed.

If the broadcast notification fails, an error message is returned describing the issue. To troubleshoot a failed broadcast notification:

- Make sure you are checking on the devices that explicitly have the iOS (`ipa` file) or Android (`apk` file) branded app installed. For example, if you have a device with only the non-branded version of the app installed (that is, the app was accessed using the App Gallery from the AppSheet app installed from Google Play or iOS App Store), the broadcast notification won't be delivered to that device.
- Review the steps described above and make sure that there are no errors.
- Ensure that the email copied from AppSheet is visible in the Service accounts page as a principal with Service Account Token Creator permission.
- Wait 10 minutes after granting the service account permissions to ensure that they take effect.

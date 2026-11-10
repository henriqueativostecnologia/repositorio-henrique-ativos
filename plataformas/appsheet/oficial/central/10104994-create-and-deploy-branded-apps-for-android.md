---
fonte: https://support.google.com/appsheet/answer/10104994?hl=en
baixado: 2026-11-10
---

# Create and deploy branded apps for Android

Make and deploy an app with customized branding to the app store for Android. See also [What is a branded app?](https://support.google.com/appsheet/answer/10105390)

To learn more about the different aspects of deploying your app, see [Deploy](https://support.google.com/appsheet/topic/10104993).

- [How do I create a branded app?](#create)
- [How do I distribute my app?](#distribute)
- [Make updates to your app in Google Play Store](#update)

## How do I create a branded app?

To create a branded AppSheet app for Android:

1.  Open the app in the AppSheet app editor.
2.  Open the **Manage** ** \> Deploy** tab and expand the **Branded Apps** section.
3.  Turn on **Brand this app?**
4.  Expand the **For Android** section.
5.  Optionally, configure the settings if you want to [enable push notifications](https://support.google.com/appsheet/answer/10104711).
6.  Click **Create a branded version of this app for Android devices**

This starts the branded app creation process, which can take up to 24 hours.

You'll receive an email with links to download your App Bundle and APK files once the process is complete. Note that these links are only valid for 30 days, please download and keep your files somewhere accessible and do not use these links to share the app with your users.

The App Bundle can be uploaded to the Google Play Store and the APK file can be used to directly install your app on Android devices.

## How do I distribute my app?

The most popular way to distribute a broadly available Android app is through the Google Play Store. Keep in mind that if you deploy to the Play Store, anybody will be able to download and install your app.

To distribute your AppSheet app:

1.  Register for a developer account with Google. To do so, visit the following page and follow the instructions: [https://play.google.com/console/u/0/signup](https://play.google.com/console/u/0/signup).

    After you set up a developer account, you'll be able to publish your branded app.
2.  Go to the [Google Play Developer Console](https://play.google.com/apps/publish) and click on the **Create app** button located in the top right.
3.  Follow the steps to upload the App Bundle file to the store. You will be prompted for additional information before you can publish the app, including screenshots, a short description, icons, banners, and so on.
4.  When prompted, enable **App signing by Google Play**.
5.  At the **Does your app use advertising ID?** prompt, select **No**.

After a few hours, your users will be able to download your app from the Google Play Store.

## Make updates to your app in Google Play Store

Most changes you make in the AppSheet app editor don't require you to upload a new version of your app to the Google Play Store. Your users will get your changes the next time they sync the app. Changes to the app's name or icon are exceptions and will require you to upload a newly generated version of your app.

Since some of AppSheet's internal improvements and new features can't be fetched through a sync, it is recommended that you upload the latest version of your app to the store about **once a year** to ensure your app is kept current.

To make updates to your app in Google Play Store:

1.  Go to **Manage** ** \> Deploy \> Branded Apps \> Android** and click **Disable or update the branded version of this app for Android devices**. Don't worry, this won't affect existing users.
2.  Click **Create a branded version of this app for Android devices** to start the branding process.
    You'll receive an email with links to download your App Bundle and APK files within 24 hours.
3.  Go to your app's page in the [Play console](https://play.google.com/apps/publish) and then select **Production \> Create new release**.
4.  The rest of the process is similar to when you first uploaded your app. If your app was originally uploaded as an APK (for apps that were originally uploaded to the store before Aug 1 2021), upload the update as an APK as well and don't opt in to Play App Signing. If your app was originally uploaded as an App Bundle, continue to use App Bundles to upload updates.

In some cases, you may only want to deploy your app to a specific group of users, for example to employees in an organization.

1.  You can send the APK file through email, share it through a cloud file system, or even upload it to your website and share its URL. Your users will have to download the APK file, and open it on their Android phone.
2.  Before installation, it's important your users enable installation of apps from unknown sources. Typically, this setting is located either under the Security or Applications category in the settings app of your Android phone. Enabling this setting is required for installing apps that did not come from the Google Play store.
3.  For more info on how to install an app using an APK file, refer to the following article: [How to install third-party apps without the Google Play Store](http://www.androidauthority.com/how-to-install-non-market-third-party-apps-on-your-phone-31494/)

---
fonte: https://support.google.com/appsheet/answer/10105389?hl=en
baixado: 2026-11-10
---

# Branded apps: Establish your own branding

Establish your own branding through creating branded versions of your app.

To learn more about the different aspects of deploying your app, see [Deploy: The Essentials](https://support.google.com/appsheet/answer/10104495).

The [Branded Apps](https://support.google.com/appsheet/answer/10105390) section in the **Manage \> Deploy** tab of the editor enables you to create branded versions of your AppSheet app for [Android](https://support.google.com/appsheet/answer/10104994) and [iOS](https://support.google.com/appsheet/answer/10105764), so your app can be distributed as a direct download from the Android or iOS app stores without the need to download the AppSheet app. Whether or not you make use of this deployment path, you may also choose to create branded apps in order to remove AppSheet branding and better establish your own brand within the app.

When you build your app with AppSheet, there are a few different places where the AppSheet brand is normally visible to the users of the app. Many of these are suppressed in a branded app, but for technical reasons, some are not:

1.  In the menu of the app, there are options to Go to the App Gallery or to Create a New App. These do not appear in a branded app.
2.  The splash screen shown when the app is launched features the AppSheet logo. This does not appear in a branded app when distributed as a standalone native app. For iOS deployment you can provide your own icon instead, however the phrase "Powered by AppSheet" does still appear in small print at the bottom of the screen.
3.  In email sent from the Share dialog or automations there is a "powered by AppSheet" email suffix. This does not appear in a branded app.
4.  In the email sent from the Share dialog or automations, the email originates from `noreply@appsheet.com`. This also occurs in a branded app. For security reasons, AppSheet cannot send email directly from your email address. To avoid this behavior in the Share dialog, the button can be disabled in **UX \> Options**. For automation, if you need email to originate from your own address, consider using a [webhook](https://support.google.com/appsheet/answer/11511009) to connect to your own email service.
5.  On the third-party authentication screens (such as with Google Drive), the user will see that AppSheet is asking for permission to access their user information. Similarly, the first time the app needs to take actions that require permission such as accessing the current location or the camera, users will see that [appsheet.com](http://appsheet.com/) is requesting this access. This also occurs in a branded app. Since the branded app still connects to the cloud provider through the AppSheet service, these cannot be easily removed.
6.  From some views in the app, the Share button shares the data being viewed, but from other views it shares a link to install your app via the AppSheet app. This also occurs in a branded app. Since publication of the app occurs outside the AppSheet system, we do not obtain links to the published apps. To avoid this behavior of the share button, the button can be disabled in **UX \> Options**.

The use of the branded apps requires one of the advanced subscription plans. See the [AppSheet pricing page](http://www.appsheet.com/pricing).

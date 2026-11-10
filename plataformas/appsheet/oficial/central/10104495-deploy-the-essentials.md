---
fonte: https://support.google.com/appsheet/answer/10104495?hl=en
baixado: 2026-11-10
---

# Deploy: The Essentials

Certain features of your app won't work until you deploy it. For example, automation emails will be sent to the app owner and Chat apps features won't work.

Deploying your app is an exciting step in the process of app creation. However, before you deploy your app, you need to make sure everything is ready to go.

Go to **Manage** ** \> Deploy** in the app editor to do the following tasks:

- Run a [deployment check](https://support.google.com/appsheet/answer/10104389) to see what, if anything, needs to change in your app before deploying it.
- Deploy your app. 
  There are a couple of different ways to deploy your app: [instant deployment](#instant-deployment) and [traditional deployment](#traditional-deployment). You can also [deploy your app using an install link](https://support.google.com/appsheet/answer/10105388), accessible from the Share apps dialog. 
- Convert your app into a [branded app](https://support.google.com/appsheet/answer/10105389). You can learn more about [branded apps](https://support.google.com/appsheet/answer/10105390) and more about [how to update them](https://support.google.com/appsheet/answer/10104710). You can create and deploy branded apps for both [iOS](https://support.google.com/appsheet/answer/10105764) and [Android](https://support.google.com/appsheet/answer/10104994).
- [Pause your app](#pause) temporarily to prevent access by users without deploying or deleting it.
- [Undeploy your app](#undeploy).
- [Delete your app](#delete).

Before deploying apps, you should make sure you have [tested](https://support.google.com/appsheet/answer/11998579) them.

## Quick intro

Watch the following video for an introduction to sharing and deploying your app.

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=KjrckKXeaLY

## Put the finals touches on your app

If you're at the phase of your app-building process where you'd like to add a description, an image, or other information, go to the [Info tab](https://support.google.com/appsheet/answer/10100699) of the editor to make these customizations.

## Instant deployment

If you're building an app for your team or employees, it's easiest to use instant deployment. Deploying an AppSheet app using instant deployment is as simple as clicking a link in an email and following a few simple instructions.

Instant deployment is possible because the AppSheet apps you build are hosted by the AppSheet Hosting app installed on your mobile device. When you deploy and run your app, it will appear to run on its own, but it is actually hosted by the AppSheet Hosting app. While not a perfect analogy, you can think of your AppSheet app being hosted in the AppSheet Hosting app much like a web page is hosted in a web browser.

You distribute your app [by sending your users an install link by email](https://support.google.com/appsheet/answer/10105388). When your user clicks this install link on their mobile device:

1.  The user is asked to install the AppSheet Hosting app on their device. They will be taken to the iTunes Store for iOS or the Google Play Store for Android. If the AppSheet Hosting app is already present on the device, this step is skipped.
2.  The app icon for your AppSheet app is added to their home screen.
3.  Clicking on this app icon launches the AppSheet app.

Beyond the obvious simplicity of this approach, there are a few other benefits:

- Your apps are instantly available. There is no delay between app creation and app deployment.
- Changes to your apps are instantly available, too.
- All apps automatically benefit from any new features we provide, issues we fix, and performance improvements we make.

## Traditional deployment

The traditional deployment model is to create and submit each app separately to an app store (iTunes Store for iOS and Google Play Store for Android). Your users then find and download the app from the app store.

You should consider this model if:

- The app store discovery and distribution model is important to you.
- You're aiming for large-scale consumer adoption of your app.

Once you have created and tested your app using instant deployment, you can generate a *branded* version of the app. This creates the app package you must submit to the appropriate app store. Be aware that you must go through the approval process mandated by the Google Play Store or iTunes App Store, and your app must conform to the policies of that store.

In order to get your apps onto your device, you must first download the AppSheet app from your device's app store. Any subsequent apps you create essentially run through the AppSheet app.

If you are an app creator, it's a good idea to install the AppSheet mobile app on your mobile device even if you won't be a user of the app. You may want to test your app on your own device before launching to your users. You can find the AppSheet app by searching for AppSheet in the iTunes store (for iOS devices) or Google Play store (for Android devices).

When you launch the AppSheet app, it asks you to sign in, after which it starts an [App Gallery](https://support.google.com/appsheet/answer/11510510) (which is an app created by AppSheet). The App Gallery lets you browse and run your apps, apps that have been shared with you, or public samples on your mobile device.

This becomes a convenient mechanism for app creators to test their apps on their own mobile device in the process of building and modifying the app definition, without having to actually install the apps themselves to the home screen.

You can distribute your app by sending your users (or yourself) an install link by email. You'll be able to enter in the email addresses (or full domain) of those with whom you'd like to share the app. For more information, see [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

The following provides an example of the email:

example email

When your users click on the link from a mobile device, they're asked to install AppSheet on their device (AppSheet is also available in the app stores).

## Pause your app

You can pause your app temporarily to prevent users from accessing your app without undeploying or deleting it.

To pause your app:

1.  Open the app in the app editor.
2.   Go to **Manage** ** \> Deploy**.
3.  Click **Pause app**.

To resume a paused app:

1.  Open the app in the app editor.
2.   Go to **Manage** ** \> Deploy**.
3.  Click **Resume paused app**.

## Undeploy your app

Undeploy your app by returning it to the prototype state. Apps can be accessed and will be updated in the prototype state. However, certain features of your app won't work until you redeploy your app. For example, automation emails will be sent to the app owner and Chat apps features won't work.

 To undeploy your app:

1.  Open the app in the app editor.
2.   Go to **Manage** ** \> Deploy**.
3.  Under Deployment Check, click **Return to prototype state**.

## Delete your app

If you want to permanently remove an app, you can simply delete it. The next time any existing users sync the app, it will no longer run.

If you just want to remove specific users from an app that requires user sign in, remove them from the Share dialog. The next time they sync, they won't be able to sign in. See [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

To delete your app:

1.  [Go to the My Apps page](https://support.google.com/appsheet/answer/12392972).
2.  Select **More** More  **\> Delete** for the app you want to delete.

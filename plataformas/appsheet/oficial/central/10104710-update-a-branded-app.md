---
fonte: https://support.google.com/appsheet/answer/10104710?hl=en
baixado: 2026-11-10
---

# Update a branded app

Update an app that you've deployed via an app store.

To learn more about the different aspects of deploying your app, see [Deploy](https://support.google.com/appsheet/topic/10104993).

## When to update branded apps

After your branded app has been created and deployed to an app store, it does **not** need to be updated and redeployed in the app store every time you make a change to the AppSheet app definition.

The latest app definition is automatically fetched and used along with the every sync operation performed by the user. Therefore, you should rarely need to actually reconstruct and resubmit a branded app to one of the app stores.

The reasons you might want to update a branded app include:

- You give the app itself a new name or icon.
- You add new screenshots, keywords, descriptions, or other metadata.
- AppSheet explicitly asks you to update and resubmit your app. This should be an infrequent occurrence, and may be because there is a platform change that requires an explicit update. Such platform changes could occur when AppSheet rolls out significant new features, or iOS, Android, or some other core infrastructure deprecates or changes some important underlying functionality.
- Every 1 to 1.5 years to make sure your app gets new features and bug fixes.

## How to update branded apps

Generating an update involves repeating the initial branding process. First, open the AppSheet app editor and go to **Manage** ** \> Deploy \> Branded Apps**. For Android, simply click **Create a branded version ...**. This will generate the updated APK files that can be uploaded to the Google Play Store.

For iOS, you'll need the exported certificate and provisioning profiles you used when you first created your branded app. If you no longer have these files the certificate can be re-exported from your keychain, and the provisioning profiles can be re-downloaded from the Apple Developer Center. If the certificate is no longer in your keychain you can generate a new certificate and new provisioning profiles using the same steps from the original branding process, as described in [Create and deploy branded apps for iOS](https://support.google.com/appsheet/answer/10105764).

For iOS you'll also need to specify a Short Version number for your update, and this number must match the version number you use in iTunes Connect. Once you've provided this information you can click **Create a branded version ...** to generate the `.ipa` files for upload to the Apple App Store.

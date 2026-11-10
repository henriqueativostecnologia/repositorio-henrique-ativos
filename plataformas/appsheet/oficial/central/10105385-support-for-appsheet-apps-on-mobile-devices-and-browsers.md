---
fonte: https://support.google.com/appsheet/answer/10105385?hl=en
baixado: 2026-11-10
---

# Support for AppSheet apps on mobile devices and browsers

AppSheet apps run on iOS and Android devices in a variety of device form factors, and on mobile or desktop browsers. The following sections provide more details:

- [Support for AppSheet apps on mobile devices](#support-plan-mobile)
- [Support for white label apps](#support-plan-white-label)
- [Support for mobile and desktop browsers](#browser)

## Support for AppSheet apps on mobile devices

This support plan will go into effect on **December 1, 2022**. For more information, see [Updated support plan for AppSheet apps on mobile devices](https://www.googlecloudcommunity.com/gc/Announcements/Updated-support-plan-for-AppSheet-apps-on-mobile-devices/m-p/484764#M5504). 

To ensure an optimal experience for users of your AppSheet apps:

- AppSheet is supported on **Android and iOS versions for 5 years after the last minor OS update**
  To ensure an optimal experience, we do not support mobile devices outside of this OS support window. Users with OS versions that are no longer supported stop receiving updates to their PlayStore and AppStore AppSheet apps until they upgrade their OS. 
- AppSheet supports its **native app versions on the PlayStore and AppStore for 2 years**
- Combined together, AppSheet apps won’t run on devices with iOS and Android versions that are greater than **7 years old**. After that timeline, app users need to upgrade their OS version to run AppSheet.

In addition, app users who do not update their AppSheet app from the PlayStore or the AppStore automatically are prompted to do so once support has ended, meaning two years after we release them. 

As an example, the following diagram shows the support timeline for users on iOS 15 and Android 12, assuming a device cannot have its OS upgraded beyond these versions: 

Support plan example

### FAQ: Support for AppSheet apps on mobile devices

Review the following FAQ to understand support for AppSheet apps on mobile devices.

## Which Android versions are currently supported?

AppSheet is supported on Android version 9 and higher. Android 7 and 8 will still run AppSheet, but there are no Play Store updates.

## Which iOS versions are currently supported?

AppSheet supports iOS version 12.0 or higher. Earlier versions of iOS can cause subtle bugs or performance problems. 

## What happens when an OS is no longer supported?

- Users are sent a notification to upgrade to a newer OS version and download the latest version of AppSheet app.
- If users can't upgrade to a newer OS version, then they have until the final version of the AppSheet app is two years old. After that, the app is no longer supported.

## Are users completely blocked from using the app after the support timeline?

- Users can still use AppSheet apps on a mobile browser. However, they will not have access to mobile-only functionalities, such as barcode scanning. 
- Users using an unsupported OS may not receive new features and bug fixes. Note that not all features and bug fixes need a new version of the AppSheet native apps.

## Support for branded (white label) AppSheet apps

App creators need to **[update](https://support.google.com/appsheet/answer/10104710) and distribute their branded apps every 18 months** so that app users can benefit from the latest features and bug fixes that AppSheet releases. 

Similar to users of an old version of the AppSheet native apps, users of an old version of a branded app need to upgrade their app. When they open the application, these users see a warning message to contact the app owner to get a newer version. By updating and distributing a new version of your app every 18 months, you ensure your users an optimal experience. Users are eventually blocked from using the app if it is too old. 

Branded apps work on an OS at least up to 5 years after the latest OS release and if the branded app users received is less than 18 months old. 

As an example, let’s look at Android 12 which got its last update in March 2022. AppSheet supports branded apps on Android 12 until March 2027 at a minimum. If the branded app is updated in March 2025, then that app works until September 2026. At that point, users need to get from app creators a newer version of the branded app. In this case, they can use the app until March 2028 because the app creator updated the branded app before the OS is not supported.

### FAQ: Support plan for branded AppSheet apps 

Review the following FAQ for the support for branded apps.

## What happens if I don’t remember when I last updated and distributed my branded app?

- When you open the app in the app editor it shows you a warning if the app is older than 18 months. If no warning is shown, no action is needed.
- In addition, you can open your branded app on a mobile device to see the same warnings your users see (if any).

## Is my branded app going to stop working on older devices exactly 5 years after the latest OS release?

If you follow our recommendation to update your branded app every 18 months, there is a grace period of approximately 6 months. App users can use the branded app 5 years and 6 months after the final OS update is released.

## Why isn’t the policy for branded apps the same as for non-branded apps (ie native apps)?

AppSheet controls how often it releases new versions of its native apps. For branded apps, the app creator is responsible for releasing new versions of the branded app. This creates additional dependencies that the AppSheet team needs to take into account for its support plan.

## Support for mobile and desktop browsers

The following sections describe the mobile and desktop browsers supported when you [*create apps using the AppSheet editor*](#create-apps) or when you [*use an app*](#use-app).

### Create apps in the AppSheet editor

To create apps in the AppSheet editor, we recommend using the **latest version** of the following browsers:

- [*Google Chrome*](https://www.google.com/chrome/) (minimum version supported: 95)
- [*Mozilla Firefox*](https://www.mozilla.org/) (minimum version supported: 131)
- [*Apple Safari*](https://www.apple.com/safari/) (minimum version supported: 18.4)
- [*Microsoft Edge*](http://micorosoft.com)(minimum version supported: 95)

**Note**: AppSheet is not supported for use on Internet Explorer.

To support all features, AppSheet requires that the following features be turned on in the browser settings: 

- JavaScript
- WebAssembly

To check your settings, do the following:

|             |                                                                                                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Browser** | **Setting**                                                                                                                                                                |
| Chrome      | No action required. WebAssembly is fully supported on the latest versions of Chrome.                                                                                       |
| Firefox     | Ensure the `javascript.options.wasm` setting is set to `true`. See [*Configuration Editor for Firefox*](https://support.mozilla.org/en-US/kb/about-config-editor-firefox). |
| Safari      | No action required. WebAssembly is fully supported on the latest versions of Safari.                                                                                       |
| Edge        | Ensure that enhanced security mode is on.                                                                                                                                  |

### Use an app

When using an app, we recommend using a modern browser. AppSheet works best on Chrome.

**Note**: AppSheet is not supported for use on Internet Explorer.

Most functionality is supported in a browser, except:

- Bar code scanning
- Near Field Communication (NFC) scanning
- Offline image and document caching
- Offline app launch 
- Push notifications

To open your app in a browser, ​ click in the app preview or use a [*shared link*](https://support.google.com/appsheet/answer/10104983).

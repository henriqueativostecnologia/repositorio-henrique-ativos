---
fonte: https://support.google.com/appsheet/answer/10108551?hl=en
baixado: 2026-11-10
---

# Where is my data cached?

By default, AppSheet does not cache spreadsheet data on the server. However, for read-only apps, server-side data caching significantly improves the speed perceived by app users during a Sync. In other words, the mobile app can get the data directly from AppSheet's servers without having to wait for the data to be fetched from the backend cloud storage platform (for example, Google Drive or Dropbox). 

By default, AppSheet does cache spreadsheet data on the mobile client in order to allow continued app usage despite transient loss of network connectivity (for example, getting into an elevator). However, full and seamless offline behavior needs to be explicitly enabled in the app definition.

## Configure settings for offline use

 To configure settings for offline use: 

1.   Open the app in the app editor.
2.  Select **Settings \> Offline mode**.
3.  Configure the settings under **Offline Use**.
4.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy navigation

 To configure offline mode:

1.  Open the app in the app editor.
2.  Select **Behavior \> Offline/Sync**.
3.  Configure the settings under **Offline Use**.
4.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Cache images and documents

By default, AppSheet does not cache images and documents that are referenced by the spreadsheet data for offline access.  To explicitly require AppSheet to cache images and documents, when [configuring settings for offline use](#configure-offline-use) under **Offline Use **enable **Store content for offline use**.

After this option is enabled, image and document downloads will happen asynchronously during initial app load. Subsequently, the entire app and its image and document content will be available offline.

## Enable app to start when offline

By default, your device needs to be online to start an AppSheet app from the home screen icon. Of course, it can then function despite transient loss of connectivity.

To enable the app to start when offline, when [configuring settings for offline use](#configure-offline-use) under **Offline Use** enable **The app can start when offline**.

**Your data is never stored on AppSheet servers**
The AppSheet web service is an intermediary between the mobile app and the backend spreadsheet. Importantly, it does NOT have a persistent copy of the spreadsheet so there is no danger of your data being compromised via the AppSheet web service. There are two caveats to this statement:

- You can optionally ask AppSheet to cache spreadsheet data in our service in order to improve performance. If so, this data is cached in-memory in our server for up to five minutes at a time.

- AppSheet caches resized copies of images used by the apps. Image resizing is important to conserve network bandwidth to mobile devices.

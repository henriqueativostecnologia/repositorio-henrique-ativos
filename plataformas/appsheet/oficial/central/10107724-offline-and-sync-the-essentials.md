---
fonte: https://support.google.com/appsheet/answer/10107724?hl=en
baixado: 2026-11-10
---

# Offline and Sync: The Essentials

AppSheet apps can be used on a mobile device even when that device is offline and disconnected from the network. This is possible because the information needed to run the app (the app definition, the data, and optionally images and documents) is stored locally on the mobile device. If you are running the app in a web browser, see [Run in an offline browser](#run-offline-browser).

If you have [security filters](https://support.google.com/appsheet/answer/10104488) in your app, they allow you to partially sync the app with data in the spreadsheet. 

One important precondition for all offline access is that the app must initially be launched on the device when it is online. This allows the needed information to be downloaded and stored locally.

The following sections describe how to configure and use offline and sync:

- [Configure offline and sync](#configure-offline-mode)
- [Configuration properties](#configuration-properties)
- [Delayed sync](#delayed-sync)
- [Considerations for offline use](#considerations)
- [Launch offline](#launch-offline)
- [Prolonged offline use](#prolonged-offline-use)
- [Offline with sign in](#offline-sign-in)
- [Run in an offline browser](#run-offline-browser)

## Configure offline and sync

 To configure offline and sync: 

1.   Open the app in the app editor.
2.  Select **Settings \> Offline mode**.
3.  Expand each section and configure the [offline mode properties](#offline-mode), as required.
4.  Select **Settings \> Performance**.
5.  Expand each section and configure the [performance properties](#performance), as required.
6.  Save the app.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy navigation

 To configure offline mode:

1.  Open the app in the app editor.
2.  Select **Behavior \> Offline/Sync**.
3.  Expand each section and [configure the properties](#configuration-properties), as required.
4.  Save the app.
     

## Configuration properties

Configuration properties that you can use to configure offline and sync are summarized in the following sections:

### Offline mode properties

Configure the properties for offline use. For more information, see [Where is my data cached?](https://support.google.com/appsheet/answer/10108551)

|                                |                                                                                                                                                                                                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Property**                   | **Description**                                                                                                                                                                                                                                       |
| The app can start when offline | Enable the app to start even when there is no internet connection. Changes will not be synced until the next time the user is online. See [Enable app to start when offline](https://support.google.com/appsheet/answer/10108551#start-when-offline). |
| Store content for offline use  | Make all images and files available for offline access. See [Cache images and documents](https://support.google.com/appsheet/answer/10108551#cache).                                                                                                  |

### Sync performance properties

Configure the performance properties.

- [Sync from your app to the cloud](#sync-app-to-cloud)
- [Sync from the cloud to your data source](#sync-cloud-to-datasource)

#### Sync from your app to the cloud

Configure the properties for sync from your app to the cloud.

|                   |                                                                                                                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Property**      | **Description**                                                                                                                                                                                                          |
| Sync on start     | Force sync when app starts and block access to app until sync completes. Prevent users from interacting with cached data during initial sync. To sync without blocking, use Automatic updates.                           |
| Delayed sync      | Queue data changes. When Automatic Sync is on, queue is processed automatically; otherwise user must sync app manually. Recommended if using Automatic updates. See [Delayed sync](#delayed-sync).                       |
| Automatic updates | Automatically sync in background when app starts, when data changes are queued, and when local data is more than 30 minutes old. See [Configure automatic updates](https://support.google.com/appsheet/answer/10107437). |

The following table summarizes the interactions between the **Delayed sync** and **Automatic updates** property settings. 

+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| **Properties**                | **Immediate sync**            | **Automatic sync (every 30    | **Wait for sync to complete** | **Manual sync required?**     |
|                               |                               | minutes)**                    |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Enable toggle  Delayed sync   | Yes                           | Yes                           | No                            | No                            |
|                               |                               |                               |                               |                               |
| Enable toggle  Automatic      |                               |                               |                               |                               |
| updates                       |                               |                               |                               |                               |
|                               |                               |                               |                               |                               |
| **Tip**: Best for most use    |                               |                               |                               |                               |
| cases.                        |                               |                               |                               |                               |
|                               |                               |                               |                               |                               |
| **Note**: When moving from    |                               |                               |                               |                               |
| offline to online, changes    |                               |                               |                               |                               |
| might not sync until the next |                               |                               |                               |                               |
| automatic sync occurs (within |                               |                               |                               |                               |
| 30 minutes or less).          |                               |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Enable toggle  Delayed sync   | No                            | No                            | Yes (mobile)\                 | Yes                           |
|                               |                               |                               | No                            |                               |
| Disable toggle  Automatic     |                               |                               | ([desk                        |                               |
| updates                       |                               |                               | top](https://support.google.c |                               |
|                               |                               |                               | om/appsheet/answer/12407883)) |                               |
| **Tip**: Best for apps that   |                               |                               |                               |                               |
| are expected to work offline  |                               |                               |                               |                               |
| or where you want to control  |                               |                               |                               |                               |
| when sync occurs.             |                               |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
|   Disable toggle  Delayed     | Yes                           | Yes                           | Yes (mobile)\                 | No                            |
| sync                          |                               |                               | No                            |                               |
|                               |                               |                               | ([desk                        |                               |
|   Enable toggle  Automatic    |                               |                               | top](https://support.google.c |                               |
| updates                       |                               |                               | om/appsheet/answer/12407883)) |                               |
|                               |                               |                               |                               |                               |
| **Tip**: Best for apps with   |                               |                               |                               |                               |
| data that is updated by       |                               |                               |                               |                               |
| automation or by the data     |                               |                               |                               |                               |
| source directly.              |                               |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
|    Disable toggle  Delayed    | Yes                           | No                            | Yes (mobile)\                 | No                            |
| sync                          |                               |                               | No                            |                               |
|                               |                               |                               | ([desk                        |                               |
|    Disable toggle  Automatic  |                               |                               | top](https://support.google.c |                               |
| updates                       |                               |                               | om/appsheet/answer/12407883)) |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+

#### Sync from the cloud to your data source

Configure the properties for sync from the cloud to your data source.

**Note**: The following properties require** **an AppSheet Core plan or above. See [AppSheet subscription plans](https://about.appsheet.com/pricing/).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Property**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Server caching                                                                | Store data on the AppSheet server instead of fetching from your cloud         |
|                                                                               | provider every time. This improves syncing for large tables, but will only be |
|                                                                               | used for rarely updated, read-only data.                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Delta sync                                                                    | Only update tables that have changed since the last sync. This improves       |
|                                                                               | syncing, but can't be used in certain cases (for example, spreadsheets with   |
|                                                                               | external formulas or when virtual columns need to be updated at each sync).   |
|                                                                               | See also [Improve the speed of                                                |
|                                                                               | sync](https://support.google.com/appsheet/answer/10104985).                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Quick sync                                                                    | Turn on to instantly see other users' changes as they are saved. Users only   |
|                                                                               | see changes made by other users that are using the same [version of the       |
|                                                                               | app](https://support.google.com/appsheet/answer/10104708).                    |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | For best results, we recommend turning on **Sync on start** and **Automatic   |
|                                                                               | updates** when using Quick sync.                                              |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | **Note**: With **Automatic updates** on, when moving from offline to online,  |
|                                                                               | quick sync changes won't occur until the next automatic sync occurs (within   |
|                                                                               | 30 minutes or less). After the automatic sync, quick sync updates will        |
|                                                                               | resume.                                                                       |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | You **shouldn't use** this feature if your app uses [advanced security        |
|                                                                               | fi                                                                            |
|                                                                               | lters](https://support.google.com/appsheet/answer/13865312#security-filters), |
|                                                                               | if your data sources compute values automatically (for example, if your       |
|                                                                               | Google Sheets data source uses formulas), or if your app has virtual columns  |
|                                                                               | that require a complete sync to be computed properly.                         |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | For complete details, see [Use Quick sync to instantly see other users'       |
|                                                                               | changes](https://support.google.com/appsheet/answer/13865312).                |
|                                                                               |                                                                               |
|                                                                               | Individual data updates will be cached on AppSheet servers. **If you have     |
|                                                                               | strict data residency requirements**, you may not want to use this feature.   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Delayed sync

[Sync](https://support.google.com/appsheet/answer/10108301) is the step that sends data [updates](https://support.google.com/appsheet/answer/10108001) from the device to the backend and retrieves the latest app definition and data from the backend to the device. If you choose **Delayed Sync** for your app, the app will not sync data immediately when an edit, delete, or add occurs. Rather, your changes will be queued up until you explicitly choose to sync. You should select this option for apps that are expected to work in offline environments or where you want to control when sync occurs. For example, you can use Delayed Sync to control when you use network data bandwidth.

### Intermittent connectivity

Apps that don't enable Delayed Sync will attempt to synchronize changes every time that data changes on the device. However, even in a connected environment, there may be intermittent connectivity problems that prevent synchronization from succeeding. In this case, AppSheet automatically queues changes and defaults to delayed sync behavior to prevent the loss of data. Even repeated sync retries will not cause duplication or corruption of data, except for the special case where you use RowNumber as your key. For more information, see [What is a key?](https://support.google.com/appsheet/answer/10106672)

### Viewing content offline

All spreadsheet/table data is automatically copied to the device so that it is available offline. However, images and documents are not copied to the device by default, because they may be large. You can enable Offline Content Caching to tell AppSheet to copy images and documents to the device. As with all other offline data caching, the images and documents are copied to the device when the app is initially run on the mobile device while online. The images and documents are refreshed as needed when Sync occurs. You can learn more about caching in this article: [Where is my data cached?](https://support.google.com/appsheet/answer/10108551)

Depending on the number and size of your images and documents, it may take several minutes for all of your content to be downloaded and saved on the device. Even if the images or documents are displayed by the client, this does not mean that the content has been downloaded and saved. When you first download the content, you should connect your device to the network, launch the application, and wait for a few minutes before disconnecting. Then go offline and check whether all of the images and documents have been downloaded and saved on the device. If not, reconnect and allow even more time for the images and documents to be downloaded and saved.

Note that offline content viewing of images and documents only works when the links to the images or documents use relative paths as described in [Work with PDF files](https://support.google.com/appsheet/answer/10106523).

## Considerations for offline usage

Review the following considerations for offline usage for the following data types:

- [Maps](#maps)
- [Videos](#video)
- [Audio files](#audio)

### Maps

It's possible to capture the user's current location with a `LatLong` input because this can use the device's GPS. However, you won't be able to display the position in the map view while the app is offline. AppSheet is unable to cache Google map data for offline use because it would violate Google's terms of service. Google's own Maps app does offer downloading of map regions for offline use, but they don't make this feature available for third-party apps that use maps. 

### Videos

[`Video` column data types](https://support.google.com/appsheet/answer/10106435#content) are unavailable offline, are read-only, and do not (currently) support data capture. However, you can use the data type to play video content. The `Video` type supports MP4 video URLs or YouTube embed URLs of this format: `https://www.youtube.com/embed/{id}`

### Audio files

[`File` column data types](https://support.google.com/appsheet/answer/10106435#content) are not stored locally at the moment, unlike images and other data.

## Launch offline

If you have used the lightweight deployment mechanism, you are familiar with launching apps from their home screen icons. By default, a mobile device needs to be online in order to launch an app from its home screen icon. Once launched, the app can then function offline or with intermittent connectivity.

However, if you wish to launch the app when the device is offline, you must [configure](#configure-offline-mode) **The app can start when offline **option. You must do this **before installing the app on your device**. **If your app has already been installed to the home screen, the shortcut must be deleted and installed again after enabling the offline option.** Otherwise you will need to launch it from the AppSheet app itself.

## Prolonged offline use

You should not run for prolonged periods (multiple days or weeks) while completely offline and without connectivity. There are two reasons for this:

1.  The app creator may make modifications to the app definition, and the user's app falls out of date.
2.  There may be changes to the underlying data. If the offline app makes its own data changes, an eventual sync will apply the older updates at a much later time and override changes made by other users.

## Offline with sign in

If your app [requires sign-in](https://support.google.com/appsheet/answer/10104975), your users will occasionally be asked to sign in again when their authentication expires.  This will only occur during a sync when the device has connectivity.

## Run in an offline browser

Some customers choose to run the app in a web browser (fullscreen or in an iframe). This is particularly useful when running on mobile platforms where the mobile app isn't supported.

The browser must be online when the AppSheet application is first loaded. Once the app is loaded, it can be used when the device is offline or has intermittent network connectivity. However, offline image and document caching will not work. You can keep working in this manner offline as long as the page isn't closed or unloaded. Saved changes will persist across page reloads or browser restarts for all data types except images or documents in a form.  For images or documents, sync must be performed before that browser tab is closed-- otherwise, the captured image or document content will be lost.

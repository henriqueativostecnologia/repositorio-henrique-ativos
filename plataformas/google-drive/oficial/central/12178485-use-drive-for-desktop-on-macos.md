---
fonte: https://support.google.com/drive/answer/12178485?hl=en
baixado: 2026-11-10
---

# Use Drive for desktop on macOS

With [Drive for desktop](https://support.google.com/drive/answer/10838124) on macOS, you can:

- Access Drive from Finder
- Sync between local and Cloud files

**Important:**

- When you sync files using Drive for desktop, you can choose to sync by streaming or mirroring. [Learn what it means to mirror or stream your files.](https://support.google.com/drive/answer/13401938)
- If you sync files on macOS with Drive for desktop, you may need to give macOS permission. [Learn how to give macOS permission](#macOS-permission-mirror).
- If you stream files on macOS 12.1 and up, Drive for desktop uses File Provider to give your files built-in support. [Learn more about File Provider](#File-Provider).
- Check if your macOS version is supported by Drive for desktop to ensure full functionality.[Learn which macOS versions Drive for desktop supports](https://support.google.com/drive/answer/2375082).

### Give macOS permission to sync files

If you sync certain files, you might need to give macOS permission to access folders and devices. Those folders and devices include:

- Desktop, Documents, and Downloads folders
- Removable and network volumes
- Your Photos library

Drive for desktop requires permission to:

- Access folders or devices you sync with Google Drive or backup to Google Photos
- Use Real-time presence or a Bluetooth key to sign in

If you don't initially grant approval, and later decide to sync a folder or device, go to "System Preferences" and change your privacy settings.

1.  On your computer, at the top-left corner, click the Apple Apple menu and then **System Settings** and then **Privacy and Security**.
2.  Open **Files and Folders** or **Photos**.
3.  Toggle the permission.

**Tip:** For changes to take effect, you might need to restart Drive for desktop or your computer.

### Use File Provider to stream Drive files

If you use macOS 12.1 and up with Drive for desktop to stream files, Drive for desktop uses macOS's File Provider technology to provide built-in support for cloud file systems like Drive.

#### Confirm if you're using File Provider

To confirm you're using File Provider:

1.  Open Drive for desktop.
2.  Click Settings Settings and then **Preferences**.
3.  At the top right, click Settings Settings .
4.  Under “Google Drive streaming location,” check if you see a notification that says “Folder location is controlled by macOS.” If so, you are on file provider. Otherwise, you are not.

#### Learn how File Provider differs from the legacy streaming method

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
|                                                    | **File Provider**                                  | **Legacy streaming method**                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Find your files                                    | You can find your files in the Finder sidebar,     | You can find your files in the Finder sidebar,     |
|                                                    | under “Locations.”                                 | under “Favorites.”                                 |
|                                                    |                                                    |                                                    |
|                                                    | **For advanced users:** You can find them in       | **For advanced users:** You can find them in       |
|                                                    | "\~/Library/CloudStorage" or                       | “/Volumes/GoogleDrive” by default. You can change  |
|                                                    | "/Users/\$USER/Library/CloudStorage" by default.   | this location.                                     |
|                                                    | You can’t change this location.                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Drag and drop behavior                             | Dragging items in and out of a Google Drive folder | Dragging items in and out of a Google Drive folder |
|                                                    | will **move** them. The cloud file will be trashed | will **copy** them and keep the cloud version      |
|                                                    | if moved out.                                      | intact.                                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Spotlight search                                   | Spotlight search will only search a subset of your | Spotlight only searches through your files if you  |
|                                                    | files including any downloaded files. To search    | explicitly turn on that functionality in           |
|                                                    | all files, use the Drive for desktop search tool   | preferences. Otherwise it won't search at all.     |
|                                                    | or the Drive website.                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Downloading files when syncing is paused           | When syncing is paused, you **can’t** download     | When syncing is paused, you **can** download       |
|                                                    | files.                                             | files.                                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| File accessibility when Drive for Desktop is not   | Downloaded and locally created files are           | Downloaded and locally created files are **not**   |
| running                                            | accessible when Drive for desktop isn’t running.   | accessible when Drive for desktop isn’t running.   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| QuickLook preview                                  | QuickLook previews only work for downloaded files  | QuickLook previews work for all files, assuming    |
|                                                    | (files without a cloud icon).                      | you have an internet connection.                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| File streaming                                     | In many settings, you can’t stream files and you   | File data can always be streamed.                  |
|                                                    | need to fully download files before you can        |                                                    |
|                                                    | examine them. This can cause delays when you       |                                                    |
|                                                    | examine larger files.                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

#### Understand drag & drop behavior while you use File Provider

When you drag and drop a folder or file within Finder, that item moves from its original location to its new location, provided both locations reside on the same disk volume. This remains true even when dragging the item in or out of the Drive for desktop file stream location.

**Tip:** To copy a file or folder, hold down the Option key and drag it to another location.

#### Learn why you're asked to enable Google Drive

To enable Google Drive when using File Provider, you must give explicit approval. To approve:

1.  Open **Finder**.
2.  On the left, under "Locations," click **Google Drive**.
3.  At the top right, click **Enable**.

You can also give permissions by clicking **OK** on the pop-up window.

If you do not enable Google Drive, you will not be able to stream your files using File Provider.

#### Troubleshoot startup failure with File Provider

Google Drive is unable to start when it encounters a File Provider initialization error. This error is an error from macOS. If you encounter this error:

1.  Update your macOS operating system to the latest version
2.  Restart your computer

#### Learn what happens to in-progress uploads when you sign out

When you sign out or disconnect an account while file uploads are in progress:

- In-progress uploads are preserved and recovered by File Provider.
- The next time you launch Drive for desktop, the application displays a notification with the location of the recovered files.

## Related resources:

- [System requirements and browsers](https://support.google.com/drive/answer/2375082)
- [Use Google Drive for desktop](https://support.google.com/docs/answer/10838124)

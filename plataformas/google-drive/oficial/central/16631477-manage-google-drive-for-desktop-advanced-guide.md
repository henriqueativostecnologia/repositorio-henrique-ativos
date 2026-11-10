---
fonte: https://support.google.com/drive/answer/16631477?hl=en
baixado: 2026-11-10
---

# Manage Google Drive for desktop: Advanced guide

**New to Google Drive for desktop?** Before you go through this article, [learn how to use Google Drive for desktop](https://support.google.com/drive/answer/10838124).

You can use this advanced guide to:

- [Understand mirroring vs. streaming My Drive](https://support.google.com/drive/answer/16631477#understand)
- [Use Google Drive for desktop with macOS](https://support.google.com/drive/answer/16631477#macos)
- [Back up photos and videos](https://support.google.com/drive/answer/16631477#back_up)
  - [Back up your macOS Photos library](https://support.google.com/drive/answer/16631477#back_up_macos)
- [Open files and folders offline](https://support.google.com/drive/answer/16631477#offline)
  - [Troubleshoot offline access](https://support.google.com/drive/answer/16631477#troubleshoot)
- [Customize your Google Drive for desktop settings](https://support.google.com/drive/answer/16631477#customize)
- [Troubleshoot Microsoft Office and Outlook files](https://support.google.com/drive/answer/16631477#microsoft)

## Understand mirroring vs. streaming My Drive

The 2 primary ways to sync your My Drive folder with your computer are mirroring or streaming.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| #### **Feature**                                   | #### **Streaming mode (default)**                  | #### **Mirroring mode**                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| #### **Local disk space usage**                    | **Minimal:** Space is only used for files you open | **Significant:** You store a full copy of My Drive |
|                                                    | or make available offline.                         | on your computer.                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| #### **Offline access**                            | To be available offline, you must manually select  | All files are available offline by default.        |
|                                                    | files or folders.                                  |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| #### **When app isn’t running**                    | Files are generally not accessible.                | You can fully access files as they’re standard     |
|                                                    |                                                    | local files.                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| #### **Data resilience**                           | Unsynced changes are stored in a local cache.      | Local files remain on your computer even if the    |
|                                                    | These changes can be lost if the cache is cleared  | app crashes. Unsynced changes are still present    |
|                                                    | or corrupted.                                      | locally.                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

**Important:** Shared drives use streaming, and folders you sync from your computer, under “Folders from your computer,” use mirroring.

### Change sync mode

1.  On your computer, open Google Drive for desktop Drive File Stream .
2.  Click on Settings Settings and then **Preferences**.
3.  On the left side, click **Google Drive**.
4.  Under “My Drive syncing options,” select **Stream files** or **Mirror files**.

### Switch between modes

**Important:** To prevent data loss, always make sure your recent changes have finished syncing before you switch your sync mode.

- This is especially critical when changing from “Mirror” to “Stream.”
- If you delete your old local folder from Mirror mode before all your changes have been uploaded to the cloud, those un-synced files will be lost.

**Recover from backups:** In version 85.0.13.0, you can now recover unsynced local files lost during a specific issue in version 84.x. To access it:

1.  Press and hold **Shift**.
2.  Click Settings Settings .

Recovered files are placed in a new “Google Drive Recovery” folder on your desktop.

[Learn more about streaming and mirroring files with Google Drive for desktop](https://support.google.com/drive/answer/13401938).

## Use Google Drive for desktop with macOS

To access your folders and devices when you sync files on a macOS computer, you must grant permission for Google Drive.

If you’re on macOS 12.1 or later with the “Stream files” feature, Google Drive for desktop uses Apple's File Provider technology. This provides a more native and integrated experience. Here's what you need to know:

- **Permissions:** To access your desktop, documents, downloads folders, and any external drive you want to sync, you must give it permission. To manage these settings, click **System Settings** and then **Privacy & Security**. [Learn how to give macOS permission to sync files](https://support.google.com/drive/answer/12178485#macOS-permission-mirror).
- **File provider integration:** To check if “File Provider” is active, click **Drive's Preferences** and then **Settings**. If it says “Folder location is controlled by macOS” the feature is in use. [Learn how to use File Provider to stream Google Drive files](https://support.google.com/drive/answer/12178485#File-Provider).
- **Cache location:** You can’t change the cache location for streamed files to an external drive. With File provider, macOS now manages where these temporary files are stored.
- **Offline files:** You can access offline files even when the Google Drive for desktop app isn’t open.

[Learn more about using Google Drive for desktop on macOS](https://support.google.com/drive/answer/12178485).

## Back up photos & videos

Note: Backup to Google Photos is no longer available in Google Drive for desktop. To continue backing up their folders to Google Photos, users will need to reselect their preferred backup folders in the new Google Photos interface. Any items previously backed up will remain in Google Photos.

[Learn more at the Google Photos help center](https://support.google.com/photos/answer/6193313#stop_folder_backups).

You can set up Google Drive for desktop to automatically back up your photos and videos to Google Photos.

**Important:**

- If you set a folder with photos, videos, and other file types to "Back up to Google Photos", only photos and videos will back up to Google Photos.
- If you set a folder to both “Sync with Google Drive” and “Back up to Google Photos,” your photos and videos are uploaded twice and use more of your Google storage.
- You can only back up photos and videos in Google Drive for desktop from a Network Attached Storage (NAS) device to Google Photos. You can’t fully sync a NAS folder with Google Drive.

### Back up your macOS Photos library

You can sync your Apple Photos library with Google Drive, but it comes with risks.

**Important:**

- The Apple Photos library is a complex database. Changes in more than one place can cause corruption.
- If you have multiple photo libraries on your Mac, only the one designated as the System Photo library syncs with iCloud services. This is usually the first library you created or opened.
- To avoid issues, it's best to export photos from the Photos app and then sync the exported files, rather than sync the live library package.

## Open files & folders offline

To access your files and folders without an internet connection, simply make them available offline. The way this works depends on whether you’re streaming or mirroring your files.

- **Mirror files:** When you mirror your My Drive, a complete copy of all your files is downloaded to your computer. They’re available offline by default.
- **Stream files:** When you stream, files are stored in the cloud and only downloaded when you need them. To access them offline:
  1.  Right-click the file or folder.
  2.  Select **Offline Access** and then **Available offline**.

[Learn more about using files offline with Google Drive for desktop](https://support.google.com/drive/answer/2375012#Use_files_offline_for_desktop).

### Troubleshoot offline access

- **“Available offline” option is missing:**
  - This option is only available when you‘re in “Stream files” mode and the Google Drive for desktop application runs. It won’t show in “Mirror files” mode, as all your files are already on your computer.
  - To use Google Docs, Google Sheets, and Google Slides offline, you must [make them available offline in Drive on the web.](https://support.google.com/drive/answer/2375012#files_offline_drive_web&zippy=%2Csave-non-google-files-for-offline-use%2Coffline-differences-between-streaming-mirroring%2Cstorage-consumption-on-the-local-hard-drive)
- **Error making files offline:** Check your disk space, internet connection, or file permission. If you make a large number of files available offline at once, you can also get errors like “too many open files.” To avoid these errors, make smaller batches instead.
- **Offline files aren’t accessible:** To access offline files in “Stream files” mode, the Google Drive for desktop application must be open. Your account must be connected. If the app is closed or you’ve signed out, you can’t access your cached files.

## Customize your Google Drive for desktop settings

You can improve your Google Drive for desktop experience through the Advanced Settings menu.

To go to the Advanced Settings menu,

1.  On your computer, click the Google Drive for desktop menu Drive File Stream .
2.  At the top right, click **Settings** Settings and then **Preferences** and then **Advanced settings** Settings

From there, you can:

- **Manage Microsoft Office presence:** To check when others edit a shared Microsoft Office file, turn **Real-time presence** on or off.
- **Change Google Drive letter (Windows):** Customize the letter assigned to your Google Drive virtual drive, like “G.”
- **Configure proxy settings:** Adjust your proxy settings. Auto-detect uses your system's settings, while direct connection bypasses them.
- **Set bandwidth limits:** Limit the download and upload rates in kilobytes per second (KBps).
- **Set hotkeys:** To open the Google Drive search window, set a custom keyboard shortcut.

## Troubleshoot Microsoft Office & Outlook files

To streamline your workflow, Google Drive for desktop integrates with Microsoft Office and Outlook.

### Learn about real-time presence in Microsoft Office

This feature lets you check if other people currently edit a shared Word, Excel, or PowerPoint file stored in Google Drive.

- **Requirements:** You need Microsoft Office 2010 or later. On macOS, you must also grant “Accessibility” permissions to Google Drive in your system settings.
- **Troubleshooting:** If real-time presence is unavailable, check if the feature is on in Google Drive's preferences and that macOS permissions are set correctly. You must confirm that a collaborator doesn’t turn off the feature on their end.

### Install Microsoft Outlook add-in (Windows)

For Windows users with a work or school account, an Outlook add-in is available to help you insert Google Drive files into emails and save attachments directly to Google Drive.

- **Unable to save files to Google Drive:**
  - Run Outlook as an administrator.
  - To fix potential issues with your Outlook data file, run the Inbox Repair Tool (ScanPST.exe).
- **Conflicts with other add-ins:** To find conflicts, try to turn off other add-ins like those for Salesforce and Adobe one by one.
- **Error codes in Outlook:** Errors like “0x80004005 (unspecified error)” or “0x8004011D (server not available),” can indicate a conflict with antivirus software, corrupted Microsoft Office files, or a faulty add-in. To identify the “faulting module name,” you can examine Windows Event Viewer logs for Event ID 1000 (Application Error). This points directly to the problematic add-in.

## Related resources

- [Use Google Drive for desktop](https://support.google.com/drive/answer/10838124)
- [Customize Google Drive for desktop settings](https://support.google.com/drive/answer/13470231)
- [Use Google Drive for desktop on macOS](https://support.google.com/drive/answer/12178485)
- [Learn how to fix problems in Google Drive for desktop](https://support.google.com/drive/answer/2565956#fix-error-messages)

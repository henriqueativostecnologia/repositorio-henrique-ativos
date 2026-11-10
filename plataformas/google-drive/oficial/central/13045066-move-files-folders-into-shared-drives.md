---
fonte: https://support.google.com/drive/answer/13045066?hl=en
baixado: 2026-11-10
---

# Move files & folders into shared drives

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

For easier collaboration, you can move files and folders from My Drive to a shared drive on a computer if you’re logged into a [work or school account](https://support.google.com/accounts/answer/6250166?hl=en). By default, you can only move files and folders you own.

- If your admin enables the setting to allow file editors to move files into a shared drive, you may move files on which you’re an Editor. For more information on this admin setting, go to [Move your organization's content to a shared drive](https://support.google.com/a/answer/7374057#users_files).
- You can only move a folder to a shared drive if you’re a manager of the shared drive.

### Learn how file access changes

When you move content to a shared drive:

- Non-members of a shared drive could lose access to content moved into a shared drive.
- Only members of the shared drive and people with whom the file is directly shared can access the file.
- File permissions inherited from folders aren’t copied.
  - If you move a child folder to a shared drive, permissions inherited from the parent folder won’t be copied over.
  - If you move a parent folder to a shared drive, the child folder will still inherit those permissions.
- If the original owner of a file is in your organization but not a member of the shared drive, they lose ownership, but can still access the file.

If you have access to a shared drive, all of its files are visible to you by default. However, [certain roles](https://support.google.com/drive/answer/14254362#certain_roles) can limit access to specific folders, and control who can check and edit their content. [Learn how to limit access to folders](https://support.google.com/drive/answer/14254362).

### Understand limitations when you move files & folders

Here are some general problems you could find when you move files and folders from My Drive to a shared drive:

#### Move files owned by users outside of your organization

- You can’t move folders or files external users own, even if the external user is a member of the destination shared drive.
- You can’t move internally-owned subfolders that are part of an externally-owned folder.

#### Move Google Sites files to shared drives

- If the original owner of the site is in the same organization as the shared drive, the published site is still visible. For users with whom the site was previously shared, the Sites file related to the site is still accessible.
- If the original owner of the site is in a different organization than the shared drive, the published site is still visible. Even if it was previously shared with them, the associated file isn’t accessible to people who aren’t members of the shared drive.

#### Understand other limitations when you move Drive folders to shared drives

- Shortcuts are created for any items that can’t be moved. If there are any items that can’t be moved because of permission or access issues, when you move folders from My Drive to a shared drive, it creates a shortcut in the shared drive to preserve the current folder hierarchy. In order to do this, we enforce the following folder move limits:
  - Folders can't be moved if there are either 25 unmovable items or if 10% of items are unmovable (the limit is the smaller of either 10% or 25 items per folder).
  - The move can have no more than 100,000 items total.
- When shortcuts are created, the original items are relocated to the owner’s My Drive folder.
- When you move a large number of folders into a shared drive that might exceed the limit, you could get a warning notice before you attempt to move.

#### Understand why pre-move dialog may not match pre-move download

- The number of moveable items in your pre-move dialogue may not match the number shown in your pre-move download because:
  - The pre-move dialog counts items which you don't have access to, the pre-move download doesn't include these items.
  - If a folder that contains other folders or items (a parent folder) is unmovable and there are more items within that parent folder that can’t be moved, only the parent folder is listed. The items within that parent folder aren't counted toward the number of movable items.

### Understand error codes

If you receive a notification that items can’t be moved, you’ll have an option to click **Download item list (CSV).** It'll prompt a download of a CSV file which includes a list of the items that can’t be moved and the error code associated with each item. More information about each error code is listed below:

##### UNKNOWN_UNMOVABLE_REASON and OTHER

The files can't be moved because of various reasons.

##### INSUFFICIENT_PERMISSION

The files can't be moved because you don't have the necessary permissions. Ask the owner of the file for permissions.

##### DIFFERENT_CUSTOMER

The files can't be moved because they belong to organizations that don't allow it.

##### ABUSE

The files can’t be moved because they have harmful content.

##### BLOCKED_TYPE

The files can’t be moved because their file types aren’t supported in shared drives.

##### SHARED_DRIVE_NOT_FOUND

The files can’t be moved because the target destination has been removed.

##### ALREADY_IN_SHARED_DRIVE

The files can’t be moved because they’re already in the destination shared drive.

##### EDITOR_MOVE_IN_DISABLED

The files can’t be moved because your domain doesn’t allow editors to move files to shared drives.

##### OWNER_MUST_BE_MEMBER_OF_DESTINATION_SHARED_DRIVE

The files can’t be moved because the owner isn’t a member of the shared drive.

##### CANNOT_MOVE_AS_ADMIN

The files can't be moved because the admin user lacks move-in privileges.

## Version: Android phone & tablet

You can only move files and folders from My Drive to a shared drive on a computer. To move files and folders into shared drives, from a computer, log into your [work or school account](https://support.google.com/accounts/answer/6250166?hl=en).

## Version: iPhone & iPad

You can only move files and folders from My Drive to a shared drive on a computer. To move files and folders into shared drives, from a computer, log into your [work or school account](https://support.google.com/accounts/answer/6250166?hl=en).

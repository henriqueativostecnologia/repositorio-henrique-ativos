---
fonte: https://support.google.com/drive/answer/2375114?hl=en
baixado: 2026-11-10
---

# Search for files in Google Drive

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

There are many ways to search for your files in Drive. To quickly narrow your search by File type, People, Date Modified, and more, use filter chips. You can use filter chips on their own or in combination with other search terms, like file names or text within the file.

**Tip:**

- If you have access to [Gemini in Workspace features](13952129), you can use natural language to ask questions directly in the search bar to find information quickly.
- When you enter a question like *"Summarize the project timeline"* into the search bar, an AI Overview appears at the top of your results. This overview provides a summary answer from your files, along with links to the sources used. [Learn more about natural language search in Gemini.](https://support.google.com/drive/answer/16685111)

In this section, you'll learn how to: 

- [Search & filter your files](#search_filter_files)
- [Use advanced search](#use_advanced_search)
- [Find files by size](#find_files_by_size)
- [Find missing files](#find_missing_files)

### Search & filter your files

To narrow the list of files in Drive, you can use filter chips, conventional search, or both. If you start with filter chips, you can search and filter by:

- Type
- People
- Modified

These search filters also appear inside the search bar and will filter results directly within the search dropdown box. You can select from the same filters listed above, or start typing the desired filter to see a suggestion. For example, if you type “doc,” a suggested filter chip appears that lets you filter by Documents within the search dropdown box.

After you select the desired filter chip, select:

- Your file from the newly filtered list in the search box.
- To get more results, hit “Enter.”

You can layer these filters with additional text as well. For example, if you select “Type=Presentations” and then type “Client” in the search box, your results are filtered to all Presentations with the word “Client.”

- **To remove a filter chip:** On the right of the chip, click Remove .
- **To remove all filter chips:** At the end of the chips, click **Clear filters**.

**Tip:** Your search results are automatically sorted by relevance. Click any of the column headers to sort by that column. To sort by relevance again, click More sorting options More .

### Use advanced search

**Important:** Not all examples work on all devices.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Advance search type**                            | **Definition**                                     | Example                                            |
+====================================================+====================================================+====================================================+
| **Quotes**                                         | Find documents that contain an exact word or       | Example:                                           |
|                                                    | phrase.                                            |                                                    |
|                                                    |                                                    | `"match this phrase exactly"`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Minus sign**                                     | Find documents that exclude a particular word. If  | Example:` `                                        |
|                                                    | you want "salsa," but not "dancing.”               |                                                    |
|                                                    |                                                    | `salsa -dancing`                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **owner**                                          | Find documents owned by a specific person.         | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | `owner:bob@gmail.com`                              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **pendingowner**                                   | Find files you’re a pending owner of.              | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    | **Important:** You can only search for files that  | `pendingowner:me`                                  |
|                                                    | you’re the pending owner of.                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **creator**                                        | Find documents in shared drives created by a       | Example:                                           |
|                                                    | specific person.                                   |                                                    |
|                                                    |                                                    | `creator:jane@yourdomain.com`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **to**                                             | Find documents you shared with a specific person   | Examples:                                          |
|                                                    | or group or documents shared with you.             |                                                    |
|                                                    |                                                    | -   `to:me`                                        |
|                                                    |                                                    | -   `to:bob@gmail.com`                             |
|                                                    |                                                    | -   `to:bobsgroup@googlegroups.com`                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **from**                                           | Find documents a specific person shared with you   | Examples:                                          |
|                                                    | or you shared                                      |                                                    |
|                                                    |                                                    | -   `from:me`                                      |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `from:bob@gmail.com`                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **app**                                            | Search by app name. This includes any app          | Examples:                                          |
|                                                    | connected to your Google Drive account             |                                                    |
|                                                    |                                                    | -   `app:"Google Apps Script"`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `app:"Google Jamboard"`                        |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `app:"Google Meet"`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **sharedwith**                                     | Find documents a specific Workspace account or     | Examples:                                          |
|                                                    | group has access to. Exclude files the account     |                                                    |
|                                                    | owns.                                              | -   `sharedwith:me`                                |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:bob@gmail.com`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:external`                          |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |     -   Find items explicitly shared with users or |
|                                                    |                                                    |         groups outside your Google Workspace       |
|                                                    |                                                    |         organization.                              |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:public`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **is:starred**                                     | Find items that you starred.                       | `is:starred`                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **is:trashed**                                     | Find items moved to trash.                         | `is:trashed`                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **type**                                           | Search by document type:                           | Examples:                                          |
|                                                    |                                                    |                                                    |
|                                                    | -   Folder                                         | -   `type:document`                                |
|                                                    |                                                    | -   `type:forms`                                   |
|                                                    | -   Document                                       | -   `type:spreadsheet`                             |
|                                                    |                                                    | -   `type:email-layout`                            |
|                                                    | -   Spreadsheet                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Presentation                                   |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   PDF                                            |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Image                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Video                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Drawing                                        |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Form                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Site                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Script                                         |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Table                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Email layout                                   |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Jam file                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **before & after**                                 | Find items modified before or after a certain      | Examples:                                          |
|                                                    | date. Format the date as YYYY-MM-DD.               |                                                    |
|                                                    |                                                    | -   `before:2021-05-02`                            |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `after:2021-05-01`                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **createdbefore & createdafter**                   | Find items created before or after a certain date. | Examples:                                          |
|                                                    | Format the date as YYYY-MM-DD.                     |                                                    |
|                                                    |                                                    | -   `createdbefore:2022-05-02`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `createdafter:2022-05-01`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **title**                                          | Search for items by title.                         | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | `title:Conference 2021`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **followup**                                       | Find files that have any action items or           | Examples:                                          |
|                                                    | suggestions assigned to you.                       |                                                    |
|                                                    |                                                    | -   `followup:any`                                 |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `followup:suggestions`                         |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `followup:actionitems`                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **unorganized**                                    | Find a file you created in someone else's folder   | Example:                                           |
|                                                    | if they delete that folder. Your file isn't        |                                                    |
|                                                    | deleted. It's automatically moved to your My       | `is:unorganized owner:me`                          |
|                                                    | Drive.                                             |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Important:** Only you can delete the files you   |                                                    |
|                                                    | own.                                               |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

### Find files by size

To find files by size:

1.  On your computer, go to [drive.google.com](http://drive.google.com).
2.  On the left, click **Storage**.
3.  **To sort by file size:** on the right, click **Storage used**.
4.  **To reverse the sort order:** On the right, click **Storage used**.

### Find missing files

If you’re unable to locate your file with the search methods listed above, there may be other ways to find the lost file. [Find lost files in Google Drive](https://support.google.com/drive/answer/15701190).

### Related resources

- [Recover a deleted file](https://support.google.com/drive/answer/1716222)
- [Reorder your files](https://support.google.com/drive/answer/2375177)
- [Find lost files in Google Drive](https://support.google.com/drive/answer/15701190)

## Version: Android phone & tablet

There are many ways to search for your files in Drive. To quickly narrow your search by File type, People, Date Modified, and more, use filter chips. You can use filter chips on their own or in combination with other search terms, like file names or text within the file.

### Search tips

- Your Drive searches include the titles and content of all files you have permission to access.
- To save your Drive searches, turn on Web & App Activity.
  - [Learn how to turn Web & App Activity on or off](https://support.google.com/websearch/answer/54068).
- To search within a folder:
  1.  Go to the folder.
  2.  Below the search bar, a filter chip for the folder shows.
      - To limit the search within the folder, select the folder chip.
  3.  Enter your search term.
      - You get additional filter suggestions as you enter text.

In this section, you'll learn how to:

- [Search for your files](#search_files)
- [Use Drive search categories](#drive_search_categories)
- [Use advanced search](#advanced_search)
- [Find missing files](#find_missing_files)
- [Search Drive with your feed](#search_drive_with_feed)

### Search for your files

To narrow the list of files in Drive, you can type text in the search box, use filter chips, or both.

To start with text:

On your Android phone or tablet, open the [Google Drive app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs).

1.  At the top, tap **Search in Drive**.
    - To filter the list automatically, type a word or phrase in the search box. Drive suggests filter chips to narrow your search by Type, People, Date Modified, and more.
      - For example, if you type “doc,” a filter chip appears to filter by Google Documents, as well as any results in Drive that contain the word “doc.”
    - If you select a filter chip, your list of files narrows by that selection.
    - To remove a filter chip, tap the chip and from the pop-up window, tap **Clear**.

To start with filter chips:

1.  On your Android phone or tablet, open the [Google Drive app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs).
2.  At the top, tap **Search in Drive**.
3.  To refine your search by Type, People, or Modified, select a filter chip.
4.  Once you select a chip, you can filter results by keyword.
5.  To remove a filter chip, tap the chip and from the pop-up menu, tap **Clear**.

### Use Drive search categories

In Drive, you can search by:

- File title
- File contents
- Type
- Other metadata, that includes:
  - Description field
  - Shared labels
  - File location
  - Owner
  - Creator
  - Modified date
  - Approvals
  - Follow-ups
- Items or words featured in pictures, PDF files, or other files stored on your Drive

### Use advanced search

**Important:** Not all examples work on all devices.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Advance search type**                            | **Definition**                                     | Example                                            |
+====================================================+====================================================+====================================================+
| **Quotes**                                         | Find documents that contain an exact word or       | Example:                                           |
|                                                    | phrase.                                            |                                                    |
|                                                    |                                                    | `"match this phrase exactly"`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Minus sign**                                     | Find documents that exclude a particular word. If  | Example:` `                                        |
|                                                    | you want "salsa," but not "dancing.”               |                                                    |
|                                                    |                                                    | `salsa -dancing`                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **owner**                                          | Find documents owned by a specific person.         | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | `owner:bob@gmail.com`                              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **pendingowner**                                   | Find files you’re a pending owner of.              | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    | **Important:** You can only search for files that  | `pendingowner:me`                                  |
|                                                    | you’re the pending owner of.                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **creator**                                        | Find documents in shared drives created by a       | Example:                                           |
|                                                    | specific person.                                   |                                                    |
|                                                    |                                                    | `creator:jane@yourdomain.com`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **to**                                             | Find documents you shared with a specific person   | Examples:                                          |
|                                                    | or group or documents shared with you.             |                                                    |
|                                                    |                                                    | -   `to:me`                                        |
|                                                    |                                                    | -   `to:bob@gmail.com`                             |
|                                                    |                                                    | -   `to:bobsgroup@googlegroups.com`                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **from**                                           | Find documents a specific person shared with you   | Examples:                                          |
|                                                    | or you shared.                                     |                                                    |
|                                                    |                                                    | -   `from:me`                                      |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `from:bob@gmail.com`                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **app**                                            | Search by app name. This includes any app          | Examples:                                          |
|                                                    | connected to your Google Drive account.            |                                                    |
|                                                    |                                                    | -   `app:"Google Apps Script"`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `app:"Google Jamboard"`                        |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `app:"Google Meet"`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **sharedwith**                                     | Find documents a specific Workspace account or     | Examples:                                          |
|                                                    | group has access to. Exclude files the account     |                                                    |
|                                                    | owns.                                              | -   `sharedwith:me`                                |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:bob@gmail.com`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:external`                          |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |     -   Find items explicitly shared with users or |
|                                                    |                                                    |         groups outside your Google Workspace       |
|                                                    |                                                    |         organization.                              |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:public`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **is:starred**                                     | Find items that you starred.                       | `is:starred`                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **is:trashed**                                     | Find items you moved to trash.                     | `is:trashed`                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **type**                                           | Search by document type:                           | Examples:                                          |
|                                                    |                                                    |                                                    |
|                                                    | -   Folder                                         | -   `type:document`                                |
|                                                    |                                                    | -   `type:forms`                                   |
|                                                    | -   Document                                       | -   `type:spreadsheet`                             |
|                                                    |                                                    | -   `type:email-layout`                            |
|                                                    | -   Spreadsheet                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Presentation                                   |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   PDF                                            |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Image                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Video                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Drawing                                        |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Form                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Site                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Script                                         |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Table                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Email layout                                   |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Jam file                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **before & after**                                 | Find items modified before or after a certain      | Examples:                                          |
|                                                    | date. Format the date as YYYY-MM-DD.               |                                                    |
|                                                    |                                                    | -   `before:2021-05-02`                            |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `after:2021-05-01`                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **createdbefore & createdafter**                   | Find items created before or after a certain date. | Examples:                                          |
|                                                    | Format the date as YYYY-MM-DD.                     |                                                    |
|                                                    |                                                    | -   `createdbefore:2022-05-02`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `createdafter:2022-05-01`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **title**                                          | Search for items by title.                         | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | `title:Conference 2021`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **followup**                                       | Find files that have any action items or           | Examples:                                          |
|                                                    | suggestions assigned to you.                       |                                                    |
|                                                    |                                                    | -   `followup:any`                                 |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `followup:suggestions`                         |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `followup:actionitems`                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **unorganized**                                    | Find a file you created in someone else's folder   | Example:                                           |
|                                                    | if they delete that folder. Your file isn't        |                                                    |
|                                                    | deleted. It's automatically moved to your My       | `is:unorganized owner:me`                          |
|                                                    | Drive.                                             |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Important:** No one but you can delete files you |                                                    |
|                                                    | own.                                               |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | \                                                  |                                                    |
|                                                    | .                                                  |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

### Find missing files

If you’re unable to locate your file with the search methods listed above, there may be other ways to find the lost file. [Find lost files in Google Drive](https://support.google.com/drive/answer/15701190).

### Search Drive with your feed

If you have the Drive app on your Android phone or tablet, you can search for files in Drive [from your feed](https://support.google.com/websearch/answer/2819496).

1.  Open your feed.
2.  Type or speak the words, "Search Drive for" followed by the phrase you want to search for in Drive.
    - To type your search, tap the search box at the top.
    - To speak your search, tap the microphone in the search box.
3.  Tap Done Done .
4.  The Drive app will open and search for the phrase you requested.

To return to "My Drive" after your search, tap Back Back .

### Related resources

- [Recover a deleted file](https://support.google.com/drive/answer/1716222)
- [Reorder your files](https://support.google.com/drive/answer/2375177)
- [Find lost files in Google Drive](https://support.google.com/drive/answer/15701190)

## Version: iPhone & iPad

There are many ways to search for your files in Drive. To quickly narrow your search by File type, People, Date Modified, and more, use filter chips. You can use filter chips on their own or in combination with other search terms, like file names or text within the file.

### Search tips

- Your Drive searches include the titles and content of all files you have permission to access.
- To save your Drive searches, turn on Web & App Activity.
  - [Learn how to turn Web & App Activity on or off](https://support.google.com/websearch/answer/54068).
- To search within a folder:
  1.  Go to the folder.
  2.  Below the search bar, a filter chip for the folder shows.
      - To limit the search within the folder, select the folder chip.
  3.  Enter your search term.
      - You get additional filter suggestions as you enter text.

In this section, you'll learn how to:

- [Search for your files](#search_for_files)
- [Use Drive search categories](#drive_search_categories)
- [Use advanced search](#use_advanced_search)
- [Find missing files](#find_missing_files)

### Search for your files

To narrow the list of files in Drive, you can type text in the search box, use filter chips, or both.

To start with text:

On your iPhone or iPad, open the [Google Drive app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs).

1.  At the top, tap **Search in Drive**.
    - To filter the list automatically, type a word or phrase in the search box. Drive suggests filter chips to narrow your search by Type, People, Date Modified, and more.
      - For example, if you type “doc,” a filter chip appears to filter by Google Documents, as well as any results in Drive that contain the word “doc.”
    - If you select a filter chip, your list of files narrows by that selection.
    - To remove a filter chip, tap the chip and from the pop-up window, tap **Clear**.

To start with filter chips:

1.  On your iPhone or iPad, open the [Google Drive app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs).
2.  At the top, tap **Search in Drive**.
3.  To refine your search by Type, People, or Modified, select a filter chip.
4.  Once you select a chip, you can filter results by keyword.
5.  To remove a filter chip, tap the chip and from the pop-up menu, tap **Clear**.

### Drive search categories

In Drive, you can search by:

- File title
- File contents
- Type
- Other metadata, that includes:
  - Description field
  - Shared labels
  - File location
  - Owner
  - Creator
  - Modified date
  - Approvals
  - Follow-ups
- Items or words featured in pictures, PDF files, or other files stored on your Drive

### Use advanced search

**Important:** Not all examples work on all devices.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Advance search type**                            | **Definition**                                     | Example                                            |
+====================================================+====================================================+====================================================+
| **Quotes**                                         | Find documents that contain an exact word or       | Example:                                           |
|                                                    | phrase.                                            |                                                    |
|                                                    |                                                    | `"match this phrase exactly"`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Minus sign**                                     | Find documents that exclude a particular word. If  | Example:` `                                        |
|                                                    | you want "salsa," but not "dancing.”               |                                                    |
|                                                    |                                                    | `salsa -dancing`                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **owner**                                          | Find documents owned by a specific person.         | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | `owner:bob@gmail.com`                              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **pendingowner**                                   | Find files you’re a pending owner of.              | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    | **Important:** You can only search for files that  | `pendingowner:me`                                  |
|                                                    | you’re the pending owner of.                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **creator**                                        | Find documents in shared drives created by a       | Example:                                           |
|                                                    | specific person.                                   |                                                    |
|                                                    |                                                    | `creator:jane@yourdomain.com`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **to**                                             | Find documents you shared with a specific person   | Examples:                                          |
|                                                    | or group or documents shared with you.             |                                                    |
|                                                    |                                                    | -   `to:me`                                        |
|                                                    |                                                    | -   `to:bob@gmail.com`                             |
|                                                    |                                                    | -   `to:bobsgroup@googlegroups.com`                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **from**                                           | Find documents a specific person shared with you   | Examples:                                          |
|                                                    | or you shared.                                     |                                                    |
|                                                    |                                                    | -   `from:me`                                      |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `from:bob@gmail.com`                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **app**                                            | Search by app name. This includes any app          | Examples:                                          |
|                                                    | connected to your Google Drive account.            |                                                    |
|                                                    |                                                    | -   `app:"Google Apps Script"`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `app:"Google Jamboard"`                        |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `app:"Google Meet"`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **sharedwith**                                     | Find documents a specific Workspace account or     | Examples:                                          |
|                                                    | group has access to. Exclude files the account     |                                                    |
|                                                    | owns.                                              | -   `sharedwith:me`                                |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:bob@gmail.com`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:external`                          |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |     -   Find items explicitly shared with users or |
|                                                    |                                                    |         groups outside your Google Workspace       |
|                                                    |                                                    |         organization.                              |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `sharedwith:public`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **is:starred**                                     | Find items that you starred.                       | `is:starred`                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **is:trashed**                                     | Find items you moved to trash.                     | `is:trashed`                                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **type**                                           | Search by document type:                           | Examples:                                          |
|                                                    |                                                    |                                                    |
|                                                    | -   Folder                                         | -   `type:document`                                |
|                                                    |                                                    | -   `type:forms`                                   |
|                                                    | -   Document                                       | -   `type:spreadsheet`                             |
|                                                    |                                                    | -   `type:email-layout`                            |
|                                                    | -   Spreadsheet                                    |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Presentation                                   |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   PDF                                            |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Image                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Video                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Drawing                                        |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Form                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Site                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Script                                         |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Table                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Email layout                                   |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   Jam file                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **before & after**                                 | Find items modified before or after a certain      | Examples:                                          |
|                                                    | date. Format the date as YYYY-MM-DD.               |                                                    |
|                                                    |                                                    | -   `before:2021-05-02`                            |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `after:2021-05-01`                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **createdbefore & createdafter**                   | Find items created before or after a certain date. | Examples:                                          |
|                                                    | Format the date as YYYY-MM-DD.                     |                                                    |
|                                                    |                                                    | -   `createdbefore:2022-05-02`                     |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `createdafter:2022-05-01`                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **title**                                          | Search for items by title.                         | Example:                                           |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | `title:Conference 2021`                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **followup**                                       | Find files that have any action items or           | Examples:                                          |
|                                                    | suggestions assigned to you.                       |                                                    |
|                                                    |                                                    | -   `followup:any`                                 |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `followup:suggestions`                         |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | -   `followup:actionitems`                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **unorganized**                                    | Find a file you created in someone else's folder   | Example:                                           |
|                                                    | if they delete that folder. Your file isn't        |                                                    |
|                                                    | deleted. It's automatically moved to your My       | `is:unorganized owner:me`                          |
|                                                    | Drive.                                             |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Important:** No one but you can delete files you |                                                    |
|                                                    | own.                                               |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | \                                                  |                                                    |
|                                                    | .                                                  |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

### Find missing files

If you’re unable to locate your file with the search methods listed above, there may be other ways to find the lost file. [Find lost files in Google Drive](https://support.google.com/drive/answer/15701190).

### Related resources

- [Recover a deleted file](https://support.google.com/drive/answer/1716222)
- [Reorder your files](https://support.google.com/drive/answer/2375177)
- [Find lost files in Google Drive](https://support.google.com/drive/answer/15701190)

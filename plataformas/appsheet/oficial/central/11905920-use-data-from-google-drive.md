---
fonte: https://support.google.com/appsheet/answer/11905920?hl=en
baixado: 2026-11-10
---

# Use data from Google Drive

AppSheet allows you to create a table based on a collection of files stored in Google Drive. This feature allows you to view files contained within a folder as rows of a table, with attributes of those files presented as columns in the table.

**Note**: Access to a Google Drive using a [shortcut](https://support.google.com/drive/answer/9700156) is not supported.

## How do I create a table from a collection of files?

To create a table based on a collection of files, you must have set up Google as a data source:

1.  In AppSheet, go to **Data ** and click **+** in the top header of the Data panel.

    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables **and click **+ New Table**.  

2.  Select **Google Drive Documents**.
    The Create a new document table dialog displays.

3.  Under **Folder**, click **Collection of Files**.

    Click Collection of files under Folder on the Create a new document table dialog

4.  Select the folder from which to create the table.
    **Note**: The file picker will only show and allow selection of folders, even if there are files contained within a folder.

5.  If desired, customize the name of the table and select **Create Table**.

## What can I do with a collection of files?

Tables based on a collection of files are regular AppSheet tables. This means that they can be used in any way that a table usually can be used. This includes:

- Creating UX views for interacting with file data. You can build views that allow users to view file metadata and even upload files to the underlying folder.
- Adding and deleting rows from the table. This results in files being added or deleted to the underlying folder.
- Creating slices. This allows you to create subsets of data to, for example, filter based on file names or date modified.

Creating cross-references from other tables. Other tables which reference files contained in the underlying folder can specify these files as [Ref columns](https://support.google.com/appsheet/answer/10106510). This enables using file metadata from tables which use files.

## Table schema

The following table describes the default schema given for a collection of files.

|                  |                |                                                                                              |                                             |
|------------------|----------------|----------------------------------------------------------------------------------------------|---------------------------------------------|
| **Field Name**   | **Field Type** | **Description**                                                                              | **Example**                                 |
| `_ID`            | `Text`         | Internal Drive ID of the file.                                                               | `1Y1XAe9j0s3XenHPeROyB3FhAIcbBB3Uz`         |
| `Path`           | `Text`         | Full path to the file, from the root of the drive.                                           | `Documents/Invoices/Invoice-2021-04-20.pdf` |
| `File`           | `File`         | File within the containing folder.                                                           | `Invoice-2021-04-20.pdf`                    |
| `CreateTime`     | `DateTime`     | Time when the file was created.                                                              | `7/13/2020 7:39:11 PM`                      |
| `LastModifiedBy` | `Email`        | Email of the user who last modified the file. This field may not be available in some cases. | `me@example.com`                            |
| `MimeType`       | `Text`         | MIME type of the content.                                                                    | `text/plain`                                |

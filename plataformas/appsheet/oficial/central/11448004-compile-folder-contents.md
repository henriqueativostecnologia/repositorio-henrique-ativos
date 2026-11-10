---
fonte: https://support.google.com/appsheet/answer/11448004?hl=en
baixado: 2026-11-10
---

# Compile folder contents

AppSheet enables you to compile a list of files and metadata from a folder in Google Drive. Then, you can expose the files directly in your app and use the file metadata in your application logic, such as filtering by file name, date modified, and so on.

To compile a list of files and metadata from a folder in Google Drive:

1.  Open the app in the editor.

2.   Go to **Data** and click **+** in the top header of the Data panel.

3.   We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables **and click **+ New Table**.  

4.  Select **Documents on Google Drive** in the **Get data from…** dialog.

5.  Under **Folder**, click **Collection of files**.

6.  Navigate to the folder on Google Drive that contains the documents and click **Select**.
    The **Source File Folder** and **Table Name** fields are displayed and populated based on the folder you select. Click **Change** to edit the **Source File Folder**, if required

7.  Edit the **Table name**, if required.
    The table name defaults to the folder name.

8.  Click **Create Table**.
    The document table is created.

9.  Click **View data** in the table header to view the file list and metadata in your new document table.

The following table summarizes the information extracted for each file

|                  |            |
|------------------|------------|
| **Column**       | **Format** |
| `_ID` (Key)      | Text       |
| `Path`           | Text       |
| `File`           | File       |
| `CreateTime`     | DateTime   |
| `LastModifiedBy` | Email      |
| `MimeType`       | Text       |

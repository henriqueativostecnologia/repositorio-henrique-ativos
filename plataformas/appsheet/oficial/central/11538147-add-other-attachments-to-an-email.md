---
fonte: https://support.google.com/appsheet/answer/11538147?hl=en
baixado: 2026-11-10
---

# Add other attachments to an email

Add other attachments to an email by setting the **Other Attachments** property when [configuring an email](https://support.google.com/appsheet/answer/11447614), as described in the following sections.

- [Supported file types for other attachments](#supported-file-types)
- [Set the Other Attachments property](#set-property)
- [How AppSheet locates other attachment files](#how-locates)
- [Restrict the other attachment files in your app](#restrict)
- [Secure other attachment files](#secure)

AppSheet simply attaches the files you specify to the email; it does not replace variables in the email attachments as with an [email attachment template](https://support.google.com/appsheet/answer/11539957).

### Supported file types for other attachments

You can attach a wide variety of file types. For example, it is common to attach photographs, drawings, PDF files, or Microsoft Office files.

AppSheet supports the following file types for other attachments:

- Images
- Thumbnails
- Signatures
- Drawings
- PDF files
- Microsoft Word files
- Microsoft Excel files
- CSV files
- JSON files
- XML files
- Files created by a preceding **Create a new file** task
- Other types of files

### Set the Other Attachments property

When configuring the **Other Attachments** property, you can specify the following:

- **Filename**, such as `MyPhoto.jpeg` or `MyWordFile.docx`.
- **Simple column expression**, such as `[ImageColumn]` or `[FileColumn]` where the filename is stored in the column.
- **More complex expression**, like the dereference expression `[ProductRef].[ProductPhoto]`. In this example, the filename is stored in the `[ProductPhoto]` column.
- It is common to store the images for a parent table in a child table. This allows each parent record to have zero, one, or more child images. Each child record contains an image field and a `Ref` field to the parent record. The parent record contains a `Reverse Ref` field containing the key values of the child image records. For example, if the `Reverse Ref` field in the parent record is called `Related Images` and the image field in the child record is called `Image`, then you can include the child images as attachments by specifying **`[Related Images][Images]`**.

You can attach a file created by a previously invoked **Create a new file** task in the same bot or a prior bot.

### How AppSheet locates other attachment files

AppSheet expects your other attachment files to reside in a specific location, based on your authentication provider and whether it can store files.

**Authentication providers that can store files**

For Google, Microsoft, Dropbox, Box, and other authentication providers that can store files, AppSheet checks for other attachment files in the following locations:

- **Folder that contains your bot**
  If your other attachment specifies a file name without a folder name, AppSheet looks for the file within the folder containing your bot. If your other attachment specifies both folder and file names, AppSheet looks for the folder and file path within the folder containing your bot.
- **Default folder path**
  Define the default folder path by navigating to **My Account \> Settings \> App Creator Settings** and updating the **Default folder path** property. For example, if the default folder path is `Files` and the filename is `MyFileName.pdf`, the path is: `Files/MyFileName.pdf`

  If the other attachment specified a folder path, include it in the value. For example: `Files/`**`MyFolderPath`**`/MyFileName.pdf`

Files that you create using the **Create a new file** task will be saved to the default folder path. For example, if the default folder path is `Files` and the filename is `MyFileName.pdf`, the path is: `Files/MyFileName.pdf`

If the **Create a new file** task specified a **File Folder Path**, include it in the value. For example: `Files/`**`MyFolderPath`**`/MyFileName.pdf`

**Authentication providers that cannot store files**

For SQL Server, MySQL, SmartSheet, and other authentication providers that cannot store files, AppSheet locates other attachment files in the main cloud file system associated with the app creator's primary AppSheet account, such as Google Drive, Dropbox, Office 365, or Box.

Define the default folder path by navigating to **My Account \> Settings \> App Creator Settings** and updating the **Default folder path** property.

For example, if the default folder path is `Files` and the filename is `MyFileName.pdf`, the path is: `Files/MyFileName.pdf`

If the other attachment specified a folder path, include it in the value. For example: `Files/`**`MyFolderPath`**`/MyFileName.pdf`

### Restrict the other attachment files in your app

Restrict the other attachment files that users can add to your app, as follows:

1.  Create an [EnumList](https://support.google.com/appsheet/answer/10107878) field containing the names of the other attachments your app user can add to your app. For example, create an EnumList field named **Attachments** and define the following values: **PDF1**, **PDF2**, and **PDF3**.
2.  When configuring an email, specify the following expression in the **Other Attachments** property:`LIST(IF(CONTAINS([Attachments], "PDF1"),"PDF1.pdf","")) + LIST(IF(CONTAINS([Attachments], "PDF2"),"PDF2.pdf","")) + LIST(IF(CONTAINS([Attachments], "PDF3"),"PDF3.pdf",""))`

### Secure other attachment files

Your other attachment files must be secured properly in order for AppSheet to retrieve them. Normally, you must secure your other attachment files so that the app owner can read them as the app is running under the identity of the app owner.

In the rare case when your app is using a private table, you must secure your other attachment files so that the current app user can read them. This is necessary because when private tables are used, the app is running under the identity of the app user rather than the app creator. When using private files, AppSheet looks for the other attachments relative to the private user's automation process. As a result, the other attachment files from each private user are unique to that user.

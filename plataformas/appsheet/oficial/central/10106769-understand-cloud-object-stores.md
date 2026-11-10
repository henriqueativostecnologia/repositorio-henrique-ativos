---
fonte: https://support.google.com/appsheet/answer/10106769?hl=en
baixado: 2026-11-10
---

# Understand cloud object stores

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

Learn how to use cloud object stores to store data:

- [Store image and file data](#store)
- [Archive automation attachments](#archive)
- [Supported cloud object stores](#supported)

## Store image and file data

Tables that contain `Image` or `File` column types must always have a place where the image or file data is written. When the image or file data is added or updated, the image or file data is written to a new file which is given a unique name. The file name contains the table and column name and a suffix which is append to the file name to make it unique. This file name is then stored in the image or file column.

When the `Image` or `File` column is referenced, AppSheet retrieves the image or file data using the file name stored in the image or file column.

By default, the files containing the image and file data are written to the table data source. The image and data files are written to a folder which is adjacent to the table data file.

If the table data source is a Google Sheet, the image and file data is stored on Google Drive in a folder that is collocated with the Google Sheet.

If the table data source is an Excel worksheet, the image and file data is stored in a folder on the storage device where the Excel worksheet resides. If the Excel worksheet resides on Office 365, the image and file data will be stored in a folder that is collocated with the Excel worksheet on OneDrive. If the Excel worksheet resides on Dropbox, the image and file data will be stored in a folder that is collocated with the Excel worksheet on Dropbox. If the Excel worksheet resides on Google Drive, the image and file data will be stored in a folder that is collocated with the Excel worksheet on Google Drive. The same is true for Excel worksheets stored on Box, or any other data sources that is capable of storing files.

If the table data source is a database, the default image or file storage location is the cloud file system used to create the app owner's account.

Alternatively, tables that contain `Image` or `File` column types can write and read the image and file data to a cloud object store.

## Archive automation attachments

Automation bots can create attachment files such as PDF, HTML, JSON, or XML files. You can choose to [archive](https://support.google.com/appsheet/answer/11538747) [](https://help.appsheet.com/en/articles/2744751-email-attachment-file-archiving) these newly created attachment files. By default, the archived attachment files are written to the default application folder. Alternatively, attachment files can be archived to a cloud object store.

## Supported cloud object stores

AppSheet currently supports the following cloud object stores:

- [Google Cloud Storage (GCS)](https://support.google.com/appsheet/answer/10106382)
- [Amazon Web Services S3 (AWS S3)](https://support.google.com/appsheet/answer/10106679)
- [Relational Databases](https://support.google.com/appsheet/answer/10106513)

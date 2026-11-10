---
fonte: https://support.google.com/appsheet/answer/11447601?hl=en
baixado: 2026-11-10
---

# Overview of document processing

AppSheet Automation can extract and validate content from documents, like invoices and receipts, using Google Cloud's state-of-the-art Document AI. 

## Watch a demo

Learn about intelligent document processing with AppSheet Automation.** **

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=4vy-c8TzjWQ

## Document processing tasks

AppSheet supports the following document processing tasks:

|                                                                                                   |                                                                                                    |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| **Tasks**                                                                                         | **Description**                                                                                    |
| [Extract content from documents in a folder](https://support.google.com/appsheet/answer/11447806) | Extract content from documents, such as PDF or image files, using AppSheet document parsing.       |
| [Compile folder contents](https://support.google.com/appsheet/answer/11448004)                    | Collect a list of files and metadata from a folder in Google Drive to use within your application. |

## About the folder data source

The *folder data source* can be either **implicitly** used as part of document parsing and extraction or **explicitly** used as the data source for collecting folder contents. For example, a "user manual view" in an application can explicitly use a Google Drive folder data source containing documents that can be viewed, updated, added, or deleted within an application.

Folders are fixed schema tables, where the attributes (table columns) are the properties of files (such as name, size, last modified at, and so on) for generic files or document-specific content (for example, invoices, receipts, or w9 forms), and the entries (table rows) are the files themselves. In this release, if a folder is specified as a particular document type each folder should contain files of the same document type, although the files can vary in mime and extension type.

**Note:** Supported extensions include `.tiff`, `.gif`, `.pdf`, `.jpg`, and `.png`. Folders containing mixed document types can be used for document viewing and uploading inside applications, but cannot be automatically extracted.

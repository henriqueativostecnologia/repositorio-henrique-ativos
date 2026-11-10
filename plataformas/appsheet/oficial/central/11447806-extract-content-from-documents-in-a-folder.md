---
fonte: https://support.google.com/appsheet/answer/11447806?hl=en
baixado: 2026-11-10
---

# Extract content from documents in a folder

Extract content from documents, such as PDF or image files, using AppSheet document parsing as described to the following sections:

- [What is document parsing?](#what-is)
- [Use document parsing](#use)

See also [Overview of document processing](https://support.google.com/appsheet/answer/11447601).

## What is document parsing?

*Document parsing* with AppSheet enables you to extract content from documents using Google’s Document AI solution.

You can parse the following **document types**:

- Invoices
- Receipts
- W-9 forms

The documents can be saved using one of the following **file formats**: PDF, GIF, PNG, JPEG, and TIFF.

AppSheet automation extracts a document's content based on the *document type*, regardless of MIME type or extension type (such as, `.pdf`, `.docs`, `.png`). If a document in the folder is not of the specified type or format, it will not be processed.

**Notes**:

- AppSheet only supports parsing documents stored on Google Drive.
- Additional document types and formats will be supported as Google's Document AI solution supports them.

### How AppSheet measures extraction confidence

In some cases, source documents may have defects that result in extraction accuracy that is less than 100%. For example, some documents may be based on scanned sources, utilize complex images, use unusual fonts, or have spelling errors or omissions.

The extraction service includes an *extraction confidence* score that is used by the automation process to determine if the extracted data should be manually reviewed. If the extraction confidence score falls below the configured threshold, an exception flow is triggered to involve manual review by a human. For more information, see [Monitor document parsing](https://support.google.com/appsheet/answer/11447502?hl=en&ref_topic=10105391#monitor-document-parsing).

**Note**: The extraction confidence threshold is not configurable at this time.

### How AppSheet parses monetary content

For documents that include a monetary column, the amount and currency code are extracted into two columns to provide more flexibility for using the extracted data. For example, you might support a centralized repository of documents that span multiple currencies and that allow for customizing downstream processes. Each document is expected to use a single currency; if there appears to be inconsistencies in the extraction, they are flagged.

## Use document parsing

To use document parsing to extract content from documents:

1.  Open the app in the editor.

2.   Go to **Data** and click **+** in the top header of the Data panel.

3.   We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables **and click **+ New Table**.  

4.  Select **Google Drive Documents** in the **Add data from…** dialog.

5.  Under **Documents**, select one of the supported document types: **Invoices**, **Receipts**, or **W-9 forms**.

6.  Navigate to the folder on Google Drive that contains the documents and click **Select**.
    The **Source Invoice Folder** and **Table Name** fields are displayed and populated based on the folder you select.

7.  Click **Change** to edit the **Source Invoice Folder**, as required.

8.  Edit the **Table name**, as required.
    The table name defaults to the folder name.

9.  Click **Create Table**.
    The document tables are created. For invoice and receipt documents, a second table is generated to capture the line items. For more information, see [Table schemas for document parsing](https://support.google.com/appsheet/answer/11448610).

10. Click **View data** in the table header to view the extracted content in your new document table.

Only documents with `SUCCESS` document parsing status will be listed in your app table. Documents that were not successful or registered a [low confidence](#measure-extraction-confidence) level will be logged to the automation monitoring and audit logs. For more information, see [Monitor document parsing](https://support.google.com/appsheet/answer/11447502?hl=en&ref_topic=10105391#monitor-document-parsing).

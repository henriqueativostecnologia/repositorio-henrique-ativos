---
fonte: https://support.google.com/docs/answer/12236443?hl=en
baixado: 2026-11-10
---

# Learn how to optimize your data ingestion

You might need to ingest a large amount of data that includes:

- Values
- Formulas
- Images

To be more efficient, use the best practices below for some common use cases.

## Use Copy & Paste to ingest your data

You can use copy and paste when you ingest a small amount of data. For example, when you ingest a few hundred rows of values or images smaller than 1 MB.

**Tip:** To only paste values from your data without the format or formulas, click **Paste special** and then **Values only**.

## Use Import functions to ingest small amount of dynamic data

These are a family of functions that allow Sheets users to dynamically read data when they’re subject to frequent changes.

#### Import functions & their use cases

[IMPORTRANGE](https://support.google.com/docs/answer/3093340?hl=en&ref_topic=9199554): Imports a range of cells from a specified spreadsheet.
[IMPORTDATA](https://support.google.com/docs/answer/3093335?hl=en&ref_topic=9199554): Imports data at a given URL in .csv or .tsv format.
[IMPORTHTML](https://support.google.com/docs/answer/3093339?hl=en&ref_topic=9199554): Imports data from a table or list within an HTML page.
[IMPORTFEED](https://support.google.com/docs/answer/3093337?hl=en&ref_topic=9199554): Imports an RSS or ATOM feed.
[IMPORTXML](https://support.google.com/docs/answer/3093342): Imports data from any of various structured data types that includes:

- XML
- HTML
- CSV
- TSV
- RSS
- ATOM XML feeds

**Tip:** You can [learn more about Import functions](https://support.google.com/docs/answer/12188454).

 

You can use Import functions when your data is dynamic or subject to frequent changes. For example, if the spreadsheet you read from is to record inventory data from another spreadsheet that updates every 2 hours, use Import functions to read the most up-to-date data, as Import functions update the result periodically.

## Use Import or Upload to Drive to ingest data from Excel or other supported files

If you have a lot of data that exists on an Excel file or [other supported file type](https://support.google.com/docs/answer/40608), you can use **File** and then **Import** instead of direct copy and paste. It’s more reliable and faster, especially when you ingest a large amount of data. It also tends to keep as many features as possible from other file types.

In the input dialog, to replace or append data in a sheet, you can select to import files.

1.  Click **File** and then **Import**.
2.  Go to **Upload** and then **Select a file from your device**.
3.  Select your file.
4.  Select an **Import location**.
5.  Select a **Separator type**.
6.  Click **Import data**.

You can also use Google Drive to upload your Excel file.

1.  Open your **Google Drive**.
2.  Click **New** and then **File upload**.
3.  Select your Excel file.
4.  Click **Upload**.

### Import datasets with Connected Sheets

If you have a large .csv file to import into Sheets or to upload from Drive, you can also choose to import the file to BigQuery directly from Sheets and continue your analysis using Connected Sheets. This allows users to open .csv files of any size and analyze them using familiar Sheets tools.

**Tip:** If you import into Sheets or upload from Drive and get the message “This file is too large to import directly into Google Sheets,” use Connected Sheets.

To import a file through Connected Sheets:

1.  Open the file.
2.  In the menu at the top, click **Data** and then **Data connectors** and then **Connect to BigQuery**.
3.  Under “Select Google Cloud project,” search for your project.
4.  Enter a name for your table.
5.  Click **Continue**.
    - A pop-up shows after the file is uploaded.
6.  To check your file, in the pop-up, click **Open file**.

## Use Insert Image to ingest large images

**Important:** Cells with an image can’t contain text.

If you have a large image to ingest, you can use Insert Image instead of Copy and Paste.

1.  To insert an image in Google Sheets, click the cell you want.
2.  Click **Insert** and then **Image**.
3.  Select an option:
    - **Insert image in cell**
    - **Insert image over cells**
4.  Select an image or take a screenshot.
5.  Click **Open** or **Select**.

## Use Copy to transfer a large amount of data from one Google sheet to another

When you have a lot of data from another Google sheet that‘s static and not subject to changes, you can copy spreadsheets.

1.  On the bottom, next to the sheet's name, click Down arrow Down arrow and then **Copy to**.
2.  Select an option:
    - To create a new spreadsheet with a copy of the data, click **New spreadsheet**.
    - To select another spreadsheet to copy the sheet into, click **Existing spreadsheet**.

## Use Google Apps Script to create your own data ingestion functions

To create your own functions with more flexibility to ingest data, use [Google Apps Script](https://developers.google.com/apps-script/overview#try_a_quickstart).

## Use Google Sheets API with your programming language

If you’re a developer or user who wants to use your preferred programming language to write and read Google Sheets data with more complex logic, use the [Google Sheets API](https://developers.google.com/sheets/api).

## Use Connected Sheets when your data lives in BigQuery

If your data lives in BigQuery, to ingest data to Google Sheets, use [Connected Sheets](https://support.google.com/docs/answer/9702507?hl=en&ref_topic=9699960).

## Import Google Forms data into Google Sheets

Google Forms and Google Sheets also support a seamless experience that makes it easier to ingest data from Forms into Sheets. It automatically generates a spreadsheet that updates your response. [Learn more about linked spreadsheets with Google Forms](https://support.google.com/docs/answer/2917686?hl=en#zippy=%2Cchoose-where-to-store-responses).

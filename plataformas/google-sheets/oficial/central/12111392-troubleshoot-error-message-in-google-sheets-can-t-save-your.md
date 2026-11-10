---
fonte: https://support.google.com/docs/answer/12111392?hl=en
baixado: 2026-11-10
---

# Troubleshoot error message in Google Sheets: “Can't save your changes. Please copy your recent edits then revert your changes.”

If you encounter this message in Google Sheets, “Can't save your changes. Please copy your recent edits, then revert your changes,” it's because it took too long for the server to save your changes. Here are some suggestions to resume your progress.

## Internet connection issues

#### Copy your changes and reload

A glitch in your internet connection may trigger this error message. To restore your connection, try these steps:

1.  Copy all your unsaved changes.
2.  Reload the sheet.
3.  Paste in your previous changes.
4.  If the error shows up again, disconnect from your internet and then reconnect.

## Turn on Offline mode on your Chrome or Microsoft Edge browser 

To continue your work, you can switch to Offline mode. Offline mode saves your work locally on your device. All your local changes will be uploaded to the Cloud when your device restores a stable internet connection. [Learn more about how to turn on Offline mode](https://support.google.com/drive/answer/2375012?hl=en&co=GENIE.Platform%3DDesktop). 

## Input a large amount of data or images

#### Use the Import functions to import a large amount of data

When you input a large amount of data, instead of copy and paste, use the more effective and reliable Import functions. Google Sheets provides a wide range of Import functions that support various import needs.

- [IMPORTRANGE](https://support.google.com/docs/answer/3093340?hl=en&ref_topic=9199554) - Imports a range of cells from a specified spreadsheet.
- [IMPORTDATA](https://support.google.com/docs/answer/3093335?hl=en&ref_topic=9199554) - Imports data at a given url in .csv or .tsv format.
- [IMPORTHTML](https://support.google.com/docs/answer/3093339?hl=en&ref_topic=9199554) - Imports data from a table or list within an HTML page.
- [IMPORTFEED](https://support.google.com/docs/answer/3093337?hl=en&ref_topic=9199554) - Imports a RSS or ATOM feed.

**Important:** These Import functions cannot be used to import Excel files. [Learn more about how to work with Excel files in Google Sheets](https://support.google.com/docs/answer/9331167?hl=en#2.1).

#### Import your Excel file to Google Drive instead of direct copy & paste

If you copy and paste directly from an Excel file to a Google spreadsheet, you may also encounter the error. We suggest you import your Excel file in the following way:

1.  In [Sheets](https://sheets.google.com/), create a new or open an existing spreadsheet.
2.  Click **File** and then ** Import**.
3.  Choose the Excel file.
4.  Click **Select**.
5.  Choose an import option:
    - Create new spreadsheet
    - Insert new sheet(s)
    - Replace spreadsheet
6.  Click **Import data**.
7.  If prompted, click **Open now**.

[Learn more about how to work with Excel files in Google Sheets](https://support.google.com/docs/answer/9331167?hl=en#2.1). 

#### Use Insert Image to import images instead of direct copy & paste

To import images, use "Insert Image" as a more effective way to copy and paste images.

If you tried to paste images into Sheets and triggered the error message, try these steps:

1.  Revert your change.
2.  Reload the sheet.
3.  Click the cell where you want to add an image.
4.  Click **Insert** and then  **Image**. 
5.  Choose whether to place your image in the cell or over the cells.
    - Cells with an image can’t also contain text.
6.  Choose an image or take a snapshot.
7.  Click **Open** or **Select**.

#### Do not exceed Sheets limits

When your input data exceeds Sheets limits, it could trigger this error message. [Learn more about limits in Google Sheets](https://support.google.com/drive/answer/37603?hl=en). 

 

If you encounter a different error message such as, "Something went wrong. Reload" or "Unable to load file," [learn more about troubleshooting Sheets errors](https://support.google.com/docs/answer/7505592).

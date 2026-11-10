---
fonte: https://support.google.com/appsheet/answer/10105404?hl=en
baixado: 2026-11-10
---

# Issues with Google Drive

Learn how to resolve problems with Google Drive.

## 403 or 404 Errors

Users of Google Drive can sometimes see Error 403 (permission denied) or Error 404 (not found). There are a few common reasons for this:

1.  You may have inadvertently deleted the Google worksheet. You can recover the deleted Google worksheet as described in [Recover a deleted Google file or worksheet](https://support.google.com/appsheet/answer/10105007). 
2.  You are not the owner of the document but this is a shared document owned by a different Google account. Check your document sharing permissions on Google.
3.  You have multiple Google accounts (let's call them Acct1 and Acct2): your spreadsheet is owned by Acct1 but you sign into AppSheet using Acct2 to access the spreadsheet. Either use the same account or share the document across accounts. 
4.  You had access to the file at one point, but the access has been removed.
5.  This can sometimes occur if you have a corporate Google Docs account that has an admin policy that prohibits all users from enabling third-party software like AppSheet (so you may need to talk to your account admin).

See also [Share files from Google Drive](https://support.google.com/drive/answer/2494822).

## Google AppScript onEdit Triggers

If you use one of the AppSheet add-ons to integrate with Google Forms, Sheets, or Docs, see [Use data from Google Sheets](https://support.google.com/appsheet/answer/10106594) to learn more about specific limitations on those integrations. 

In particular, if you utilize Google AppScript onEdit triggers on your Google Sheet, or a third-party add on that utilizes these triggers, the triggers are not fired when AppSheet makes a change to the data in the spreadsheet. This is an unfortunate limitation imposed by Google on all third-party solutions like AppSheet. The best workaround is to utilize a timed AppScript trigger (or an onChange trigger) rather than an onEdit trigger.

## Google Sheet filters

Also, do not use filters on your Google Sheets -- it can make the filtered rows invisible to updates. Instead, use filter views (this is a Google Sheets feature that lets each user create and use their own filters without affecting other users of the sheet). See also: [Use data from Google Sheets](https://support.google.com/appsheet/answer/10106594)

## Public Google Sheets

Make certain that your spreadsheet is not marked as **Public**. The Google Sheets API doesn't enable updates against public spreadsheets.

## Google worksheet names exceeding 31 characters in length

Make certain that your Google worksheet names do not exceed 31 characters in length. All characters in the name are counted including blanks and special characters.

## Error: Unable to read spreadsheet: hexadecimal value 0xNN is an invalid character

 When AppSheet attempts to read your Google worksheet you may see an error like the following:

`Unable to read the spreadsheet for '<worksheet name>' due to spreadsheet reader error: '', hexadecimal value 0x0C, is an invalid character. Line 9999, position 999`

The actual hexadecimal value will vary and as will the line and position values. The line and position are not helpful for the reason described below.

AppSheet reads the Google Sheet by asking Google to export the worksheet as an Excel `.xlsx` document. Google converts the Google worksheet into an Excel `.xlsx` document file and returns this `.xlsx` file to AppSheet. AppSheet reads the `.xlsx` file and extracts all of the worksheet cell values, formulas, formatting, and other information from the Excel `.xlsx` document.

An invalid character error occurs when Google fails to export the Google worksheet as a valid Excel `.xlsx` document. Instead, the exported Excel `.xlsx` document contains invalid data that Excel cannot read. The line and position values in the error message are not useful because they refer to a location in the exported Excel `.xlsx` document. There is no easy way to use these values to locate the problem in your worksheet.

You may be able to locate the problem by doing the following:

1.  Open your workbook in Google Sheets.
2.  From the Google Sheets **File** menu select **Download as...** and then select **Microsoft Excel (.xlsx)**. By doing this you are exporting the Google workbook to Excel in the same way that Google Sheets is exporting it to AppSheet.
3.  When the export finishes, you will see the exported `.xlsx` file name at the bottom left of your browser screen. 
4.  Click the **^** character to the right of the `.xlsx` file name and select **Open**. This will open the exported file in Excel. Excel is very likely to report an error when reading the exported file. The Excel error message may help you locate the problem.
5.  Return to Google Sheets and modify your workbook to eliminate the problem.
6.  Repeat the steps above until the you have eliminated the problem. 

Here are some things to check:

- Ensure there are no invalid character values in your worksheet cell values. Invalid character values may be displayed in the form . You can use the Google Sheets search function to locate the invalid character. Open your worksheet in Google Sheet. From the **Edit** menu select **Find and replace ...** Copy into the **Find** box to search for the invalid character.
- One customer reported their problem was caused by an import range function in a cell of their Google worksheet. Replacing the import range with the actual data values eliminated the problem.
- If you discover other causes for this problem, report them to us. We will add your information to this list to help other users.

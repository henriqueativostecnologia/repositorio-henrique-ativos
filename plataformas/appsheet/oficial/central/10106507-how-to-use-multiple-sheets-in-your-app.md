---
fonte: https://support.google.com/appsheet/answer/10106507?hl=en
baixado: 2026-11-10
---

# How to use multiple sheets in your app

With Google Sheets, a **spreadsheet** is a file that contains one or more sheets; a sheet contains cells organized in rows and columns. We use Google Sheets terminology in this article. With Excel, a **workbook** is a file that contains one or more worksheets; a **worksheet** contains cells organized in rows and columns.

A single dataset used by AppSheet is called a [table](https://support.google.com/appsheet/answer/10105821). You can add multiple standalone sheets as AppSheet tables. It's also possible to create AppSheet tables from different sheets within the same spreadsheet.

Either approach works just fine, depending on your circumstances. The performance of the two options may differ based on the specific content. The AppSheet backend has to download the entire spreadsheet file, but if the same file (spreadsheet) is referenced multiple times (from several tables referencing individual sheets), the backend will download it just once. On the other hand, multiple small files can be fetched and processed efficiently in parallel.

In most cases, you should pick whichever approach is most convenient for you to manage. However, if you use only two sheets out of a spreadsheet file with a hundred large sheets in it, you'd be better off splitting them into their own single spreadsheet files.

For more information, see [Add multiple tables](https://support.google.com/appsheet/answer/10105821#add-multiple). You'll need to create a [view](https://support.google.com/appsheet/answer/10106688) pointing to the new table to get that sheet's data to display in the app.

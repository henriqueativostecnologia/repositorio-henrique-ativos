---
fonte: https://support.google.com/appsheet/answer/10106426?hl=en
baixado: 2026-11-10
---

# Use spreadsheets with pivoted data

But what if your data is pivoted with field names down the first column and data entries in the other columns? For example, employee names might be used as column headers and employee attributes might be used as rows. 

AppSheet doesn't work with pivoted data. This is because apps are generated from the column structure of the data. The column structure tells us the "shape" of the data that needs to be processed. This structure needs to stay stable as the app is being used. New data should take the form of new rows, and changes to data should take the form of row edits or row deletes.

Luckily most data can be re-pivoted so that the attributes of each data item form column headers, and the values of each data item are represented in a row. This is very easy to do in a spreadsheet. In Google Sheets or Excel, you first copy the data and then use **Paste Transpose**. Consider an additional spreadsheet with a `SUMIF` or `SUMIFS` sheet formula.

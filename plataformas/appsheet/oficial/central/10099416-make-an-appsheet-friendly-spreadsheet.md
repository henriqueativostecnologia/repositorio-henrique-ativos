---
fonte: https://support.google.com/appsheet/answer/10099416?hl=en
baixado: 2026-11-10
---

# Make an "AppSheet-friendly" spreadsheet

Consider the following when designing your spreadsheet for use with AppSheet.

- **AppSheet uses the first sheet.** When a new app is created from an existing spreadsheet, AppSheet will automatically configure the new app to use only the first sheet in the spreadsheet, even if the spreadsheet contains more than one sheet. Once the app has been created initially, you can configure your app to use [other sheets](https://support.google.com/appsheet/answer/10106507) within the same spreadsheet, sheets in other spreadsheets, or even [other data sources](https://support.google.com/appsheet/answer/10106309) entirely.
- **Avoid special characters in sheet names.** For example, Microsoft Excel prohibits its names from containing these seven special characters: `\` (backslash), `/` (forward slash), `*` (asterisk), `[` (left square bracket), `]` (right square bracket), `:` (colon), and `?` (question mark). Although permitted by AppSheet, it is best to avoid using these special characters in your sheet name.
- **Just header and data**. You could put almost any content in a spreadsheet, including charts, pictures, free form text, and so on. However, if the data isn't obviously tabular, AppSheet might fail to identify it. Ideally, the first row should contain [well-formatted column headers](https://support.google.com/appsheet/answer/10099523), and the remaining rows should contain only data. For maximum app performance, delete blank columns and rows.
- **Use well-formatted column headers and provide a data sample for column type deduction**. When creating a new app, AppSheet will try to deduce the [column types](https://support.google.com/appsheet/answer/10106435) of your data by considering the [well-formatted column headers](https://support.google.com/appsheet/answer/10099523) and any existing data.
- **Use spreadsheet data validation rules where appropriate**, as described in the article about [drop-downs from spreadsheet validation rules](https://support.google.com/appsheet/answer/10107325).
- You can adjust your column structure in the app editor.

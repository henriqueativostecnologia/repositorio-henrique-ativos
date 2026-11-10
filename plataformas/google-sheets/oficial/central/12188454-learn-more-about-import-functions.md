---
fonte: https://support.google.com/docs/answer/12188454?hl=en
baixado: 2026-11-10
---

# Learn more about Import functions

Google Sheets have Import functions to help optimize spreadsheets, such as:

- [IMPORTHTML](https://support.google.com/docs/answer/3093339?hl=en)
- [IMPORTDATA](https://support.google.com/docs/answer/3093335?hl=en)
- [IMPORTFEED](https://support.google.com/docs/answer/3093337?hl=en)
- [IMPORTXML](https://support.google.com/docs/answer/3093342?hl=en)
- [IMPORTRANGE](https://support.google.com/docs/answer/3093340?hl=en)

## Usage Limits

When Import functions create too much traffic, you get this error message: “Error Loading data may take a while because of the large number of requests. Try to reduce the amount of IMPORTHTML, IMPORTDATA, IMPORTFEED, or IMPORTXML functions across spreadsheets you’ve created.”

The creator of the document has strict limits. Users must consider usage across all open documents they create. If a collaborator makes an edit, it may also count against your quota.

To resolve error messages, reduce the amount of changes on the source range from where the Import function imported. For example, if the resolved value for source source range in =IMPORTDATA(source range) changes frequently, you must issue external calls, which may cause a throttle.

## Data Freshness

To ensure users get fresh data while they keep their usage reasonable, IMPORTDATA, IMPORTHTML, and IMPORTXML share some rules:

- All three functions automatically check for updates every hour while the document is open, even if the formula and sheet don’t change.
- If you delete and re-add cells or overwrite the cells with the same formula, it triggers a refresh of the functions.

**Importan**t: If you open and refresh the document, it won’t trigger a refresh on any of the functions.

## Volatility

When you use an Import function, you may get an in-cell “#ERROR!” with the message: “Error: This function is not allowed to reference a cell with NOW(), RAND(), RANDARRAY(), or RANDBETWEEN()”.

Import functions cannot directly or indirectly reference a volatile function such as NOW, RAND, or RANDBETWEEN to prevent an overload in our users' spreadsheet because these volatile functions update frequently.

If you get the above error message, but still want to read results of the volatile functions, copy the result of the volatile functions. Use **Paste special** and then **Values only**.

**Important:** If you take these steps, it makes all values static. For example, if you copy and **Paste special** NOW results as values, the values you paste no longer change based on your time.

**Tip**: The only exception is made for the TODAY function, which is volatile but doesn't update more than one time per day.

## Error message: “Result too large”

For IMPORTXML, if you get this error message, reduce the amount of data that your [XPATH query returns](https://www.w3schools.com/xml/xpath_intro.asp).

## Error message: "Admin has not allowed imports from..."

If you get this error message, contact your admin to allow imports from this URL.

## User Notifications

If an IMPORT function is added or edited for the first time in a Sheet for the following functions, a warning banner will appear as the sheet will be able to send and receive data to external parties.

- IMPORTHTML
- IMPORTXML
- IMPORTFEED
- IMPORTDATA
- IMAGE

To allow access, editors of the spreadsheet can click **Allow access**

## Error message: "Please use a desktop web browser to allow access to fetch data from external urls."

If you get this error, you can either switch to a desktop web browser to allow access to IMPORT functions, or follow the steps here:

1.  Paste the spreadsheet URL in Chrome browser
2.  Select an option:
    - For **iPhone & iPad**: Tap **More** More and then **Request Mobile Site**
    - For **Android**: Tap **More** More and then **Desktop site**
3.  Click **Allow access**

### **Notification behaviors:**

- This notification will be triggered once per Sheet, but only editors can act on it. Once an editor takes action, the notification is dismissed and will not be shown to other collaborators.
- All existing IMPORTs on the page will be blocked until **Allow access** is clicked
- The user will not be able to revoke access after accepting it, unless they use Version history. In [*Version history*](https://support.google.com/drive/answer/2409045?hl=en&co=GENIE.Platform%3DAndroid) revert to a version prior to the notification appearing, then re-add or re-edit the IMPORT. The notification will re-appear . You can then remove all `IMPORTHTML(), IMPORTXML(), IMPORTFEED(), IMPORTDATA(), `or `IMAGE()` functions in the spreadsheet.

## Related resources

- [IMPORTFEED](https://support.google.com/docs/answer/3093337?hl=en)
- [IMPORTXML](https://support.google.com/docs/answer/3093342?hl=en)
- [IMPORTHTML](https://support.google.com/docs/answer/3093339?hl=en)
- [IMPORTDATA](https://support.google.com/docs/answer/3093335?hl=en)
- [IMPORTRANGE](https://support.google.com/docs/answer/3093340?hl=en)
- [IMAGE](https://support.google.com/docs/answer/3093333)

---
fonte: https://support.google.com/appsheet/answer/11494252?hl=en
baixado: 2026-11-10
---

# Google Sheets having protected sheets or protected ranges

Google Sheets allows you to protect the contents of your Google worksheet using protected sheets and ranges, as described in [Protected content in Sheets](https://support.google.com/a/users/answer/9308980).

Appsheet is not aware of and does nothing special for Google Sheets having protected sheets or ranges.

1.  Appsheet is not aware of the presence of protected sheets or ranges in your Google worksheets.
2.  Appsheet does nothing to enforce the rules defined for the protected sheets or ranges in your worksheets. Google Sheets does all such enforcement.
3.  Appsheet always updates entire rows of a worksheet. It does nothing to avoid updating cells contained in a protected range. For example, if your worksheet contains five cells per row of which two are in a protected range, Appsheet will update all five cells. This may lead to update errors as described below.

### Update errors for worksheets having protected ranges

Appsheet may encounter update errors if your Google worksheet contains a protected range depending on how you set the permissions of that protected range and how you set the [Access mode](https://support.google.com/appsheet/answer/10105756) in your Appsheet application.

We recommend that you set **Access mode** to **as app creator** and define all protected ranges in your Google worksheet to allow update by the app creator. This will ensure that Appsheet can update your worksheet regardless of which of your users makes updates through your application. In this case, Appsheet performs all updates under the identity of the app creator and the protected ranges in your Google worksheet will permit those updates. You can use the [Editable if](https://support.google.com/appsheet/answer/10099520) feature of Appsheet to control which fields your users can update.

If you set **Access mode** to **as app user**, you may encounter update errors when your user makes a update through your Appsheet application. This may occur when Appsheet attempts to apply the change to your worksheet by updating all cells in the affected worksheet row. An update error will occur if the affected row contains one or more cells in a protected range and that user does not have permission to update those cells. This will occur even if the user is only updating values outside the protected range because Appsheet updates the entire row.

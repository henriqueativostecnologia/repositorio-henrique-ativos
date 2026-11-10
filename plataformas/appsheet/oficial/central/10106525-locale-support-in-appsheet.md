---
fonte: https://support.google.com/appsheet/answer/10106525?hl=en
baixado: 2026-11-10
---

# Locale support in AppSheet

The following sections summarize the locale support in AppSheet:

- [Locale for Google Sheets](#google-sheets)
- [Locale for AppSheet ](#appsheet-data)
- [Configure the locale](#configure)
- [About the compatibility locale](#compatibility-locale)
- [Locale for Excel](#excel)
- [Locale for Smartsheet](#smartsheet)

## Locale for Google Sheets

The Google Sheets **Locale** setting controls how `Date`, `DateTime`, `Decimal`, `Percent`, `Price` (`Currency`), and `Time` values are entered into Google Sheets. See [Set a spreadsheet's location and calculation settings](https://support.google.com/docs/answer/58515).

For `Date` value, when the Google Sheets Locale is **United States**, dates are normally entered in `MM/DD/YYYY` format. Conversely, when the Google Sheets Locale is **United Kingdom**, dates are normally entered in `DD/MM/YYYY` format.

For `Decimal` values, when the Google Sheets Locale is **Japan**, **United Kingdom**, or **United States**, you must enter a period as the decimal separator between the whole and fractional parts of `Decimal`, `Percent`, and `Price` values. Conversely, when the Google Sheets Locale is `Brazil`*,* `France`, or `Germany`, you must enter a comma as the decimal separator.

If your Google Sheet was generated as a response sheet for a Google Form, setting the sheet locale may not automatically apply the new locale formatting to existing columns. To fix this, highlight the column and apply the appropriate formatting from the **Format \> Number** menu in the toolbar.

## Locale for AppSheet

When [configuring table settings](https://support.google.com/appsheet/answer/10105821#configure-table), the AppSheet **Data locale** setting in the **Localization** section controls how AppSheet reads and writes values from Google Sheets. The AppSheet Data Locale must match the Google Sheets Locale. This ensures that your application reads and writes `Date`, `DateTime`, `Decimal`, `Percent`, `Price` (`Currency`), and `Time` values to the Google sheet in the proper locale format.

When you add a new table to your application using the app editor, AppSheet automatically retrieves the Locale setting from the Google worksheet and sets the table's Data Locale setting appropriately.

If you later change the Google Sheets Locale setting, AppSheet automatically retrieves the new setting from the worksheet and sets the table's Data Locale setting appropriately the next time you open the app in the app editor.

**Note**: Data Locale does not impact the Price Currency settings and AppSheet does not provide currency conversions. Data should be entered in your spreadsheet/app according to the currency you would like displayed. See [How to convert from US Dollars to my local Currency](https://support.google.com/appsheet/answer/10107385).

## Configure the locale

To configure the locale:

1.  Make sure that your Google Sheet specifies the appropriate locale. From the Google Sheets **File** menu, select **Spreadsheet settings**. In the **Settings** dialog, set **Locale** to your locale. For example, in Thailand select **Thailand**.

    Spreadsheet settings dialog showing Locale setting under the General tab
2.  Make sure that each `Currency`, `Date`, `DateTime`, `Number`, `Percent`, and `Time` value in the Google Sheet is formatted appropriately. Do this by selecting all of the cells in the column containing the data values. From the `Format` menu, select `Number` and then the appropriate formatting style. For example, for date values, select `Date`, for currency values, select `Currency`, for time values, select `Time`, and so forth. Do this for each `Currency`, `Date`, `DateTime`, `Number`, `Percent`, and `Time` column.
3.  [Add the Google worksheet as a table](https://support.google.com/appsheet/answer/10105821#add) using the app editor. AppSheet will automatically set the table's locale to match the Google worksheet's locale. If you later change the Google worksheet Locale setting, AppSheet will automatically set the table's locale to match the Google worksheet when you next open the application in the editor.

    Data Locale setting for table
     
4.  Make sure that your browser or device is set to use your locale. For example, in the United Kingdom, select the **UK** locale. In Thailand, select the **Thai** locale. The browser or device setting completely determines how data values are displayed within the app running on your browser or device. For information about setting the locale on a Chrome browser, see [Change Chrome languages and translate web pages](https://support.google.com/chrome/answer/173424?hl=en&co=GENIE.Platform%3DDesktop&sjid=12538349331069305486-NA).
5.  If you use a calendar other than the Gregorian calendar, make sure that your browser or device is set to use that calendar. For example, in Thailand, select the **Buddhist** calendar. Many countries use the Gregorian calendar, so in many cases you can skip this step.
6.  Click **Sync** in the app to read the latest values from the Google Sheet. See if the `Date`, `DateTime`, `Decimal`, `Percent`, `Price`, and `Time` values are displayed correctly in the app. If not, verify your browser or device locale settings.
7.  Try updating a `Date`, `DateTime`, `Decimal`, `Percent`, `Price`, and `Time` value and saving the changes to the server. See if the correct values appear in the Google Sheet and the app.
8.  All data is sent between the app and the AppSheet server in a common universal format. This makes it easier for the app and server to communicate. It has no effect on how data is stored in the worksheet or displayed in the client. 

## About the compatibility locale

One of the values appearing in the **Data locale** drop-down is the **Compatibility** locale. This value is present for backward compatibility only. It preserves AppSheet’s old, limited locale behavior. If you choose Compatibility locale, AppSheet uses a period as the decimal separator between the whole and fractional parts of `Decimal`, `Percent`, and `Price` values. AppSheet uses simple rules for saving `Date`, `DateTime`, and `Time` values. We save formulas in the United States locale format, which works for many locales that use a period for the decimal separator.

If your Google Sheet does not specify a Locale, AppSheet sets the AppSheet Data locale to Compatibility locale. However, we strongly recommend you specify a Google Sheet Locale.

We currently support approximately 70 Locale values. We selected these locales based upon the locales that Google Sheets currently supports. [Contact Support](https://www.appsheet.com/Support/Contact) if a locale you need is missing from AppSheet.

## Locale for Excel

It is not necessary to set the AppSheet locale for apps that store data in Excel files on Box, Dropbox, Google Drive, Office 365, or OneDrive. This is a consequence of the way we add and update data and formula values in Excel files. The AppSheet Data locale should be set to either **United States** or **Compatibility**.

## Locale for Smartsheet

It is not necessary to set the AppSheet locale for apps that store data in Smartsheet. This is a consequence of the way AppSheet adds and updates data and formula values in Smartsheet. The AppSheet Data locale should be set to either **English (United States)** or **Compatibility**.

If your app involves workflow rules that send emails or SMS messages, we use the locale of your table/sheet to determine how to format the values (like dates and times) in the message body. In this case, it is important to set the locale of your Smartsheet appropriately.

**Note**: Changing the table's* *Data locale in AppSheet does not retroactively change the format of previous written entries, nor does it affect how values are displayed in the app emulator. What’s displayed in the app emulator is based on the locale settings of your mobile phone or web browser. The table's Data locale setting only affects how data is read and written to the spreadsheet.

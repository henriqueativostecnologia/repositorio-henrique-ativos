---
fonte: https://support.google.com/docs/answer/58515?hl=en
baixado: 2026-11-10
---

# Set a spreadsheet’s location & calculation settings

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

You can change a spreadsheet’s locale, time zone, calculation settings, and functions language in Google Sheets.

When you make a change, it changes for the entire spreadsheet. Everyone working on it will see the changes, regardless of their location.

##### Change locale and time zone

When you change the locale and time zone of a spreadsheet, it changes the spreadsheet’s default currency, date, and number formatting.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/).
2.  Click **File** and then **Settings**.
3.  Under "General," click the "Locale" and "Time zone" menus to change your settings.
4.  Click **Save settings**.

Changing the locale doesn’t change your language settings in Google Sheets. You can set the language in [Google Account settings](https://myaccount.google.com/language).

##### Change the language for functions

You can change the language of Google Sheets functions between English and 21 other languages.

1.  Make sure you’re set to a non-English language in [Google Account settings](https://myaccount.google.com/language).
2.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/).
3.  Click **File** and then **Settings**.
4.  Under "Display language," uncheck "Always use English function names" to see functions in your display language.
5.  Click **Save Settings**.

##### Language options

Google Sheets supports functions in these languages:

- Czech
- Danish
- Dutch
- English
- Estonian
- Finnish
- French
- German
- Hungarian
- Italian
- Japanese
- Malaysian
- Norwegian (Bokmal)
- Polish
- Portuguese (Portugal)
- Portuguese (Brazil)
- Russian
- Slovenian
- Spanish
- Swedish
- Turkish
- Ukrainian

##### Choose how often formulas calculate

When any value in a sheet changes, the change can automatically trigger a recalculation.

For example, if cell A1 = 5, and no other tabs, cells, or formula refers to A1, then when you change the value in A1 from 5 to 7, there’s no recalculation.

However, if other tabs, cells, or formulas refer to A1, then whenever you change A1, a recalculation is automatically triggered. For example, B1 contains the formula =A1+10.

Some functions need to have specific controls in terms of how often we want to trigger a recalculation. For example volatile functions such as TODAY, NOW, RAND, and RANDBETWEEN, because those values inherently change all the time. TODAY changes every new day, NOW changes every second, and RAND and RANDBETWEEN change at an infinite frequency.

This can cause the entire sheet to not work. To choose how often formulas calculate:

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/).
2.  Click **File** and then **Settings** and then **Calculation**.
3.  Under Calculation Mode, select an option:
    - **Automatic** **mode** instructs Sheets to look for and apply changes as soon as you make a spreadsheet action.
    - **Manual mode** only calculates the document when you select **Calculate** at the top of the screen.
4.  Click **Save settings**.

Functions that pull data from outside the spreadsheet recalculate at the following times:

- **ImportRange:** 30 minutes
- **ImportHtml, ImportFeed, ImportData, ImportXml:** 1 hour
- **GoogleFinance:** may be delayed up to 20 minutes

**Tips:**

- Manual calculation is only available for Sheet Editors and is not available in the Sheets mobile app.
- Once activated, at the top, you’ll see a banner which reminds you that Manual Calculation Mode is on.

## Version: Android phone & tablet

You can change a spreadsheet’s locale, time zone, calculation settings, and functions language in Google Sheets.

When you make a change, it changes for the entire spreadsheet. Everyone working on it will see the changes, regardless of their location.

To change your sheet’s location and calculation settings, open it in [Google Sheets](https://docs.google.com/spreadsheets/) on your computer.

## Version: iPhone & iPad

You can change a spreadsheet’s locale, time zone, calculation settings, and functions language in Google Sheets.

When you make a change, it changes for the entire spreadsheet. Everyone working on it will see the changes, regardless of their location.

To change your sheet’s location and calculation settings, open it in [Google Sheets](https://docs.google.com/spreadsheets/) on your computer.

---
fonte: https://support.google.com/appsheet/answer/10106702?hl=en
baixado: 2026-11-10
---

# Considerations for apps using Date, Time, and DateTime formats

If your data includes `Dates`, `Times`, `DateTimes`, or `Timestamps`, there are some special considerations to keep in mind.

- [Date, Time, and DateTime formats in spreadsheets](#spreadsheets)
- [Date, Time, and DateTime formats in apps](#apps)
- [Impact of daylight savings time](#dst)

Some constant values, such as `"MM/DD/YYYY"`, are evaluated as a `Date` value by AppSheet. Similarly, `"000:00:00"` is evaluated as a `Duration` value. This doesn't mean your spreadsheet data must use the same formats: the date and time formats in your spreadsheets are determined by the locale/language setting. Column will always be evaluated as the type of column. Additionally, you can convert data, both columns and string literals, to specific types using functions such as `DATE()`, `TIME()`, or `DATETIME()`. 

## Date, Time, and DateTime formats in spreadsheets

`Date`, `Time`, and `DateTime` formats vary widely across locales. It is important that your worksheet specifies the correct locale and that all your worksheet data cells are formatted correctly, as described in [Locale support in AppSheet](https://support.google.com/appsheet/answer/10106525).

Many spreadsheets use automatic mechanisms to add a timestamp in the first column. A timestamp is generally a poor choice for a key: though it uniquely identifies the row, the timestamp isn't really meaningful to the rest of the app. So if the timestamp is chosen as your key, you may need to change that explicitly.

## Date, Time, and DateTime formats in apps

`Date`, `Time`, and `DateTime` formats are displayed in AppSheet apps based on:

1.  Your mobile device's locale when running your app on a mobile device.
2.  Your browser's language setting when running your app in a browser.

If you are seeing the wrong `Date`, `Time`, and `DateTime` format on your mobile device or browser, make sure your mobile device's locale or your browser's language setting is correct.

To change your language on:

- Android, see [https://support.google.com/accounts/answer/32047?source=gsearch&hl=en](https://support.google.com/accounts/answer/32047?source=gsearch&hl=en)
- iPhone / iPad, see [https://support.apple.com/en-us/HT204031](https://support.apple.com/en-us/HT204031)
- Chrome, see [https://support.google.com/chrome/answer/173424?hl=en](https://support.google.com/chrome/answer/173424?hl=en)

## Impact of daylight savings time

When the AppSheet client sends data to the server, it uses the current daylight savings time. When saving a date that is not in the same daylight savings time period, the saved date will be off by one hour.

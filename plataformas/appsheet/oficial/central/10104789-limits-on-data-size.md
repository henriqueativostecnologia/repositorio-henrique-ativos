---
fonte: https://support.google.com/appsheet/answer/10104789?hl=en
baixado: 2026-11-10
---

# Limits on data size

AppSheet is meant for mobile apps that are designed to work seamlessly despite intermittent connectivity or being completely offline. As a result, all data used by the app must be cached locally on the mobile device. This is an important factor to consider when designing your app. 

Ideally, you should make your data set as small as possible to achieve the desired functionality.

## Actual limits

Do not build an AppSheet app against a huge data set. What is "huge"? For an AppSheet app, the compressed data size limit is **5MB** or **10MB** (depending on the device) for all the data in one app. It is difficult to translate this accurately into a specific number of rows or columns because compressed data size depends on how much repetition there is in the data. For example, a large spreadsheet with a lot of empty cells will probably compress better than a smaller spreadsheet with no empty cells. In general, the fewer cells in the sheet, the better.

External data like images and documents are not included in this data size limit. You can definitely have applications with many rows and an image in every row. Images and documents are not cached locally on the device by default. If you do enable the option to cache images for offline access, they are stored in a different location on the device that does not have the same size limitations.

## Limits on the spreadsheet

Do not exceed **100K** rows or **1000 columns** in your spreadsheet.

Each spreadsheet provider has their own limitations based on performance, file size, number of formulas and calculations. Keep this in mind as you build your app. If you've ever worked in an Excel spreadsheet that uses all the processors in your PC and takes over a minute to refresh because of formulas, then you should expect a similar behavior in your app if it's connected to that spreadsheet. 

If you want to know the limitations by provider, please check the links below:

- Google Drive: [Files you can store in Google Drive](https://support.google.com/drive/answer/37603?hl=en)
- Excel and Office 365: [Excel specifications and limits](https://support.office.com/en-us/article/Excel-specifications-and-limits-ca36e2dc-1f09-4620-b726-67c00b05040f)
- Smartsheet: [Sheet and file size limitations](http://help.smartsheet.com/customer/portal/articles/504531-creating-renaming-sheets)
- Box: [What is the maximum file size I can upload?](https://community.box.com/t5/Managing-Your-Content/What-s-the-maximum-file-size-I-can-upload/ta-p/307) \*
- Dropbox: [Is there a limit or maximum to how big my files can be?](https://www.dropbox.com/en/help/5) \*

\* Excel limitations apply across all cloud providers when you use an Excel file to build your app.

### Performance concerns

In practice today, this is not a meaningful limit because system performance degrades well before you reach the limit. This happens for three reasons:

1.  Slow iterative development-- the data set is checked repeatedly during app development to ensure that the app is consistent with the data.
2.  Long sync times-- when data is synchronized between the device and the backend, the delay depends on the size of the data set. 
3.  Sluggish app behavior-- large data sets can make the app itself sluggish in its interactions like scrolling, search, and so on.

---
fonte: https://support.google.com/docs/answer/3540681?hl=en
baixado: 2026-11-10
---

# Sort & filter your data

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

Want advanced Google Workspace features for your business?

[Try Google Workspace today!](https://workspace.google.com/business/signup/welcome?utm_source=gwslearningcenter&utm_medium=support&utm_campaign=3540681)

You can sort data in alphabetical and numerical order, or use filters to hide data you don't want to find.

Video: https://www.youtube.com/watch?v=zQrPZvednYA

Video: https://www.youtube.com/watch?v=nSo_Ops5o2w

For this same video with audio descriptions: [Sort and Filter Your Data](https://youtu.be/JgMji5ceayc).

To get an example spreadsheet and follow along with the video, click “Make a Copy” below.

[Make a copy](https://docs.google.com/spreadsheets/d/1O0294rwuZ9C3q1wcb4GtRixypUZat_sVtxbcEiy99TM/copy)

### Sort data in alphabetical or numerical order

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  Highlight the group of cells you'd like to sort.
3.  If your sheet includes a header row, [freeze the first row](https://support.google.com/docs/answer/9060449).
4.  Click **Data** and then **Sort range** and then **Advanced range sorting options**.
5.  If your columns have titles, click **Data has header row**.
6.  Select the column you'd like to be sorted first and choose a sorting order.
    - To add another sorting rule, click **Add another sort column**.
7.  Click **Sort**.

##### Sort an entire sheet

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  At the top, right-click the letter of the column you want to sort by.
3.  Click **Sort sheet A to Z** or **Sort sheet Z to A**.

##### Sort by color

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  Select a range of cells.
3.  Click **Data** and then **Create a filter**.
4.  To find the filter options, go to the top of the range and click Filter Filter .
    - **Sort by color:** Choose which text or fill color to filter or sort by. Cells with the color you choose to sort by will move to the top of the range. You can sort by conditional formatting colors, but not alternating colors.
5.  To turn the filter off, click **Data** and then **Remove filter**.

### Filter your data

**Important:**

- When you add a filter, anyone with access to your spreadsheet will find the filter too. Anyone with permission to edit your spreadsheet will be able to change the filter.
- The “Create a filter” option is unavailable under certain conditions. [Learn more about these conditions](https://support.google.com/docs/answer/3540681#filter_unavailability).
- Your filter settings are saved, ensuring consistent filtering even if the data you filter on is removed. To reset filter settings, you can remove the filter from your data range.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).

2.  To create a filter, select an option:

    - Select a range of cells, then click **Data** and then **Create a filter**.
    - Right click on a cell or a range of cells, then click **Create a filter**.

    ##### Learn why ”Create a filter” is unavailable

    The option to “Create a filter” can be unavailable due to:
    - Formatting
      - Check for any merged cells or hidden rows or columns in the sheet. Try to unmerge the cells and unhide the rows or columns.
      - Check for any conditional formatting applied to the sheet.
        1.  Go to **Format**.
        2.  Select **Conditional formatting**.
            - Make sure there are no rules applied.
      - Data validation
        - Check for any data validation rules applied to the sheet.
          1.  Go to Data.
          2.  Select **Data Validation**.
              - Make sure there are no rules applied.
      - If none of the above solutions work, you might not have access. To get access:
        1.  Create a copy of the sheet.
        2.  Check if the filter option is enabled in the copy.
            - If it is, you can use the copy of the sheet instead.

3.  To find the filter options, go to the top of the range and click Filter Filter list .
    - **Filter by condition:** Choose conditions or write your own custom formulas.
      ##### Custom formula examples

      Find unique values within a data range
      - Select **Custom formula is**
      - Type `=COUNTIF(data_range, data_range)=1`

      Find text matching “Good” or “Great” within a data range
      - Select **Custom formula is**
      - Type `=OR(REGEXMATCH(data_range, "Good"), REGEXMATCH(data_range, "Great"))`

      - You can filter cells that have valid or invalid data validation rules.
    - **Filter by values:** To hide data points, uncheck the box next to the data point and click **OK**.
      - To create a filter and filter by cell value, right click on a cell then click **Filter by cell value**.
    - **Search:** Search for data points by typing in the search box.
    - **Filter by color:** Choose which text or fill color to filter by. You can filter by conditional formatting colors, but not alternating colors.

4.  To remove the filter, select an option:
    - Click **Data** and then **Remove filter**.
    - Right click on any cell then click **Remove filter**.

Once filtered, at the bottom right users can find the number of rows being displayed out of the total rows in the table.

**Tip:** Filters also apply to merged cells. [Learn how to merge rows or columns](https://support.google.com/docs/answer/9060449?sjid=8635359179334335214-NA#zippy=%2Cmerge-rows-or-columns).

### Create, save, delete, or share a filter view

**Important**: If you only have permission to view a spreadsheet, you can create a temporary filter view that only you can use. Your filter view won’t be saved.

On a computer, you can filter data so the filtered data only applies to your view of the spreadsheet. Your filter view changes are automatically saved.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  Click **Data** and then **Create filter view**.
3.  Sort and filter the data.
4.  To save your filter view, at the top right, click **Save View**.
5.  Click **Save**.

To delete or duplicate a filter view, at the top right, click Options More and then **Delete view** or **Duplicate view**.

To remove all filters, go to each filter view and click Options More and then **Delete view**.

**Tip:** You can’t change the order of filter views.

##### Find an existing filter view

**Important:** You can only apply one filter view at a time.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  Click **Data** and then **Change view**.
3.  Select a filter view.
4.  Your filter will be applied to the spreadsheet.
5.  To close your filter view, in the top right, click Close Close .

##### Rename a filter view

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  Click **Data** and then **Change view**.
3.  Select a filter view.
4.  At the top left of the sheet, next to "Name", click the filter view name and type the new name.
5.  Press Enter.

##### Share or send a filter view link

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets).
2.  Apply the filter view .
3.  Copy the URL.
4.  Share the filter view link.

### Learn more about filters & filter views

Filters and filter views help you analyze a set of data in a spreadsheet.

You can use filters to:

- Show a specific filter when people open your spreadsheet.
- Sort your data after using a filter.

You can use filter views to:

- Save multiple filters.
- Name your filter.
- Let multiple people find different filter views at the same time.
- Share different filters with people.
- Make a copy or create another view with similar rules.
- Filter or sort a spreadsheet you don't have edit access to. In this case, a temporary filter view will be created.

**Tip:** When you have a formula that points to a cell inside a filtered range, note that sorting the filtered range won't change the formula. For example "=B2" will continue to be "=B2" when B2 is within the filtered range.

 

 

### Related resources

- [Use tables in Google Sheets](https://support.google.com/docs/answer/14239833)
- [Name a range of cells](https://support.google.com/docs/answer/63175)

## Version: Android phone & tablet

Want advanced Google Workspace features for your business?

[Try Google Workspace today!](https://workspace.google.com/business/signup/welcome?utm_source=gwslearningcenter&utm_medium=support&utm_campaign=3540681)

### Sort your data

You can sort columns of cells alphabetically and numerically.

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets).
2.  To select a column, tap a letter at the top.
3.  To open the menu, tap the top of the column again.
4.  Tap More More .
5.  Scroll down and tap **SORT A-Z** or **SORT Z-A**. Your data will be sorted.

### Filter your data

**Tip:** Filter views are only available on desktop.

Filters let you hide data you don't want to find. You can still find all your data when you turn the filter off.

##### Filter by values

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets).
2.  Tap More More and then **Create a filter**.
3.  Look at the column titles to find if filters have been applied:
    - Filter applied filter applied
    - Filter not applied Filter
4.  At the top of the column you want to filter, tap Filter Filter .
5.  The "Sort and filter" menu will open.
6.  Tap Search Search .
7.  Type in the search bar to find a value or scroll up on the list to find the values in the column.
8.  Tap an item to uncheck it and filter it out. The sheet will update automatically.
9.  To select all items, tap **Select all**. To deselect all items, tap **Clear**.

To turn off the filter, tap More More and then **Remove filter**.

##### Filter by condition or color

You can also choose to filter data based on a condition. For example, you can choose to only filter items if the cell starts with a certain letter.

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets).
2.  Tap More More and then **Create a filter**.
3.  At the top of the column you want to filter, tap Filter Filter .
4.  Tap **Filter by condition** or **Filter by color**.
5.  Tap the Down arrow Down Arrow and tap an option.
6.  To save, go to the top left and tap Done Done .
7.  Tap Filter Filter and then **Filter by condition** and then **Remove**.

### Related resources

- [Use tables in Google Sheets](https://support.google.com/docs/answer/14239833)
- [Name a range of cells](https://support.google.com/docs/answer/63175)

## Version: iPhone & iPad

Want advanced Google Workspace features for your business?

[Try Google Workspace today!](https://workspace.google.com/business/signup/welcome?utm_source=gwslearningcenter&utm_medium=support&utm_campaign=3540681)

### Sort your data

You can sort columns of cells alphabetically and numerically.

1.  On your iPhone or iPad, open a spreadsheet in the [Google Sheets app](https://itunes.apple.com/us/app/google-sheets/id842849113?mt%3D8).
2.  To select a column, tap the letter at the top.
3.  Tap the top of the column again to open the menu.
4.  Tap More Right arrow .
5.  Tap **SORT A-Z** or **SORT Z-A**. Your data will be sorted.

### Filter your data

**Tip:** Filter views are only available on desktop.

Filters let you hide data you don't want to find. You can still find all your data when you turn the filter off.

##### Filter by values

1.  On your iPhone or iPad, open a spreadsheet in the [Google Sheets app](https://itunes.apple.com/us/app/google-sheets/id842849113?mt%3D8).
2.  Tap More   and then **Create a filter**.
3.  Look at the column titles to find if filters have been applied:
    - Filter applied filter applied
    - Filter not applied Filter
4.  At the top of the column you want to filter, tap Filter Filter .
5.  The "Sort and filter" menu will open.
6.  Tap Search Search .
7.  Type in the search bar to find a value or scroll up on the list to find the values in the column.
8.  Tap an item to uncheck it and filter it out. The sheet will update automatically.
9.  To select all items, tap **Select all**. To deselect all items, tap **Clear**.

To turn off the filter, tap More   and then  **Remove filter**.

##### Filter by condition or color

You can also choose to filter data based on a condition. For example, you can choose to only filter items if the cell starts with a certain letter.

1.  On your iPhone or iPad, open a spreadsheet in the [Google Sheets app](https://itunes.apple.com/us/app/google-sheets/id842849113?mt%3D8).
2.  Tap More and then **Create a filter**.
3.  At the top of the column you want to filter, tap Filter Filter .
4.  Tap **Filter by condition** or **Filter by color**.
5.  Tap the Down arrow Down Arrow and tap an option.
6.  To save, go to the top left and tap Done Done .
7.  Tap Filter Filter and then **Filter by condition** and then **Remove**.

### Related resources

- [Use tables in Google Sheets](https://support.google.com/docs/answer/14239833)
- [Name a range of cells](https://support.google.com/docs/answer/63175)

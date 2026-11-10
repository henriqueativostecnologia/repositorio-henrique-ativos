---
fonte: https://support.google.com/docs/answer/186103?hl=en
baixado: 2026-11-10
---

# Create an in-cell dropdown list

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

Create dropdown lists in a cell with Google Sheets.

### Create a dropdown list

1.  In Google Sheets, open a spreadsheet.
2.  Select the cell or cells where you want to create a dropdown list.
3.  Select an option:
    - Enter “@.” In the Menu, under the components section, click “**Dropdowns**."
      - **Tip:** You can also insert preset dropdowns for use cases such as "Project status" or "Priority."
    - At the top, click **Insert** and then **Dropdown**.
    - Click **Data** and then **Data validation** and then Add rule .
    - Right click on a cell and then **Dropdown**.
4.  On the Data validation rules panel, under "Criteria," select an option:
    - **Dropdown from a range:** Choose the cells to include in the list.
    - **Dropdown:** Enter the dropdown value.
      - Click **Add another item** to add additional dropdown values.
        - Optional: To allow multiple selections in your drop-down menus, select **Allow multiple selections**.
    - **Tips:**
      - Remove any leading/trailing whitespace in dropdown options to allow multiple dropdown selections.
      - "Allow multiple selections" can only be enabled for chip format dropdowns.
      - On mobile, you currently can't select multiple dropdown options even when multiple selection is enabled.
    - Optional: If you enter data in a cell that doesn’t match an item on the list, it is rejected. If you want people to be able to enter items not from the list:
      1.  Click **Advanced options**.
      2.  Under "If the data is invalid:," select **Show a warning**.
    - Click **Done**.

### Turn dropdown chip suggestions on or off

1.  In Google Sheets, open a spreadsheet.
2.  At the top, click **Tools** and then **Suggestion controls** and then **Enable dropdown chip suggestions**.

### Create a dropdown list on cells with existing data

1.  In Google Sheets, open a spreadsheet.
2.  Select the cell or cells with existing data.
3.  Right-click and then **Dropdown**.
    1.  If a selected cell includes an existing dropdown, other cell values are appended to the selected dropdown list rule.
    2.  Dropdown options are created in the order of ranges that are selected. The order of options goes down columns first, then across rows.
    3.  Optional: To add more dropdown values:
        1.  Go to the Data validation rules panel.
        2.  Under "Criteria," click **Add another item**.
4.  Optional: If you enter data in a cell that doesn’t match an item on the list, it is rejected. If you want people to be able to enter items not from the list:
    1.  Click **Advanced options**.
    2.  Under "If the data is invalid:," select **Show a warning**.
5.  Click **Done**.

### Change or delete a dropdown list

**Important:** If you delete a value with an assigned color from the criteria source range when the dropdown is populated from a range, the value and color will still appear under criteria, but as uneditable. To remove the value from the list, change the source range or any other item’s color.

1.  In Google Sheets, open a spreadsheet.
2.  Select the cell or cells you want to change, then select an option:
    - Click **Data** and then **Data validation**.
    - Click the dropdown and then Edit button .
3.  Edit the dropdown list:
    - To change the options listed, edit the items under "Criteria."
    - To delete a list, select an option:
      - Click **Remove Rule**.
      - If cells are empty, select the cells. Then, press the **Backspace** key.
      - If cells are empty, select the cells. Then, click **Edit** and then **Delete** and then **Values**.
    - To change the display style: Click **Advanced options**. Then, under "Display Style," select either:
      - **Chip**
      - **Arrow**
      - **Plain text**
4.  Click **Done**. If you change the content of the range you select, the changes are made in the list automatically.

## Version: Android phone & tablet

Create dropdown lists in a cell with Google Sheets.

### Create a drop-down list

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Tap the cell or cells where you want to create a drop-down list.
3.  In the top right, tap More More .
4.  Tap **Data Validation**.
5.  Under "Criteria," choose an option:
    - **List of items**: To add an item, tap **+Add** and enter an item. To save an item, tap Done Select .
    - **List from a range**: Enter the cells that will be included in the list.
6.  The cells will have a Down arrow  Down arrow . To remove the arrow, next to "Show dropdown list in cell," turn off the switch On .
7.  If you enter data in a cell that doesn’t match an item on the list, you’ll see a warning. If you want people to only enter items from the list, choose "Reject input" under "On invalid data."
8.  In the top right, tap **Save**. The cells will show a drop-down list.

### Change or delete a drop-down list

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Select the cell or cells you’d like to change.
3.  In the top right, tap More More .
4.  Select **Data Validation**.
    - To change the items listed, go to "Criteria" and edit the items. In the top right, tap **Save**.
    - To delete a list, go to the bottom right and tap **Remove rule**.

**Note: **If you change the contents of the range you've selected, the changes will be made in the list automatically.

## Version: iPhone & iPad

Create dropdown lists in a cell with Google Sheets.

To create and edit drop-down lists, you’ll need to use a computer.

After you create a drop-down list on a computer, you can select an option from the list on your iPhone or iPad.

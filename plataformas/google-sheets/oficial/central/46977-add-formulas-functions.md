---
fonte: https://support.google.com/docs/answer/46977?hl=en
baixado: 2026-11-10
---

# Add formulas & functions

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

Want advanced Google Workspace features for your business?

[Try Google Workspace today!](https://workspace.google.com/business/signup/welcome?utm_source=gwslearningcenter&utm_medium=support&utm_campaign=46977)

You can use functions and formulas to automate calculations in Google Sheets.

**Tip:** If you’re already familiar with functions and formulas and just need to know which ones are available, go to [Google Sheets function reference](https://support.google.com/docs/table/25273).

Video: https://www.youtube.com/watch?v=J-YF5A-w54s

To get an example spreadsheet and follow along with the video, click “Make a Copy” below.

[Make a copy](https://docs.google.com/spreadsheets/d/1O0294rwuZ9C3q1wcb4GtRixypUZat_sVtxbcEiy99TM/copy)

### Use a formula

1.  Open a spreadsheet.
2.  Type an equal sign (**=**) in a cell and type in the function you want to use. 

**Note:** You may see suggested formulas and ranges based on your data.

A function help box will be visible throughout the editing process to provide you with a definition of the function and its syntax, as well as an example for reference. If you need more information, click the “Learn more” link at the bottom of the help box to open a full article.

**Tip:** You might get suggestions to help you complete formulas with the relevant functions. You can accept or reject these suggestions.

To turn formula suggestions on or off, at the top, click **Tools** Next **Suggestion controls** and then **Enable formula suggestions**.

You might find correction suggestions in previously compiled data and analyses, to improve confidence in insights. You can accept or reject these suggestions.

To turn formula corrections on or off, at the top, click **Tools** and then **Suggestion controls** and then **Enable formula corrections**.

 

### Additional features for creating formulas

##### Simple ways to select and edit ranges

#### Range-selection mode

- When editing a formula, the range-selection signal (a grey bracket) will appear next to your cursor where you’re likely to need a range in the formula. When you see the signal, you can move the keyboard arrows around your sheet to select a range.
- Toggle this mode on and off using the keyboard shortcuts **F2** or **Ctrl + e**. If range-selection mode is turned off, use the arrow keys to move your cursor inside the input box instead of selecting a range.
- You can also click within the sheet to select a range when editing a formula.

#### Range replacement

- When you have the text of a range highlighted in your formula, use **F2** or **Ctrl + e** to enter range-selection mode and easily make adjustments to the range.
- If you press **Shift + F2** or **Shift + Ctrl + e** while editing the text of a range, you can easily make adjustments to all occurrences of that range in the formula.

**Tip: **You can also select ranges for your formula that are non-adjacent. To select multiple cells, click and hold **Ctrl** on your keyboard (**Cmd** on a Mac) as you select the cells you want to include in the formula.

#### Formula corrections

If there are errors after you apply a formula to a range, a "Formula correction" box may appear with a suggested fix.

To accept or reject suggestions, you can

- Click Accept  or Dismiss cancel .
- Press **Crtl **+ Enter or **Cmd **+ Return (on a Mac).

To turn Formula correction on or off:

1.  At the top left, click **Tools** and then  **Autocomplete**. 
2.  Click **Enable formula corrections**.   

##### Nested functions

A function used in the same cell with another function is called a nested function. When functions are combined, Google Sheets will calculate the innermost function first. The nested function is contained in parentheses and is used as one of the components of the surrounding function.

For example, let's say you want to calculate the absolute value of a sum of several numbers in the cell range A1:A7. To calculate the sum of these numbers, you would enter '=SUM(A1:A7)' into a cell.

To calculate the absolute value of this sum, you need to nest the sum formula within absolute value formula. To calculate both formulas in a single cell, enter '=ABS(SUM(A1:A7))' into the cell. Note that the =SUM() function is performed first and is used as a component in the =ABS() function.

##### Formula highlighting

When you reference other cells in a formula, those cells will be highlighted in contrasting colors to help you more easily build a formula. When you click on a cell that contains a completed formula, you'll also see these cells highlighted.

##### Change the formula bar size

To make the formula bar bigger or smaller, click the bottom of it, then drag it up or down.

**Note**: You can also use keyboard shortcuts to change the size. Click the formula bar, then click:

- PC: **Ctrl + Up** and **Ctrl + Down** 
- Mac: **Ctrl + Option + Up** and **Ctrl + Option + Down**

##### Functions that don't work

Some functions from other spreadsheet programs don't work in Sheets.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Type                                                                          | Description                                                                   |
+===============================================================================+===============================================================================+
| CALL                                                                          | Calls a dynamic link library or code resource. Since this resource might not  |
|                                                                               | be available on all devices, Sheets doesn’t use this function.                |
|                                                                               |                                                                               |
|                                                                               | **Tip:** You can use [macros](https://support.google.com/docs/answer/7665004) |
|                                                                               | or [Apps Script](https://support.google.com/docs/answer/2942256) instead.     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CUBE functions (CUBEKPIMEMBER, CUBEMEMBER, CUBEMEMBERPROPERTY)                | Lets you use Excel’s CUBE data model.                                         |
|                                                                               |                                                                               |
|                                                                               | **Tip:** If you want to use similar CUBEs, you can use the Data Connectors    |
|                                                                               | feature.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| INFO                                                                          | Returns information about the Sheets document file, such as its filepath.     |
|                                                                               |                                                                               |
|                                                                               | **Note:** Because Sheets emphasizes online collaboration, much of the         |
|                                                                               | information from this method may not be available or the most transparent to  |
|                                                                               | all users.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| REGISTER.ID                                                                   | Gets the registry ID from Windows.                                            |
|                                                                               |                                                                               |
|                                                                               | **Note:** Since Sheets isn’t linked to any one operating system, this         |
|                                                                               | function isn’t supported.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| RTD                                                                           | Gets data from a Component Object Model (COM) Automation server.              |
|                                                                               |                                                                               |
|                                                                               | **Tip:** Since everyone can’t get to the COM server, you can use              |
|                                                                               | [macros](https://support.google.com/docs/answer/7665004) or [Apps             |
|                                                                               | Script](https://support.google.com/docs/answer/2942256).                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| WEBSERVICE                                                                    | Relies on Windows to work fully.                                              |
|                                                                               |                                                                               |
|                                                                               | **Note:** Since Sheets isn’t linked to any one operating system, this         |
|                                                                               | function isn’t supported.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Version: Android phone & tablet

Want advanced Google Workspace features for your business?

[Try Google Workspace today!](https://workspace.google.com/business/signup/welcome?utm_source=gwslearningcenter&utm_medium=support&utm_campaign=46977)

You can use functions and formulas to automate calculations in Google Sheets.

**Tip:** If you’re already familiar with functions and formulas and just need to know which ones are available, go to [Google Sheets function reference](https://support.google.com/docs/table/25273).

### Create a formula

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&hl=en).
2.  Tap the cell where you want to add the formula.
    - To pick from a list of functions, tap Function  Function . Then choose a category and pick the function you want to use in your formula.
    - To enter a function manually, enter `=` and the function you want to use.
    - If the cell already has a formula in it, skip to step 5.
3.  A description of the function will show as you’re working on it to guide you through formula creation.
4.  To use the content of other cells in your formula equation, type the names of the cells into the formula.
5.  Choose from the symbols below the text box to add to the formula. For example, to subtract the contents of one cell from another, tap the **-** **(minus)** symbol.
6.  To finish the formula, tap Done Done .

### Additional features for creating formulas

##### Nested functions

A function used in the same cell with another function is called a nested function. When functions are combined, Google Sheets will calculate the innermost function first. The nested function is contained in parentheses and is used as one of the components of the surrounding function.

For example, let's say you want to calculate the absolute value of a sum of several numbers in the cell range A1:A7. To calculate the sum of these numbers, you would enter '=SUM(A1:A7)' into a cell.

To calculate the absolute value of this sum, you need to nest the sum formula within absolute value formula. To calculate both formulas in a single cell, enter '=ABS(SUM(A1:A7))' into the cell. Note that the =SUM() function is performed first and is used as a component in the =ABS() function.

##### Formula highlighting

When you reference other cells in a formula, those cells will be highlighted in contrasting colors to help you more easily build a formula. When you click on a cell that contains a completed formula, you'll also see these cells highlighted.

### Functions that don't work

Some functions from other spreadsheet programs don't work in Sheets.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Type                                                                          | Description                                                                   |
+===============================================================================+===============================================================================+
| CALL                                                                          | Calls a dynamic link library or code resource. Since this resource might not  |
|                                                                               | be available on all devices, Sheets doesn’t use this function.                |
|                                                                               |                                                                               |
|                                                                               | **Tip:** You can use                                                          |
|                                                                               | [macros](http                                                                 |
|                                                                               | s://support.google.com/docs/answer/7665004?co=GENIE.Platform%3DAndroid&oco=1) |
|                                                                               | or [Apps                                                                      |
|                                                                               | Script](http                                                                  |
|                                                                               | s://support.google.com/docs/answer/2942256?co=GENIE.Platform%3DAndroid&oco=1) |
|                                                                               | instead.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CUBE functions (CUBEKPIMEMBER, CUBEMEMBER, CUBEMEMBERPROPERTY)                | Lets you use Excel’s CUBE data model.                                         |
|                                                                               |                                                                               |
|                                                                               | **Tip:** If you want to use similar CUBEs, you can use the Data Connectors    |
|                                                                               | feature.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| INFO                                                                          | Returns information about the Sheets document file, such as its filepath.     |
|                                                                               |                                                                               |
|                                                                               | **Note:** Because Sheets emphasizes online collaboration, much of the         |
|                                                                               | information from this method may not be available or the most transparent to  |
|                                                                               | all users.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| REGISTER.ID                                                                   | Gets the registry ID from Windows.                                            |
|                                                                               |                                                                               |
|                                                                               | **Note:** Since Sheets isn’t linked to any one operating system, this         |
|                                                                               | function isn’t supported.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| RTD                                                                           | Gets data from a Component Object Model (COM) Automation server.              |
|                                                                               |                                                                               |
|                                                                               | **Tip:** Since everyone can’t get to the COM server, you can use              |
|                                                                               | [macros](http                                                                 |
|                                                                               | s://support.google.com/docs/answer/7665004?co=GENIE.Platform%3DAndroid&oco=1) |
|                                                                               | or [Apps                                                                      |
|                                                                               | Script](https                                                                 |
|                                                                               | ://support.google.com/docs/answer/2942256?co=GENIE.Platform%3DAndroid&oco=1). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| WEBSERVICE                                                                    | Relies on Windows to work fully.                                              |
|                                                                               |                                                                               |
|                                                                               | **Note:** Since Sheets isn’t linked to any one operating system, this         |
|                                                                               | function isn’t supported.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Version: iPhone & iPad

Want advanced Google Workspace features for your business?

[Try Google Workspace today!](https://workspace.google.com/business/signup/welcome?utm_source=gwslearningcenter&utm_medium=support&utm_campaign=46977)

You can use functions and formulas to automate calculations in Google Sheets.

**Tip:** If you’re already familiar with functions and formulas and just need to know which ones are available, go to [Google Sheets function reference](https://support.google.com/docs/table/25273).

### Create a formula

1.  On your iPhone or iPad, open a spreadsheet in the [Google Sheets app](https://itunes.apple.com/us/app/google-sheets/id842849113?mt=8).
2.  Tap the cell where you want to add the formula.
    - To pick from a list of functions, tap Function  Function . Then choose a category and pick the function you want to use in your formula.
    - To enter a function manually, enter `=` and the function you want to use.
    - If the cell already has a formula in it, skip to step 5.
3.  A description of the function will show as you’re working on it to guide you through formula creation.
4.  To use the content of other cells in your formula equation, type the names of the cells into the formula.
5.  Choose from the symbols below the text box to add to the formula. For example, to subtract the contents of one cell from another, tap the **-** **(minus)** symbol.
6.  To finish the formula, tap Done Done .

### Additional features for creating formulas

##### Nested functions

A function used in the same cell with another function is called a nested function. When functions are combined, Google Sheets will calculate the innermost function first. The nested function is contained in parentheses and is used as one of the components of the surrounding function.

For example, let's say you want to calculate the absolute value of a sum of several numbers in the cell range A1:A7. To calculate the sum of these numbers, you would enter '=SUM(A1:A7)' into a cell.

To calculate the absolute value of this sum, you need to nest the sum formula within absolute value formula. To calculate both formulas in a single cell, enter '=ABS(SUM(A1:A7))' into the cell. Note that the =SUM() function is performed first and is used as a component in the =ABS() function.

##### Formula highlighting

When you reference other cells in a formula, those cells will be highlighted in contrasting colors to help you more easily build a formula. When you click on a cell that contains a completed formula, you'll also see these cells highlighted.

### Functions that don't work

Some functions from other spreadsheet programs don't work in Sheets.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Type                                                                          | Description                                                                   |
+===============================================================================+===============================================================================+
| CALL                                                                          | Calls a dynamic link library or code resource. Since this resource might not  |
|                                                                               | be available on all devices, Sheets doesn’t use this function.                |
|                                                                               |                                                                               |
|                                                                               | **Tip:** You can use                                                          |
|                                                                               | [macros](http                                                                 |
|                                                                               | s://support.google.com/docs/answer/7665004?co=GENIE.Platform%3DAndroid&oco=1) |
|                                                                               | or [Apps                                                                      |
|                                                                               | Script](http                                                                  |
|                                                                               | s://support.google.com/docs/answer/2942256?co=GENIE.Platform%3DAndroid&oco=1) |
|                                                                               | instead.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CUBE functions (CUBEKPIMEMBER, CUBEMEMBER, CUBEMEMBERPROPERTY)                | Lets you use Excel’s CUBE data model.                                         |
|                                                                               |                                                                               |
|                                                                               | **Tip:** If you want to use similar CUBEs, you can use the Data Connectors    |
|                                                                               | feature.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| INFO                                                                          | Returns information about the Sheets document file, such as its filepath.     |
|                                                                               |                                                                               |
|                                                                               | **Note:** Because Sheets emphasizes online collaboration, much of the         |
|                                                                               | information from this method may not be available or the most transparent to  |
|                                                                               | all users.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| REGISTER.ID                                                                   | Gets the registry ID from Windows.                                            |
|                                                                               |                                                                               |
|                                                                               | **Note:** Since Sheets isn’t linked to any one operating system, this         |
|                                                                               | function isn’t supported.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| RTD                                                                           | Gets data from a Component Object Model (COM) Automation server.              |
|                                                                               |                                                                               |
|                                                                               | **Tip:** Since everyone can’t get to the COM server, you can use              |
|                                                                               | [macros](http                                                                 |
|                                                                               | s://support.google.com/docs/answer/7665004?co=GENIE.Platform%3DAndroid&oco=1) |
|                                                                               | or [Apps                                                                      |
|                                                                               | Script](https                                                                 |
|                                                                               | ://support.google.com/docs/answer/2942256?co=GENIE.Platform%3DAndroid&oco=1). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| WEBSERVICE                                                                    | Relies on Windows to work fully.                                              |
|                                                                               |                                                                               |
|                                                                               | **Note:** Since Sheets isn’t linked to any one operating system, this         |
|                                                                               | function isn’t supported.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

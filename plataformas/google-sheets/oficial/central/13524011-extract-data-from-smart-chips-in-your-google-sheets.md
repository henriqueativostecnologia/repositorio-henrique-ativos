---
fonte: https://support.google.com/docs/answer/13524011?hl=en
baixado: 2026-11-10
---

# Extract data from smart chips in your Google Sheets

When you [*insert smart chips into a spreadsheet*](https://support.google.com/docs/answer/12319513?sjid=10162500325649056368-NA), you can extract data from the smart chips into separate rows or columns.

1.  On your computer, [open a spreadsheet in Google Sheets](http://sheets.google.com/).
2.  Select a cell with a single chip or a range of cells that each contain a chip.
3.  Choose an option:
    1.  Right click on the cell or cells and then **Data extraction** .

    Dataextraction
    2.  Click **Data** \> **Data extraction** .
4.  Under “Data to extract,” select the data types you want to extract.
5.  Under “Extract to,” select a cell or a range of cells for the extracted data.

## Extract data with syntax

#### Sample Usage

`A2.Location`

`A2.[Creation Time]`

`A2:A4.Title`

#### Syntax

`Cell_or_range.data_type`

- `Cell_or_range`: A cell with one smart chip, or a range of cells each containing a smart chip with the same type.
- `Data_type`: The data type to be extracted from the selected cell or range of cells.

#### **Example**

Input this formula in B2: `=A2.[file name]`

Input this formula in C2: `=A2.[creation time]`

Input this formula in D2: `=A2.[last modified time]`

#### **Result:**

|       |               |                            |                    |                        |
|-------|---------------|----------------------------|--------------------|------------------------|
|       | **A**         | **B**                      | **C**              | **D**                  |
| **1** | **Chip**      | **File Name**              | **Creation Time**  | **Last Modified Time** |
| **2** | \<file chip\> | Sample Chip Extraction Doc | 1/25/2023 13:22:29 | 1/25/2023 13:22:41     |

## Extract data from smart chip

1.  On your computer, [open a spreadsheet in Google Sheets](http://sheets.google.com/).
2.  Hover over a cell with a single chip.
3.  Click **Data extraction** to open a sidebar on the right.
4.  Under “Data to extract,” select the data types you want to extract.
5.  Under “Extract to,” select a cell or a range of cells for the extracted data.

## Refresh extracted data

To refresh extracted data from cells:

1.  On your computer, [open a spreadsheet in Google Sheets](http://sheets.google.com/).
2.  Select a cell with a single chip or a range of cells with each containing a chip.
3.  Right click on a cell and then **Smart chips** and then **Refresh data**.

To refresh extracted data from Data extraction sidebar:

1.  On your computer, [open a spreadsheet in Google Sheets](http://sheets.google.com/).
2.  Select a cell with a single chip or a range of cells with each containing a chip.
3.  Choose an option:
    1.  Right click on the cell or cells and then **Data extraction** .
    2.  Click **Data** \> **Data extraction** .
4.  Click **Refresh & manage**.
5.  Find the smart chips data you want to refresh.
6.  Click Refresh data Refresh

**Tip:** to refresh all smart chips data, click **Refresh all** at the bottom of the sidebar.

## Types of data you can extract

You can extract data from smart chips in your Google Sheets to include information about the following chips:

## People smart chip

Information comes from domain profiles.

- Email
- Name
- Location\*
- Phone\*
- Title\*

**Note:** Information with \* are only available to Google Workspace Business Standard, Business Plus, Enterprise Essentials, Enterprise Standard, Enterprise Plus, Education Fundamentals, Education Plus, Education Standard, and the Teaching and Learning Upgrade users.

## File smart chip

Information comes from your files in Google Drive.

- MIME Type
- URL
- File Name
- Owner\*
- Creation Time\*
- Last Modified By\*
- Last Modified Time\*

**Note:** information with \* are only available to Google Workspace Business Standard, Business Plus, Enterprise Essentials, Enterprise Standard, Enterprise Plus, Education Fundamentals, Education Plus, Education Standard, and the Teaching and Learning Upgrade users.

## Event smart chip

Information comes from events on your calendar.

- URL
- Summary
- Creator\*
- Description\*
- Date/time\*
- Location\*
- Attendees\*

**Note:** information with \* are only available to Google Workspace Business Standard, Business Plus, Enterprise Essentials, Enterprise Standard, Enterprise Plus, Education Fundamentals, Education Plus, Education Standard, and the Teaching and Learning Upgrade users.

**Tip**: Data extraction uses your permissions to access the data. You can extract data into a file that collaborators get, even if they don't have direct access to the original data.

## Related articles

[*Insert smart chips in your Google Sheets*](https://support.google.com/docs/answer/12319513?sjid=10162500325649056368-NA)

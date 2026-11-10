---
fonte: https://support.google.com/appsheet/answer/10104397?hl=en
baixado: 2026-11-10
---

# Issues with Google Sheets formulas

When you create an AppSheet application from Google Sheets, AppSheet does the following.

1.  Asks Google Sheets to export your Google workbook as an Excel `.xlsx `file.
2.  AppSheet uses an Excel library to read the contents of the exported `.xlsx` file. This allows it to extract the cell data values, cell formats, cell formulas, and other values from each worksheet in the exported `.xlsx` file.  
3.  In the case of formulas, AppSheet converts the formulas from `A1` format to `R1C1` format. It is easier for AppSheet to interpret formulas in `R1C1` format. AppSheet can more easily determine if a formula is accessing values in other rows. To learn move about `R1C1` formulas see [A1 versus R1C1 formulas](https://www.google.com/search?rlz=1C1NDCM_enUS827US827&ei=WIzAXKThCKGB0wLMhouQBg&q=A1+vs+R1C1+formulas&oq=A1+vs+R1C1+formulas&gs_l=psy-ab.12...23709.23709..28059...0.0..0.62.62.1......0....1..gws-wiz.......0i71.ZJsLS6ZdIX8).
4.  AppSheet uses all of the information extracted from the worksheet to infer the attributes of each column in the worksheet. AppSheet uses this information to determine the name, type, precision, formula, and other attributes of each field in the table created from the worksheet.
5.  AppSheet does this when you first add a table that is based on a Google Sheet and repeats this each time you click **Regenerate**. 

Fortunately, the vast majority of Google Sheets formulas can be translated into equivalent Microsoft Excel formulas. Unfortunately, some Google Sheets formulas have no Microsoft Excel equivalents. These include:

- `ADD`
- `ARRAYFORMULA`
- `CONCAT`
- `CONTINUE`
- `COUNTUNIQUE`
- `DETECTLANGUAGE`
- `DIVIDE`
- `EQ`
- `FILTER`
- `GOOGLEFINANCE`
- `GOOGLETOURNAMENT`
- `GOOGLETRANSLATE`
- `GT`
- `GTE`
- `IMAGE`
- `IMPORTDATA`
- `IMPORTFEED`
- `IMPORTHTML`
- `IMPORTRANGE`
- `IMPORTXML`
- `JOIN`
- `LT`
- `LTE`
- `MINUS`
- `MULTIPLY`
- `POW`
- `QUERY`
- `SORT`
- `SPARKLINE`
- `SPLIT`
- `UMINUS`
- `UNARY_PERCENT`
- `UPLUS`

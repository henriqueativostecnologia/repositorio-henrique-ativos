---
fonte: https://support.google.com/appsheet/answer/11510988?hl=en
baixado: 2026-11-10
---

# Import a CSV file for this view

The **App: import a CSV file for this view** action uploads the rows in a CSV file through the specified view. You can use this action to:

- Add one or more new records to an AppSheet table.
- Update one or more existing records in an AppSheet table.
- Both add one or more new records to an AppSheet table and update one or more other existing records in an AppSheet table.

Import only works for applications that [require sign-in](https://support.google.com/appsheet/answer/10104975), and only when the app is running in a desktop browser and not when it is running on a iOS or Android device. It is not supported for public applications.

When importing a CSV file, if the timezone is not specified then `UTC+0` is used.

## Invoke an "import a CSV file for this view" action

Once you have created an Import action as described in the sections below, you can invoke it as follows:

1.  Open the application in a desktop browser. 
2.  Navigate to the table view having the Import action.
3.  Click the **Import** button. (If you do not see the **Import** button, you may need to edit the Import action and choose a different **Prominence** on the **Appearance** tab.)
4.  Use the **File Open** dialog which is displayed to select the CSV file you wish to import.
5.  An **Import CSV Started** dialog like the following will be displayed.

    Import CSV file started dialog
6.  When the Import finishes successfully, an **Import CSV Finished** dialog like the following will be displayed.

    Import CSV succeeded dialog
7.  If an error occurs, an **Import CSV Failed** dialog like the following will be displayed. Refer to the Troubleshooting guidelines section below.

    Import CSV failed dialog

## Considerations for the CSV file size

AppSheet imposes a 4-minute time limit when importing a CSV file. We do this to ensure that all users get fair access to the system. Keep this time limit in mind when creating your CSV file.

The following work all counts towards the time limit:

1.  Time to compute initial value expressions and virtual field app formulas.
2.  Time to check and update Change fields.
3.  Time to verify that each field contain a value of the appropriate type.
4.  Time to enforce `Required`, `Required_If`, and `Valid_If` conditions.
5.  Time to add or update the records to the table. This time depends, in part, on which provider the table uses. For SQL providers we batch read and write operations for efficiency.
6.  Time to re-read the added or updated records to obtain after images, if automations are present.
7.  Time to process the automations, if any.

As you can see, the time required to import a CSV file depends on a lot of factors and can be hard to predict. In general, the more rows and columns in the CSV file, the longer the import time. We suggest you start with a batch size of a few hundred to a few thousand records, and experiment to see how long CSV import takes for your table. Then adjust your batch size to stay comfortably within the time limit.

## Create the "import a CSV file for this view" action

Do the following to create an **App: import a CSV file for this view** action:

1.  Open the app in the app editor.
2.  [Configure the table settings](https://support.google.com/appsheet/answer/10105821#configure-table) for the table you wish to import into and ensure both **Adds** and **Updates** are checked for the **Are updates allowed?** property.
3.  Go to **Actions**, click **+ **in the top header of the Actions panel, and click **Create a new action**..
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Behavior \> Actions **and click **+ New Action**.
4.  Give the action a meaningful name by setting the **Action name** property.
5.  Use the **For a record of this table** drop-down to select the table in which the records should be added or updated.
6.  In the **Do this** dropdown select **App: import a CSV file for this view (not a row-level action)**.
7.  Set the **CSV file locale** property as described in [configure the CSV locale](https://support.google.com/appsheet/answer/11512216).
8.  Select a **Position **to control how prominently the Import button is displayed.
9.  Expand the **Display **section.
10. Give the Import button a meaningful name by setting the **Display name** property.
11. Select an **Action icon** for the Import button. You can enter **import** in the search window and hit **Enter** to narrow down the list of icons. One of the icons showing an arrow going into a document is often a good choice.
12. Click **Save**.

## CSV file format

Each row in the CSV file corresponds with a record to be added or updated in the table, except for the first row which must be a header row.

Each column in the CSV file corresponds with a field in the table. The header row contains the field names of the columns in the table. The column names in the CSV header row must exactly match the field names in the table including capitalization. The columns in the CSV file may occur in any order. They need not match the field order of the table.

It is not necessary to include a column in the CSV file for every field in the table. This is explained further below.

## CSV file with unicode data

If your CSV file contains Unicode data, make certain the file is save in Unicode format. For example, on Microsoft Windows you can:

1.  Open the CSV file in **Notepad**.
2.  From the **File** menu select **Save As...**
3.  In the **Encoding** dropdown select any of the UTF values such as **UTF-8** or **UTF-8 with BOM** (Byte Order Mark).
4.  Click **Save**

For example, this is necessary if:

The file contains any of the five French accent marks:

- ç – la cédille (the cedilla)
- é – l'accent aigu (the acute accent)
- â/ê/î/ô/û – l'accent circonflexe (the circumflex)
- à/è/ì/ò/ù – l'accent grave (the grave accent)
- ë/ï/ü – le tréma (the trema)

The file contains Greek, Russian, or Arabic characters.

- [Α](https://en.wikipedia.org/wiki/%CE%91) α, [Β](https://en.wikipedia.org/wiki/%CE%92) β, [Γ](https://en.wikipedia.org/wiki/%CE%93) γ, [Δ](https://en.wikipedia.org/wiki/%CE%94) δ, [Ε](https://en.wikipedia.org/wiki/%CE%95) ε, [Ζ](https://en.wikipedia.org/wiki/%CE%96) ζ, [Η](https://en.wikipedia.org/wiki/%CE%97) η, [Θ](https://en.wikipedia.org/wiki/%CE%98) θ, [Ι](https://en.wikipedia.org/wiki/%CE%99) ι, [Κ](https://en.wikipedia.org/wiki/%CE%9A) κ, [Λ](https://en.wikipedia.org/wiki/%CE%9B) λ, [Μ](https://en.wikipedia.org/wiki/%CE%9C) μ, [Ν](https://en.wikipedia.org/wiki/%CE%9D) ν, [Ξ](https://en.wikipedia.org/wiki/%CE%9E) ξ, [Ο](https://en.wikipedia.org/wiki/%CE%9F) ο, [Π](https://en.wikipedia.org/wiki/Pi_(letter)) π, [Ρ](https://en.wikipedia.org/wiki/%CE%A1) ρ, [Σ](https://en.wikipedia.org/wiki/%CE%A3) σ/ς, [Τ](https://en.wikipedia.org/wiki/%CE%A4) τ, [Υ](https://en.wikipedia.org/wiki/%CE%A5) υ, [Φ](https://en.wikipedia.org/wiki/%CE%A6) φ, [Χ](https://en.wikipedia.org/wiki/%CE%A7) χ, [Ψ](https://en.wikipedia.org/wiki/%CE%A8) ψ, and [Ω](https://en.wikipedia.org/wiki/%CE%A9) ω. (Greek characters)
- А, Б, В, Г, Д, Е, Ё, Ж, З, И, Й, К, Л, М, Н, О, П, Р, С, Т, У, Ф, Х, Ц, Ч, Ш, Щ, Ъ, Ы, Ь, Э, Ю, Я (Russian characters)

The file contains Unicode currency signs such as:

- The Pound Sign £
- The Euro Sign **€**
- The Yen Sign ¥
- The Cent Sign ¢

The file contains Unicode signs such as:

- The Degree Sign °
- The Copyright Sign ©
- The Registered Sign ®

The file contains Fraction signs such as:

- The One Quarter Sign ¼
- The One Half Sign ½
- The Three Quarters Sign ¾

The file contains Unicode superscripts or subscripts.

## Add records

Each CSV Row value must normally include the key field value of the record being added. However, if the key field contains an `Initial value`, you can omit the key field value because the system will initialize the key field to that value. For example, you should omit the key field value when the key field has an `Initial value` of [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) or [`RANDBETWEEN()`](https://support.google.com/appsheet/answer/10107982).

If no CSV column is present for a field of the table, the table field's `Initial value` will be used to give the field a value.

When a record is added:

1.  All fields are initialized to initial values and all app formulas are computed.
2.  The field values you specify in the CSV row are applied.
3.  App formulas are computed and change fields are updated.
4.  `Required`, `Required_If`, and `Valid_If` conditions are enforced.
5.  The record is added to the table.
6.  Automations, if any, are invoked.

## Update records

Each CSV row must specify the key value of a table record to be updated.

The CSV file should contain a column for every updatable field in the table except `Virtual` and `Change` columns. If you include a `Virtual` or `Change` column, the column value you specify will be ignored. If the CSV file omits an updatable column, the field's "`Initial value` is used.

When a record is updated:

1.  All fields are initialized to initial values and all app formulas are computed.
2.  The field values you specify in the CSV row are applied.
3.  App formulas are computed and change fields are updated.
4.  `Required`, `Required_If`, and `Valid_If` conditions are enforced.
5.  The record is updated in the table.
6.  Automations, if any, are invoked.

## CSV row data values

Each column's values must be suitable for its [column type](https://support.google.com/appsheet/answer/10106435).

The value for a `Yes/No` column can be specified in several equivalent ways.
All of the following values are equivalent ways of specifying `TRUE`.
Field values within quotes are case-insensitive. For example, **"TRUE"**, **"True"**, **"true"**, and **"TruE"** are equivalent.

    "MyBool": true
    "MyBool": "True"
    "MyBool": "true"
    "MyBool": "T"
    "MyBool": "t"
    "MyBool": "Yes"
    "MyBool": "yes"
    "MyBool": "Y"
    "MyBool": "y"

All of the following values are equivalent ways of specifying `FALSE`.
Field values within quotes are case insensitive. For example, **"FALSE**, **"False"**, **"false"**, and **"FalsE"** are equivalent.

    "MyBool": false
    "MyBool": "False"
    "MyBool": "false"
    "MyBool": "F"
    "MyBool": "f"
    "MyBool": "No"
    "MyBool": "no"
    "MyBool": "N"
    "MyBool": "n"

## Private tables

CSV Import can be used to import data into [private](https://support.google.com/appsheet/answer/10106508) tables.

The app creator must first create an **App: import a CSV file for this view** action for the private table, as described above.

The app user can then sign in to AppSheet using their account, invoke the application, and invoke the **App: import a CSV file for this view** action as described above. AppSheet will locate the private table belonging to the signed-in user and import the CSV file contents into that private table.

## Troubleshoot

If CSV import fails see [Troubleshoot CSV Import](https://support.google.com/appsheet/answer/11513071).

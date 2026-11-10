---
fonte: https://support.google.com/appsheet/answer/10099523?hl=en
baixado: 2026-11-10
---

# Effective use of column headers

The following sections provide guidance on the effective use of column headers:

- [How AppSheet identifies column headers](#locate-column-headers)
- [How AppSheet infers column types from headers](#infer-column-types)

See also: [Display column headers in table views](https://support.google.com/appsheet/answer/15496439)

## How AppSheet identifies column headers

AppSheet uses the following heuristics to locate your spreadsheet's header row: 

1.  Assumes that rows containing bold text are more likely header rows.
    When all of your data values are bold text, this can mislead AppSheet header detection. In this case, making your header row bold, helps AppSheet find your header row. 
2.  Examines the data value in each cell of the row and tries to determine each cell's data type based on the cell's value.
    If AppSheet determines that the cell's value is one of the known data types, then it can be fairly confident the row contains data and is not a header.
3.  Examines the format value in each cell of the row.
    If the cell's format matches one of the known data types, then AppSheet can be fairly confident the row contains data and is not a header.
4.  Examines the text value in each cell of the row.
    If the cell's text value is a frequently occurring header word like "Name", "Address", "Amount", "Total", and so forth, AppSheet can be fairly confident the row is a header.
5.  Assumes rows that appear closer to the top of the sheet are more likely to be header rows.
    However, people sometimes create multi-row headers where the last header row is actually the most meaningful (or the most specific) header row, so AppSheet attempts to recognize multi-row headers. 

## How AppSheet infers column types from headers

AppSheet infers the types of columns from the column header names as well as from the content of the rows. Especially in cases where there are no existing data rows, it is important to pay attention to the column header names.

There are special words in column headers that AppSheet will use to infer column data types. For example, a column header name Web Site suggests that the data is of the `URL` type. Currently, this only works with English but we intend to add similar capabilities for other languages in the future.

There are a few special cases to be aware of:

- A column header ending with a question mark is inferred as a `Yes/No` data type. 
- A column header ending with an exclamation mark is inferred as an action URL
- A column header whose name is similar to another table already in the app may be inferred as a table `Ref` type. For example, if there is a table called `Products` and a new spreadsheet is added with a column called `Product` or `Products`, AppSheet will infer that it is a `Ref` type.

If you are building an app from a Google Form and your question is marked as `Text`, a similar inference process occurs on the question title.

Here is a complete list of field types, what they do, and the words AppSheet uses to infer the column data type.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Field type**                                     | **Description**                                    | **Words that infer column data type**              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Address`                                          | Full postal address that can be displayed as a map | address, where                                     |
|                                                    | pin on a Google map. The completeness of the       |                                                    |
|                                                    | address will increase the accuracy of the map pin  |                                                    |
|                                                    | location.                                          |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `ChangeCounter`                                    | Numeric counter value reflecting how many times an | N/A                                                |
|                                                    | entry has been changed.                            |                                                    |
|                                                    |                                                    | [Configure                                         |
|                                                    |                                                    | type](ht                                           |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10106509) |
|                                                    |                                                    | in editor                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `ChangeLocation`                                   | Latitude and longitude value reflecting the        | N/A                                                |
|                                                    | current GPS location where an entry has been       |                                                    |
|                                                    | changed.                                           | [Configure                                         |
|                                                    |                                                    | type](ht                                           |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10106509) |
|                                                    |                                                    | in editor                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `ChangeTimestamp`                                  | Date and time value reflecting when an entry has   | N/A                                                |
|                                                    | been changed.                                      |                                                    |
|                                                    |                                                    | [Configure                                         |
|                                                    |                                                    | type](ht                                           |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10106509) |
|                                                    |                                                    | in editor                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Color`                                            | Color value. By default the value can be any one   | blue, green, orange, purple, red, yellow           |
|                                                    | of the standard color values: blue, green, orange, |                                                    |
|                                                    | purple, red, or yellow. You can specify other      |                                                    |
|                                                    | color values when defining the field. You can      |                                                    |
|                                                    | populate the color field using an expression in    |                                                    |
|                                                    | the `InitialValue` or `AppFormula` field. That     |                                                    |
|                                                    | expression can compute the color value based on    |                                                    |
|                                                    | the value of other fields in the record.           |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Date`                                             | Date value that specifies a year, month, and day.  | birthday, dob, day, month, year                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `DateTime`                                         | Date and time value that specifies a year, month,  | date, dates, day, days, month, months, year,       |
|                                                    | day, hour, minute, and second.                     | years, timestamp                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Decimal`                                          | Decimal number with a specified decimal precision. | altitude, altitudes, amount, amounts, amt, amts,   |
|                                                    |                                                    | age, ages, capacity, capacities, depth, depths,    |
|                                                    |                                                    | displacement, displacements, height, heights,      |
|                                                    |                                                    | hours, latitude, latitudes, length, lengths,       |
|                                                    |                                                    | longitude, longitudes,  magnitude, magnitudes,     |
|                                                    |                                                    | mass, masses, population, populations, pop, qty,   |
|                                                    |                                                    | qtys, quantity, quantities, size, sizes, sum,      |
|                                                    |                                                    | sums, total, totals, units, weight, weights,       |
|                                                    |                                                    | width, widths, volume, volumes                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Drawing`                                          | **What it does:** A `Drawing` field contains a     | depiction, diagram, drawing, illustration, layout, |
|                                                    | drawing or notes that you can enter through your   | likeness, rendering, sketch                        |
|                                                    | application. You can choose from a set of seven    |                                                    |
|                                                    | colors when entering the drawing.                  |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Trigger words: **                                |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Duration`                                         | **What it does:** A `Duration` field contains a    | duration, timespan, period, elapse                 |
|                                                    | time duration specified in hours, minutes, and     |                                                    |
|                                                    | seconds.\                                          |                                                    |
|                                                    | **Trigger words:** d                               |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Email`                                            | **What it does:** An `Email` field contains an     | email, e-mail                                      |
|                                                    | email address. You can use the email address to    |                                                    |
|                                                    | send an email.                                     |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Trigger words:**                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Enum`                                             | **What it does:** An `Enum` field contains one     | No trigger words. The field type is determined     |
|                                                    | value from a specified list of values. The list of | automatic if a Data Validation rule was specified  |
|                                                    | values can be obtained in several ways.            | in your sheet; otherwise, you must specify the     |
|                                                    |                                                    | field type in the app editor.                      |
|                                                    | 1.  You can enter the list values manually in the  |                                                    |
|                                                    |     app editor when you define the field.          |                                                    |
|                                                    | 2.  The list values can be obtained from a Data    |                                                    |
|                                                    |     Validation rule you specify in your sheet.     |                                                    |
|                                                    | 3.  The list values can be obtained from another   |                                                    |
|                                                    |     table in your AppSheet application.            |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Trigger words:**                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `EnumList`                                         | One or more values from a specified list of        | N/A                                                |
|                                                    | values. You specify the list of values from which  |                                                    |
|                                                    | the user can pick as described for `Enum` above.   | [Configure                                         |
|                                                    |                                                    | type](ht                                           |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10106509) |
|                                                    |                                                    | in editor                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `File`                                             | Reference to a data file in your cloud drive, such | file, files                                        |
|                                                    | as a PDF or document file, by adding a string      |                                                    |
|                                                    | indicating the location of the file in relation to |                                                    |
|                                                    | the spreadsheet. AppSheet will locate the file and |                                                    |
|                                                    | add a link to it from the app. For example:        |                                                    |
|                                                    | `Reference/guide.pdf`                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Image`                                            | Reference  to an image in `.jpg`, `.png`, or       | image, images, picture, pictures, photograph,      |
|                                                    | `.gif` format. It allows you to capture images     | photographs, photo, photos, figure, figures, fig,  |
|                                                    | from your mobile device's camera or camera roll.   | figs, icon, icons, illustration, illustrations,    |
|                                                    |                                                    | snapshot, snapshots                                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `LatLong`                                          | Latitude and longitude value as                    | latlong, geolocation                               |
|                                                    | `48.5564, -122.3421`. It allows you to capture the |                                                    |
|                                                    | current location from your mobile device's GPS.    |                                                    |
|                                                    | The field value can be displayed as a map pin on   |                                                    |
|                                                    | Google Maps.                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `LongText`                                         | Long multi-line text values.                       | notation, notations, note, notes, desc,            |
|                                                    |                                                    | description, descriptions, comment, comments       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Name`                                             | Name of a person, place, or thing.                 | first, givenname, given-name, last, middle, mi,    |
|                                                    |                                                    | name, names, surname, surnames                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Number`                                           | Positive or negative integer value.                | altitude, altitudes, amount, amounts, amt, amts,   |
|                                                    |                                                    | age, ages, capacity, capacities, depth, depths,    |
|                                                    |                                                    | displacement, displacements, height, heights,      |
|                                                    |                                                    | hours, latitude, latitudes, length, lengths,       |
|                                                    |                                                    | longitude, longitudes,  magnitude, magnitudes,     |
|                                                    |                                                    | mass, masses, population, populations, pop, qty,   |
|                                                    |                                                    | qtys, quantity, quantities, size, sizes, sum,      |
|                                                    |                                                    | sums, total, totals, units, weight, weights,       |
|                                                    |                                                    | width, widths, volume, volumes                     |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Percent`                                          | Percent value with a specified decimal precision.  | %, discount, discounts, interest, percent,         |
|                                                    |                                                    | percentage, chance, percentages, probability,      |
|                                                    |                                                    | probabilities, quota, quotas, split                |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Phone`                                            | Telephone number value. Your application can call  | cell, cellphone, fax, mobile, pager, phone,        |
|                                                    | or text this number.                               | phonenumber, tdd, tel, telephone, telex, tty       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Postal Code`                                      | ZIP code or postal code value. Typically, the      | zip, zipcode, postalcode                           |
|                                                    | postal code is part of a multi-column field        |                                                    |
|                                                    | consisting of a `Street` column, `City` column,    |                                                    |
|                                                    | `State/Province` column, optional `Country`        |                                                    |
|                                                    | column, and a `Postal Code` column. AppSheet       |                                                    |
|                                                    | creates a multi-column `Address` field that        |                                                    |
|                                                    | combines the values from these columns.            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Price`                                            | Decimal number with a specified decimal precision  | amount, amounts, amt, amts, balance, balances,     |
|                                                    | and currency symbol.                               | bonus, bonuses, cash, commission, commissions,     |
|                                                    |                                                    | compensation, contribution, contributions, cost,   |
|                                                    |                                                    | costs,  discount, discounts, dividend, dividends,  |
|                                                    |                                                    | donation, donations, dues, duty, duties, earnings, |
|                                                    |                                                    | excise, expense, expenses, fee, fees, fine, fines, |
|                                                    |                                                    | gain, gains, gross, indemnity, income, levy,       |
|                                                    |                                                    | levies, loss, losses, pay, payment, payments,      |
|                                                    |                                                    | payoff, pension, pledge, pledges, premium,         |
|                                                    |                                                    | premiums, price, prices,  proceeds, profit,        |
|                                                    |                                                    | profits, receipts, reimbursement, reimbursements,  |
|                                                    |                                                    | remittance, remittances, remuneration,             |
|                                                    |                                                    | remunerations, rent, rents, revenue, revenues,     |
|                                                    |                                                    | royality, royalities, salary, salaries, sales,     |
|                                                    |                                                    | stipend, stipends, subtotal, subtotals, tariff,    |
|                                                    |                                                    | tariffs, tax, taxes, tip, tips, tithe, tithes,     |
|                                                    |                                                    | toll, tolls, total, totals, value, values, wage,   |
|                                                    |                                                    | wages, winnings                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Ref`                                              | Reference to a specific record in another table.   | N/A                                                |
|                                                    | When you define the `Ref` field, you specify the   |                                                    |
|                                                    | name of the target table. Each `Ref` field value   | [Configure                                         |
|                                                    | is the key value of a specific record in the       | type](ht                                           |
|                                                    | target table. A `Ref` field is the equivalent of a | tps://support.google.com/appsheet/answer/10106509) |
|                                                    | foreign key field in a relational database.        | in editor                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Signature`                                        | Signature. It allows you to capture a signature on | signature, signatures                              |
|                                                    | your mobile device. Each captured signature is     |                                                    |
|                                                    | saved to its own file on the app creator’s Google  |                                                    |
|                                                    | Drive. The name of this file is stored in the      |                                                    |
|                                                    | `Signature` field.                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Thumbnail`                                        | Small image. It is exactly like an `Image` field   | thumbnail, thumbnails, logo, logos                 |
|                                                    | except the captured images are expected to be      |                                                    |
|                                                    | smaller.                                           |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Time`                                             | Time value that specifies an hour, minute, and     | hour, hours, mins, minute, minutes, second,        |
|                                                    | second.                                            | seconds, secs, time, times                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `URL`                                              | URL value. When an application user clicks the     | site, sites, URL, URLs, web, website, websites     |
|                                                    | field value, the default device browser will load  |                                                    |
|                                                    | the page                                           |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| `Yes/No`                                           | Value of `True`, `False`, or `Not specified`. The  | Starts with "has" or "is" or ends with "?"         |
|                                                    | field value is displayed as `Y` (True), `N`        |                                                    |
|                                                    | (False), or `N/A` (Not specified). A `Yes/No`      |                                                    |
|                                                    | field is the equivalent of a Boolean field in a    |                                                    |
|                                                    | relational database.                               |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

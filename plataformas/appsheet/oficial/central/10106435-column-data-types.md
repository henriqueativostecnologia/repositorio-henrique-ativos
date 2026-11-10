---
fonte: https://support.google.com/appsheet/answer/10106435?hl=en
baixado: 2026-11-10
---

# Column data types

Below is a list of available column data types that you can use when structuring your columns.

See also: [Change a column type](https://support.google.com/appsheet/answer/10106375)

- [Change types](#change)
- [Communication types](#communication)
- [Content types](#content)
- [Enumerated types](#enumerated)
- [Mappable types](#mappable)
- [Numeric types](#numeric)
- [Show types](#show)
- [Temporal types](#temporal)
- [Text types](#text)
- [Other types](#other)

## Change types

Use change types to do the following:

- [Track changes made through an app](#app-change-type): Track counter, location, and timestamp for changes that are made through an app.
- [Track changes made to a row in an AppSheet database](#appsheet-database-change-type): Track the timestamp for changes that are made to a row in an AppSheet database through the AppSheet database editor or the app.

### Track changes made through an app

In some apps, it's important to record a timestamp or increment a counter automatically in a row when changes are made to other columns, and even *values* within the columns, through the app. The following change types are available to track changes made through an app:

- `ChangeCounter`: shows how many times an entry has been edited.
- `ChangeLocation`: will automatically populate with the current GPS location (where the change was made).
- `ChangeTimestamp`: shows when an entry was last edited.
  **Note**: If the app is offline at the time the change is made, `ChangeTimestamp` stores the time of the change, not the time the app is synced.

By default, change types automatically update when *any* other column value changes. However, they can be constrained to react to changes only on specific other columns. Change types can also be constrained to react to changes to certain values.

See [Track app changes using change column types](https://support.google.com/appsheet/answer/10106528).

### Track changes made to a row in an AppSheet database

The `Update row timestamp` column data type specifies the last time data in a row of an AppSheet database was changed through the AppSheet database editor or the app. The value is displayed using the local timezone and is read-only.

The `Update row timestamp` column data type shouldn't be confused with the [`Change Timestamp`](https://support.google.com/appsheet/answer/10106435#change) column type, which tracks changes made through the app only and displays them using the user-specified time zone.

## Communication types

Values of these types can be tapped to launch communication.

- `Email`: an email address, giving you the ability to send emails by clicking the email address. See also [Set up email auto-completion for Email columns](https://support.google.com/appsheet/answer/13604441).
- `Phone`: a phone number, giving you the option to both call and SMS text through the app. AppSheet only automatically recognizes phone numbers in North American format.

## Content types

Values of these types are shown as inline content or open in an external content viewer.

- `Drawing`: creates a drawing pad in the app.
- `File`: any file content (typically used for PDF documents). Capture of files is only supported when running in a browser. In app environments, it is read-only.
- `Image`: `.jpg`, .`png` and `.gif` images. The values may be image URLs or names of files in the source file system of the spreadsheet. See [Display images and documents](https://support.google.com/appsheet/answer/10107317). Images are captured on the device using the camera or from the local camera roll. Optionally, you can [allow users to draw on an image](https://support.google.com/appsheet/answer/10105830#display-image-drawing-tools) when editing a column.
- `Signature`: a user signature. These are captured using a touch-based signature pad and are stored as small inline images in the spreadsheet.
- `Thumbnail`: also models images, but instructs the app to expect small icons and thumbnails. Thumbnails are captured just like images.
- `Video`: `.mpeg` videos and YouTube videos. The values should be publicly accessible URLs of videos. The YouTube embed URL format is also supported. Capture of video is not supported.

## Enumerated types

Columns of these types are constrained to having one of a fixed list of allowed values.

- `Color`: Color code entries in your app with a subset of standard colors: `Black`, `Blue`, `Green`, `Orange`, `Purple`, `Red`, `Yellow`, and `White`.

- `Enum`: Allows the user to select a single value from a list of allowed values. See also: [Drop-downs in forms](https://support.google.com/appsheet/topic/10102053)

- `EnumList`: Identical to `Enum` except it allows the user to select multiple values from a list of allowed values. See also: [Drop-downs in forms](https://support.google.com/appsheet/topic/10102053)

- `List`: Collection of zero or more values; supported for [virtual columns](https://support.google.com/appsheet/answer/10106758) only.

- `Progress`: A system-defined `Enum` that can be used to record the progress for a project. It can be assigned any one of the following values: `Empty`, `Quarter` (or `One Quarter`), `Half`, `Three Quarter` (or `Three Quarters`), and `Full`

  The state of progress is depicted graphically using [Harvey balls](https://en.wikipedia.org/wiki/Harvey_balls).

  The `Progress Enum` type is commonly used for applications based on Smartsheet worksheets. Smartsheet worksheets support a `Progress` column type. When you create an AppSheet application from a Smartsheet worksheet containing a `Progress` column, AppSheet creates a `Progress Enum` type in your AppSheet application that corresponds with the Smartsheet `Progress` column.

  Although, the `Progress Enum` type was originally added to support Smartsheet `Progress` columns. you can include a `Progress Enum` type in any table for any data provider.

  See how the `Progress` function works in the [Marketing Projects](https://www.appsheet.com/Template/AppDef?appName=ProjectManager-2078346&appId=ProjectManager-2078346) sample. 

- `Ref`: are used to create relationships between one record and another. See also: [References between tables](https://support.google.com/appsheet/answer/10106510).

- `Yes/No:` also known as a [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type).

## Mappable types

In the app, values of these types can be seen on a map.

- `Address`: a fully-specified postal or street address.

- `LatLong`: a latitude and longitude (such as `48.5564, -122.3421`). Form fields for this data type can fill in the current location with a single click. For an example of using `LatLong`, see the  [Calculate distances](https://www.appsheet.com/template/showdef?appId=Calculatedistances-71626) sample app.

- `XY`: models a location inside an image, such as a location on a custom map or schematic. `XY` is a comma-separated pair of values, specified without parentheses, that define the X axis and Y axis position within the selected image. For example, `0, 0` corresponds to the top-left corner and `100, 100` the bottom-right corner. You choose the background image by providing a URL in the **Background image for the XY coordinates** setting for the column; this image is then used as the background for the [map view](https://help.appsheet.com/en/articles/961579-working-with-maps) when viewing `XY` column values. The image must be public (anyone with the link can view) for the map to be displayed.

### Simple address field

You can specify a complete address in a single worksheet column.

Include the word "Address" in the column name to help AppSheet identify the address column. For example, you could name the column `Address` or `Customer Address`.

Enter the complete address including the street, city, state, country and postal code values. This helps ensure the address geo-codes correctly.

You can include two or more addresses in the same worksheet. For example, your worksheet might contain a `Billing Address` in one column and a `Shipping Address` in another column.

### Automatically-computed address field

You can store address information in AppSheet by creating adjacent columns in your worksheet and naming them appropriately. When you do this, AppSheet automatically recognizes the adjacent columns form an address.

For example, you can create adjacent columns in your worksheet, and name them `Street`, `City`, `State`, `Country`, `Zip`. In this case, AppSheet will recognize that, taken together, these columns represent an address and it will create a `Computed Address` column that concatenates the values in the component columns.

Do not specify a column name containing the word "Address" in place of "Street". AppSheet interprets any column name containing the word "Address" to mean the column contains an entire address. For example, a column name such as `Street Address` or `Home Address` is assumed to contain an entire address. This will prevent adjacent fields from being recognized as a multi-part address.

If you need two (or more) lines of street information, use `Street1` and `Street2` rather than just `Street`.

You can include an apartment, suite, or unit number in your address by adding a column between `Street` and `City` named `Apartment`, `Apt`, `Suite`, or `Unit`. If you do this, ensure that the data values you enter in this column are legitimate apartment, suite, or unit numbers. These values are included when computing the  geo-coded address. If you enter illegitimate apartment, suite, or unit number values such as "around the back" this may reduce the accuracy of the geo-coded address. 

If you need to store other information with the address, such as "around the back", create a separate column following the address to contain this information. For example, you might call this column `Delivery Notes`.

You may use `Province` in place of `State`.

You can omit `Country`, but this may reduce the accuracy of the geo-coded address.

You may use `PostalCode` or `ZipCode` in place of `Zip`.

You can include two or more addresses in the same worksheet. For example, your worksheet might contain both a `Home Address` and a `Work Address`. AppSheet recognizes the two addresses based upon a combination of naming and adjacency. Keep the `Home Address` columns adjacent to one another and likewise for the `Work Address` columns. Then name the columns to help AppSheet group them appropriately. For example, you might name the adjacent home address columns `Home Street`, `Home City`, `Home State`, `Home Country`, `Home Zip`. You might name the adjacent work address columns `Work Street1`, `Work Street2`, `Work City`, `Work State`, `Work Country`, `Work Zip`. 

You can use this approach to include three or more addresses in your worksheet.

### Manually-computed address field

You can populate an address column by manually combining the values of two or more columns.

1.  In your worksheet create a column and include "Address" in the column's name. For example, you might call the column `Customer Address`.
2.  In the app editor, add the worksheet as a table.
3.  Go to the **Data \> Column Structure** tab. Ensure the `Customer Address` column has a type of `Address`.
4.  Assign the column an app formula such as `CONCATENATE([Calle], ",", [Ciudad], ",", [Estado], ",", [Pais], ",", [Postal])`, where the column names in the [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400) function represent the names of the street, city, state, country, and postal code columns.

## Numeric types

Values of these types can be graphed and used in mathematical operations.

- `Decimal`: a real number; a number with a fractional component; a floating-point number.
- `Number`: a whole number; an integer. Internally, the value is stored as a 54-bit integer, allowing a range of -2^53 to 2^53.
  **Note**: AppSheet databases store `Number` values as 64-bit integers, but AppSheet converts them to 32-bit integer when displayed in an app.
- `Percent`: a `Decimal` value representing a percentage. 0% is stored as `0.00`; 100% is stored as `1.00`.
- `Price`: a `Decimal` representing a currency value.

## Show types

`Show` types are empty columns in your spreadsheet that serve the sole purpose of improving the presentation of data capture forms and detail views. For more information, see [Improve the presentation of detail and form views using Show types](https://support.google.com/appsheet/answer/12463320).

By default, `Show` type columns are only permitted in form views. To include `Show` type columns in detail views, enable **Include Show columns in detail views** on the **UX \> Options** pane in the **Detail View** section.

## Temporal types

These values are shown using the timezone and presentation format of the user's device.

- `Date`: a specific year, month, and day.
- `DateTime`: a specific year, month, day, hour, minute, and second.
- `Duration`: a period of time as a number of hours, minutes, and seconds.
- `Time`: a specific hour, minute, and second without regard to the date.

## Text types

- `LongText`: one or more lines of text.
- `Name`: a `Text` value representing the name of a person or place.
- `Text`: a single line of text.

Available as part of the [Preview Program](https://community.appsheet.com/t/preview-program-for-new-app-features/42388), for data that is typed as `LongText` app creators can choose to render Markdown or HTML in detail views. For more information about how to use this feature and the formatting tags that are supported, see [Rich Text Formatting - in Preview Program](https://www.googlecloudcommunity.com/gc/Announcements/Rich-Text-Formatting-in-Preview-Program/m-p/352427).

## Other types

- `URL`: a web address. There are two parts to a URL value: a hyperlink address like `http://en.wikipedia.org` and an optional hyperlink text like `Click here to visit Wikipedia`. If you wish to specify the hyperlink text value of the URL field, set its **Content** property to a fully qualified URL in the **Data \> Columns** tab of the Editor. To set its display text, change the expression for the **Display** on the attribute.

&nbsp;

- `App`: navigate to another AppSheet app or to navigate to a different view in the current app

- `Multi Column Key`: a composite field representing the combination of multiple fields for the purpose of a key.

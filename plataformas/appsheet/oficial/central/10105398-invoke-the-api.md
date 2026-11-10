---
fonte: https://support.google.com/appsheet/answer/10105398?hl=en
baixado: 2026-11-10
---

# Invoke the API

**Note**: This feature is supported for Enterprise plans only.

Invoke the API as described in the following sections:

- [URL format](#url)
- [Specify the application access key](#app-access-key)
- [HTTP request body](#request-body)
- [API response HTTP status codes](#api-response-http-status-codes)

## URL format

Use a URL in the following form to invoke the API:

`POST https://{appsheet-region}/api/v2/apps/{appId}/tables/{tableName}/Action `

Where:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Variable**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `{appsheet-region}`                                                           | Domain used to invoke the API based on the supported [data residency          |
|                                                                               | regions](https://support.google.com/appsheet/answer/13788479). Valid values   |
|                                                                               | include:                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   Global: `www.appsheet.com`                                                |
|                                                                               |                                                                               |
|                                                                               | If you have [enabled data                                                     |
|                                                                               | residency](https://support.google.com/appsheet/answer/13788479) on your       |
|                                                                               | AppSheet Enterprise Plus account, one of the following values are             |
|                                                                               | available based on the regions selected:                                      |
|                                                                               |                                                                               |
|                                                                               | -   EU: `eu.appsheet.com`                                                     |
|                                                                               |                                                                               |
|                                                                               | -   Asia Pacific: `asia-southeast.appsheet.com`                               |
|                                                                               |                                                                               |
|                                                                               | **Note**: The `api.appsheet.com` domain is still supported, but has been      |
|                                                                               | deprecated.                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `{app-id}`                                                                    | ID of the AppSheet app. To enable the API and view the **App Id**, see        |
|                                                                               | [Enable the API for cloud-based service                                       |
|                                                                               | communication](https://support.google.com/appsheet/answer/10105769).          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `{table-name)`                                                                | Name of the table. Select **Data \> Tables** and expand the table details to  |
|                                                                               | view the table name.                                                          |
|                                                                               |                                                                               |
|                                                                               | **Note**: The table name should be                                            |
|                                                                               | [URL-encoded](https://en.wikipedia.org/wiki/Percent-encoding).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

You must pass the application access key using one of the methods described in [Specify the application access key](#app-access-key). 

**Note**: The following URL format is still supported, but has been deprecated:
`POST https://api.appsheet.com/api/v2/apps/{appId}/tables/{tableName}/Action`

## Specify the application access key

You must include the API application access key in every API call.

### Specify application access key when invoking from a webhook

If you [invoke the API from a webhook](https://support.google.com/appsheet/answer/11548405) to access an app **owned by you**, the system automatically adds an [HTTP header](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields) containing the `ApplicationAccessKey`.

If you invoke the API from a webhook to access an application **not owned by you**, you must explicitly specify an HTTP header containing the `ApplicationAccessKey` for that application, and enclose the value in quotes. For example:

    applicationAccessKey: "V2-bA2SK-l5kzd-SdvFb-mqIe6-gBT8a-CXp3D-cjCYB-oiJ6U"

### Specify application access key in HTTP header

If you are invoking the API from something other than a webhook action, you must specify the `ApplicationAccessKey`.

It is best to specify the `ApplicationAccessKey` in the [HTTP headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields) because this is most secure. It is specified in the form: 

`ApplicationAccessKey=<applicationAccessKey>`

For example:

`ApplicationAccessKey=V2-bA2SK-l5kzd-SdvFb-mqIe6-gBT8a-CXp3D-cjCYB-oiJ6U`

### Specify application access key in HTTP query string

If you must explicitly specify the `ApplicationAccessKey` but cannot do so in the HTTP headers, you can provide it in the [HTTP query string](https://en.wikipedia.org/wiki/Query_string). This is less secure than using HTTP headers. It is specified in the form:

`https://{appsheet-region}``/api/v2/apps/{appId}/tables/{tableName}/Action?applicationAccessKey=<applicationAccessKey>`

For example:

`https://{appsheet-region}/api/v2/apps/{appId}/tables/{tableName}/Action?applicationAccessKey=V2-bA2SK-l5kzd-SdvFb-mqIe6-gBT8a-CXp3D-cjCYB-oiJ6U`

If the `ApplicationAccessKey` is specified in both the HTTP headers and the HTTP query string, the value in the HTTP headers is used.

### Application access key validation

When the API is invoked, the `ApplicationAccessKey` is compared to the **Application Access Key** and **Alternate Application Access Key** values on the API page. See [Enable the API](https://support.google.com/appsheet/answer/10105769).

If the `ApplicationAccessKey` does not match any of the enable keys, the HTTP request is rejected and logged to the [audit history](https://support.google.com/appsheet/answer/10104794).

## HTTP request body

The following provides an example of the HTTP request body:

    {
      "Action": "Add",
      "Properties": {
        "Locale": "en-US",
        "Location": "47.623098, -122.330184",
        "Timezone": "Pacific Standard Time",
        "UserSettings": {
          "Option 1": "value1",
          "Option 2": "value2"
        }
      },
      "Rows": [
        {
          "FirstName": "Jan",
          "LastName": "Jones",
          "Age": 33,
          "Department": "Accounting",
          "Street": "110 Beach Blvd",
          "City": "Newport Beach",
          "State": "CA",
          "Zip": 92661,
          "Home Phone": 4257868765,
          "Fax": 4253214432,
          "Date Hired": "10/31/2014",
          "Arrived": "8:15:25",
          "Departed": "18:30:33",
          "Last Review": "08/31/2017 23:59:59",
          "Rating": 0.9950,
          "Salary": 3333.45,
          "Image": "http://images6.fanpop.com/image/photos/36300000/Emilia-Clarke-image-emilia-clarke-36399128-460-276.jpg"
        }
      ]
    }

 

The API HTTP request body specifies the content defined in the following sections.

### Action

The `Action` property in the HTTP request body specifies the name of the action to perform. Valid values include:

- `Add`: Adds a new row to the table.
- `Delete`: Deletes existing rows from the table.
- `Edit`: Updates existing rows in the table.
- `Find`: Reads an existing row of the table.

Or specify the name of an existing data-change [action](https://support.google.com/appsheet/answer/10107706) for the table.

### Properties

The properties of the API request are in [JSON format](https://en.wikipedia.org/wiki/JSON). These properties are optional.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Property**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `Locale`                                                                      | [Locale](https://en.wikipedia.org/wiki/Locale_(computer_software)) of the     |
|                                                                               | client making the request. For example, `en-US` indicates English, United     |
|                                                                               | States. If this value is not specified, `Locale` defaults to `en-US`.\        |
|                                                                               | \                                                                             |
|                                                                               | The `Locale` is used when validating `Date`, `DateTime`, `Decimal`,           |
|                                                                               | `Percent`, `Price`, and `Time` data values. For example, when `Locale` is     |
|                                                                               | `en-US`, date values must be entered in `MM/DD/YYYY` format; when `Locale` is |
|                                                                               | `en-GB`, date values must be entered in `DD/MM/YYYY` format.                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `Location`                                                                    | Latitude and longitude of the client making the request.\                     |
|                                                                               | \                                                                             |
|                                                                               | This value is used for                                                        |
|                                                                               | [ChangeLocation](https://support.google.com/appsheet/answer/10106528)         |
|                                                                               | columns. For example `47.623098, -122.330184` represents Seattle, Washington  |
|                                                                               | in the US. If not specified, `Location` defaults to `0.000000, 0.000000`.     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `RunAsUserEmail`                                                              | User email address of the person taking the action. The action is performed   |
|                                                                               | under the user email address you specify. If this value is not specified, the |
|                                                                               | action is performed under the user email address of the application owner.\   |
|                                                                               | \                                                                             |
|                                                                               | If you are performing an action against a table that uses [data               |
|                                                                               | partitions](https://support.google.com/appsheet/answer/10105383) and the      |
|                                                                               | partition expression is based on a                                            |
|                                                                               | [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) value,   |
|                                                                               | you should specify the user email value here.                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `Timezone`                                                                    | [Timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of   |
|                                                                               | the client making the request. For example, `Pacific Standard Time` indicates |
|                                                                               | Pacific Standard Time in the United States and Canada. If not specified,      |
|                                                                               | `Timezone` defaults to `UTC`.                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `UserSettings`                                                                | [User setting](https://support.google.com/appsheet/answer/10106760) to be     |
|                                                                               | used when performing the action. If not specified, no user settings are       |
|                                                                               | used.\                                                                        |
|                                                                               | \                                                                             |
|                                                                               | If you are performing an action against a table that uses [data               |
|                                                                               | partitions](https://support.google.com/appsheet/answer/10105383) and the      |
|                                                                               | partition expression is based on                                              |
|                                                                               | [`USERSETTINGS()`](https://support.google.com/appsheet/answer/10108291)       |
|                                                                               | values, you should specify those values here.                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Rows

Include each column name and its intended value, in [JSON format](https://en.wikipedia.org/wiki/JSON).

For all actions except `Add`, the row's [key column](https://support.google.com/appsheet/answer/10106672) name and value must be explicitly included.

For an `Add` action**,** the new row's key column must be given an explicit value, or enough other column values must be provided to allow the key column value to be generated according to the key column's definition. For instance, if the key column's [Initial value](https://support.google.com/appsheet/answer/10106437) expression is blank, the key column value must be provided explicitly. If the **Initial value** expression generates the key column value using other columns of the row, values for those other columns must be provided. If **Initial value** simply uses [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) (for instance) to generate the key column value, the key column may be omitted.

[Column constraints](https://support.google.com/appsheet/answer/10107948), if present in the column's definition, are enforced on column values provided through API calls: only a column allowed to change (per [`Editable_If`](https://support.google.com/appsheet/answer/10107954)) may be changed; a required column (per [`Required_If`](https://support.google.com/appsheet/answer/10106535)) must have a non-blank value; a non-blank value must be valid (per [`Valid_If`](https://support.google.com/appsheet/answer/10107949)).

For an `Add` action, for each column not included in the API call, the column's **Initial value** expression will be used to give the column a value.

For an action that modifies an existing row, for each column not included in the API call, the column's **Reset on edit?** setting will be checked and **Initial value** applied if indicated. Otherwise, the column's value will be unchanged.

### Row column values

Each column's values must be suitable for its [column type](https://support.google.com/appsheet/answer/10106435).

The value for a **Yes/No** column can be specified in several equivalent ways.
All of the following values are equivalent ways of specifying "True".
Field values within quotes are case insensitive. For example, "TRUE, "True", "true", "TruE" are equivalent.

    "MyBool": true
    "MyBool": "True"
    "MyBool": "true"
    "MyBool": "T"
    "MyBool": "t"
    "MyBool": "Yes"
    "MyBool": "yes"
    "MyBool": "Y"
    "MyBool": "y"

All of the following values are equivalent ways of specifying "False".
Field values within quotes are case insensitive. For example, "FALSE, "False", "false", "FalsE" are equivalent.

    "MyBool": false
    "MyBool": "False"
    "MyBool": "false"
    "MyBool": "F"
    "MyBool": "f"
    "MyBool": "No"
    "MyBool": "no"
    "MyBool": "N"
    "MyBool": "n"

### Special characters in JSON

The following JSON special characters must be escaped when they appear in column names or column values.

|                 |                        |
|-----------------|------------------------|
| **Character**   | **Escaped JSON Value** |
| Backslash       | \\                     |
| Backspace       | \b                     |
| Carriage Return | \r                     |
| Double Quote    | \\                     |
| Form Feed       | \f                     |
| Newline         | \n                     |
| Tab             | \t                     |

## API Response HTTP Status Codes

The API returns the following HTTP status codes.

- 200 Success
- 400 Bad Request
  - The Application Access Key is missing.
  - The App ID is missing.
  - The `POST` body contains invalid data.
- 403 Forbidden
  - The Web API is not enabled for this application.
  - The Application Access Key is invalid.
- 404 Not Found
  - The application specified by the App ID cannot be found.
- 500 Internal Server Error
  - An unexpected error occurred.

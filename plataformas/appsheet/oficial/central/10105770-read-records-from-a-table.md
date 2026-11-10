---
fonte: https://support.google.com/appsheet/answer/10105770?hl=en
baixado: 2026-11-10
---

# Read records from a table

Read existing records in a table using the API.

See also: [Example: Copy updated records](https://support.google.com/appsheet/answer/10104717)

## URL

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

You must pass the application access key using one of the methods described in [Specify the application access key](https://support.google.com/appsheet/answer/10105398#application-access-key). For example, to pass it in the HTTP query string, use the following format:

`https://api.appsheet.com/api/v2/apps/{appId}/tables/{tableName}/Action?applicationAccessKey=<applicationAccessKey>`

## Request body

The HTTP request body contains:

- The Action name `Find`.
- Optional properties such as `Locale`, `Location`, and `Timezone`.
  The [`Locale`](https://support.google.com/appsheet/answer/10107704) is used when validating `Date`, `Time`, `DateTime`, `Decimal`, `Percent`, and `Price` data values. For example, when `Locale` is `en-US`, date values must be entered in `MM/DD/YYYY` format. When Locale is` en-GB`, date values must be entered in `DD/MM/YYYY` format.
- The optional `Selector` property.

## Examples

### Read all rows

You can omit the `Selector` property and not specify any input `Rows`. This will return all rows in the table.

`{`
`"Action": "Find",`
`"Properties": {`
`   "Locale": "en-US",`
`   "Location": "47.623098, -122.330184",`
`   "Timezone": "Pacific Standard Time",`
`   "UserSettings": {`
`      "Option 1": "value1",`
`      "Option 2": "value2"`
`   }`
`},`
`"Rows": [`
`]`
`}`

### Read selected rows

In the `Selector` property, you can specify an expression to select and format the rows returned.

For example, you can specify one of the following expressions:

- [`FILTER()`](https://support.google.com/appsheet/answer/10108196) to return keys to rows in a table or slice.
- [`ORDERBY()`](https://support.google.com/appsheet/answer/10107362) expression to control the sort order of the returned records. 
- [`SELECT()`](https://support.google.com/appsheet/answer/10108207) expression that yields a list of record key values. The records identified by the key values are returned in the `Rows` response. The `SELECT()` expression can refer to a slice.
- [`TOP()`](https://support.google.com/appsheet/answer/10107704)** **expression to limit the number of returned rows.

&nbsp;

    {
    "Action": "Find",
    "Properties": {
       "Locale": "en-US",
       "Location": "47.623098, -122.330184",
       "Selector": "Filter(People, true)",
       "Timezone": "Pacific Standard Time",
       "UserSettings": {
          "Option 1": "value1",
          "Option 2": "value2"
       }
    },
    "Rows": [
    ]
    }

The following provides additional examples of the `Selector` property:

    "Selector": "Filter(People, true)"

    "Selector": "Filter(People, [Age] >= 21)"

    "Selector": "Select(People[_ComputedKey], And([Age] >= 21, [State] = "CA"), true)"

    "Selector": "OrderBy(Filter(People, [Age] >= 21), [LastName], true)"

    "Selector": "Top(OrderBy(Filter(People, [Age] >= 21), [LastName], true), 10)"

    "Selector": "Top(OrderBy(Select(People[_ComputedKey], And([Age] >= 21, [Date Hired] > "01/01/2016"), true), [LastName], false), 100)"

### **Read input rows**

You can omit the `Selector` property and specify input `Rows` containing the key values of the records to be read. This will return all rows having matching key values from the table.

    {
    "Action": "Find",
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
    }
    ]
    }

## Security filters

The `Find` is performed under the identity of the application owner by default. Your can override this by specifying the **RunAsUserEmail** property in the request properties.

[Security filters](https://support.google.com/appsheet/answer/10104488) are applied when the `Find` is performed.

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

## Response body

The API returns the rows in HTTP contents.

The returned records include all field values. This includes virtual fields and field values computed by worksheet formulas.

    {
      "Rows": [
    {
    "_RowNumber": 10,
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

## Response HTTP status codes

See [Response HTTP status codes](https://support.google.com/appsheet/answer/10104497#status-codes) in Invoke an action.

## What happens when a record is read?

1.  The record is retrieved based on the key values you specify.
2.  The record is returned in the HTTP content.

## Error: Row having key not found

See [Troubleshoot API calls](https://support.google.com/appsheet/answer/10104718) for information on the following error:

`Row having key '<key value>' not found`

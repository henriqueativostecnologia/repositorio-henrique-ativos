---
fonte: https://support.google.com/appsheet/answer/10105399?hl=en
baixado: 2026-11-10
---

# Delete records from a table

Delete one or more existing records from a table using the API.

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

The HTTP request body contains:

- The Action name `Delete`.

- Optional properties such as `Locale`, `Location`, and `Timezone`.

  The [`Locale`](https://support.google.com/appsheet/answer/10107704) is used when validating `Date`, `Time`, `DateTime`, `Decimal`, `Percent`, and `Price` data values. For example, when `Locale` is `en-US`, date values must be entered in `MM/DD/YYYY` format. When Locale is` en-GB`, date values must be entered in `DD/MM/YYYY` format.

- One or more `Rows` elements to be deleted.
  Each `Row` value may contain field values of the key field values of the record to be deleted. In the following example, the key fields of the record are `FirstName` and `LastName`.

  When you wish to delete two or more rows, it is more efficient to delete all of the rows in a single API call than to delete each row in a separate API call. Using a single API call is significantly more efficient because we make few calls to the data provider.

&nbsp;

    {
    "Action": "Delete",
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
    "LastName": "Jones"
    },
    {
    "FirstName": "Ian",
    "LastName": "Ivans",
    }
    ]

## Response body

The API returns the deleted rows in HTTP contents.

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
    },
    {
    "_RowNumber": 11,
    "FirstName": "Ian",
    "LastName": "Ivans",
    "Age": 22,
    "Department": "Payroll",
    "Street": "118 E Oceanfront",
    "City": "Newport Beach",
    "State": "CA",
    "Zip": 92661,
    "Home Phone": 4257868148,
    "Fax": 4253217798,
    "Date Hired": "09/30/2014",
    "Arrived": "7:40:25",
    "Departed": "19:22:33",
    "Last Review": "09/30/2017 23:59:59",
    "Rating": 0.9750,
    "Salary": 4444.45,
    "Image": "http://images4.fanpop.com/image/photos/16300000/Christopher-Walken-3-christopher-walken-16367376-720-480.jpg"
    }
    ]
    }

## Response HTTP status codes

See [Response HTTP status codes](https://support.google.com/appsheet/answer/10104497#status-codes) in Invoke an action.

## What happens when a record is deleted?

1.  The key field values you specify in the Incoming webhook request are used to retrieve the record.
2.  The record or records are deleted from the table.
3.  Automations, if any, are invoked separately for each new row.
    **Note**: Automations will only be triggered if the event source is set to an [app data change event](https://support.google.com/appsheet/answer/11445188#configure-app-event).
4.  The deleted record or records are returned in the HTTP content.

## Error: Row having key not found

See [Troubleshoot API calls](https://support.google.com/appsheet/answer/10104718) for information on the following error:

`Row having key '<key value>' not found`

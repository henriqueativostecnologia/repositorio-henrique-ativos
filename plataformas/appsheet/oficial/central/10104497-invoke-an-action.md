---
fonte: https://support.google.com/appsheet/answer/10104497?hl=en
baixado: 2026-11-10
---

# Invoke an action

Invoke one the following types of actions using the API:

- [Data-change action](https://support.google.com/appsheet/answer/10107706#data-change)
- [Composite action](https://support.google.com/appsheet/answer/10107706#composite) (Grouped: execute a sequence of actions)
  All actions invoked in the Grouped sequence must be either a data-change action or **Grouped: execute a sequence of actions**.

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

`https://{appsheet-region}/api/v2/apps/{appId}/tables/{tableName}/Action?applicationAccessKey=<applicationAccessKey>`

## Request body

The HTTP request body contains:

- The action name.
- Optional properties such as `Locale`, `Location`, and `Timezone`.
- One or more `Rows` elements specifying the key field values of the rows to which the action is to be applied.

The [Locale](https://support.google.com/appsheet/answer/10107704) is used when validating `Date`, `Time`, `DateTime`, `Decimal`, `Percent`, and `Price` data values. For example, when `Locale` is `en-US`, date values must be entered in `MM/DD/YYYY` format. When `Locale` is `en-GB`, date values must be entered in `DD/MM/YYYY` format.

When you wish to invoke an action on two or more rows, it is more efficient to invoke the action on all of the rows in a single API call than to invoke the action on each row in a separate API call. 

See [Use templates in an automation](https://support.google.com/appsheet/answer/11539957) for more on creating webhook body templates.

The following provides an example of the request body.

    {
    "Action": "IncrementCountAction",
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

The API returns the updated rows in the HTTP response body.

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

## Response HTTP status codes

The API returns the following HTTP status codes. 

- 200 Success
- 400 Bad Request
  - The Application Access Key is missing.
  - The AppId is missing.
  - The POST body contains invalid data.
- 403 Forbidden
  - The Web API is not enabled for this application.
  - The Application Access Key is invalid.
- 404 Not Found
  - The application specified by the AppId cannot be found.
- 500 Internal Server Error
  - An unexpected error occurred.

## What happens when an action is invoked?

1.  The Data Change action is applied to the record or records.
2.  The record or records are updated in the table.
3.  Automation workflows, if any, are invoked. 
4.  The updated record or records are returned in the HTTP content.

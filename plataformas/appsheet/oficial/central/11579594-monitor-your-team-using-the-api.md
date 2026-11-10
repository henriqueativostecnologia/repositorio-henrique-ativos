---
fonte: https://support.google.com/appsheet/answer/11579594?hl=en
baixado: 2026-11-10
---

# Monitor your team using the API

**Notes**:

- Teams are supported for AppSheet Enterprise accounts only.
- You must be team root or admin to manage and monitor your team using the API.

You can use the AppSheet API to to perform the following tasks:

- [Monitor app usage by email](https://support.google.com/appsheet/answer/11918345#app-usage-email-api)
- [Monitor app usage by user](https://support.google.com/appsheet/answer/11918345#app-usage-user-api)
- [Monitor team membership](https://support.google.com/appsheet/answer/11918345#team-membership-api)

**If your team user accounts are managed by your Google Workspace organization**, don't use the API to automate the removal of team users accounts. To control access to AppSheet by users in the organization, see [Turn AppSheet on or off for users](https://support.google.com/a/answer/10216943).

The following sections provide general guidance for using the AppSheet API to monitor and manage teams:

- [Required headers](#required-headers)
- [Generate an API key](#generate-api-key)
- [Use curl](#use-curl)

## ****Required headers

To call the AppSheet team APIs, you need to pass the following headers:

|             |                                                        |
|-------------|--------------------------------------------------------|
| **Header**  | **Description**                                        |
| `AccessKey` | API key. See [Generate an API key](#generate-api-key). |
| `UserId`    | Your user account ID.                                  |

## Generate an API key

To generate an API key:

1.  Navigate to **My Account \> Settings**.
2.  Under API Settings click **Generate Api Key**.
3.  Click **Save**.

## ****Use curl

The examples throughout the documentation use [curl](https://curl.haxx.se/) to demonstrate how to use the AppSheet API. curl is an open source, command-line tool for transferring data with URL syntax, supporting common protocols such as HTTP and HTTPS.

The following table summarizes the curl command-line options used in the examples.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Option**                                                                    | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `-H`\                                                                         | Defines a request header. See [Required headers](#required-headers).          |
| `--header`                                                                    |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `-X`                                                                          | Specifies the type of request (GET, POST, and so on).                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

The following provides an example AppSheet API call using curl:

`curl https://{appsheet-region}/api/v2/admin/reports/usage \`
`  -X GET \`
`  -H "AccessKey: DcTx1-TFq3c-7ka6t-PcnnI-7d0dO-M4wTm-vWwx0-1KBte" \`
`  -H "UserId: 1234567"`

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
|                                                                               | -   EU: `eu.appsheet.com`                                                     |
|                                                                               |                                                                               |
|                                                                               | -   Asia Pacific: `asia-southeast.appsheet.com`                               |
|                                                                               |                                                                               |
|                                                                               | **Note**: The `api.appsheet.com` domain is still supported, but has been      |
|                                                                               | deprecated.                                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

-

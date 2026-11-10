---
fonte: https://support.google.com/appsheet/answer/11918345?hl=en
baixado: 2026-11-10
---

# Monitor your team

**Note**: Teams are supported for Enterprise plans only.

Monitor your team as described in the following sections:

- [Monitor team app activity by using Audit History](#audit-history)
- [Monitor AppSheet database activity](#monitor-database)
- [Monitor team app usage by email](#app-usage)
- [Monitor team app usage by user](#billing-information)
- [Monitor team membership](#team-membership)

## Monitor team app activity by using Audit History

To monitor team app activity using Audit History:

1.  Sign in to [*AppSheet*](http://www.appsheet.com).
2.  Select **My team** in the account profile drop-down.
3.  Click **Usage**.
4.  Expand the details for a specific user.
5.  Click **Log** for an app to view related activity by using Audit History.

See also [*Monitor app activity using Audit History*](https://support.google.com/appsheet/answer/10104794).

As the team root or admin, you can export Audit History logs for your team to BigQuery as described in [Export team audit logs to BigQuery.](https://support.google.com/appsheet/answer/12469223)

## Monitor AppSheet database activity

To monitor AppSheet database activity:

1.  Sign in to [*AppSheet*](http://www.appsheet.com).
2.  Select **My team** in the account profile drop-down.
3.  Click **Usage**.
4.  Expand the details for a specific user.
5.  Click **Log** for an AppSheet database to view related activity in the database audit log.

See also [Manage and monitor databases in your account](https://support.google.com/appsheet/answer/13536908).

## ****Monitor team app usage by email

Monitor team app usage by email. See also [Monitor app usage statistics](https://support.google.com/appsheet/answer/11449228).

In this report, if a user signs in to AppSheet using multiple identity providers, app usage for each email is logged ***separately***.

**Note**: You must have **team root** or **admin** privileges to access team app usage by email.

## Use the UI

To monitor team app usage by email using the AppSheet UI:

1.  Sign in to [*AppSheet*](http://www.appsheet.com).
2.  Select **My team** in the account profile drop-down.
3.  Click **Usage**.
4.  To download usage data for all team apps as a CSV file, click **Download usage data**.
5.  To view usage data for a specific app:
    1.  Expand the app details for a specific user.
    2.  Click ***x*** **monthly users** under the **Usage** column for an app to view relevant usage details.

#### Use the API

To monitor your team app usage by email using the API, issue a `GET` request to:

`https://{appsheet-region}/api/v2/admin/reports/usage`

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

### Headers

You must pass the `AccessKey` and `UserId` headers, as described in [Manage and monitor your team using the API](https://support.google.com/appsheet/answer/11579594).

### Example

For example:

`curl https://www.appsheet.com/api/v2/admin/reports/usage \`
`  -X GET \`
`  -H "AccessKey: DcTx1-TFq3c-7ka6t-PcnnI-7d0dO-M4wTm-vWwx0-1KBte" \`
`  -H "UserId: 1234567"`

If successful, the API call returns `200 OK` and the CSV is downloaded to your local drive in the current directory.

The team app usage CSV file contains the following columns.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Column**                                         | **Description**                                    | **Example**                                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Id                                            | User account ID for the team member that accessed  | 1234567                                            |
|                                                    | the app.                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | The total number of User Ids in a report is        |                                                    |
|                                                    | equivalent to the total number of AppSheet app     |                                                    |
|                                                    | owners (different from billable users).            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Email                                         | Email for the team member that accessed the app.   | user@example.com                                   |
|                                                    |                                                    |                                                    |
|                                                    | The total number of User Emails in a report is     |                                                    |
|                                                    | equivalent to the total number of AppSheet app     |                                                    |
|                                                    | owners (different from billable users).            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| App ID                                             | ID of the app that was accessed.                   | 6fb80a26-04ae-4b96-8d27-4bc851e0cf2c               |
|                                                    |                                                    |                                                    |
|                                                    | The total number of App Ids in a report is         |                                                    |
|                                                    | equivalent to the total number of AppSheet apps in |                                                    |
|                                                    | the team account, regardless of their deployment   |                                                    |
|                                                    | status.                                            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| App Internal Name                                  | Internal name of the app that was accessed.        | MyFirstApp                                         |
|                                                    |                                                    |                                                    |
|                                                    | The total number of App Internal Names in a report |                                                    |
|                                                    | is equivalent to the total number of AppSheet apps |                                                    |
|                                                    | in the team account, regardless of their           |                                                    |
|                                                    | deployment status.                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Install link                                       | Link to install app on mobile device.              | https://www.appsheet.co                            |
|                                                    |                                                    | m/newshortcut/6fb80a26-04ae-4b96-8d27-4bc851e0cf2c |
|                                                    |                                                    |                                                    |
|                                                    |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Browser link                                       | Link to access app in a browser.                   | https://www.appsh                                  |
|                                                    |                                                    | eet.com/start/6fb80a26-04ae-4b96-8d27-4bc851e0cf2c |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Runnable?                                          | Flag that specifies whether the app is able to     | TRUE                                               |
|                                                    | run. For example, if there is an error in your app |                                                    |
|                                                    | preventing it from being run, this flag is set to  |                                                    |
|                                                    | **FALSE**.                                         |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Deployed?                                          | Flag that specifies whether the app is deployed.   | TRUE                                               |
|                                                    | See                                                |                                                    |
|                                                    | [Deployment](ht                                    |                                                    |
|                                                    | tps://support.google.com/appsheet/topic/10104993). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Public Sample?                                     | Flag that specifies whether the app is a public    | TRUE                                               |
|                                                    | sample. See [Share sample apps in your public      |                                                    |
|                                                    | portfolio](htt                                     |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/11938113). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Team Sample                                        | Flag that specifies whether the app is a team      | TRUE                                               |
|                                                    | sample. See [Share team sample                     |                                                    |
|                                                    | apps](https://support.googl                        |                                                    |
|                                                    | e.com/appsheet/answer/10104795#share-sample-apps). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Secure                                             | Flag that specifies whether the app is secure. See | TRUE                                               |
|                                                    | [How to require user                               |                                                    |
|                                                    | sign-in](https://su                                |                                                    |
|                                                    | pport.google.com/appsheet/answer/10104975#how-to). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Auth Provider                                      | Authorization provider used by the app. See [How   | google                                             |
|                                                    | to require user                                    |                                                    |
|                                                    | sign-in](https://su                                |                                                    |
|                                                    | pport.google.com/appsheet/answer/10104975#how-to). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Allow all signed-in users                          | Flag that specifies whether all signed-in users    | FALSE                                              |
|                                                    | are able to access the app. See [Share your app    |                                                    |
|                                                    | with all signed-in                                 |                                                    |
|                                                    | users](https://support.goo                         |                                                    |
|                                                    | gle.com/appsheet/answer/10104983#share-signed-in). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Monthly users                                      | Total active users in current monthly billing      | 10                                                 |
|                                                    | cycle. An active user is anyone who accessed your  |                                                    |
|                                                    | app within the last 30 days. See also [What is an  |                                                    |
|                                                    | active                                             |                                                    |
|                                                    | user?](ht                                          |                                                    |
|                                                    | tps://support.google.com/appsheet/answer/10105090) |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Most recently used                                 | Date and timestamp that the app was most recently  | 12/2/2021 10:33:56 AM                              |
|                                                    | used in the last month. Useful for time-based      |                                                    |
|                                                    | reporting such as confirming that an app is no     |                                                    |
|                                                    | longer being accessed after it is deprecated.      |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Least recently used                                | Date and timestamp that the app was first used in  | 11/11/2021 2:19:36 PM                              |
|                                                    | the last month. Useful for time-based reporting    |                                                    |
|                                                    | such as determining when a new app was first       |                                                    |
|                                                    | accessed.                                          |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| App Public Name                                    | Public name of app. See [Customize the About       | My App                                             |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Version                                            | Version of app. See [Customize the About           | 1.000005                                           |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Short description                                  | Short description of the app. See [Customize the   | Sample App                                         |
|                                                    | About                                              |                                                    |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Description                                        | Description of the app. See [Customize the About   | A sample app with sample data                      |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Guidance                                      | App user guidance. See [Customize the About        | Some user guidance                                 |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| About Url                                          | URL for about app information. See [Customize the  | about.example.com                                  |
|                                                    | About                                              |                                                    |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Privacy policy Url                                 | URL for app privacy policy. See [Customize the     | privacy-policy.example.com                         |
|                                                    | About                                              |                                                    |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Category                                           | Category of the app. See [Customize the About      | Tracking Apps                                      |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Function                                           | Function of the app. See [Customize the About      | Inventory Management                               |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Industry                                           | Industry for the app. See [Customize the About     | Retail                                             |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Purpose                                            | Purpose of the app. See [Customize the About       | Track item details and log incoming and outgoing   |
|                                                    | page](htt                                          | inventory amounts.                                 |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Design Details                                     | App design details. See [Customize the About       | Some design details                                |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Reference Url                                      | URL for app reference information. See             | reference-url.example.com                          |
|                                                    | [Customize the About                               |                                                    |
|                                                    | page](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/10106613). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Owner Id                                           | Account ID of app owner.                           | 1899830                                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## ****Monitor team app usage by user

Monitor team app usage by user.

In this report, if a user signs in to AppSheet using multiple identity providers, app usage for each email is grouped together and ***logged as a single user.*** In this way, the team app usage accurately reflects the total usage by a single user.

**Notes**:

- You must have **team root** or **admin** privileges to access team app usage by user.
- You can access up to **30 days** of billing information.
- You can disregard the **User ID** column that is returned in this report. It has no relevance and does not equate to the number of licenses required.

## Use the UI

To monitor team app usage by user:

1.  Sign in to [*AppSheet*](http://www.appsheet.com).
2.  Select **My team** in the account profile drop-down.
3.  Click **Billing**.
4.  To download billing information for all team apps as a CSV file, click **Download billing data**.
5.  Expand the plan details for a specific user to view more information.

#### Use the API

To monitor team app usage by user using the API, issue a `GET` request to:

`https://{api-domain}/api/v2/admin/reports/billing`

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

### Query parameters

Optionally, you can pass the following as query parameters. If not specified, billing information is returned for the last 30 days.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Query parameter**                                                           | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `startDate`                                                                   | Start date for the billing information. The value must be in the following    |
|                                                                               | URL-encoded form: **`M`**`%2F`**`D`**`%2F`**`YYYY`**` `                       |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | `1%2F1%2F2021` (1/1/2021)                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `endDate`                                                                     | End date for the billing information. The value must be in the following      |
|                                                                               | URL-encoded form: **`M`**`%2F`**`D`**`%2F`**`YYYY`**                          |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
|                                                                               |                                                                               |
|                                                                               | `1%2F1%2F2021` (1/1/2021)                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Headers

You must pass the `AccessKey` and `UserId` headers, as described in [Manage and monitor your team using the API](https://support.google.com/appsheet/answer/11579594).

### Example

For example:

`curl https://www.appsheet.com/api/v2/admin/reports/billing \`
`  -X GET \`
`  -H "AccessKey: DcTx1-TFq3c-7ka6t-PcnnI-7d0dO-M4wTm-vWwx0-1KBte" \`
`  -H "UserId: 1234567"`

If successful, the API call returns `200 OK` and the CSV is downloaded to your local drive in the current directory.

The team app usage CSV file contains the following columns.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Column**                                         | **Description**                                    | **Example values**                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Id                                            | **Note**: You can disregard the User ID column     | 1234567                                            |
|                                                    | that is returned in this report. It has no         |                                                    |
|                                                    | relevance and does not equate to the number of     |                                                    |
|                                                    | licenses required.                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Email                                         | Email for the team member that accessed the app.   | user@example.com                                   |
|                                                    |                                                    |                                                    |
|                                                    | The total number of User Emails in a report is     |                                                    |
|                                                    | equivalent to the total number of AppSheet users   |                                                    |
|                                                    | for the billing period.                            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| App Count                                          | Number of apps that the user has accessed or       | 10                                                 |
|                                                    | edited.                                            |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Deployed App Count                                 | Number of deployed apps that the user has accessed | 9                                                  |
|                                                    | or edited.                                         |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| App Names                                          | Comma-separated list of apps that the user has     | App1, App2, App3, …                                |
|                                                    | accessed.                                          |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Last access                                        | Date and timestamp of the user's last access.      | 12/2/2021 10:33:56 AM                              |
|                                                    | Useful for time-based reporting.                   |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Monitor team membership

Monitor detailed team membership information for governance and management purposes.

**Note**: You must have **team root** or **admin** privileges to monitor team membership.

## Use the UI

To monitor team membership using the AppSheet UI:

1.  Sign in to [*AppSheet*](http://www.appsheet.com).
2.  Select **My team** in the account profile drop-down.
3.  Click **Members**.
4.  To download membership data for all team apps as a CSV file, click **Download membership data**.
5.  To view details for a specific team member, expand the associated section

#### Use the API

To monitor your team membership by using the API, issue a `GET` request to:

`https://{api-domain}/api/v2/admin/reports/membership`

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

### Headers

You must pass the `AccessKey` and `UserId` headers, as described in [Manage and monitor your team using the API](https://support.google.com/appsheet/answer/11579594).

### Example

For example:

`curl https://www.appsheet.com/api/v2/admin/reports/membership \`
`  -X GET \`
`  -H "AccessKey: DcTx1-TFq3c-7ka6t-PcnnI-7d0dO-M4wTm-vWwx0-1KBte" \`
`  -H "UserId: 1234567"`

If successful, the API call returns `200 OK` and the CSV is downloaded to your local drive in the current directory.

The monitor team membership CSV file contains the following columns.

To distinguish between app creators and app users, note that app users won't ever have an entry for Last App Edit or an app count of 0.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Column**                                         | **Description**                                    | **Example values**                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Id                                            | User account ID for the team member that accessed  | 1234567                                            |
|                                                    | the app.                                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | The total number of User Ids in a report is        |                                                    |
|                                                    | equivalent to the total number of AppSheet team    |                                                    |
|                                                    | members (different from AppSheet users).           |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Email                                         | Email for the team member that accessed the app.   | user@example.com                                   |
|                                                    |                                                    |                                                    |
|                                                    | The total number of User Emails in a report is     |                                                    |
|                                                    | equivalent to the total number of AppSheet team    |                                                    |
|                                                    | members (different from AppSheet users).           |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Name                                          | Name of the user.                                  |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | If a recipient is sent an email team invitation    |                                                    |
|                                                    | and they manually accept it in the email, their    |                                                    |
|                                                    | display name will appear in this column. If,       |                                                    |
|                                                    | however, the admin use the **Adopt my entire       |                                                    |
|                                                    | domain** feature, then this column is empty for    |                                                    |
|                                                    | signed-in users.                                   |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Plan                                          | Subscription plan.                                 | Core (Google Workspace)                            |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| User Role                                          | Role of user, such as Member, Admin, Root.         | Member                                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Date Created                                       | Date and timestamp that the user was created.      | 12/2/2020 10:33:56 AM                              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Last App Edit                                      | Last time an app was edited by the user.           | 11/11/2021 2:19:36 PM                              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| App Count                                          | Number of apps owned by the user.                  | 10                                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

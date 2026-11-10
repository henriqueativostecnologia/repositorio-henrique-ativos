---
fonte: https://support.google.com/appsheet/answer/11579184?hl=en
baixado: 2026-11-10
---

# Automate the removal of team user accounts using the API

**If your team user accounts are managed by your Google Workspace organization**, do not use the API to automate the removal of team users accounts. To control access to AppSheet by users in the organization, see [Turn AppSheet on or off for users](https://support.google.com/a/answer/10216943).

 

**If your app is connected to one or more AppSheet databases**, you'll need to transfer the database to a new owner using the app editor, as described in [Transfer databases between team members](https://support.google.com/appsheet/answer/12007391#transfer-databases-between-team-members).  This step cannot be automated using the API at this time. 

When a user leaves the organization, you can automate the removal of their user account using the AppSheet API to [transfer app ownership](#transfer-app-ownership) and [delete the user account](#delete-user-account) as described in the following sections.

**Notes**:

- Teams are supported for AppSheet Enterprise accounts only.
- You must have team root or admin permissions to use the APIs and be on the same team as the referenced user accounts.

## ****Transfer app ownership

To transfer ownership of all apps owned by a user account to another user account within a team issue a `POST` request to the following API:

`https://{appsheet-region}/api/v2/admin/apps/transferall?oldOwnerId={id}&newOwnerId={id}`

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

You must pass the following as query parameters:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Query parameter**                                                           | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `oldOwnerId`                                                                  | User account ID for the current owner.                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `newOwnerId`                                                                  | User account ID to which you want to assign all apps.                         |
|                                                                               |                                                                               |
|                                                                               | **Note**: The users must be members of the same team.                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Headers

You must pass the `AccessKey` and `UserId` headers, as described in [Manage and monitor your team using the API](https://support.google.com/appsheet/answer/11579594).

### Example

For example:

`curl https://{appsheet-region}/api/v2/admin/apps/transferall?oldOwnerId=14853665&newOwnerId=14853667 \`
`  -X POST` \\
`  -H "AccessKey: DcTx1-TFq3c-7ka6t-PcnnI-7d0dO-M4wTm-vWwx0-1KBte" \`
`  -H "UserId: 1234567"`

If successful, the API call returns `200 OK`.

## ****Delete the user account

**Note**: Deleting a user account is permanent and non-recoverable. If you do not want to delete the apps owned by this account, [transfer them](#transfer-app-ownership) before deleting the account.

To delete a user account issue a `POST` request to the following API:

`https://{appsheet-region}/api/v2/admin/users/delete?userId={id}`

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

### Query parameter

You must pass the following as query parameters:

|                     |                                          |
|---------------------|------------------------------------------|
| **Query parameter** | **Description**                          |
| `userId`            | User account ID that you want to delete. |

### Headers

You must pass the `AccessKey` and `UserId` headers, as described in [Manage and monitor your team using the API](https://support.google.com/appsheet/answer/11579594).

### Example

For example:

`curl https://{appsheet-region}/api/v2/admin/users/delete?userId=14853665 \`
`  -X POST \`
`  -H "AccessKey: DcTx1-TFq3c-7ka6t-PcnnI-7d0dO-M4wTm-vWwx0-1KBte"`
`  -H "UserId: 1234567"`

If successful, the API call returns `200 OK`.

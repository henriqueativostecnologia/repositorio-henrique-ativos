---
fonte: https://support.google.com/appsheet/answer/10104794?hl=en
baixado: 2026-11-10
---

# Monitor app activity using Audit History

The Audit History for an application is retained for 53 days for Enterprise Plus accounts and 7 days for other types of accounts.

AppSheet's Audit History is a record of recent interactions occurring in your application.

The Audit History contains an entry for every:

- Sync between the users of your app and the AppSheet backend
- Add, edit, or delete between the users of your app and the AppSheet backend
- Add, edit, delete, action invocation, or read call made using the AppSheet API
- Invocation of a bot
- Creation of a report or document

You can use Audit History to troubleshoot:

- Issues where a user says that they synced their changes but no changes have been recorded
- AppSheet API calls
- Zapier API calls
- Bot issues

**Note**: You may need to wait for up to five minutes for an audit record to appear in Audit History. AppSheet groups audit records and periodically writes the grouped audit records to reduce overhead. This can result in a delay before an audit record appears in the Audit History. Click **Get audit history records** periodically until you see the audit record.

Monitor app activity using Audit History as described in the following sections:

- [Use Audit History](#use-audit-history)
- [Configure alerts on Audit History errors](#alerts)
- [Filter Audit History alerts](#filter)
- [Audit changes by user](#audit-changes-by-user)

As the root admin, you can export Audit History logs for your team to BigQuery, as described in [Export team audit logs to BigQuery.](https://support.google.com/appsheet/answer/12469223)

## Use Audit History

To use Audit History log filtering and analytics, you must [subscribe to an Enterprise plan](https://support.google.com/appsheet/answer/10104499#enterprise-plan). 

To use Audit History do one of the following:

- Open your app in the editor, go to the **Manage \> Monitor** tab, expand **Audit History**, and click **Launch log analyzer**.
- (AppSheet admins only) Use the AppSheet Admin Console (preview) to [view details for an app](https://support.google.com/appsheet/answer/15098215) in your team or organization and select **More**  **\> Audit history**.

The Audit History log shows:

- A list of recommendations for improving performance, if applicable
- Summary charts of recent audit log entries by user and by operation
- Audit History log results based on filters selected (see below)

Do any of the following tasks:

- Filter the log by:
  - Syncs, Adds, Updates, Deletes, Automations, Reports, API calls, or Documents
  - Start or end date
  - Failures only
  - Table name, user ID, or rule name
- Within a record, click the **Details** icon to view the outcome of the action.
- Optionally, click **Download Search results** to download a copy of the search results as a JSON payload.

By default, the Audit History is shown for a limited recent period of time. Richer filtering and analysis capabilities are available as part of the Enterprise [pricing plans](https://www.appsheet.com/Pricing).

## Configure alerts on Audit History errors

As the application creator, you can subscribe to automatically receive an email alert each time an error is recorded in Audit History. Audit History alerts are available as part of the Enterprise [pricing plans](https://www.appsheet.com/Pricing).

To enable or disable Audit History alerts:

1.  Go to the **Manage** \> **Monitor** tab.
2.  Expand **Audit History**.
3.  Enable **Enable Audit History alerts**.
4.  Click **Change settings** to save your change. 

Each Audit History alert email message contains the following information.

- Subject: `Alert for AppSheet application <application name> at <gmtTime> GMT`
- Message: Error message from the Audit History record.
- Log URL: URL of the Audit History record.
- Operation: Operation type from the Audit History record.
- Application URL: URL of the application.

## Filter Audit History alerts

You may wish to filter Audit History alerts to highlight some alerts and to suppress others. You can do this by creating email filter rules in your email client. Most email clients provide rich email filtering rules for categorizing and routing email messages.

## Audit changes by user

**Note**: To audit changes by user, you must  [require users to sign in to the app](https://support.google.com/appsheet/answer/10104975).

For some apps, it's important to track specific interactions by user. You can examine the **By User** property in the Audit History log to determine who performed an add, update, or delete, as follows:

- If your application requires sign in, the **By User** property in the Audit History log will contain the user ID of the user that performed the add, update, or delete.

- If your application does not require sign in, the **By User** property in the Audit History log will contain the value `-1` which indicates a *guest user id*.

- If your application does require sign in but the user has not yet granted consent, the **By User** property in the Audit History log will contain the value `-2` which indicates an *unconsented user id*.

You can keep track of which user performed the most recent add or update for each record by adding an extra column of type **Email** to each record. You can populate this column with the [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) of the most recent user to add or update the record. If you specify `USEREMAIL()` as the default value of this column, then every new record will automatically contain the email address of the currently signed-in user who added the record. Then, you can update this column when a user updates the record.

Some apps require a richer audit trail to maintain the history of changes made by different users. Typically, the backend cloud storage provider has an auditing mechanism. For example, Google Sheets provides a **Change History** that shows a detailed list of changes made, including a timestamp and user information. In order to use this backend audit history, it's important that the AppSheet app runs with the security setting [As App User](https://support.google.com/appsheet/answer/10105756). Each potential user should also be given permissions to access the backend spreadsheet.

&nbsp;

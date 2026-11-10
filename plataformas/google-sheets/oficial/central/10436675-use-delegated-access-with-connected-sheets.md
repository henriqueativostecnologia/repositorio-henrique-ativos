---
fonte: https://support.google.com/docs/answer/10436675?hl=en
baixado: 2026-11-10
---

# Use Delegated Access with Connected Sheets

**Important:** In Connected Sheets, Delegated Access is only available if:

- Users are in an [Enterprise](https://workspace.google.com/pricing.html), Education Standard, or Education Plus plan.
- [The admin setting is enabled](https://support.google.com/a/answer/9604541#delegate).

Contact your admin to enable Delegated Access from the admin console.

With Delegated Access:

- A user who creates a Connected Sheet can choose to have all subsequent queries to the underlying data source use their account credentials, even when the queries are triggered by other users of the sheet.
- Collaborators can perform analysis on the data even if they don't have access to the underlying data source. This is useful when people who don’t have access to the data source want to perform data analysis and refresh data derived from a Connected Sheet.
- Standard BigQuery rates apply when queries are run with Delegated access.

Both the user who delegates their access and the user who runs a query appear in BigQuery logs. [Learn how to use audit logs with Connected Sheets](https://support.google.com/a/answer/9604541#audit).

Delegated Access can't be:

- Turned on through Apps Script and Sheets API
- Used to set up scheduled refreshes
- Used in a spreadsheet that can be accessed publicly via a link

## Turn Delegated Access on or off

You can turn Delegated Access on or off for a Connected Sheet when you set up the connection. If you want to turn it on or off at a later time, go to the Connection settings.

For a new connection:

1.  At the top of the sheet, click **Data** and then  **Data Connectors** and then  **Connect to BigQuery**.

2.  Choose a cloud project, dataset, and table or view.

3.  Click **Continue**.

    **Tip:** After you select a cloud project, you can write a custom query.

4.  To turn on Delegated Access, under “Delegate access,” click **Allow**.
    - To turn off Delegated Access, click **Do not allow**.

5.  Click **Connect**.

For an existing connection:

1.  At the top right of the preview sheet, click Connection settings  Settings .
2.  Under “Delegate access,” click **Allow**.
3.  Click **Connect**.

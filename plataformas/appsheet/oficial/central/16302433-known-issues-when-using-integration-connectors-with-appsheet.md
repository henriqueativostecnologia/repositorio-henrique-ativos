---
fonte: https://support.google.com/appsheet/answer/16302433?hl=en
baixado: 2026-11-10
---

# Known issues when using Integration Connectors with AppSheet

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

The following list the known issues with the preview release of Integration Connectors with AppSheet.

- Connections that are in an interim or error state will be hidden and won't appear when trying to add connections as data sources from a Google Cloud project.

  **Workaround**: Ask your Google Cloud admin to check the status of the connection in the Google Cloud console.
   

- When adding a connection as a data source from My Account or from within the app editor, the data source may not immediately appear.

  **Workaround**: Refresh the page.

- Connections with authentication override enabled are not supported at this time. You'll receive the following error if you try to add the connection as a data source.

  `No columns found`
  `Tables must specify a column structure. For some reason, the app definition has been corrupted. It may also be possible that you left your column structure in an inconsistent state. Delete and re-add the table to create the column structure.`

  **Workaround**: Ask your Google Cloud admin to disable authentication override for the connection.

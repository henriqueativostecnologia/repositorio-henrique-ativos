---
fonte: https://support.google.com/appsheet/answer/16085168?hl=en
baixado: 2026-11-10
---

# Troubleshoot using Integration Connectors with AppSheet

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

Troubleshoot using Integration Connectors with AppSheet as described in the following sections.

------------------------------------------------------------------------

 [Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/16085168)

#### I don't see the option to use Integration Connectors when adding a data source

To use Integration Connectors with AppSheet, the following must be true:

- You must have an [AppSheet Enterprise Plus license](https://support.google.com/appsheet/answer/14101111)
- You must be an [AppSheet team admin](https://support.google.com/appsheet/answer/13691133#supported-roles)
- As the AppSheet team admin, make sure that you have worked together with the Google Cloud admin to [set up the team to use Integration Connectors](https://support.google.com/appsheet/answer/16178778#set-up-team) and [allowed AppSheet to connect to your connections](https://support.google.com/appsheet/answer/16178778#allow-appsheet-to-connect)

#### When adding a data source, I don't see the Google Cloud connections for the specified Google Cloud project

If you don't see your Google Cloud connections for the selected Google project ID, do the following:

- As the AppSheet team admin, make sure that you have worked together with the Google Cloud admin to [set up the team to use Integration Connectors](https://support.google.com/appsheet/answer/16178778#set-up-team)
- Make sure you have [created at least one connection](https://support.google.com/apposheet/answer/16178778#create-connection) in the Google Cloud project

#### I see some connectors for the specified Google Cloud project, but not the one I'm looking for

If you don't see the connection in the Google Cloud project, make sure of the following:

- As the AppSheet team admin, make sure that you have worked together with the Google Cloud admin to [set up the team to use Integration Connectors](https://support.google.com/appsheet/answer/16178778#set-up-team) and [allowed AppSheet to connect to your connections](https://support.google.com/appsheet/answer/16178778#allow-appsheet-to-connect)
- Check the IAM role assigned for any rules that would filter the connection you're looking for

#### App creators on my team don't see the connection as a data source

If an app creator on your team doesn't see the connection as a data source, do the following: 

- Make sure the data source has been [shared with your team](https://support.google.com/appsheet/answer/10104795#share-data-sources)
- Check team policies for any rules that would prevent use of the data source by the creator

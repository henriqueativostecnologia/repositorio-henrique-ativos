---
fonte: https://support.google.com/appsheet/answer/11905679?hl=en
baixado: 2026-11-10
---

# Use data from Google BigQuery with AppSheet

To use data from Google BigQuery with AppSheet apps, use one of the following options:

1.  Use the built-in Cloud Database BigQuery data source, as described in [Use data from Google BigQuery with the BigQuery data source](https://support.google.com/appsheet/answer/11905680).
2.  Use the Connected Sheets feature in Sheets to connect to BigQuery, as described in [Use data from Google BigQuery with Connected Sheets](https://support.google.com/appsheet/answer/11903794).

The following table provides a comparison on features to help you choose the best option based on your use case:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Feature**                                        | **BigQuery data source**                           | **Connected Sheets**                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Maximum number of rows                             | 100,000 rows plus [security                        | Refer to [files you can store in Google            |
|                                                    | filters](ht                                        | Drive                                              |
|                                                    | tps://support.google.com/appsheet/answer/10104488) | ](https://support.google.com/drive/answer/37603).  |
|                                                    | to select the most relevant rows first             |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Note**: In some cases, the provider-specific row |                                                    |
|                                                    | limit may be lower than this maximum limit.        |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Subscription plan                                  | Enterprise-level AppSheet account as BigQuery      | Enterprise-level Google Workspace account (see     |
|                                                    | Connector is considered an Advanced Connector (see | [details                                           |
|                                                    | [details](https://support.google.com               | ](https://support.google.com/docs/answer/9703214)) |
|                                                    | /appsheet/answer/11905680#licensing-requirements)) |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Initial setup                                      | Configure BigQuery in Google Cloud (more complex)  | Configure Connected Sheets feature in Sheets       |
|                                                    |                                                    | (simpler for non-technical users)                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Sync time                                          | App is connected and synced in near real time to   | Sheet syncs on a schedule you configure; your app  |
|                                                    | the BigQuery dataset providing access to the       | data may become stale between syncs                |
|                                                    | latest data                                        |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

**Note**: If you have a lightweight use case and need to have production support right away, or have a lower license than is required, use [BigQuery with Connected Sheets](https://support.google.com/appsheet/answer/11903794).

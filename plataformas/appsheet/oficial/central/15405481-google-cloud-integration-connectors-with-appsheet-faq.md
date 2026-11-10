---
fonte: https://support.google.com/appsheet/answer/15405481?hl=en
baixado: 2026-11-10
---

# Google Cloud Integration Connectors with AppSheet FAQ

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

Find answers to your questions about using Google Cloud Integration Connectors with AppSheet.

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/15405481)

#### How does it work?

AppSheet apps can now connect with external data sources, like BigQuery, using Google Cloud [Integration Connectors](https://cloud.google.com/integration-connectors/docs/overview). This feature uses a service account provided by AppSheet, but you'll need to set up a connection within Integration Connectors first.

#### How do I get access to this feature?

Anyone with an AppSheet Enterprise Plus account has access to the Integration Connectors with AppSheet (preview), but only AppSheet team admins can configure AppSheet to use Integration Connectors and add connections as data sources. Once added, data sources can be shared with the team and any team member can add the data source to an app.

To create Integration Connectors, customers must have an [*Application Integration plan*](https://cloud.google.com/application-integration/pricing).  Pricing and fees will apply for any connection used in AppSheet apps.

#### What's the cost?

The standard [Integration Connector pricing](https://cloud.google.com/application-integration/pricing) applies. You'll need an AppSheet Enterprise Plus account.

#### What is the Integration Connector pricing?

Integration Connectors has several [pricing plans](https://cloud.google.com/application-integration/pricing).

- If you are on a **Pay-as-you-go** plan, the **free tier** offers 2 connection nodes for Google services, like BigQuery.  if you only have one connection, we recommend setting the max connection nodes to 2 to prevent autoscaling. If you have more than one connection or when you add a new one, your standard billing rates will apply.
- If you are on an Integration Connectors **Subscription** plan, there is no additional cost.

If you do not already have an Application Integration plan, we suggest starting with the Pay-as-you-go plan

#### Where will the Application Integration charges for Integration Connectors appear?

Application Integration charges will appear in Google Cloud Billing. AppSheet charges will continue to be billed through Google Admin console.

#### How is security and governance handled?

Google Cloud admins grant AppSheet access to Integration Connector connections by project. Google Cloud admins can revoke access to a project and its connections by deleting the connection or removing privileges granted to the AppSheet service account. Revoking access will cause connected AppSheet apps to no longer work.

AppSheet team admins [add connections as data sources](https://support.google.com/appsheet/answer/15297394) to AppSheet. They can then use these data sources in their apps. Team admins can also share data sources with their team, allowing any team member to then create an app [using the connections as data sources](https://support.google.com/appsheet/answer/16322183).

#### Who can create connections?

Integration Connector connections are created in the Google Admin console so only Google Cloud admins, or those they grant permissions to, can create connections in their project.

Once the connections are created, and AppSheet is configured and granted access to use connections in the project, AppSheet team admins can [add the connections as data sources](https://support.google.com/appsheet/answer/15297394) to AppSheet, just like any other data source.

#### Who can add connections to AppSheet?

Only AppSheet team admins can [add connections as data sources](https://support.google.com/appsheet/answer/15297394) to AppSheet. They can then use these data sources in their apps. Team admins can also share data sources with their team, allowing any team member to then create an app [using the connections as data sources](https://support.google.com/appsheet/answer/16322183).

#### Are there limits?

AppSheet does not have explicit limits, however, there are [*best practices*](https://support.google.com/appsheet/answer/15297394?sjid=15239340109349366459-NA#add-connection-as-data-source) to optimize for performance. 

Limits, quotas, and charges for use of the Integration Connectors connections themselves are subject to the customer’s specific [*Application Integration plan*](https://cloud.google.com/application-integration/pricing).  In addition, there are performance quotas and [*overall limits*](https://cloud.google.com/integration-connectors/docs/quotas) and each connector might have constraints.  See the [*connector*](https://cloud.google.com/integration-connectors/docs/all-integration-connectors) for details on specific constraints. 

#### What is the difference between using the existing BigQuery connection method and the new BigQuery connector?

The following table compares the [existing BigQuery connection method](https://support.google.com/appsheet/answer/11905680) with the new [BigQuery connector](https://support.google.com/appsheet/answer/15297394).

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Feature**                                        | **BigQuery data source**                           | **BigQuery using Integration Connectors (private   |
|                                                    |                                                    | preview)**                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Maximum number of rows                             | 100,000 rows plus [security                        | No maximum.                                        |
|                                                    | filters](ht                                        |                                                    |
|                                                    | tps://support.google.com/appsheet/answer/10104488) | **Note**:  We recommend using security filters to  |
|                                                    | to select the most relevant rows first             | keep the number of rows returned below 100,000 for |
|                                                    |                                                    | performance and to avoid timeouts, especially for  |
|                                                    | **Note**: In some cases, the provider-specific row | tables with many columns.                          |
|                                                    | limit may be lower than this maximum limit.        |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Subscription plan                                  | AppSheet Enterprise Plus account as BigQuery       | -   AppSheet Enterprise Plus account as BigQuery   |
|                                                    | connector is considered an advanced connector      |     connector is considered an advanced connector  |
|                                                    |                                                    | -   Application Integration Plan (see [pricing     |
|                                                    |                                                    |     plans](https://                                |
|                                                    |                                                    | cloud.google.com/application-integration/pricing), |
|                                                    |                                                    |     including a free tier)                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Initial setup                                      | Configure BigQuery in Google Cloud and create      | Configure Integration Connector to BigQuery in     |
|                                                    | service accounts and JSON keys. See [Use data from | Google Cloud and grant access to the service       |
|                                                    | Google BigQuery with the BigQuery data             | account created by the AppSheet team. See [Use     |
|                                                    | source](htt                                        | BigQuery data sources with Integration             |
|                                                    | ps://support.google.com/appsheet/answer/11905680). | Connectors](htt                                    |
|                                                    |                                                    | ps://support.google.com/appsheet/answer/15297394). |
|                                                    |                                                    |                                                    |
|                                                    |                                                    | **Note**: For the private preview release,         |
|                                                    |                                                    | AppSheet will create the service account on your   |
|                                                    |                                                    | behalf and then give you the name so you can then  |
|                                                    |                                                    | grant access.                                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Security                                           | AppSheet access to BigQuery is granted to a        | Follows [best security                             |
|                                                    | service account and a key is generated for that    | practices](https://cloud.google.com/iam/docs       |
|                                                    | service account in the Google Cloud console.  The  | /best-practices-for-managing-service-account-keys) |
|                                                    | secure key is then manually entered into AppSheet  | by avoiding user-managed service account keys.     |
|                                                    | so no passwords or credentials are shared.         |                                                    |
|                                                    |                                                    | AppSheet access to BigQuery is granted directly to |
|                                                    | The key used in AppSheet needs to be updated when  | a service account and is centralized in the Google |
|                                                    | the credentials for the service account are        | Cloud console so service account keys no longer    |
|                                                    | rotated.                                           | need to be created, manually entered, or refreshed |
|                                                    |                                                    | into AppSheet, reducing exposure.                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

#### Is this like a team cloud data source?

Yes, when an AppSheet organization admin sets up the integration to a data source within a Google Cloud project, that data source is created and can be shared with a team so it is available to any AppSheet app editor on that team.

#### Are there sync performance differences?

During the preview, we will measure performance across both methods for comparison.

#### How do I stop allowing AppSheet to connect to the Integration Connector?

Yes. If you no longer need to use your Integration Connector as an AppSheet data source, you can [stop allowing AppSheet to connect to your connector](https://support.google.com/appsheet/answer/15297394#stop-allowing-appsheet-connect). Optionally, you can then [delete the data source](https://support.google.com/appsheet/answer/10106309#delete).

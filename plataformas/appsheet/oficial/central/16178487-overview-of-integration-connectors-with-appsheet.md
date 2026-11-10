---
fonte: https://support.google.com/appsheet/answer/16178487?hl=en
baixado: 2026-11-10
---

# Overview of Integration Connectors with AppSheet

This is a **preview release** of Integration Connectors with AppSheet. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

Integration Connectors with AppSheet (preview) requires an **AppSheet Enterprise Plus** account.

[Google Cloud Integration Connectors](https://cloud.google.com/integration-connectors/docs/overview) let you expose your enterprise data in different applications and integrations, including AppSheet. The connections you create in Google Cloud can be used as data sources in AppSheet. 

Learn how to use Integration Connectors with AppSheet as described in the following sections:

- [Supported Integration Connectors](#supported-connections)
- [Get started](#get-started)
- [Use Integration Connectors with AppSheet](#use)
- [Limitations when using Integration Connectors with AppSheet](#limitations)

## Supported Integration Connectors

You can add connections as data sources in AppSheet using the following Integration Connectors.

|                                                                                                                             |                                                                                                                                    |                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Connectors for Google Services**                                                                                          |                                                                                                                                    |                                                                                                                                                        |
| Alloydb  [AlloyDB](https://cloud.google.com/integration-connectors/docs/connectors/alloydb/configure)                       |    Google BigQuery  [BigQuery](https://cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)                 |  Bigtable  [Bigtable](https://cloud.google.com/integration-connectors/docs/connectors/bigtable/configure)                                              |
|    [Cloud Spanner](https://cloud.google.com/integration-connectors/docs/connectors/cloudspanner/configure)                  |    [Cloud SQL - MySQL](https://cloud.google.com/integration-connectors/docs/connectors/cloudsqlformysql/configure)                 |    [Cloud SQL - PostgreSQL](https://cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure)                           |
|    [Cloud SQL - SQL Server](https://cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure) |                                                                                                                                    |                                                                                                                                                        |
| Connectors for other applications                                                                                           |                                                                                                                                    |                                                                                                                                                        |
|  [Acumatica](https://cloud.google.com/integration-connectors/docs/connectors/acumatica/configure)                           |   Airtable  [Airtable](https://cloud.google.com/integration-connectors/docs/connectors/airtable/configure)                         |  [Amazon S3](https://cloud.google.com/integration-connectors/docs/connectors/amazons3/configure)                                                       |
| Asana  [Asana](https://cloud.google.com/integration-connectors/docs/connectors/asana/configure)                             |   [Azure DevOps](https://cloud.google.com/integration-connectors/docs/connectors/azuredevops/configure)                            |    Azure Synapse  [Azure Synapse](https://cloud.google.com/integration-connectors/docs/connectors/azuresynapse/configure)                              |
|    CockroadDB  [CockroachDB](https://cloud.google.com/integration-connectors/docs/connectors/cockroachdb/configure)         |  [Dynamic 365](https://cloud.google.com/integration-connectors/docs/connectors/dynamics365/configure)                              | [EnterpriseDB](https://cloud.google.com/integration-connectors/docs/connectors/enterprisedb/configure)                                                 |
|  [Freshbooks](https://cloud.google.com/integration-connectors/docs/connectors/freshbooks/configure)                         |   Hubspot  [HubSpot](https://cloud.google.com/integration-connectors/docs/connectors/hubspot/configure)                            |      IBM Db2  [IBM Db2](https://cloud.google.com/integration-connectors/docs/connectors/db2/configure)                                                 |
|   Jira Cloud  [Jira Cloud](https://cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure)             |   Jira Server  [Jira Server (Data Center)](https://cloud.google.com/integration-connectors/docs/connectors/jiraserverdc/configure) |    Jira Service Management  [Jira Service Management](https://cloud.google.com/integration-connectors/docs/connectors/jiraservicemanagement/configure) |
|     [MariaDB](https://cloud.google.com/integration-connectors/docs/connectors/mariadb/configure)                            | Monday  [Monday](https://cloud.google.com/integration-connectors/docs/connectors/monday/configure)                                 |    MySQL  [MySQL](https://cloud.google.com/integration-connectors/docs/connectors/mysql/configure)                                                     |
|  [Neo4j](https://cloud.google.com/integration-connectors/docs/connectors/neo4j/configure)                                   | NetSuite  [NetSuite](https://cloud.google.com/integration-connectors/docs/connectors/netsuite/configure)                           |     Oracle DB  [Oracle DB v2](https://cloud.google.com/integration-connectors/docs/connectors/oracledb/configure)                                      |
|   [Oracle Sales Cloud](https://cloud.google.com/integration-connectors/docs/connectors/oraclesalescloud/configure)          |     PostgreSQL  [PostgreSQL](https://cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)                 |    Redshift  [Redshift](https://cloud.google.com/integration-connectors/docs/connectors/redshift/configure)                                            |
|  [Sage Intacct](https://cloud.google.com/integration-connectors/docs/connectors/sageintacct/configure)                      |      Salesforce  [Salesforce](https://cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)                |   AP ERP  [SAP ERP](https://cloud.google.com/integration-connectors/docs/connectors/saperp/configure)                                                  |
|    SAP ASE (Sybase)  [SAP ASE (Sybase)](https://cloud.google.com/integration-connectors/docs/connectors/sybase/configure)   | [SAP Hybris C4C](https://cloud.google.com/integration-connectors/docs/connectors/saphybrisc4c/configure)                           |     [ServiceNow](https://cloud.google.com/integration-connectors/docs/connectors/servicenow/configure)                                                 |
|   [SingleStore](https://cloud.google.com/integration-connectors/docs/connectors/singlestore/configure)                      |    [Snowflake](https://cloud.google.com/integration-connectors/docs/connectors/snowflake/configure)                                |  [SQL Server](https://cloud.google.com/integration-connectors/docs/connectors/sqlserver/configure)                                                     |
|    Streak  [Streak](https://cloud.google.com/integration-connectors/docs/connectors/streak/configur)                        |   Trello  [Trello](https://cloud.google.com/integration-connectors/docs/connectors/trello/configure)                               |   Workday  [Workday](https://cloud.google.com/integration-connectors/docs/connectors/workday/configure)                                                |
|  [Xero](https://cloud.google.com/integration-connectors/docs/connectors/xero/configure)                                     |   Zendesk  [Zendesk](https://cloud.google.com/integration-connectors/docs/connectors/zendesk/configure)                            |     Custom connectors  [Custom connectors](https://cloud.google.com/integration-connectors/docs/custom-connectors)                                     |

You will need an Application Integration plan to create connections in Google Cloud. **Connection and data processing charges may apply**. See [Application Integration pricing](https://cloud.google.com/application-integration/pricing) and the [Google Cloud Integration Connectors with AppSheet FAQ](https://support.google.com/appsheet/answer/15405481).

## Get started

Watch a quick tour of using Integration Connectors with AppSheet.

Video: https://www.youtube.com/watch?v=mfda9\_-wGa4

## Use Integration Connectors with AppSheet

To use Integration Connectors with AppSheet, do the following steps:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Step**                                           | **Description**                                    | **Completed by**                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 1                                                  | [Set up Integration Connectors with                | AppSheet team admin &\                             |
|                                                    | AppSheet](ht                                       | Google Cloud admin                                 |
|                                                    | tps://support.google.com/appsheet/answer/16178778) |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 2                                                  | [Add a connection as a data                        | AppSheet team admin                                |
|                                                    | source](https://support.google.com/appsh           |                                                    |
|                                                    | eet/answer/15297394#add-connection-as-data-source) |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| 3                                                  | [Use the connection as a data source in an         | AppSheet team member                               |
|                                                    | app](ht                                            |                                                    |
|                                                    | tps://support.google.com/appsheet/answer/16322183) |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Limitations when using Integration Connectors with AppSheet 

Consider the following limitations when using Integration Connectors with AppSheet:

- Review the [known limitations for Integration Connectors](https://cloud.google.com/integration-connectors/docs/quotas).
- Connections with authentication override enabled are not supported at this time. 
- If a column in a connected data source isn't explicitly set to be editable, AppSheet considers the column to be read-only.
- There are complex types in Google BigQuery that aren't supported by AppSheet, including `Array`, `Bytes`, `Geography`, and `Struct`. These types are displayed as `String`.

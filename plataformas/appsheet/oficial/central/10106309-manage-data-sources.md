---
fonte: https://support.google.com/appsheet/answer/10106309?hl=en
baixado: 2026-11-10
---

# Manage data sources

Your AppSheet account always has a primary data source used for account authentication (commonly Google Drive), and spreadsheets from that account can be used in your apps. In addition, you can add other data sources. All data sources in your account are available when you create or add tables to your AppSheet app.

Manage data sources as described in the following sections.

- [Summary of data source types](#summary)
- [View data sources](#view-data-sources)
- [Add a data source](#add)
- [Use a data source in your app](#use-data-source)
- [Copy an app table to a new data source](#copy-data-new-source)
- [Delete a data source](#delete)

## Summary of data source types

The following table summarizes the data source types that can be used with AppSheet in the following categories: native, spreadsheets, databases, other data or provider services, and connections using Integration Connectors.

+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| **Native**                    | **Spreadsheets**              | **Databases**                 | **Other data or provider      | **Connections using           |
|                               |                               |                               | services**                    | Integration Connectors        |
|                               |                               |                               |                               | (preview) **                  |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| [AppSheet                     | -   [Google                   | -   [AWS                      | -   [Airt                     | -   Google BigQuery  Google   |
| datab                         |     Sh                        |     Dyna                      | able](https://support.google. |     BigQuery                  |
| ases](https://support.google. | eets](https://support.google. | moDB](https://support.google. | com/appsheet/answer/10106767) | -   Jira Cloud  Jira Cloud    |
| com/appsheet/answer/12631542) | com/appsheet/answer/10106594) | com/appsheet/answer/10106600) | -   [Ap                       | -     PostgreSQL  PostgreSQL  |
|                               | -   [Microsoft                | -   [Google                   | igee](https://support.google. | -   Salesforce  Salesforce    |
|                               |     Excel](ht                 |     BigQ                      | com/appsheet/answer/10106762) | -    ServiceNow               |
|                               | tps://support.google.com/apps | uery](https://support.google. | -   Box                       |                               |
|                               | heet/answer/10106311) (Office | com/appsheet/answer/11905679) | -   Dropbox                   | For details, see [Use Google  |
|                               |     365 and SharePoint)       | -   [Mar                      | -   [Google                   | Cloud Integration Connectors  |
|                               |                               | iaDB](https://support.google. |     Cale                      | with                          |
|                               |                               | com/appsheet/answer/10106677) | ndar](https://support.google. | AppS                          |
|                               |                               | -   [M                        | com/appsheet/answer/10106764) | heet](https://support.google. |
|                               |                               | ySQL](https://support.google. | -   [Google                   | com/appsheet/topic/15297774). |
|                               |                               | com/appsheet/answer/10106676) |     D                         |                               |
|                               |                               | -   [On-premises              | rive](https://support.google. |                               |
|                               |                               |     data                      | com/appsheet/answer/11905920) |                               |
|                               |                               | base](https://support.google. | -   [Google                   |                               |
|                               |                               | com/appsheet/answer/10106597) |     For                       |                               |
|                               |                               | -   [Or                       | ms](https://support.google.co |                               |
|                               |                               | acle](https://support.google. | m/appsheet/answer/10106596)\* |                               |
|                               |                               | com/appsheet/answer/10106766) | -   [Gmail                    |                               |
|                               |                               | -   [Postgr                   | ](https://support.google.com/ |                               |
|                               |                               | eSQL](https://support.google. | appsheet/answer/15699343)\*\* |                               |
|                               |                               | com/appsheet/answer/10106598) | -   [Looker                   |                               |
|                               |                               | -   [SQL                      |     St                        |                               |
|                               |                               |     Se                        | udio](https://support.google. |                               |
|                               |                               | rver](https://support.google. | com/appsheet/answer/11911810) |                               |
|                               |                               | com/appsheet/answer/10106599) | -   [O                        |                               |
|                               |                               |                               | Data](https://support.google. |                               |
|                               |                               |                               | com/appsheet/answer/10106380) |                               |
|                               |                               |                               | -   [Salesf                   |                               |
|                               |                               |                               | orce](https://support.google. |                               |
|                               |                               |                               | com/appsheet/answer/10106381) |                               |
|                               |                               |                               | -   [Smarts                   |                               |
|                               |                               |                               | heet](https://support.google. |                               |
|                               |                               |                               | com/appsheet/answer/10107843) |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+

**Note**: 

\* When using a Google Forms data source in your app, a read-only table is added.

\*\* At this time, a Gmail data source can only be used within the context of an automation. Gmail events are triggered by external sources. See [Externally triggered events](https://support.google.com/appsheet/answer/11445188#externally-triggered-events). When you connect a Gmail account to your AppSheet app when adding a Gmail event to an automation, it is added as a data source but no table is added to your app. You can [view](#view-data-sources) or [delete](#delete) the Gmail data source.

## View data sources

To view data sources, go to the **My account \> Sources**.

The data sources that are currently available for your use are shown, including:

- Account data sources added by you. See [Add data sources](#add) (below).
- Team data sources added by team members. See [Share data sources with your team](https://support.google.com/appsheet/answer/10104795#share-data-sources).

## Add a data source

You don't need to add [AppSheet databases](https://support.google.com/appsheet/answer/12631542) to your account in order to use them in your apps. They are native to AppSheet and once created, they are available to your apps by default. 

You can also add a data source when creating an app using a Google Workspace add-on, such as [Google Sheets AppSheet add-on](https://workspace.google.com/marketplace/app/appsheet/376242260902) or  [Google Forms AppSheet add-on](https://workspace.google.com/marketplace/app/appsheet/865237847665).

To add a data source, do the following:

1.  Do one of the following:
    - To add a data source to your account, go to the **My account \> Sources** and click **+ New Data Source**.
    - To add a data source when creating an app, go to the **My Apps** page, select + **Create \> App \> Start with existing data**, and select **+ New source** when choosing your data.
      **Note**: This method is not applicable to Gmail data sources.
    - To add a data source to an existing app, open the app in the editor, go to **Data**, click **+**, and click **+ New source**.

    The Add data source wizard displays.
2.  Choose one of the following options:
    - **Use AppSheet** - To add a data source using AppSheet. Proceed to step 3.
    - **Use Integration Connectors** - To add an Integration Connector as a data source. Go to [Set up Integration Connectors](https://support.google.com/appsheet/answer/16178778) and [Add and use connections as data sources](https://support.google.com/appsheet/answer/15297394).
      **Note:** The Use Integration Connectors option is only available to [AppSheet team admins](https://support.google.com/appsheet/answer/13691133#supported-roles).
3.  Click the type of data source that you want to add.
4.  Follow the prompts to name and authenticate your new data source. 
5.  Optionally, you can [share the data source with your team](https://support.google.com/appsheet/answer/10104795#share-data-sources).

## Use a data source in your app

Use a data source in your app when you [create an app](https://support.google.com/appsheet/answer/11980957) from existing data or [add a table](https://support.google.com/appsheet/answer/10105821#add) to an existing app. The same app can add tables from multiple data sources.

## Copy an app table to a new data source

To copy an app table to a new data source:

1.  Open in the app editor the app containing the table that you want to copy.
2.  Go to **Data ** .
3.  Select the table in the list.
4.  Click **Table settings**  Table settings icon  in the table header.
5.  Expand the **Storage** section.
6.  Click **Copy Data to New Source** adjacent to the **Data Source** field.
7.  Select a data source from the list of available data sources.
    The data source type must be compatible with the data being saved; otherwise, an error is returned.
8.  Enable the **Include file data** option, if required.
9.  Click **Copy data**.
    A message displays indicating whether or not the data was copied successfully.
10. Click **Close**.

## Delete a data source 

You can delete a data source that you own.

**Notes**:

- Before you delete a data source, be sure to remove any related tables from existing apps. Otherwise, the apps may no longer execute as expected.
- Before you delete an Integration Connector data source, [stop allowing AppSheet to connect to the Integration Connector](https://support.google.com/appsheet/answer/16085546).
- If the data source is shared with your team, it will no longer be accessible to other members of your team after you delete it.

To delete a data source: 

1.  Go to the **My account \> Sources**.
    You can view all of the data sources that are currently available for your use.
2.  Locate the data source you want to delete.
3.  Select  More menu options  **More** **\> Delete**.

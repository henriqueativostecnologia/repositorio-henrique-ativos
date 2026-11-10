---
fonte: https://help.asana.com/s/article/power-bi-integration?language=en_US
baixado: 2026-11-10
---

# Power BI integration

**Available on Asana [Advanced](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise) and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Business and Legacy Enterprise. Visit our [*pricing page*](https://asana.com/pricing) for more information.**

The Asana Power BI Connector enables Power BI to connect directly to Asana to retrieve data about your tasks in a specified project, team, or portfolio.  After the Power BI dashboards have been configured, they can be shared with other Power BI users within the organization.

## Use cases

Power BI amplifies your business insights and the value of your Asana data. From Power BI visuals to embedded analytics, your team will gain insights, see opportunities and gain a competitive advantage.

For example, suppose a project manager wants to add Asana data to internal BI reporting. In that case, they can add Asana as a data source to Power BI to build more up-to-date reports and tell a compelling story.

When asked to deliver key insights about a team using Asana, a team lead can filter and group data in Power BI to build reports more tailored to the business that spots trends and make data-driven decisions.

## Supported Asana data for exports

Portfolios, portfolio and project status updates, goals, allocations, projects, tasks, subtasks, and their associated custom fields.

## Requirements for installation

- Access to BI Desktop (Windows only) for full customization, dashboard creation, and publishing
- Access to Power BI Service (online) to view data with template or published dashboards

> If synching data from a team, the team needs to be on an [Enterprise](https://asana.com/enterprise) or [Enterprise+](https://asana.com/enterprise) plan in Asana

## How to connect

1.  Right-click [here](https://asana.com/downloads/AsanaV2-071625.mez) and select **Copy Link Address**
2.  Paste the link in a new tab to download the connector (.mez) file. If you encounter an error, change the language picker of the Help Center to English and that should allow you to download the file.
3.  Open Power Bi Desktop
4.  Click **Get Data**
5.  Under **Online Services**, find Asana and click **Connect**
6.  Enter the URL to the Asana team or portfolio you would like to analyze
7.  Put the connector file with the extension *.mez* in your local *\[Documents\]\Microsoft Power BI Desktop\Custom Connectors* folder. If the folder doesn't exist, create it.
8.  To adjust the data extension security settings, in Power BI Desktop, select **File** \> **Options and settings** \> **Options** \> **Security**
9.  Under **Data Extensions**, select **Allow any extension to load without validation or warnin**
10. Select **OK**, and then restart Power BI Desktop
11. Click Get Data, and search **Asana V2**
12. Enter the Asana URL you want to export into Power BI
    1.  If you are looking to exclude tasks data from your export, add ?export_tasks=false at the end of the URL. For example, [app.asana.com/0/portfolio/{...}/{...}?export_tasks=false](http://app.asana.com/0/portfolio/%7B...%7D/%7B...%7D?export_tasks=false) will export portfolio and project level data without tasks
13. You may be prompted to sign in to Asana and grant permission to Power BI to retrieve your data. Please sign in with a user that has access to your data.

### How to create a dashboard from exported data:

**Data is broken out into modular schema.** Click the checkboxes for the tables you want to export, then click **Load**.

You may choose to transform the retrieved data before using it to build a dashboard.

Your task data should now be syncing with Power BI. This can take anywhere from a few seconds to 10 minutes, depending on the size of the team or portfolio you specified.

Once the data is loaded, you’ll be able to start creating a dashboard using the available fields on the right.

If you export fewer than 1000 tasks, you’ll always receive real-time export from Asana.

If you export more than 1000 tasks, you’ll receive the most up-to-date data with the first data load. Subsequent updates happen every 4 hours (If you reload your dashboard within the 4-hour window, you’ll still complete data loading successfully but you won’t receive the latest data).

> You can choose to expand the custom field data and pivot the custom field values so that they show up as individual columns in your dataset.

## How to set up scheduled refresh with PowerBI online

After you complete building the dashboard, you can optionally set up scheduled refresh with PowerBI online following the instructions below (Alternatively, you can follow [this video](https://drive.google.com/file/d/1xkq6iC2LdKKudE0yBqrqEd7KX68XmuCH/view?usp=sharing) for scheduled refresh setup).

**Prerequisite**: Download and install from [Install an on-premises data gateway \| Microsoft Learn](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-install#download-and-install-a-standard-gateway)

1.  Set Up the Gateway

    1.  Place your connector file in a designated folder.
    2.  Open the installed gateway software and log in via the **Status** tab.
    3.  Go to the **Connectors** tab, add the folder path containing the connector, and verify that it appears under "Custom data connectors." Leave the gateway application running.

2.  Configure Gateway in Power BI Online

    1.  Log in to Power BI Online: [https://app.powerbi.com/](https://app.powerbi.com/).
    2.  Navigate to Settings → Manage Connections and Gateways.
    3.  Switch to On-premises data gateways:
        1.  Locate your custom connector.
        2.  Expand its settings and check:
            1.  Allow user's cloud data sources to refresh through this gateway cluster.
            2.  Allow user's custom data connectors to refresh through this gateway cluster.

3.  Create a Connection

    1.  In Manage Connections and Gateways, switch to the Connections tab
    2.  Create a new connection:
        1.  switch to connection tab and create new connection
        2.  For gateway cluster use entity create on a previous step
        3.  For connection type select Asana V2
        4.  For url use the same link to team/portfolio/project as what was user on power bi report
        5.  Under Authentication provide valid Asana credentials for Asana via 'Edit credentials'

4.  Configure the Published Report

    1.  in Power BI Online, locate the uploaded report under [OneLake](https://app.powerbi.com/onelake/).
    2.  Open **Settings** for the report and find the "Use an On-premises or VNet data gateway" section:
        1.  Enable Use an On-premises or VNet data gateway.
        2.  Select the data source connection created in Step 4.

## Limitations

Exported data with more than 1000 tasks refresh every 4 hours. You’ll receive the most up-to-date data with the first data load. Subsequent updates happen every 4 hours (If you reload your dashboard within the 4-hour window, you’ll still complete data loading successfully but you won’t receive the most up-to-date data).

Custom field value change history, or Full domain exports.

> Like what you see? Get started with a free Asana trial today. [Try for free](https://asana.com/create-account "Try for free").

## Example dashboard

 

This example shows how work management data from Asana can provide insight into how your team works. Use the Asana for Power BI Integration to access Asana, including tasks, custom fields, tags, projects, and more.

> Combine Asana data with other datasets to take a holistic approach to your business.

 

[](https://forum.asana.com/c/forum-en/tips/6)

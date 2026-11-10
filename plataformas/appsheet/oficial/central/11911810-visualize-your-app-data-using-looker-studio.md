---
fonte: https://support.google.com/appsheet/answer/11911810?hl=en
baixado: 2026-11-10
---

# Visualize your app data using Looker Studio

[Looker Studio](https://cloud.google.com/looker/docs/studio/) (formerly Data Studio) is a free reporting and dashboarding tool that enables you to generate fully customizable visualizations of your app data. You can combine data from multiple data sources to generate a rich dashboard to share with stakeholders.

For example, the following dashboard built using Looker Studio shows charts and reports for facility inspections.

To visualize your app data using Looker Studio:

- [Create an AppSheet data source in Looker Studio](#create-data-source)
- [Use Looker Studio to visualize data from your AppSheet app](#use-datastudio)

See also: [Quick start: Visualize your app data using Looker Studio](https://support.google.com/appsheet/answer/12176287)

## Create an AppSheet data source in Looker Studio

Create an AppSheet data source in Looker Studio that is associated with your AppSheet account. You can create an *embedded* or *reusable* data source. See [Embedded versus reusable data sources](https://cloud.google.com/looker/docs/studio/embedded-data-sources).

The following steps describe how to create a reusable data source:

1.  Sign in to [Looker Studio](https://datastudio.google.com/).

2.  Select **Create \> Data source**.

3.  Edit the data source name and click **AppSheet**.

    Set the name to My Data Source and search for and click AppSheet

4.  If prompted, click **Authorize** and follow the prompts to authorize access to your AppSheet account.

    AppSheet integration dialog prompting for username and token

5.  Select the region to connect to in the **Region** drop-down.

6.  Select the app to access the data source in the **Application** field.

7.  Click **Next**.

8.  Select a table to use as the data source in the **Table** field.

9.  Click **Connect**.

## Use Looker Studio to visualize data from your AppSheet app

You must be an **app creator** or **app editor** to visualize your app data using Looker Studio. You can only access your AppSheet apps created with the same Google account.

Use Looker Studio to visualize data from your AppSheet app as described in the following sections.

## Configure the data source

The data source fields panel is where you configure the data source by renaming fields and adding descriptions, adding calculated fields, and changing data types and aggregations. Learn more about how to [model your data](https://support.google.com/looker-studio/answer/6402048).

## Control who sees the data

At the top of the fields panel, you can change the data credentials. Credentials control who can see the data that this data source provides.

**OWNER'S CREDENTIALS **let other people view or create reports that use this data without requiring them to have their own access to the dataset.

**VIEWER'S CREDENTIALS**, on the other hand, require each user of the data source to provide their own credentials to access the dataset.

Learn more about [data credentials](https://support.google.com/looker-studio/answer/6371135).

## Create a new report from the data source

To create a new report from the data source, follow these steps:

1.  In the upper right, click **CREATE REPORT**. The report editor appears.
2.  Click **ADD TO REPORT**.
    1.  This action adds the data source to the report.
    2.  You can now create charts and controls that get their data from this data source.

### New to Looker Studio?

See:

- [Create a new report](https://support.google.com/looker-studio/answer/6292570) tutorial
- [Add charts and controls to your report](https://support.google.com/looker-studio/answer/6371822)

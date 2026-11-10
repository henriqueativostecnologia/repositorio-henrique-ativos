---
fonte: https://support.google.com/appsheet/answer/12176287?hl=en
baixado: 2026-11-10
---

# Quick start: Visualize your app data using Looker Studio

In this Quick Start, you'll copy the AppSheet Facility Inspections app template and then use the app to create an AppSheet data source in Looker Studio and create a report. See also: [Visualize your app data using Looker Studio](https://support.google.com/appsheet/answer/11911810)

The steps are as follows:

1.  [Create an app in AppSheet](#create-app)
2.  [Create an AppSheet data source in Looker Studio](#create-data-source)
3.  [Create a report in Looker Studio](#create-report)
4.  [View and share the report](#view-report)

### Create an app in AppSheet

For this demo, you'll copy the [**Facility Inspections**](https://www.appsheet.com/templates/Inspect-points-throughout-various-properties?appGuidString=d8389191-0217-42c0-bd50-406993b660f6) app template.

1.  Sign in to [AppSheet](https://www.appsheet.com).
2.  Click **Templates** in the top navigation bar to view the Sample app templates.
3.  Locate the **Facility Inspections** app template and click **Copy**.
4.  Optionally, you can update the **App name** and choose a category from the **Category** drop-down.
5.  Click **Copy app**.

### Create an AppSheet data source in Looker Studio

To create an AppSheet data source in Looker Studio:

1.  Go to Looker Studio and create an AppSheet data source:

    [Create an AppSheet data source](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxy0_bVIUsKVRWtvA0fJfEq_F_wdP2whFOQGskykubSizkpmQojrOFMe1EN9rz6klk0)

2.  In the Region drop-down, select the region to connect to.

3.  In the Application field, select the **Facility Inspections** app.

    Facility Inspections is selected in the Application drop-down

4.  Click **Next**.

5.  Select a table to use as the data source in the **Table** field.

6.  Click **Connect**.

My Data Source is opened in Looker Studio. You can configure the fields in the editor. For this demo, you'll use the default list.

My Data Source in Data Studio

### Create a report in Looker Studio based on the AppSheet data source

To create a report in Looker Studio based on the AppSheet data source:

1.  Click **Create Report**.

    Create report button in AppSheet UI
2.  If prompted to confirm adding My Data Source to the report, click **Add to Report**.

    You are about to add data to this report dialog with the Add to Report button highlighted
3.  An Untitled Report is created.

    A default table is added to the report with Inspection ID and Facility ID columns.

4.  Configure the table.
    1.  Left-click and drag the table to the bottom of the canvas. Resize the table using the handles to fit across the width of the canvas.

    2.  Ensure that the table is selected, click the **Data** tab in the right pane, and do the following:
        1.  Ensure that **Date Range Dimension** is set to **Inspection Date**.
        2.  Under Dimension, add (drag and drop) the following fields in the order shown:
            - **Inspection Date**
            - **Inspected By**
            - **Facility ID**
            - **Area Organized?**
            - **Doors Locked?**
            - **Garage Emptied? **
        3.  Delete **Facility ID** under Metric.
    3.  Adjust the column widths, as desired.

        The table appears similar to the following:

5.  To allow users to filter the report by Facility ID:
    1.  Select **Add a control \> Drop-down control**.

        Drop-down list item in the Add a control list
    2.  Drag and drop the element in the top center of the canvas.

        Drag and drop the Facility ID field to the top center of the canvas
    3.  Make sure the **Control field** is set to **Facility ID**.
6.  To allow users to filter the report by date:
    1.  Select **Add a control \> Drop-down control**.

        Date range control in the Add a control menu
    2.  Drag and drop the element to the right of the Facility ID drop-down list filter.
        **Note**: You may need to adjust the placement of the Facility ID filter to fit both filters.

        Drag and drop elements to the upper right corner
7.  Add a pie chart to show number of inspections by facility:
    1.  Select **Add a chart \> Pie Chart**.

        Add a pie chart
    2.  Drag and drop the element in the top left of the canvas.

        Drag and drop pie chart in the top left of the canvas
    3.  Ensure that the pie chart is selected, click the **Data** tab in the right pane, and do the following:
        1.  Ensure that **Date Range Dimension** is set to **Inspection Date**.
        2.  Under **Dimension**, add (drag and drop) **Facility ID** to replace the existing value.
        3.  Ensure **Metric** is set to **Inspection ID**.
        4.  Ensure that **Cross-filtering** is enabled.
    4.  Click the **Style** tab in the right pane and do the following:
        1.  In the **Label** section, change Percentage to **Value**
        2.  In the **Legend** section, adjust the settings to show the legend centered and below the pie chart.

        For example:

        Pie chart with legend at the bottom
8.  Add another pie chart to show number of inspections by facility:
    1.  Select **Add a chart \> Pie Chart**.
    2.  Drag and drop the element in the top right of the canvas, below the filters.
    3.  Ensure that the pie chart is selected, click the **Data** tab in the right pane, and do the following:
        1.  Ensure that **Date Range Dimension** is set to **Inspection Date**.
        2.  Under **Dimension**, add (drag and drop) **Area organized?** to replace the existing value.
        3.  Ensure **Metric** is set to **Inspection ID**.
    4.  Click the **Style** tab in the right pane and do the following:
        1.  In the **Label** section, change Percentage to **Value**
        2.  In the **Legend** section, adjust the settings to show the legend centered and below the pie chart.

The final report canvas should look similar to the following:

### View and share the report

1.  Click **View** to view and interact with the report.
2.  Set the filters to view data for a particular facility.

    Filter report by Facility
3.  Select a specific date range to narrow the results.

    Filter report by date
4.  Click within a pie chart to further filter the results.

5.  Share the report.

    For example, select **Share \> Schedule email delivery** to schedule email delivery to a list of recipients.

    Select Schedule email delivery from Share menu
6.  Configure the email delivery and click **Schedule**.

    Email delivery configuration dialog with From, To, Start time, and Repeat fields

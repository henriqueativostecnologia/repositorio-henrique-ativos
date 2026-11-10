---
fonte: https://support.google.com/appsheet/answer/10107847?hl=en
baixado: 2026-11-10
---

# Chart view type

In general, charting is a complex topic. As the designer of a chart, you typically have to make three choices:

- How many individual series *lines* do you draw?
- What values are on the X and Y axes?
- What chart display type do you use, such as line, bar chart, and so on?

We have tried to keep it simple by limiting the possible answers for each of these choices:

- **Row Series chart** - Appropriate for spreadsheet data where most of the data is numeric on a uniform scale (such as monthly sales data). Every row forms a series, each of which is identified by the row key. You choose a subset of the column names that will be charted on the X axis. The Y axis is based on the numeric values in the row cells. You can choose a line chart, a bar chart, or a stacked bar chart as the display type.
- **Column Series chart** - Appropriate for spreadsheet data with just a few rows corresponding to items to compare (such as monthly sales data by category). Every column forms a series, each of which is identified by the column name. Each row (using its row key column) forms one entry on the X axis. The Y axis is based on the numeric values in the row cells. You can choose a line chart, a bar chart or a stacked bar chart as the display type.
- **Histogram** - Special kind of bar chart to show aggregate distributions. For example, if you want to see the number of customers who purchased each automobile model, you specify the column whose values will be aggregated. The X axis gets one entry for each unique value in this column and the Y axis shows the count of the number of rows that have that value in that column.

For a deeper dive into charts, please see [Charts: The Essentials](https://support.google.com/appsheet/answer/10107874). 

The following sections describe how to [create](#create-view) and [configure](#configure-view-options) a chart view.

## ** **Create a chart view

To create a chart view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
2.  Configure the chart view, as follows:
    - Select **chart** as the **View type** when configuring the card view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - Configure the [chart view options](#configure-view-options).
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
3.  When you are done, save your changes by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## ****Configure the chart view options

Configure the chart **View options** by using the settings described in the following table.

|                 |                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Setting**     | **Description**                                                                                                                  |
| Chart type      | Chart type. Select one of the [chart types](https://support.google.com/appsheet/answer/10107874#chart-types) from the drop-down. |
| Group aggregate | Display a numeric summary of the rows in each group. Select the format to use for the display from the drop-down.                |
| Chart columns   | Identify which columns to display in the chart. Click **Add** and select the column name. Repeat to add additional columns.      |
| Chart colors    | Customize the colors used in the chart. Click **Add** and select the color. Repeat to add additional colors.                     |
| Trend line      | Overlay the chart with a regression trend line. Select the type of trend line from the drop-down                                 |
| Show legend     | Turn on to show a legend for the chart.                                                                                          |

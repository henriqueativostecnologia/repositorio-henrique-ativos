---
fonte: https://support.google.com/docs/answer/18180907?hl=en
baixado: 2026-11-10
---

# Combo charts

A combo chart allows you to combine different chart types, such as column and line charts, within a single visualization. This is particularly useful for showing how different metrics relate to each other over time or across categories.

## Select and customize your combo chart type

When you create a combo chart in Google Sheets, you can choose from these initial types:

- **Clustered Column - Line**: Combines columns for some series and a single line for another.
  - **Important:** If there are 2 or more data series, the first half of your series will display as columns. The second half will display as lines.
- **Clustered Column - Line on Secondary Axis**: Similar to the above, but the line series uses a secondary vertical axis. This is useful for comparing data with different scales.
- [**Custom Combo**](#Combo-chart): Provides full flexibility to define each series type from the start.

After selecting an initial chart type, you can use the chart editor to change how each series is displayed.

## Format your data

To effectively create a combo chart, structure your data in a Sheet. Place categories in the first column. Use subsequent columns for numerical values of each series.

1.  **First column:** Contains categories for your chart, such as months, product names, or quarters.
2.  **Subsequent columns:** Contain numeric data for each series you want to plot.
3.  **Optional:** You can use the first row of a Sheet for the names of your data series. These appear in your chart's legend.

## Explore combo chart examples

### **Compare website visitors & conversion rate**

This chart compares website visitors (high volume) with conversion rate (percentage). It uses a secondary vertical axis to make it easier to see how traffic changes affect conversions.

|             |                                 |                                 |                         |
|-------------|---------------------------------|---------------------------------|-------------------------|
| **Quarter** | **Website Visitors from tab A** | **Website Visitors from tab B** | **Conversion Rate (%)** |
| Q1          | 75000                           | 20000                           | 2.5%                    |
| Q2          | 82000                           | 50000                           | 2.8%                    |
| Q3          | 78000                           | 15000                           | 2.3%                    |
| Q4          | 95000                           | 45000                           | 3.1%                    |

To get the data and chart, make a copy of this [Google Sheet](https://docs.google.com/spreadsheets/d/1cYby16JeocB2aIVSWdy9UfP_-pGB-n3oZ7kCzfMjnHs/copy).

## Customize a combo chart

After creating a combo chart, you can customize its appearance. Use the chart editor to adjust how each data series is represented. For example, you can choose a "Line", "Column", "Area", or "Step Area" chart. You can also assign any series to either the primary (left) or secondary (right) vertical axis.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select the chart you want to customize. This will open the Chart editor on the right side.
3.  Select the **Customize** button.
4.  Choose an option:
    - [**Chart style**](https://support.google.com/docs/answer/63824)**:** Change fonts, background, borders, and maximize options.
    - [**Chart & axis titles**](https://support.google.com/docs/answer/9085334)**:** Edit the chart title, subtitle, horizontal and vertical axis titles.
    - [**Series**](https://support.google.com/docs/answer/9085344)**:** Change individual data series types (e.g., "Column", "Line", "Area", "Step Area"), assign the series to an axis, and adjust colors, markers, data labels, and trendlines.
      1.  You can change the series type under Type.
      2.  You can choose to let a series appear on either the left or the right axis under Axis.
    - [**Legend**](https://support.google.com/docs/answer/63824)**:** Adjust the position and formatting of the chart legend.
    - [**Horizontal axis**](https://support.google.com/docs/answer/9085334)**:** Customize the axis labels, text style, and order.
    - [**Vertical axis**](https://support.google.com/docs/answer/9085334)**:** Control the left vertical axis (primary) and right vertical axis (secondary, if applicable). Options include scale, text formatting, and an axis line.
    - [**Gridlines**](https://support.google.com/docs/answer/63824)**:** Adjust major and minor gridlines for both horizontal and vertical axes.

## Related resources

- [Types of charts & graphs in Google Sheets](https://support.google.com/docs/answer/190718)
- [Add & edit a chart or graph](https://support.google.com/docs/answer/63824)
- [Add data labels, notes, or error bars to a chart](https://support.google.com/docs/answer/9085344)

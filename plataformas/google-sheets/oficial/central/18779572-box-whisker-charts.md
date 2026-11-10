---
fonte: https://support.google.com/docs/answer/18779572?hl=en
baixado: 2026-11-10
---

# Box & whisker charts

Box and whisker charts in Google Sheets are statistical charts that let you analyze data distribution, compare groups, and identify outliers.

- **Box:** Spans the interquartile range from the first quartile (25th percentile) to the third quartile (75th percentile).
- **Median line:** The line across the box representing the midpoint (50th percentile) of the dataset.
- **Whiskers:** Lines extending from the box to the lowest and highest values within 1.5 times the interquartile range.
- **Outliers:** Points plotted beyond the whiskers representing atypical values.

## Format your data

Summary statistics are calculated automatically from raw data, including the minimum, quartiles, median, maximum, and outliers.

- **First column (optional):** Enter labels or categories to group your data, like Department, Class, or Year.
- **Subsequent columns:** Enter numerical values. Each column or group generates a distinct box plot.
- **Pre-calculated data:** Use a Candlestick chart instead if your data already contains summary statistics, like min, max, or quartiles.

**Note:** Microsoft Excel spreadsheets imported into Google Sheets work automatically with box and whisker charts.

## Examples

|             |            |            |
|-------------|------------|------------|
| **Subject** | **Quiz 1** | **Quiz 2** |
| Math        | 80         | 90         |
| Math        | 76         | 85         |
| Math        | 62         | 90         |
| Math        | 76         | 78         |
| Math        | 73         | 82         |
| Math        | 63         | 93         |
| Science     | 75         | 93         |
| Science     | 87         | 100        |
| Science     | 89         | 77         |
| Science     | 80         | 90         |
| Science     | 66         | 78         |
| Science     | 89         | 82         |

## Create a box & whisker chart

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select the cells that contain the data you want to display.
3.  Select **Insert** and then **Chart**.
4.  In the Chart editor panel, select **Setup**.
5.  Under "Chart type," scroll to "Statistical" and select **Box and whisker chart**.

## Customize your chart

Modify how your statistical data and distribution appear:

1.  Open the chart you want to modify and select **Customize**.
2.  To configure display options, select **Series**:
    - **Show outlier points:** Display data points that fall outside the interquartile range whiskers.
    - **Show mean marker:** Display an indicator representing the average value of each series.
    - **Show mean line:** Connect mean markers across multiple categories.
    - **Quartile calculation:** Select whether to calculate quartiles using inclusive or exclusive median methods.
3.  **Optional:** Under "Chart & axis titles" or "Legend," add descriptive labels to your axes and data series.

## Related articles

- [Types of charts and graphs in Google Sheets](https://support.google.com/docs/answer/190718)
- [Add and edit a chart or graph](https://support.google.com/docs/answer/63824)

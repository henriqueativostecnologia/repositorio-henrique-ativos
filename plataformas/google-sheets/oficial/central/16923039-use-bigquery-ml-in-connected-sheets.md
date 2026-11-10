---
fonte: https://support.google.com/docs/answer/16923039?hl=en
baixado: 2026-11-10
---

# Use BigQuery ML in Connected Sheets

**Important:** You might need additional GCP permission to use BigQueryML in Connected Sheets. For more info, [visit the BQML reference documentation here](https://docs.cloud.google.com/bigquery/docs/timesfm-model).

To detect data anomalies, directly generate data forecasts and predict key business metrics, you can now use BigQuery ML with TimesFM models directly from Connected Sheets.

You can:

- Create forecasts and detect anomalies with BQML in Connected Sheets using the TimesFM model.
- Configure inputs and customize settings with the Forecast creator interface.
- Skip model creation and training and use Google’s TimesFM model, pre-trained on billions of real-world data points.

This feature includes:

- **Simple configuration:** Create forecasts and detect anomalies from any BigQuery dataset or custom query with a user-friendly configuration panel in the Sheets UI.
- **Customizable parameters:** Adjust input parameters like prediction horizon and confidence intervals. Filter input data to only predict based on subsets of historical data. Default options are available.
- **Granular analysis:** Break out data into multiple groupings based on any data dimension. For example, forecasts of sales broken out by region.
- **Visual insights:** Automatically generate a chart for single time-series forecasts. This chart visualizes the forecast and can optionally include historical data.

## Generate forecasts in Connected Sheets

The forecast data displays in a new sheet. For a single time-series forecast, Google Sheets automatically creates a chart that visualizes the forecast alongside historical data. [Learn more about the AI.FORECAST function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast).

1.  On your computer, open [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select an existing Connected Sheet or create a new connection to BigQuery data.
    - To create a new connection to BigQuery data, in the menu at the top, click **Data** and then **Data Analytics** and then **Connect to BigQuery**, and configure your data connection.
3.  Click Advanced analytics and then Create a forecast .
4.  From your connection’s dataset, select a time series.
    - You can automatically aggregate data points in different time windows. To see all options, next to "Group by Day," click the Down arrow Down arrow .
5.  Select a prediction column. This will be the value you wish to forecast.
    - To change the aggregation method, next to "Aggregate by Sum," click the Down arrow Down arrow .
6.  Optional: To add a breakout, click Add breakout . This creates unique forecasts for each value in this column. For example, one forecast for every region in the dataset.
    - Select an option from the dropdown.
7.  Under the "Enter horizon" field, enter a number. This determines how far in advance your data will be forecasted.
    - The forecast interval is automatically determined by the time series aggregation, if any.
    - This field has a max value of 10,000.
8.  Optional: To filter input data, next to "Filter input data," click Add .
    - Select an option from the dropdown.
9.  Under "Data output options," choose:
    - Include historical data. To help you identify trends, this option lets you match historical data with your forecast.
    - Include prediction levels. Lower and upper bounds of the forecasted value appear in additional columns.
    - Modify your forecast confidence level if desired. The default value is 95%.
10. Click **Create**.
    - Sheets runs the query and creates your forecast. To edit any inputs and re-run a forecast, click the generated forecast. This opens the Forecast Editor panel.

## Discover data errors & anomalies

You can use anomaly detection in Google Sheets to find unusual patterns in time-series data you track. This function quickly shows the difference between normal trends and actual outliers. [Learn more about the AI.DETECT_ANOMALIES function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-detect-anomalies).

1.  On your computer, open [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select an existing Connected Sheet or create a new connection to BigQuery data.
    - To create a new connection to BigQuery data, in the menu at the top, click **Data** and then **Data Analytics** and then **Connect to BigQuery**, and configure your data connection.

&nbsp;

3.  Click Advanced analytics and then Detect anomalies .
4.  From your connection’s dataset, select a time series.
    - You can automatically aggregate data points in different time windows.

&nbsp;

5.  (Optional) To change how the dataset is organized, next to “Group by Day,” click the Down arrow Down arrow .
    - **Note:** Whichever option you select affects the “Time period” field below.
6.  Select a detection column. This is where Sheets looks for anomalies.
    - To change the aggregation method, next to “Aggregate by Sum,” click the Down arrow Down arrow .

&nbsp;

7.  (Optional) To add a breakout, click Add breakout .
8.  In the “Time period” section, fill in the time span you want to review.
    - Or, you can click **Set end date instead**.
9.  (Optional) To filter input data, next to “Filter input data,” click Add .
10. Under “Data output options,” choose:
    - Customize the anomaly probability. This sets the threshold for what will be considered an anomaly or not.
    - Include prediction interval columns. The lower and upper bounds of the data range that's not considered anomalistic appears in additional columns.

&nbsp;

11. Click **Apply**.

You can find the anomalies in a new tab labeled “Anomaly Detection.” The process may take a few minutes to complete.

**Tips:**

- For easy reference, any detected anomalies are highlighted red.
- If the function fails, you can find an error message in the “Status” column.
- You can detect errors up to 10,000 points into the future.

## Related resources

- [Get started with BigQuery data in Google Sheets](https://support.google.com/docs/answer/9702507)
- [Sort & filter BigQuery data in Google Sheets](https://support.google.com/docs/answer/9702999)
- [Analyze & refresh BigQuery data in Google Sheets using Connected Sheets](https://support.google.com/docs/answer/9703214)

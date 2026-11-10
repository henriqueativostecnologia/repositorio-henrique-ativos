---
fonte: https://support.google.com/docs/answer/3093281?hl=en
baixado: 2026-11-10
---

# GOOGLEFINANCE

Fetches current or historical securities information from Google Finance.

### Sample Usage

`GOOGLEFINANCE("NASDAQ:GOOG", "price", DATE(2014,1,1), DATE(2014,12,31), "DAILY")`

`GOOGLEFINANCE("NASDAQ:GOOG","price",TODAY()-30,TODAY())`

`GOOGLEFINANCE(A2,A3)`

### Syntax

`GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date|num_days], [interval])`

- `ticker` - The ticker symbol for the security to consider. It’s **mandatory** to use **both** the exchange symbol and ticker symbol for accurate results and to avoid discrepancies. For example, use “NASDAQ:GOOG” instead of “GOOG.”

  - If the exchange symbol is not specified, `GOOGLEFINANCE` will use its best judgement to choose one for you.

  - Reuters Instrument Codes are no longer supported. Use TSE:123 or ASX:XYZ instead of ticker 123.TO or XYZ.AX.

  - Not all futures are supported at this time.

- `attribute` - **\[** OPTIONAL - `"price"` by default **\]** - The attribute to fetch about `ticker` from Google Finance and is required if a date is specified.

  - `attribute` is one of the following for real-time data:

    - `"price"` - Real-time price quote, delayed by up to 20 minutes.

    - `"priceopen"` - The price as of market open.

    - `"high"` - The current day's high price.

    - `"low"` - The current day's low price.

    - `"volume"` - The current day's trading volume.

    - `"marketcap"` - The market capitalization of the stock.

    - `"tradetime"` - The time of the last trade.

    - `"datadelay"` - How far delayed the real-time data is.

    - `"volumeavg"` - The average daily trading volume.

    - `"pe"` - The price/earnings ratio.

    - `"eps"` - The earnings per share.

    - `"high52"` - The 52-week high price.

    - `"low52"` - The 52-week low price.

    - `"change"` - The price change since the previous trading day's close.

    - `"beta"` - The beta value.

    - `"changepct"` - The percentage change in price since the previous trading day's close.

    - `"closeyest"` - The previous day's closing price.

    - `"shares"` - The number of outstanding shares.

    - `"currency"` - The currency in which the security is priced. Currencies don't have trading windows, so `open`, `low`, `high`, and `volume` won't return for this argument.

  - `attribute` is one of the following for historical data:

    - `"open"` - The opening price for the specified date(s).

    - `"close"` - The closing price for the specified date(s).

    - `"high"` - The high price for the specified date(s).

    - `"low"` - The low price for the specified date(s).

    - `"volume"` - The volume for the specified date(s).

    - `"all"` - All of the above.

- `start_date` - **\[** OPTIONAL **\]** - The start date when fetching historical data.

  - If `start_date` is specified but `end_date|num_days` is not, only the single day's data is returned.

- `end_date|num_days` - **\[** OPTIONAL **\]** - The end date when fetching historical data, or the number of days from `start_date` for which to return data.

- `interval` - **\[** OPTIONAL **\]** - The frequency of returned data; either "DAILY" or "WEEKLY".

  - `interval` can alternatively be specified as `1` or `7`. Other numeric values are disallowed.

### Notes

Usage restrictions: The data is not for financial industry professional use or use by other professionals at non-financial firms (including government entities). Professional use may be subject to additional licensing fees from a third-party data provider.

- All parameters must be enclosed in quotation marks or be references to cells containing text. 
  **Important:** A possible exception is when `interval` is specified as a number and when `end_date|num_days` is specified as a number of days.

- Real-time results will be returned as a value within a single cell. Historical data, even for a single day, will be returned as an expanded array with column headers.

- Some attributes may not yield results for all symbols.

- If any date parameters are specified, the request is considered historical and only the historical attributes are allowed.

- `GOOGLEFINANCE` is only available in English and does not support most international exchanges.

- Historical data cannot be downloaded or accessed via the Sheets API or Apps Script. If you attempt to do so, you'll see a \#N/A error in place of the values in the corresponding cells of your spreadsheet.

- [Quotes are not sourced from all markets and may be delayed up to 20 minutes.](https://www.google.com/googlefinance/disclaimer/#realtime) Information is provided 'as is' and solely for informational purposes, not for trading purposes or advice.

- Google treats dates passed into `GOOGLEFINANCE` as as noon UTC time. Exchanges that close before that time may be shifted by a day.

- Mutual fund attributes are currently not supported in Google Sheets.

## Examples

[Make a copy](https://docs.google.com/spreadsheets/d/14kqcSOMBEIdnnmX6rdMpIVMH9w3KUCWzMgB9s3tTD3I/copy)

**Important:** Each example is in its own tab.

### General usage

Retrieves market information from Google Finance.

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdERNdWdJZ3QtQ0hfRXVCN0ktY1FGU2c&single=true&gid=0&output=html&widget=true

 

### Common attributes

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdERNdWdJZ3QtQ0hfRXVCN0ktY1FGU2c&single=true&gid=1&output=html&widget=true

 

### Historical market data

Retrieves historical market information based on the specified dates from Google Finance.

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdERNdWdJZ3QtQ0hfRXVCN0ktY1FGU2c&single=true&gid=2&output=html&widget=true

 

### Currency exchange trends

Creates a chart inside a cell to display the currency exchange trend during the last 30 days, using the retrieving result returns by `GoogleFinance`.

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdERNdWdJZ3QtQ0hfRXVCN0ktY1FGU2c&single=true&gid=5&output=html&widget=true

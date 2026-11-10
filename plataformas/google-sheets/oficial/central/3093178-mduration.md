---
fonte: https://support.google.com/docs/answer/3093178?hl=en
baixado: 2026-11-10
---

# MDURATION

Calculates the modified Macaulay duration of a security paying periodic interest, such as a US Treasury Bond, based on expected yield.

### Sample Usage

`MDURATION(DATE(2010,01,02), DATE(2039,12,31), 3, 1.2, 2)`

`MDURATION(A2, B2, C2, D2, E2, 1)`

### Syntax

`MDURATION(settlement, maturity, rate, yield, frequency, [day_count_convention])`

- `settlement` - The settlement date of the security, the date after issuance when the security is delivered to the buyer.

- `maturity` - The maturity or end date of the security, when it can be redeemed at face or par value.

- `rate` - The annualized rate of interest.

- `yield` - The expected annual yield of the security.

- `frequency` - The number of interest or coupon payments per year (1, 2, or 4).

- `day_count_convention` - **\[** OPTIONAL - `0` by default **\]** - An indicator of what day count method to use.

  - 0 indicates US (NASD) 30/360 - This assumes 30 day months and 360 day years as per the National Association of Securities Dealers standard, and performs specific adjustments to entered dates which fall at the end of months.

  - 1 indicates Actual/Actual - This calculates based upon the actual number of days between the specified dates, and the actual number of days in the intervening years. Used for US Treasury Bonds and Bills, but also the most relevant for non-financial use.

  - 2 indicates Actual/360 - This calculates based on the actual number of days between the specified dates, but assumes a 360 day year.

  - 3 indicates Actual/365 - This calculates based on the actual number of days between the specified dates, but assumes a 365 day year.

  - 4 indicates European 30/360 - Similar to `0`, this calculates based on a 30 day month and 360 day year, but adjusts end-of-month dates according to European financial conventions.

### Notes

- `settlement` and `maturity` should be entered using `DATE`, `TO_DATE`, or other date parsing functions rather than by entering text.
- The modified duration is different from Macaulay duration (`DURATION`) in that it measures volatility, or price sensitivity, of an investment. The modified duration is related to the Macaulay duration in the following way: `MDURATION = DURATION / [1 + (yield / frequency)]`.

### See Also

[`YIELD`](https://support.google.com/docs/answer/3093255): Calculates the annual yield of a security paying periodic interest, such as a US Treasury Bond, based on price.

[`PRICE`](https://support.google.com/docs/answer/3093188): Calculates the price of a security paying periodic interest, such as a US Treasury Bond, based on expected yield.

[`DURATION`](https://support.google.com/docs/answer/3093169): Calculates the number of compounding periods required for an investment of a specified present value appreciating at a given rate to reach a target value.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdFY1ZkEyTXB2UngwZTFXcEdYeG1NeUE&output=html

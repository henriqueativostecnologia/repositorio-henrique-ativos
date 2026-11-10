---
fonte: https://support.google.com/docs/answer/3093270?hl=en
baixado: 2026-11-10
---

# YIELDDISC

Calculates the annual yield of a discount (non-interest-bearing) security, based on price.

### Sample Usage

`YIELDDISC(DATE(2010,01,02),DATE(2010,12,31),98.45,100)`

`YIELDDISC(A2,B2,C2,D2,2)`

### Syntax

`YIELDDISC(settlement, maturity, price, redemption, [day_count_convention])`

- `settlement` - The settlement date of the security, the date after issuance when the security is delivered to the buyer.

- `maturity` - The maturity or end date of the security, when it can be redeemed at face, or par value.

- `price` - The price at which the security is bought.

- `redemption` - The redemption value of the security.

- `day_count_convention` - **\[** OPTIONAL - `0` by default **\]** - An indicator of what day count method to use.

  - 0 indicates US (NASD) 30/360 - This assumes 30 day months and 360 day years as per the National Association of Securities Dealers standard, and performs specific adjustments to entered dates which fall at the end of months.

  - 1 indicates Actual/Actual - This calculates based upon the actual number of days between the specified dates, and the actual number of days in the intervening years. Used for US Treasury Bonds and Bills, but also the most relevant for non-financial use.

  - 2 indicates Actual/360 - This calculates based on the actual number of days between the specified dates, but assumes a 360 day year.

  - 3 indicates Actual/365 - This calculates based on the actual number of days between the specified dates, but assumes a 365 day year.

  - 4 indicates European 30/360 - Similar to `0`, this calculates based on a 30 day month and 360 day year, but adjusts end-of-month dates according to European financial conventions.

### Notes

- `settlement` and `maturity` should be entered using `DATE`, `TO_DATE` or other date parsing functions rather than by entering text.

### See Also

[`YIELD`](https://support.google.com/docs/answer/3093255): Calculates the annual yield of a security paying periodic interest, such as a US Treasury Bond, based on price.

[`TBILLYIELD`](https://support.google.com/docs/answer/3093264): Calculates the yield of a US Treasury Bill based on price.

[`PRICEMAT`](https://support.google.com/docs/answer/3093191): Calculates the price of a security paying interest at maturity, based on expected yield.

[`PRICEDISC`](https://support.google.com/docs/answer/3093240): Calculates the price of a discount (non-interest-bearing) security, based on expected yield.

[`PRICE`](https://support.google.com/docs/answer/3093188): Calculates the price of a security paying periodic interest, such as a US Treasury Bond, based on expected yield.

[`DISC`](https://support.google.com/docs/answer/3093216): Calculates the discount rate of a security based on price.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdHVqQ1dYSFgtVUdCRDdJYktHTl9xUUE&output=html

---
fonte: https://support.google.com/docs/answer/3093202?hl=en
baixado: 2026-11-10
---

# ACCRINTM

Calculates the accrued interest of a security that pays interest at maturity.

### Sample Usage

`ACCRINTM(DATE(1969,12,31),DATE(1999,12,31),0.05,100,0)`

`ACCRINTM(A2,B2,C2,D2,2)`

### Syntax

`ACCRINTM(issue, maturity, rate, [redemption], [day_count_convention])`

- `issue` - The date the security was initially issued.

- `maturity` - The maturity date of the security.

- `rate` - The annualized rate of interest.

- `redemption` - \[OPTIONAL\] - The redemption value of the security.

- `day_count_convention` - **\[** OPTIONAL - `0` by default **\]** - An indicator of what day count method to use.

  - 0 indicates US (NASD) 30/360 - This assumes 30 day months and 360 day years as per the National Association of Securities Dealers standard, and performs specific adjustments to entered dates which fall at the end of months.

  - 1 indicates Actual/Actual - This calculates based upon the actual number of days between the specified dates, and the actual number of days in the intervening years. Used for US Treasury Bonds and Bills, but also the most relevant for non-financial use.

  - 2 indicates Actual/360 - This calculates based on the actual number of days between the speficied dates, but assumes a 360 day year.

  - 3 indicates Actual/365 - This calculates based on the actual number of days between the specified dates, but assumes a 365 day year.

  - 4 indicates European 30/360 - Similar to `0`, this calculates based on a 30 day month and 360 day year, but adjusts end-of-month dates according to European financial conventions.

### Notes

- `issue` and `maturity` should be entered using `DATE`, `TO_DATE` or other date parsing functions rather than by entering text.

### See Also

[`YIELDDISC`](https://support.google.com/docs/answer/3093270): Calculates the annual yield of a discount (non-interest-bearing) security, based on price.

[`YIELD`](https://support.google.com/docs/answer/3093255): Calculates the annual yield of a security paying periodic interest, such as a US Treasury Bond, based on price.

[`RECEIVED`](https://support.google.com/docs/answer/3093244): Calculates the amount received at maturity for an investment in fixed-income securities purchased on a given date.

[`PRICEMAT`](https://support.google.com/docs/answer/3093191): Calculates the price of a security paying interest at maturity, based on expected yield.

[`PRICEDISC`](https://support.google.com/docs/answer/3093240): Calculates the price of a discount (non-interest-bearing) security, based on expected yield.

[`PRICE`](https://support.google.com/docs/answer/3093188): Calculates the price of a security paying periodic interest, such as a US Treasury Bond, based on expected yield.

[`DURATION`](https://support.google.com/docs/answer/3093169): Calculates the number of compounding periods required for an investment of a specified present value appreciating at a given rate to reach a target value.

[`DISC`](https://support.google.com/docs/answer/3093216): Calculates the discount rate of a security based on price.

[`COUPPCD`](https://support.google.com/docs/answer/3093210): Calculates last coupon, or interest payment, date before the settlement date.

[`COUPNUM`](https://support.google.com/docs/answer/3093208): Calculates the number of coupons, or interest payments, between the settlement date and the maturity date of the investment.

[`COUPNCD`](https://support.google.com/docs/answer/3093157): Calculates next coupon, or interest payment, date after the settlement date.

[`COUPDAYSNC`](https://support.google.com/docs/answer/3093156): Calculates the number of days from the settlement date until the next coupon, or interest payment.

[`COUPDAYS`](https://support.google.com/docs/answer/3093204): Calculates the number of days in the coupon, or interest payment, period that contains the specified settlement date.

[`COUPDAYBS`](https://support.google.com/docs/answer/3093154): Calculates the number of days from the first coupon, or interest payment, until settlement.

[`ACCRINTM`](https://support.google.com/docs/answer/3093202): Calculates the accrued interest of a security that pays interest at maturity.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdFVQU1hMcWp5M0tiRmlDQjV3S3h0b2c&output=html

---
fonte: https://support.google.com/docs/answer/3093251?hl=en
baixado: 2026-11-10
---

# TBILLPRICE

Calculates the price of a US Treasury Bill based on discount rate.

### Sample Usage

`TBILLPRICE(DATE(2010,1,2), DATE(2010,12,31), .0125)`

`TBILLPRICE(A2,B2,C2)`

### Syntax

`TBILLPRICE(settlement, maturity, discount)`

- `settlement` - The settlement date of the security, the date after issuance when the security is delivered to the buyer.

- `maturity` - The maturity or end date of the security, when it can be redeemed at face or par value.

- `discount` - The discount rate of the bill at time of purchase.

### Notes

- `settlement` and `maturity` should be entered using `DATE`, `TO_DATE` or other date parsing functions rather than by entering text.

- `TBILLPRICE` is equivalent to using `PRICEDISC` with US Treasury Bill conventions for the absent parameters.

- `maturity` must be one year or less from the `settlement` date.

- `discount` is a percentage and must be entered as a positive number from zero to one.

### See Also

[`TBILLYIELD`](https://support.google.com/docs/answer/3093264): Calculates the yield of a US Treasury Bill based on price.

[`PRICEDISC`](https://support.google.com/docs/answer/3093240): Calculates the price of a discount (non-interest-bearing) security, based on expected yield.

[`PRICE`](https://support.google.com/docs/answer/3093188): Calculates the price of a security paying periodic interest, such as a US Treasury Bond, based on expected yield.

### Examples

Embedded content: https://docs.google.com/spreadsheet/pub?key=0As3tAuweYU9QdFdnRzhHdmNyc0owekFyQnk5aFdUYUE&output=html

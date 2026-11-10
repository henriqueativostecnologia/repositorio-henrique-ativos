---
fonte: https://support.google.com/docs/answer/9199424?hl=en
baixado: 2026-11-10
---

# VDB function

The VDB function returns the depreciation of an asset for a particular period (or partial period).

## Parts of a VDB function

`VDB(cost, salvage, life, start_period, end_period, [factor], [no_switch])`

|                |                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Part           | Description                                                                                                                             |
| `cost`         | Initial cost of the asset.                                                                                                              |
| `salvage`      | Value of the asset at the end of depreciation (salvage value).                                                                          |
| `life`         | Number of periods of depreciation (useful life of the asset).                                                                           |
| `start_period` | Starting period to calculate depreciation.                                                                                              |
| `end_period`   | Ending period to calculate depreciation.                                                                                                |
| `factor`       | \[OPTIONAL\] - Rate of balance decline (the default is 2: the double-declining balance method).                                         |
| `no_switch`    | \[OPTIONAL\] - Whether to switch to straight-line depreciation when the depreciation is greater than the declining balance calculation. |

## Examples

|       |                                       |            |
|-------|---------------------------------------|------------|
|       | **A**                                 | **B**      |
| **1** | **Formula**                           | **Result** |
| **2** | `=VDB(100, 10, 20, 10, 11, 2, TRUE)`  | \$3.49     |
| **3** | `=VDB(100, 33, 20, 10, 11, 2, FALSE)` | \$1.87     |

## Related functions

- [DB](https://support.google.com/docs/answer/3093162): The DB function calculates the depreciation of an asset for a specified period using the arithmetic declining balance method.

- [DDB](https://support.google.com/docs/answer/3093163): The DDB function calculates the depreciation of an asset for a specified period using the double-declining balance method.

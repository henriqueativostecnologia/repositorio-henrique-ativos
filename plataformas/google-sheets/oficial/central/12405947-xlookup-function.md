---
fonte: https://support.google.com/docs/answer/12405947?hl=en
baixado: 2026-11-10
---

# XLOOKUP function

The `XLOOKUP` function returns the values in the result range based on the position where a match was found in the lookup range. If no match is found, it returns the closest match.

#### XLOOKUP for BigQuery

Cross lookup. Returns the values in the data column at the position where a match was found in the search column.

## Sample Usage

`=XLOOKUP("Apple",table_name!fruit,table_name!price)`

## Syntax

`XLOOKUP(search_key,lookup_range,result_range,missing_value,match_mode)`

- `search_key`: The value to search for. For example, `42`, `"Cats"`, or `B24`.
- `search_column`: The column to consider for the search.
- `result_column`: The column to consider for the result.
- `missing_value`: \[OPTIONAL - `#N/A` by default\] The value to return if no match is found.
- `match_mode`: \[OPTIONAL - `0` by default\] The manner in which to find a match for the search_key.
  - `0`: For an exact match.
  - `1`: For an exact match or the next value that is greater than the search_key.
  - `-1`: For an exact match or the next value that is lesser than the search_key.
  - `2`: For a wildcard match.

**Tip:** `search_mode` isn’t supported in XLOOKUP for BigQuery.

## Sample Usage

`XLOOKUP("Apple", A2:A, E2:E)` to replace `VLOOKUP("Apple", A2:E, 5, FALSE)`

`XLOOKUP("Price", A1:E1, A6:E6)` to replace `HLOOKUP("Price", A1:E6, 6, FALSE)`

`XLOOKUP` where match column is to the right of the output column

`XLOOKUP("Apple", E2:E7, A2:A7)`. The `VLOOKUP` equivalent is `VLOOKUP("Apple", {E2:E7, A2:A7}, 2, FALSE)`

## Syntax

`XLOOKUP(search_key, lookup_range, result_range, missing_value, match_mode, search_mode)`

- `search_key`: The value to search for. For example, `42`, `"Cats"`, or `B24`.
- `lookup_range`: The range to consider for the search. This range must be a singular row or column.
- `result_range`: The range to consider for the result. This range's row or column size should be the same as the `lookup_range`, depending on how the lookup is done.
- `missing_value`: \[OPTIONAL - `#N/A` by default\] The value to return if no match is found.
- `match_mode`: \[OPTIONAL - `0` by default\] The manner in which to find a match for the `search_key`.
  - `0` is for an exact match.
  - `1` is for an exact match or the next value that is greater than the `search_key`.
  - `-1` is for an exact match or the next value that is lesser than the `search_key`.
  - `2` is for a wildcard match.
- `search_mode`: \[OPTIONAL - `1` by default\] The manner in which to search through the `lookup_range`.
  - `1` is to search from the first entry to the last.
  - `-1` is to search from the last entry to the first.
  - `2` is to search through the range with binary search. The range needs to be sorted in ascending order first.
  - `-2` is to search through the range with binary search. The range needs to be sorted in descending order first.

## Notes

- If `result_range` is more than one row or column, then the output will be the entire row/column at the index a match was found in the `lookup_range`.

## Examples

Lookup table for all examples.

Lookup table for all examples.

 

`XLOOKUP` for Total amount sold with `match_mode` and `search_mode` omitted and missing argument specified.

 

`XLOOKUP` for Total amount sold with `match_mode = 0` and `search_mode = 1` and `-1`.

XLOOKUP for Total amount sold with match_mode = 0 and search_mode = 1 and -1.

 

`XLOOKUP` for Total amount sold with `match_mode = 1` and `-1` and `search_mode` omitted.

XLOOKUP for Total amount sold with match_mode = 1 and -1 and search_mode omitted.

 

`XLOOKUP` using horizontal matching and returning an entire column.

XLOOKUP using horizontal matching and returning an entire column.

## Related functions

- [XMATCH](https://support.google.com/docs/answer/12406049)
- [VLOOKUP](https://support.google.com/docs/answer/3093318)
- [HLOOKUP](https://support.google.com/docs/answer/3093375)

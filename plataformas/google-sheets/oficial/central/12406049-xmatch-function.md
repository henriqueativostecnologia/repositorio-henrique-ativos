---
fonte: https://support.google.com/docs/answer/12406049?hl=en
baixado: 2026-11-10
---

# XMATCH function

`XMATCH` returns the relative position of an item in an array or range that matches a specified value. `XMATCH`:

- Supports enhanced match and search functionality
- Allows wildcard matches with a question mark (?) or asterisk (\*)

## Sample usage

`XMATCH("Apple", A2:A)`

`XMATCH("Price", A2:A)`

## Syntax

`XMATCH(search_key, lookup_range, [match_mode], [search_mode])`

- `search_key`: The value to search for. For example, `42`, `"Cats"`, or `B24`.
- `lookup_range`: The range to consider for the search. This range must be a singular row or column.
- `match_mode`: \[OPTIONAL: `0` by default\] The manner in which to find a match for the `search_key`.
  - `0` is for an exact match.
  - `1` is for an exact match or the next value that's greater than the `search_key`.
  - `-1` is for an exact match or the next value that's lesser than the `search_key`.
  - `2` is for a wildcard match.
- `search_mode`: \[OPTIONAL: `1` by default\] The manner in which to search through the lookup range.
  - `1` is to search from the first entry to the last.
  - `-1` is to search from the last entry to the first.
  - `2` is to search through the range with binary search. The range needs to be sorted in ascending order first.
  - `-2` is to search through the range with binary search. The range needs to be sorted in descending order first.

## Examples

Lookup table for all examples.

Lookup table for all examples.                                                                        

`XMATCH` on Sales rep column with `match_mode` and `search_mode` omitted.

XMATCH on Sales rep column with match_mode and search_mode omitted.

 

`XMATCH` for Total Amount sold with `match_mode` = `0` and `search_mode` = `1` and `-1`.

XMATCH for Total Amount sold with match_mode = 0 and search_mode = 1 and -1.

 

`XMATCH` with horizontal matching.

XMATCH with horizontal matching.

 

`XMATCH` with `match_mode` = `1` and `match_mode` = `-1` and `search_mode` omitted.

XMATCH with match_mode = 1 and match_mode = -1 and search_mode omitted.

## Related functions

- [XLOOKUP](https://support.google.com/docs/answer/12405947)
- [MATCH](https://support.google.com/docs/answer/3093378)

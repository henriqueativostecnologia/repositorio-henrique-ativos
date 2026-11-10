---
fonte: https://support.google.com/docs/answer/10522653?hl=en
baixado: 2026-11-10
---

# UNIQUE function

Returns unique rows in the provided source range, discarding duplicates. Rows are returned in the order in which they first appear in the source range.

### Parts of a UNIQUE function

`UNIQUE(range, by_column, exactly_once)`

| **Part**     | **Description**                                                               |
|--------------|-------------------------------------------------------------------------------|
| range        | The data to filter by unique entries.                                         |
| by_column    | Whether to filter the data by columns or by rows. By default, this is false.  |
| exactly_once | Whether to return only entries with no duplicates. By default, this is false. |

### Notes 

- If rows are returned which appear to be duplicates, ensure that cells including text do not have differing hidden text such as trailing spaces.
- Ensure that numeric values are formatted in the same way - percentages as percentages, currency values as currency values, etc.

### Examples 

|             | **Color 1**                 | **Color 2** | **Color 3** |
|-------------|-----------------------------|-------------|-------------|
|             | Red                         | Yellow      | Red         |
|             | Blue                        | Magenta     | Blue        |
|             | Red                         | Yellow      | Red         |
|             | Green                       | White       | Green       |
|             |                             |             |             |
|             |                             |             |             |
| **Formula** | =UNIQUE(B2:D5)              |             |             |
| **Output**  | Red                         | Yellow      | Red         |
|             | Blue                        | Magenta     | Blue        |
|             | Green                       | White       | Green       |
|             |                             |             |             |
|             |                             |             |             |
| **Formula** | =UNIQUE(B2:D5, TRUE)        |             |             |
| **Output**  | Red                         | Yellow      |             |
|             | Blue                        | Magenta     |             |
|             | Red                         | Yellow      |             |
|             | Green                       | White       |             |
|             |                             |             |             |
|             |                             |             |             |
| **Formula** | =UNIQUE(B2:D5, FALSE, TRUE) |             |             |
| **Output**  | Blue                        | Magenta     | Blue        |
|             | Green                       | White       | Green       |

### Related functions 

- [GT](https://support.google.com/docs/answer/3098240)
- [GTE](https://support.google.com/docs/answer/3093975)
- [LT](https://support.google.com/docs/answer/3093596)
- [LTE](https://support.google.com/docs/answer/3093976)

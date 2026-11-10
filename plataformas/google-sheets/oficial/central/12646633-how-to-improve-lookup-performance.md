---
fonte: https://support.google.com/docs/answer/12646633?hl=en
baixado: 2026-11-10
---

# How to improve LOOKUP performance

To search for information in your data, use LOOKUP functions like:

- [VLOOKUP](https://support.google.com/docs/answer/3093318)
- [HLOOKUP](https://support.google.com/docs/answer/3093375)
- [MATCH](https://support.google.com/docs/answer/3093378)
- [INDEX](https://support.google.com/docs/answer/3098242)

Though it often takes time to perform these functions, this article shows how to optimize your LOOKUP performance and reduce computational power used.

#### Use sort range with a LOOKUP function

To sort more efficiently, use **sort range** instead of the [SORT](https://support.google.com/docs/answer/3093150) function:

1.  Select cells or columns.
2.  On the top taskbar, click **Data** and then  **Sort range**.
3.  Select one of:
    - **Sort range by \[leftmost column\] (A to Z)**.
    - **Sort range by \[leftmost column\] (Z to A)**.
    - **Advanced range sorting options**: Sort by multiple columns at one time in hierarchical order.

**Tip:** "Sort range" sorts data first, then feeds the sorted data into the VLOOKUP function.

### Learn what not to do:

**Important:** The next example shows how not to use the SORT function:

=VLOOKUP(search_key, SORT(A1:B10, 1), 2)

In this example SORT is nested in a VLOOKUP function. Each time the data in the sorted range changes, the SORT function unnecessarily examines all the data again and runs a new SORT function.

**Tip:** Ideally, SORT should only be applied once to a set of data. When needed, you can reference it.

#### Remove duplicates before you use a LOOKUP function

To speed up your computations, remove duplicate data throughout the set:

1.  Select all columns and rows of interest.
2.  On the top taskbar click **Data** and then  **Data cleanup** and then  **Remove duplicates**.
3.  Select columns to analyze.
4.  Click **Remove duplicates**.

**Tip:** Data that contains many duplicate values across columns or rows may slow down the computation.

LOOKUP functions:

- Can’t detect duplicates intelligently
- Search the entire data set, which includes all duplicate values that don’t match

#### Run LOOKUP in the same spreadsheet as your source data

To run the LOOKUP computation locally on your computer, first import the data into your spreadsheet:

1.  Use IMPORTRANGE to pull your data into an empty range in the same spreadsheet where your LOOKUP lives. [Learn more about IMPORTRANGE](https://support.google.com/docs/answer/3093340).
2.  Reference the imported data as your range in your LOOKUP function.

### Learn what not to do:

**Important:** The next example shows how not to use IMPORTRANGE:

=VLOOKUP(search_key, IMPORTRANGE(spreadsheet_url, range_string), index, \[is_sorted\])

In this example, IMPORTRANGE is nested in a LOOKUP function. Each time your LOOKUP runs, it executes IMPORTRANGE first to pull the data and then performs the LOOKUP function on the fetched data.

**Tip:** Try not to nest any functions in a LOOKUP function. Otherwise, the inner function performs extra calculations inside LOOKUP whenever the LOOKUP function runs.

#### Use IFERROR() or IF() statements to skip certain search keys

To make your Sheets calculation run faster, use an IF statement to skip repeated values like N/A, \#ERROR, REF#, or empty cells.

### Learn what not to do:

**Important:** The next example shows how not to use VLOOKUP:

In the example above, you can use VLOOKUP to find the price for a list of fruits in Column A. However, there are also many empty cells in your list of fruits.

Google Sheets runs calculations in B2 to B10 on all referenced search keys in column A even though VLOOKUP in B3, B7, and B9 searches on blank. These searches don't return any meaningful results.

### Learn what to do:

Use the IF function to skip those search keys based on your desired criteria and only run VLOOKUP when the data in the list of fruits isn't blank.

The IF function tells Google Sheets, “If the search key isn’t equal to blank, then run your_formula. If it’s equal to blank, then don’t run your_formula and instead output N/A.”

In general, any formula can be used and the value to skip doesn't have to be blank. This technique saves time because if there are meaningless values, you can avoid extra computation to calculate the result.

Google Sheets can’t tell if a value is meaningful unless you specifically call the value out with the IF function.

=IF(A2 \<\> value_to_skip, your_formula, "N/A")

**Tip:** The IF function above tells Google Sheets, “If A2 isn’t equal to value_to_skip, then run your_formula. If A2 is equal to value_to_skip, then don’t run your_formula and instead output N/A.”

[Learn more about the IF function](https://support.google.com/docs/answer/3093364).

#### Use INDEX & MATCH instead of VLOOKUP

Although VLOOKUP is slightly faster, INDEX and MATCH functions can provide more flexibility to divide your LOOKUP workflow into smaller pieces. This way you can reuse your previous result and save time.

### Learn what not to do:

For example, in order for VLOOKUP to find both the price and quantity for “Apple” in this table, you must use 2 separate VLOOKUP formulas:

=VLOOKUP("Apple", \$A\$1:\$C\$4, 2, FALSE)

This VLOOKUP does 2 steps internally:

1.  Finds the location of “Apple.”
2.  Searches for the price of “Apple” by going to the second column.

=VLOOKUP("Apple", \$A\$1:\$C\$4, 3, FALSE)

This VLOOKUP does 2 steps internally:

1.  Finds the location of “Apple.”
2.  Searches for the quantity of “Apple” by going to the third column.

In the 2 formulas above, the 1st step is the same: Find the location of “Apple” in the list. However, the 2nd step in both formulas above can’t run together because VLOOKUP is a single function with a single output.

So if you run VLOOKUP to find multiple pieces of different information on the same item, you must perform the 1st step twice. This adds computation time.

### Learn what to do:

Save time when you use a combination of MATCH and INDEX. This separates Step 1 and Step 2 so you can reuse Step 1 whenever needed:

1\. Find the location of “Apple” with MATCH:

=MATCH("Apple", \$A\$2:\$A\$4, FALSE)

The output of this formula is “1”, since “Apple” is in position 1 of the range.

2\. Search for the price of “Apple” in the second column with INDEX:

=INDEX(\$A\$2:\$C\$4, cell_with_MATCH_formula, 2)

The output of this formula is “\$1.”

To search for the quantity of “Apple”, you can reuse Step 1 and reference the cell with the MATCH formula so you don’t have to recalculate that part.

3\. Search for the quantity of “Apple” in the third column with INDEX:

=INDEX(\$A\$2:\$C\$4, cell_with_MATCH_formula, 3)

In this example with INDEX and MATCH, you perform Step 1 once and Step 2 twice for 3 total computational steps. If you use VLOOKUP instead, this uses 2 VLOOKUP functions and 4 steps, which takes more time and uses more computational resources.

These efficiency gains increase the more VLOOKUP functions you use. There are also many other situations where you can reuse the MATCH result to save time.

## Related resources

- [VLOOKUP](https://support.google.com/docs/answer/3093318)
- [HLOOKUP](https://support.google.com/docs/answer/3093375)
- [MATCH](https://support.google.com/docs/answer/3093378)
- [INDEX](https://support.google.com/docs/answer/3098242)

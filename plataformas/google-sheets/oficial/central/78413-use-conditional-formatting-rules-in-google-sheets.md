---
fonte: https://support.google.com/docs/answer/78413?hl=en
baixado: 2026-11-10
---

# Use conditional formatting rules in Google Sheets

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

Cells, rows, or columns can be formatted to change text or background color if they meet certain conditions. For example, if they contain a certain word or a number.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select the cells you want to apply format rules to.
3.  Click **Format** and then **Conditional formatting**. A toolbar will open to the right.
4.  Create a rule.
    - **Single color**: Under "Format cells if," choose the condition that you want to trigger the rule. Under "Formatting style, choose what the cell will look like when conditions are met.
    - **Color scale**: Under "Preview," select the color scale. Then, choose a minimum and maximum value, and an optional midpoint value. To choose the value category, click the Down arrow Down arrow .
5.  Click **Done**.

##### Example

A teacher can highlight test scores to see which students scored less than 80%.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select the test scores.
3.  Click **Format** and then **Conditional formatting**.
4.  Under "Format cells if," click **Less than**. If there's already a rule, click it or **Add new rule**  and then  **Less than**.
5.  Click **Value or formula** and enter 0.8.
6.  To choose a red color, click Fill Fill color .
7.  Click **Done**. The low scores will be highlighted in red.

### Use advanced conditional formatting

##### Use custom formulas with conditional formatting

You can use custom formulas to apply formatting to one or more cells based on the contents of other cells.

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select the cells you want to format.
3.  Click **Format** and then **Conditional formatting**.
4.  Under the "Format cells if" drop-down menu, click **Custom formula is**. If there's already a rule, click it or **Add new rule**  and then  **Custom formula is.**
5.  Click **Value or formula** and add the formula and rules.
6.  Click **Done**.

**Note**: Formulas can only reference the same sheet, using standard notation "(='sheetname'!cell)." To reference another sheet in the formula, use the [INDIRECT](https://support.google.com/docs/answer/3093377) function.

#### Example 1

To highlight when there's more than one occurrence of the same value in your data:

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select the range you want to format. For example, cells A1 to A100.
3.  Click **Format** and then **Conditional formatting**.
4.  Under the "Format cells if" drop-down menu, click **Custom formula is**. If there's already a rule, click it or **Add new rule**  and then  **Custom formula is.**
5.  Write the rule for the first row. In this case the rule would be, "=COUNTIF(\$A\$1:\$A\$100,A1)\>1."
6.  Choose other formatting properties.
7.  Click **Done**.

#### Example 2

To format an entire row based on the value of one of the cells in that row:

1.  On your computer, open a spreadsheet in [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  Select the range you want to format, for example, columns A:E.
3.  Click **Format** and then **Conditional formatting**.
4.  Under the "Format cells if" drop-down menu, click **Custom formula is**. If there's already a rule, click it or **Add new rule**  and then  **Custom formula is.**
5.  Write the rule for the first row. For example, if you want to make the whole row green if the value in column B is "Yes", write a formula like "=\$B1="Yes"."
6.  Choose other formatting properties.
7.  Click **Done**.

#### Absolute vs. relative references

Often, you will need to add dollar signs (\$) in front of letters and numbers in formulas so that the formatting is applied using absolute references as opposed to relative references (A1 to B1, A2 to B2).

##### Use wildcard characters with conditional formatting

You can use wildcard characters to match multiple expressions. Wildcard characters can be used with the "Text contains" or "Text does not contain" fields while formatting.

- To match any single character, use a question mark (?). For example, a text rule containing "a?c" would format cells with "abc," but not "ac" or "abbc."
- To match zero (0) or more characters, use an asterisk (\*) . For example, a text rule containing "a\*c" would format cells with "abc," "ac," and "abbc" but not "ab" or "ca."
- To match a question mark or asterisk in text, you can escape the wildcard characters by adding a tilde (~) in front of them. For example, a text rule containing "a~?c" would format cells with "a?c" but not "abc" or "a~?c."

**Notes**:

- To remove a rule, point to the rule and click Remove .
- Rules are evaluated in the order listed. The first rule found to be true will define the format of the cell or range. To reorder rules, click and drag them.
- If you copy and paste from a cell or range that has formatting rules, these rules will be applied when you paste the copied data.

## Version: Android phone & tablet

### Create a conditional formatting rule

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Select the range you want to format.
3.  Tap Format Format and then **Conditional formatting**. A panel will open.
4.  Set your rule conditions. If there's already a rule in the cell or range, to add another, tap **Add** first.
    - **Single color**: Under "Format cells if," choose the condition that you want to trigger the rule. Under "Formatting style," choose what the cell will look like when conditions are met. To create your own formatting style, under custom, tap Add Plus .
    - **Color scale**: Under "Formatting style," select the color scale. You can set a minimum, maximum, and midpoint value. If you don’t set a value, it will automatically adjust based on your data.
5.  Tap **Done**.

##### Example

A teacher can highlight test scores to see which students scored less than 80%.

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Select the test scores.
3.  Tap Format Format and then **Conditional formatting**.
4.  Under "Format cells if," tap **Less than**. If there's already a rule, tap it or **Add** and then **Less than**.
5.  Tap **Value or formula** and enter "0.8."
6.  To choose a red color, tap the red box.
7.  Tap **Done**. The low scores will be highlighted in red.

##### See your conditional formatting rules

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Tap Format Format and then **Conditional formatting**.
3.  At the top, choose an option:
    - **Selected range**: Shows the rules that intersect with the selected range.
    - **All**: Shows all rules on the sheet.
4.  To return to your spreadsheet, tap Done Done .

### Use advanced conditional formatting

##### Use custom formulas with conditional formatting

You can use custom formulas to apply formatting to one or more cells based on the contents of other cells.

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Select the cells you want to format.
3.  Tap Format Format and then **Conditional formatting**.
4.  Under the "Format cells if" drop-down menu, tap **Custom formula**. If there's already a rule, tap it or **Add** and then **Custom formula**.
5.  Tap "Value or formula" and add the formula and rules.
6.  Tap **Done**.

**Note:** Formulas can only reference the same sheet, using standard notation (='sheetname'!cell). To reference another sheet in the formula, use the [INDIRECT](https://support.google.com/docs/answer/3093377) function.

#### Example 1

To highlight when there's more than one occurrence of the same value in your data:

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Select the range you want to format. For example, cells A1 to A100.
3.  Tap Format Format and then **Conditional formatting**.
4.  Under the "Format cells if" drop-down menu, tap **Custom formula.** If there's already a rule, tap it or **Add** and then **Custom formula**.
5.  Enter the rule for the first row. In this case the rule would be, "=COUNTIF(\$A\$1:\$A\$100,A1)\>1."
6.  Choose other formatting properties.
7.  Tap **Done**.

#### Example 2

To format an entire row based on the value of one of the cells in that row:

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets&referrer=utm_source%3Dsheets_hc%26utm_medium%3Dlink%26utm_campaign%3Dsheets_hc).
2.  Select the range you want to format, for example, columns A:E.
3.  Tap Format Format and then **Conditional formatting**.
4.  Under the "Format cells if" drop-down menu, tap **Custom formula**. If there's already a rule, tap it or **Add** and then **Custom formula**.
5.  Enter the rule for the first row. For example, if you want to make the whole row green if the value in column B is "Yes", write a formula like "=\$B1="Yes"."
6.  Choose other formatting properties.
7.  Tap **Done**.

#### Absolute vs. relative references

Often, you will need to add dollar signs (\$) in front of letters and numbers in formulas so that the formatting is applied using absolute references as opposed to relative references.

##### Use wildcard characters with conditional formatting

You can use wildcard characters to match multiple expressions. Wildcard characters can be used with the "Text contains" or "Text does not contain" fields while formatting.

- To match any single character, use a question mark (?). For example, a text rule containing "a?c" would format cells with "abc," but not "ac" or "abbc."
- To match zero (0) or more characters, use an asterisk (\*) . For example, a text rule containing "a\*c" would format cells with "abc," "ac," and "abbc" but not "ab" or "ca."
- To match a question mark or asterisk in text, you can escape the wildcard characters by adding a tilde (~) in front of them. For example, a text rule containing "a~?c" would format cells with "a?c" but not "abc" or "a~?c."

**Notes**:

- To remove a rule, tap Remove and then Done Done .
- Rules are evaluated in the order listed. The first rule found to be true will define the format of the cell or range. To reorder rules, tap Move Move and drag them.
- If you copy and paste from a cell or range that has formatting rules, these rules will be applied when you paste the copied data.

## Version: iPhone & iPad

You can see conditional formatting rules on an iPhone or iPad but not edit them.

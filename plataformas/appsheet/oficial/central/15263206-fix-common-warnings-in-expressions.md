---
fonte: https://support.google.com/appsheet/answer/15263206?hl=en
baixado: 2026-11-10
---

# Fix common warnings in expressions

Historically, AppSheet has been overly permissive with regards to what expressions are allowed. Going forward, these types of expressions will be flagged with warnings in the Expression Assistant, though the expressions will continue to function. Some common warnings are described in the following sections:

- [Extra content](#extra-content-warnings)
- [Extra comma or semicolon](#extra-comma-semicolon)
- [Unsupported input](#unsupported-input)
- [Multiple ampersands](#ampersands)

Although not required at this time, we recommend that you fix any issues with the expression and eliminate warnings to ensure it's functioning as intended.

## Extra content

Extra content warnings occur when there are additional characters included but that aren't evaluated as part of the expression. This might happen in the following scenarios:

- Two or more valid subexpressions are specified, possibly separated by a comma, but there is no indication for how to join them together. In practice, only one of the subexpressions (usually the first) in the expression is evaluated by AppSheet. For example, the expression `1,2` evaluates as `1`.
- Additional operators are specified at the end of the expression.

For example, for the following expression:

`=CONCATENATE([NAME]," said "[TEXT])`

The following warning message is displayed:

**Extra content: "\[TEXT\]. Did you mean to separate it with a "," (comma)?**

Click **Fix** to insert a comma to correct the expression: `=CONCATENATE([NAME]," said "`**`,`**`[TEXT])`

The following provides additional examples of expressions that result in extra content warnings:

- `1, 2`
- `[ColumnName]123`
- `"QuotedString"[ColumnName]`
- `CONCATENATE("Included"ignored)`
- `"Included1" & "Included2"ignored`
- `1 + 1 +`

To fix extra content warnings in an expression, do one of the following:

- Join the subexpressions
- Properly separate the subexpressions
- Remove the subexpressions if they are not relevant 

Here are some additional tips for fixing extra content warnings:

- To make a list, enclose them in `{}`. For example, change `1, 2 `to `{1, 2}`.

- If you are in an argument list and want to separate arguments, use a comma. For example: `AND(true [Column] = 1) => AND(true, [Column] = 1)`

- If you want to join two arguments textually, use an ampersand (`&`). It is also recommended to quote your strings. For example, change `"abc"def` to `"abc" & "def"`. (Don't use [multiple ampersands](#ampersands).)

- Remove any typos from the content. For example, change `1 + 1+`  to `1 + 1`.

## Extra comma or semicolon 

Extra comma or semicolon warnings occur when an unnecessary comma (,) or semicolon (;) is included in an expression, as described below:

- At the end of an expression. For example, change `"1,"` to `"1"`.
- Multiple times consecutively in lists. For example, change `IF(true, , 1, , , 0)` to `IF(true, 1, 0)`.

To fix extra comma or semicolon warnings, remove unnecessary commas or semicolons.

## Unsupported input

AppSheet has a standard set of punctuation characters, such as `[]{}(),.-`, that you use when building expressions.

Unsupported input warnings occur when a non-standard punctuation character is used in an unquoted string. 

For example,`【Column】`uses characters similar to `[Column]`, but will evaluate as a string. AppSheet provides a warning as this might not be what the user intended when writing this expression.

If you intended to include non-standard punctuation, enclose all enclose the string in quotes.

## Multiple ampersands

A single ampersand concatenates the adjacent subexpressions. For example: `"Today is: " & [Date] `

Multiple ampersand warnings occur when you use consecutive ampersands in an expression. For example: `"Do not" && "do this" & & "or this"`

To fix ampersand warnings, remove extra ampersands from your expression.

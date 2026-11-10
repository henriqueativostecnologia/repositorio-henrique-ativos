---
fonte: https://support.google.com/appsheet/answer/10104642?hl=en
baixado: 2026-11-10
---

# Expressions: The Essentials

Calculate new values from existing ones using expressions.

## About expressions

There are several places in the app editor where you can use expressions to affect your app's behavior and provide users with advanced functionality. Several AppSheet features use expressions, including: [app formulas](https://support.google.com/appsheet/answer/10106437), [initial values](https://support.google.com/appsheet/answer/10106437), [column constraints](https://support.google.com/appsheet/answer/10107948), [virtual columns](https://support.google.com/appsheet/answer/10106758), and [deep links](https://support.google.com/appsheet/answer/10106757).

AppSheet checks all expressions to ensure they are correctly formed and being used in an appropriate manner. For example, if an expression is being used to assign an initial value to a column of type `Number`, AppSheet checks that the result of the expression is indeed a `Number`.

**Note**: If you're familiar with spreadsheet formulas in Microsoft Excel or Google Sheets, you'll find AppSheet expressions similar in syntax and meaning.

An expression may be built with any combination of the following:

**Constants**

- Numbers: any whole numbers (integers) or real (floating-point) numbers, positive or negative.
- Dates and times, enclosed in double quotes. Format dates as `MM/DD/YYYY` and times as `HH:MM:SS`. For example, `"12/31/1999"` and `"10:15:00"`. See also [Date and time expressions](https://support.google.com/appsheet/answer/10107326).
- Text, enclosed in double quotes. For example, `"Wordy words"`.

**Columns**

- Use the value of a column by enclosing the column's name in square brackets like this: `[Column]`. Then, you can use [columns in expressions](https://support.google.com/appsheet/answer/10107945). 
- [Dereferences](https://support.google.com/appsheet/answer/10107396) are a type of expression that is useful when you have [references](https://support.google.com/appsheet/answer/10108121) between tables.
- To use columns from other tables in the app that aren't connected using [references](https://support.google.com/appsheet/answer/10108121), specify the table name and column value using the following syntax: `Table[Column]`

## Build expressions

Learn more about building expressions with AppSheet.          

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| #### [U                                                                       | #### [Expression types](https://support.google.com/appsheet/topic/10104376)   |
| se Expression Assistant](https://support.google.com/appsheet/answer/10104484) |                                                                               |
|                                                                               | Understand the types of expressions you can build.                            |
| Learn how build expressions using Expression Assistant in the AppSheet        |                                                                               |
| editor.                                                                       |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| #### [Column expressions](https://support.google.com/appsheet/topic/10104641) | #### [List expressions](https://support.google.com/appsheet/topic/10803606)   |
|                                                                               |                                                                               |
| Build column expressions that are dynamically computed to determine the       | Build list expressions that are dynamically computed to determine the         |
| behavior of a specific column when the user tries to enter or change its      | contents of a list.                                                           |
| value. For example, you can use column constraints to control the behavior of |                                                                               |
| the data in each column.                                                      |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| ####                                                                          | #### Tips and tricks                                                          |
| [AppSheet function list](https://support.google.com/appsheet/table/10104782)  |                                                                               |
|                                                                               | Learn tips and tricks for building expressions from the AppSheet Community:   |
| View all of the AppSheet functions that can be used when building             |                                                                               |
| expressions.                                                                  | -   [Expression tips and                                                      |
|                                                                               |     tricks](https://www.googlecloudcommunity.com/gc/for                       |
|                                                                               | ums/filteredbylabelpage/board-id/appsheet-tips-tricks/label-name/Expressions) |
|                                                                               | -   [Expressions                                                              |
|                                                                               |     Q&A](https://www.googlecloudcommunity.com/gc/f                            |
|                                                                               | orums/filteredbylabelpage/board-id/appsheet-questions/label-name/Expressions) |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

##  Sample template

Use the [Quote Calculator](https://www.appsheet.com/Template/SimpleDef?appName=RateCalculator-71626) template which shows the use of various expressions in [app formula](https://support.google.com/appsheet/answer/10106437).

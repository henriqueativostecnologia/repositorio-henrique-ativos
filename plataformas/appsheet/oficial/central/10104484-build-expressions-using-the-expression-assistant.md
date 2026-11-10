---
fonte: https://support.google.com/appsheet/answer/10104484?hl=en
baixado: 2026-11-10
---

# Build expressions using the Expression Assistant

Build and test simple and complex expressions using the Expression Assistant as described in the following sections.

- [Access the Expression Assistant](#access-expression-assistant)
- [Build an expression using the Expression Assistant](#build-expressions)
- [View and insert column references into expressions](#view-insert-table-columns)
- [View and insert predefined patterns into expressions](#view-insert-example-patterns)
- [Test expressions](#test)
- [Keyboard shortcuts](#keyboard-shortcuts)

See also:

- [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642)
- [Expression types](https://support.google.com/appsheet/topic/10104376)
- [AppSheet function list](https://support.google.com/appsheet/table/10104782)

## ****Access the Expression Assistant

Within the app editor, you can access the Expression Assistant anywhere you're able to enter an expression.

To access the Expression Assistant:

1.  Click the **flask** icon next to an input field to toggle to the expression format (if available). For example:

    Flask icon

2.  Click in the expression field indicated with an **equals sign (=)**. For example:

    Expression field

**Note**: The equals sign indicates that the expression's result will be used as the setting's value.

The Expression Assistant opens. [Build](#build-expressions) and [test](#test) your expressions as described in the following sections.

## Build expressions

Build expression using the Expression Assistant as shown in the following figure. 

Type expression and expand text area

As highlighted in the previous figure, the Expression Assistant enables you to:

- Build your expression in the text area

-

- Confirm the valid syntax and function of the expression

- View and insert [column references](#view-insert-table-columns) or [predefined patterns](#view-insert-example-patterns) into the expression using the tabs at the bottom of the dialog

- [Test the expression](#test)

- Format the expression to add spacing, indenting, and so on

- Expand the text area by:
  - Dragging the handle in the lower-right corner to accommodate more complex expressions that span several lines
  - Collapsing the tabs at the bottom of the dialog

- Save the expression by clicking **Save** or use `Ctrl-Shift-S` on PC or `⌘-Shift-S` on Mac

- Send feedback to AppSheet about your experience with the Expression Assistant

The Expression Assistant provides the following features to assist you with AppSheet function syntax:

- Syntax highlighting to display components of an expression in different colors
  Syntax highlighting in Expression Assistant

  Color key:
  - Green: AppSheet functions
  - Pink: Data references, such as column names
  - Blue: Text 
  - Orange: Numbers
- Syntax of current function with contextual highlighting 
  Formatting hints
- Auto-completion for columns (when cursor is positioned within an expression or column definition)
  **Note**: You can use the `Ctrl + Space` keyboard shortcut to display the auto-completion suggestions.
  Auto-completion for columns
- Documentation panel for quick access to the description and syntax for the current function
  Quick access to help for AppSheet functions

## ****View and insert column references into expressions

View and insert column references into expressions by clicking the **Data Explorer** tab, as shown in the following figure.

View and insert table columns into expression

**Data Explorer** tab enables you to:

- View all tables and columns in your app
- Insert a column reference into an expression, as described below
- View `Ref` associations ([references to other tables](https://support.google.com/appsheet/answer/10106510))
- Expand and collapse table, and pin their display in the Expression Assistant

To insert a column reference into an expression:

1.  Click within the expression text area where you want to insert the column reference.
2.  Expand the table that contains the column you want to add.
3.  Position your cursor over the column name and click **Insert**.

## ****View and insert predefined patterns into expressions

View and insert predefined patterns into expressions by clicking the **Examples** tab, as shown in the following figure.

View and insert example patterns into expressions using the Examples tab.

The **Examples** tab enables you to:

- Select an [expression type](https://support.google.com/appsheet/topic/10104376)
- Insert a predefined pattern into an expression, as described below

To insert a predefined pattern into an expression:

1.  Click within the expression text area where you want to insert the example pattern.
2.  Select the tab based on the [expression type](https://support.google.com/appsheet/topic/10104376) that you want to add.
3.  Position your cursor over the example pattern and click **Insert**.

## ****Test expressions

To test the results of the expression for each row in the table, click **Test** in the Expression Assistant. The Expression Test page displays.

The first column shows the **Expression Result** for each row in the table, as shown below:

Expression results for each row in table

Expand the **Expression Result** by clicking the **expand** icon to view the results of each part of the expression:

Expression results expanded

## Keyboard shortcuts

The following keyboard shortcuts are available in the Expression Assistant.

|                                                |                   |                   |
|------------------------------------------------|-------------------|-------------------|
| **Shortcut description**                       | **PC**            | **Mac**           |
| Save expression                                | `Ctrl-Shift-S`    | `⌘-Shift-S`       |
| Decrease indent for current or selected lines  | `Ctrl-[`          |  `⌘-[`            |
| Increase indent for current or selected lines  | `Ctrl-]`          | `⌘-]`             |
| Move selection one word to the left            | `Ctrl-LeftArrow`  | `Alt-LeftArrow`   |
| Move selection one word to the right           | `Ctrl-RightArrow` | `Alt-RightArrow`  |
| Delete word before the current cursor location | `Ctrl-Backspace`  | `Alt-Backspace`   |
| Delete word after the current cursor location  | `Ctrl-Delete`     | `Alt-Delete`      |
| Move selection one element to the left         | `Alt-LeftArrow`   | `Ctrl-LeftArrow`  |
| Move selection one element ot the right        | `Alt-RightArrow`  | `Ctrl-RightArrow` |

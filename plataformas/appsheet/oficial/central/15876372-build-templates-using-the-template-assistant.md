---
fonte: https://support.google.com/appsheet/answer/15876372?hl=en
baixado: 2026-11-10
---

# Build templates using the Template Assistant

Build templates for use in automations using the Template Assistant as described in the following sections.

- [Access the Template Assistant](#access)
- [Build templates](#use)
- [View and insert content into templates using the Data Explorer](#view-insert)

## Access the Template Assistant

Within the app editor, you can access the Template Assistant anywhere you're able to build a template in an automation.

To access the Template Assistant, click the flask icon next to a template input field to open the Template Assistant. For example:

Click flask icon to access Template Assistant

## Build templates

Build templates using the Template Assistant as shown in the following figure:

Template Assistant

As highlighted in the previous figure, the Template Assistant enables you to:

- Build your template in the text area. Enter text or insert [variables](https://support.google.com/appsheet/answer/11539253#built-in-variables), expressions, or column references enclosed in `<< >>` operators
- [View and insert data content](#view-insert) using the tabs at the bottom of the dialog (`<< >>` operators are added automatically)
- Expand the text area by:
  - Dragging the handle in the lower-right corner to accommodate more complex expressions that span several lines
  - Collapsing the tabs at the bottom of the dialog
- Save the expression by clicking **Save** or use `Ctrl-Shift-S` on PC or `⌘-Shift-S` on Mac

The Template Assistant provides syntax highlighting to display components of an expression in different colors.
 Color key:

- Green: AppSheet functions
- Pink: Data references, such as column names
- Blue: Text and [built-in variables](https://support.google.com/appsheet/answer/11539253#built-in-variables)
- Orange: Numbers
- Gray: Template operators (`<< >>`)

## View and insert data content into templates

View and insert data content into templates by clicking one of the following tabs:

- Expression Examples, shown in the previous figure, to insert predefined example expressions based on your data, such as column expressions
- Data Explorer, as shown in the following figure, to explore and insert data content

Data Explorer tab in Template Assistant

The Data Explorer tab enables you to:

- View all data content in your app
- Insert content into the template, as described below (`<< >>` operators are added automatically)
- View `Ref` associations ([references to other tables](https://support.google.com/appsheet/answer/10106510))
- Expand and collapse data sections, and pin their display in the Template Assistant

To insert data content into a template:

1.  Click within the expression text area where you want to insert the column reference or other value.
2.  Expand the table that contains the content you want to add.
3.  Position your cursor over the content and click **Insert**.

The data is automatically enclosed in the `<< >>` operators.

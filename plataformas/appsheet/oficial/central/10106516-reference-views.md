---
fonte: https://support.google.com/appsheet/answer/10106516?hl=en
baixado: 2026-11-10
---

# Reference views

When you select a row from a table view or you edit a row, you are not taken to a top-level view that is accessible in either the menu or the buttons at the bottom of your app. Instead, you are taken to a reference view (or **ref** view for short). A ref view is a hidden view that is only used when drilling down into your data, editing or adding data, or displaying a row using a `Ref` column.

- [Get started](#get-started)
- [User-defined reference views](#user-defined-ref-views)
- [System-generated reference views](#system-generated-ref-view)

## Get started

Watch the following **video** to learn more about how to manage reference views, including tips and tricks for managing the system-generated inline view (such as `Tasks_Inline`) .

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=n7fA5wm9dvI

The [Activity schedule](https://www.appsheet.com/template/showdef?appId=ExtracurricularSchedule-71626) **sample app** provides a simple example of reference views. The Notes user-defined reference view and its associated system-generated views (Notes_Detail, Notes_Form, and Notes_Inline), shown in the following figure, enable users to view or add notes to a student's activity details.

reference views in the UI

The following figure shows how the views are displayed and accessed in the app.

Notes reference view displayed in activity details

## User-defined reference views

You can also explicitly define ref views by creating a new view and setting its position to **ref** when configuring [view details](https://support.google.com/appsheet/answer/10106688#view-details).** **Any user-defined ref view takes precedence over system-defined ref views. You can create ref views based on tables or [slices](https://support.google.com/appsheet/answer/10106592). The ref view configuration will be used whenever the data source of the ref view matches that of the view you are starting from.

Select ref position when configuring view

## System-generated reference views

The system automatically generates ref views for each of the tables in the app. For example, a table called `Students` will have a **Students_Detail** view. If the table allows adds or edits, there will also be a **Students_Form** view. If the table can be shown inline because it has a reference to another table, it will also have a **Students_Inline** view.

You can modify the system-generated views to easily change the look and feel of the app. See [Views: The Essentials](https://support.google.com/appsheet/answer/10106688).

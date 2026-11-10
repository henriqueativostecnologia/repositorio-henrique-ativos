---
fonte: https://support.google.com/appsheet/answer/10106308?hl=en
baixado: 2026-11-10
---

# Slice row filter conditions

Row filters are a way to filter the rows in a slice. The following provides an example of a **Row filter condition**. This expression defines the [Yes/No](https://support.google.com/appsheet/answer/10107946) filter condition used by the slice. Rows that satisfy the condition are part of the slice; those that fail the condition are excluded.

Row filter condition when configuring a slice

When you click in the **Row filter condition** field, [Expression Assistant](https://support.google.com/appsheet/answer/10104484) is launched. Use Expression Assistant to construct an appropriate filter condition. 

## Filter rows by user

You can choose to filter data based on the user currently using the app. In order to do this, you first need to make sure your app [requires sign-in](https://support.google.com/appsheet/answer/10104975), so AppSheet can recognize who is signed in to the app and render the corresponding data.

You'll also need to make sure that your spreadsheet contains a qualifying column that can uniquely identify the user based on the row. The contents of that column should identify the user. `Email` is always best, but you could use `Name`, `Student`, `User`, and so on; anything that will require the user to type in the qualifying detail. The row filter condition `[Student Email] = USEREMAIL()` will ensure that only the appropriate rows are included.

**Note**: Avoid [`USERNAME()`](https://support.google.com/appsheet/answer/10108211) because it is unreliable. Providers like Google only return the user's name if that user has enabled Google+ on their account. Instead, use an `Email` column and compare it with [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210), rather than comparing a Name column to `USERNAME()`.

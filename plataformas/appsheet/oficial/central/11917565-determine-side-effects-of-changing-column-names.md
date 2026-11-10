---
fonte: https://support.google.com/appsheet/answer/11917565?hl=en
baixado: 2026-11-10
---

# Determine side effects of changing column names

Sometimes, you have to change the name of a column. Since columns have Display Names that are independent of the actual stored column name, the reason for this is rarely for user interface requirements. Rather, the motivation is either that the column was not named correctly initially and you want to adjust it to be logically consistent, or you are copying the app to a different storage provider. Each storage provider may have its own constraints on the length of column names. For example, MySQL requires column names to be less than 64 characters in length.

For many name changes (like the names of tables), AppSheet automatically fixes many of the references to the table. However, it does not (*at this time*) automatically fix table names and column names inside expressions/formulas. Instead, you will see errors in the expressions when you change a column name and save.

One way to handle this is to see the errors and resolve each of them manually. Another and more structured way to do this is to go to the app documentation at **Info \> Properties \> Documentation** and find the link at the bottom that has auto-generated documentation for the app. This is simply an HTML file with the URL of the form: `https://www.appsheet.com/template/appdoc?appid=<`*`app-id`*`>`

Many of our advanced users utilize this documentation to run textual searches (`Control-F` in a browser) to look for all the places a particular column name is used. While this is still a manual process (you can't actually change anything while viewing the documentation), it allows you to anticipate the impact before you make the change.

There may be column names used in expressions inside external task template files (used to generate PDF attachments for emails, for example). These aren't part of the documentation and therefore may still cause errors. Therefore, after any such change, use the **Save and Verify Changes** option from the **Save** drop-down. That forces a more thorough check of not just the app definition but all of the external files as well.

---
fonte: https://support.google.com/appsheet/answer/10104986?hl=en
baixado: 2026-11-10
---

# Limits on tables per application

AppSheet does not enforce a limit on the number of tables per application. Complex apps can have 20 to 30 tables and 20 to 30 views. However, performance degrades as the number and size of tables grows. Performance also degrades when tables are stored in separate spreadsheet files. The biggest determinant of performance is the number of times AppSheet must go to the provider, such as Google Drive, to fetch a file.  

Generally, we advocate limiting your app to a few tables and a few views. The main reason is focus. Apps are different from websites. Usually a website has everything from an organization, but apps that try to do too much usually don't serve anybody well. It is a good practice to have an app for a specific purpose. It is easy enough to build another app for another purpose. For example, even Facebook has separate apps for Messenger and regular Facebook.

This is the philosophy behind AppSheet design. This is why AppSheet has an app launcher (so you can break your mega-app into multiple sub apps) and why our per-user pricing model has a per-user cost for any number of apps.

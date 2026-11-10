---
fonte: https://support.google.com/appsheet/answer/10104695?hl=en
baixado: 2026-11-10
---

# Understand the secure flow of data

AppSheet uses industry-standard security protocols and practices to secure your data. Users of your mobile app interact with a local copy of the data on the device. This local copy is maintained in a combination of HTML5 local storage and the file system on the device. There are standard security mechanisms in place to ensure that unauthorized users cannot see this data.

When users sync their app, changes they make are sent to the AppSheet web service over an encrypted protocol (HTTPS). AppSheet then applies the changes to the backend spreadsheet (on Google Drive, Dropbox, and so on). The latest version of the spreadsheet is read (from Google Drive, Dropbox, and so on) and sent back to the mobile app.

See also [AppSheet security and governance](https://about.appsheet.com/security/).

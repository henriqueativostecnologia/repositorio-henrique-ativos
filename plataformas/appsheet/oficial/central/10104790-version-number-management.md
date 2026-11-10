---
fonte: https://support.google.com/appsheet/answer/10104790?hl=en
baixado: 2026-11-10
---

# Version number management

AppSheet automatically assigns a new version number to your app every time your app definition changes. 

The Editor displays your app's current version number on the **Info \> Properties** pane.

The version number consists of a **major version number** to the left of the decimal point and a **minor version number** to the right of the decimal point.

AppSheet automatically increments the minor version number every time you make a change using the editor and save your change.

AppSheet automatically increments the major version number when you upgrade your app. You can manually increment the major version number on the **Info \> Properties** pane. 

When the major version number changes, this signifies that you have made a significant change to your application. Before a major version number change, make certain that all of your users have synced all of their pending adds, updates, or deletes. Immediately after a major version number change, make certain that all of your users sync to retrieve the newest version of your app. 

If a user attempts to sync a pending add, update, or delete using the wrong major version number of the app, their changes will be rejected with the following error:

`This data change cannot be applied because there is a newer version of your app '<app name>'. Please reset data to discard local changes.`

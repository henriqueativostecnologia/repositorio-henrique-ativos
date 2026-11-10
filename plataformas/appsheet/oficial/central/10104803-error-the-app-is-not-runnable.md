---
fonte: https://support.google.com/appsheet/answer/10104803?hl=en
baixado: 2026-11-10
---

# Error: The App is not runnable

You may see the  `The App is not runnable `error in the app emulator (in the editor) or your users may see this error on a mobile device. 

It indicates that the app definition is invalid (most likely) or corrupt (rare).

The most likely reason for an app definition to become invalid is that the structure of the spreadsheet used to create the app changed. For example, someone added or deleted a column. Now the spreadsheet is no longer compatible with the app. Every time you open the app in the app editor, or refresh the app editor web page, AppSheet rechecks this and alerts you with error messages if the app definition is invalid. In many cases, AppSheet will automatically adjust the app to make it runnable again. However, this does not happen unless the app creator actually opens the app editor ---that is, it requires an intentional action by the app creator. 

AppSheet will also consider an app definition as invalid if the underlying spreadsheets are no longer readable (if the data cannot be read, then the app cannot be verified or run).

On a mobile device, an app definition may be corrupted if a network error occurs while the app definition is being downloaded (initially or during a sync). This is a relatively rare event and usually is resolved with a restart or sync. In rare cases, you may need to uninstall and reinstall AppSheet.

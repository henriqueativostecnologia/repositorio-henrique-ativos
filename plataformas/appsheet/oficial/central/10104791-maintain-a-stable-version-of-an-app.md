---
fonte: https://support.google.com/appsheet/answer/10104791?hl=en
baixado: 2026-11-10
---

# Maintain a stable version of an app

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

By default, all users of an app work with the latest version of the app. As the app creator, you might want to make changes to the app definition. These changes are immediately visible to the app users after a [sync](https://support.google.com/appsheet/answer/10107724).

In some situations, you might prefer to work with a new app version for a while without affecting the existing users. AppSheet provides a mechanism to do so. You can designate a Stable version of the app on the **Manage \> Versions** pane of the app editor.

Each user of the app can be assigned to either the Latest version or the Stable version of the app. This allows you to leave most users on the Stable version, build a new version, and gradually add a few test users to evaluate it. When it is ready for broader use, you can mark this as the new Stable version and all the users will now work with this version of the app. See [Manage app permissions for individual users](https://support.google.com/appsheet/answer/10104983#manage-roles-app-versions).

The Stable version feature is only available with certain subscription plans.

**Caution**: Be mindful of any changes you may make to the spreadsheets or other data that the app uses. The Stable version of the app expects its data to satisfy the column structure. If your newer versions require different columns, it is best to make a copy of the data and work with the copied data.

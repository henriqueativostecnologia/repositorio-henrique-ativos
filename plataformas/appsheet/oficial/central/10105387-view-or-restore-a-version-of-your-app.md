---
fonte: https://support.google.com/appsheet/answer/10105387?hl=en
baixado: 2026-11-10
---

# View or restore a version of your app

As you edit your app in the editor, it maintains a history of your changes. This is useful if you need to view or restore an earlier version of your application. Every time you save your application in the editor, AppSheet saves the current version in a Version History log. Sometimes these changes are ones you make explicitly. Other times the changes are made automatically by the system when it checks the consistency of your application.

- [View a version of your app](#view)
- [Restore a version of your app](#restore)
- [About the app version recovery window](#app-version-recovery-window)

## View a version of your app

To view a version of your app:

1.  Open your app in the editor.
2.  Go to the **Manage \> Versions** pane.
3.  Expand the **Version History** section.
4.  Click **Get Version History**.

    Version history
5.  Click **Expand** to view the change details for the associated app version.
6.  Click **View** to open the version of the app.
    The app editor opens in a new browser tab and displays the selected version of the app in read-only mode. You cannot edit this read-only version of the app. However, you can [restore this version of the app](#restore).

If the underlying data structure has changed, the app itself may not run in the app preview.

## Restore a version of your app

To restore a version of your app:

1.  [View a version of your app](#view).
    The editor opens in a new browser tab and displays the selected version of the app in read-only mode.
2.  Click **Restore (make this version current)**.

## About the app version recovery window

By default, the app version recovery window is 7 days.

If you have an AppSheet Enterprise Plus account, you can change the app version recovery window, as follows:

1.  Go to the **My account \> Settings**.
2.  Under **Enterprise Plan Settings**, change the **App version recovering window (days)** to the desired number of days.

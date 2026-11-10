---
fonte: https://support.google.com/appsheet/answer/10108131?hl=en
baixado: 2026-11-10
---

# Use system actions

Each action definition represents an individual task or transition that can be explicitly invoked by the user of an app. See [Actions: The Essentials](https://support.google.com/appsheet/answer/10107706).

When you're customizing the behavior of your app, you can create your own, but there are also a number of **system actions**. These are actions that are automatically created by the AppSheet system based on the column structure of a table. System actions represent the default behavior of an AppSheet app; you can think of them as behavior that comes with the app out of the box.

The most common example of system actions are per-column system actions. Every column of type `Email` has an automatically-created Email system action. This is shown as an email envelope icon next to any email address value shown in an app view. Clicking on it launches an email to that email address. Similarly, any `LatLong` value has a map pin icon next to it. Clicking on the icon opens a map and shows the location of that value on the map.

If you are using the legacy app editor, you can show or hide system actions by default. See [Configure app editor settings](https://support.google.com/appsheet/answer/13396480).

## Control system actions

In most apps, there is no reason to ever modify or control the system actions. They are designed to work correctly without the app creator's intervention.

However, there are instances where the app creator may want to control these actions. For example, you may want to:

- Enable calling only a subset of phone numbers
- Change the icon shown for email actions
- When using the [desktop design](https://support.google.com/appsheet/answer/12407883), control how users [edit content (in place or in a separate form)](https://support.google.com/appsheet/answer/10107706#form-desktop-behavior)

System actions can be edited like any other action. However, there are some caveats:

- Only some of the properties of the action can be changed --- in particular, the presentation properties and the condition that determines when it should be shown.
- If the table's column structure changes, the system will automatically delete and re-create system actions. Any changes made by the app creator will be lost if the system deletes the action. 

## Hide system actions

In some cases, you may want to hide the system action icons from your user to provide a cleaner look to your app. In that case, you can select any of the system actions and enable the **Do not display** option. This means that the action is still there if you want to use it, but won't be displayed from the user. This way you can show the user only the icons they need.

---
fonte: https://support.google.com/appsheet/answer/10107846?hl=en
baixado: 2026-11-10
---

# Form view type

The form view allows you to capture information input by app users both online or offline.

Depending on your needs you can capture signatures, photos, location services, or simple text. Similar to Google forms, new guests to your form will only be able to fill out the new form and will not see entries made by previous users.

AppSheet can be used to distribute forms through a mobile app as well as use a mobile app to view and interact with form responses. This view helps you unlock mobile-specific features for your forms that the web cannot capture such as photo capturing an input into your form directly from your mobile device.

## Create a form view

 To create a form view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
2.  Configure the form view, as follows:
    - Select **form** as the **View type** when configuring the view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - Configure the [form view options](#configure-view-options).
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
3.  Save the app.

## Important notes

- See the [sample app](https://www.appsheet.com/samples/An-app-that-uses-your-information-to-fill-out-a-bill-of-lading-template-and-send-it-to-your-email?appGuidString=abc84327-ba13-4902-92b3-2ca9017a6fa7).
- Forms are customizable to suit your individual needs. For example, you can set a form so that each user sees a fresh form when they open the form page on your application. See [Customize input forms](https://support.google.com/appsheet/answer/10106787).
- Your application can include multi-page forms. See [Create multi-page forms](https://support.google.com/appsheet/answer/10107388).

## ****Configure the form view options

Configure the form **View options** by using the settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Row key                                                                       | Enter an expression that defines the key for the row that you want to edit.   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Page style                                                                    | Set the default form page style: **Default** , **Page Count**, or **Tabs**.   |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting overrides the global [Form page style                  |
|                                                                               | setting](https://support.google.com/appsheet/answer/10107387#forms).          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Form style                                                                    |  Set the default form style, either **Default** or **Side-by-side**.          |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting overrides the global [Form style                       |
|                                                                               | setting](https://support.google.com/appsheet/answer/10107387#forms).          |
|                                                                               |                                                                               |
|                                                                               | Form style, default and side-by-side                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column order                                                                  | Control the column order in a form view if different from the original order. |
|                                                                               | See [Control column order in a                                                |
|                                                                               | view](https://support.google.com/appsheet/answer/10107315).                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Save/cancel position                                                          | Select the position for the Save and Cancel buttons, Bottom or Top.           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Max nested rows                                                               | Set the maximum number of rows to show for related reference lists.           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Auto save                                                                     | Turn on to save the form automatically after the last field is completed.     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Auto re-open                                                                  | Turn on to re-open the form automatically after saving.                       |
|                                                                               |                                                                               |
|                                                                               | **Note**: For child forms, the form re-opens automatically after saving.      |
|                                                                               | However, the child form will be permanently saved only after the parent form  |
|                                                                               | is saved.                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Finish view                                                                   | Select the view to navigate to after creating a new entry.                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Control column order in a form view

Control the column order in a form view if different from the original order. See [Control column order in a view](https://support.google.com/appsheet/answer/10107315).

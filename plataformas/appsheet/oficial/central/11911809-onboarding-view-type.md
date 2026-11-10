---
fonte: https://support.google.com/appsheet/answer/11911809?hl=en
baixado: 2026-11-10
---

# Onboarding view type

The onboarding view type enables you to provide a set of introductory pages for onboarding users.

The following provides an example of the **Instructions** onboarding view provided with the [Shift Scheduling](https://www.appsheet.com/templates/Schedule-shifts-and-manage-timesheets-for-frontline-workers) template.

Use an onboarding view in your app as described in the following sections:

- [Get started with an app template](#get-started)
- [Prepare your data](#prepare-data)
- [Create an onboarding view](#create-view)
- [Configure the onboarding view options](#configure-options)

See also [Views: The Essentials](https://support.google.com/appsheet/answer/10106688) for more information about managing views.

[Format rules](https://support.google.com/appsheet/answer/10106703) are not supported for onboarding views at this time.

## ****Get started with an app template

An example of the onboarding view can be found in the [Shift Scheduling](https://www.appsheet.com/templates/Schedule-shifts-and-manage-timesheets-for-frontline-workers) template.

## ****Prepare your data

You need to create a table that defines the content components displayed on each page in the onboarding flow, including columns for one or more of the following:

- Image
- Title of the page
- Short description
- Additional description

The following provides an example of the **Instructions** table used in the onboarding view in the [Shift Scheduling](https://www.appsheet.com/templates/Schedule-shifts-and-manage-timesheets-for-frontline-workers) template.

Instructions table content used in the Shift Scheduling example.

## ****Create an onboarding view

To create an onboarding view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).

2.  Configure the onboarding view, as follows:

    1.  When configuring the onboarding view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details):

        1.  Select **onboarding** as the **View type.**

        2.  Select the onboarding table (see [Prepare your data](#prepare-data)) in the **For this data** drop- down.

    2.  Configure the [onboarding view options](#configure-options).

    3.  Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).

3.  When you are done, save your changes by selecting one of the following:

    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## ****Configure the onboarding view options

Configure the onboarding **View options** by using the settings described in the following tables.

|                    |                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------|
| **Setting**        | **Description**                                                                                          |
| Image              | Image to display for a specific page. Select the table column in the drop-down list.                     |
| Title              | Title of the page in the onboarding flow. Select the text-based column in the drop-down list.            |
| Short blurb        | Short description. Select the text-based column in the drop-down list.                                   |
| Second short blurb | Additional description, smaller font size. Select the text-based column in the drop-down list.           |
| Finish view        | View to navigate to after completing the onboarding flow. Select an existing view in the drop-down list. |

 

The following figure shows how the **View options** settings appear in the Instructions onboarding view in the [Shift Scheduling](https://www.appsheet.com/templates/Schedule-shifts-and-manage-timesheets-for-frontline-workers) template. The sample data has been modified to include an example of the contents for the **Second short blurb**.

Image showing where view options in the Instructions onboarding view,

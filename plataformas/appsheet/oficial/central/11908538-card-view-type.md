---
fonte: https://support.google.com/appsheet/answer/11908538?hl=en
baixado: 2026-11-10
---

# Card view type

The card view type enables you to display content and actions for a single element using a format that is similar to [card components](https://material.io/components/cards) in Material Design. You choose a layout and configure the content blocks.

The following provides an example of the **Nearby** card view from the [Facility Inspections](https://www.appsheet.com/templates/Inspect-points-throughout-various-properties?appGuidString=d8389191-0217-42c0-bd50-406993b660f6) template.

Nearby card view from Facility Inspections sample.

Use a card view in your app as described in the following sections:

- [Get started with an app template](#get-started)
- [Create a card view](#create-view)
- [Configure the card view options](#configure-view-options)
- [Configure the layout](#configure-layout)

See also [Views: The Essentials](https://help.appsheet.com/en/articles/943653-views-the-essentials) for more information about managing views.

## ****Get started with an app template

Many of the [app templates](https://www.appsheet.com/Templates) demonstrate how to use the card view, such as the following templates:

- [Simple Inventory Manager](https://www.appsheet.com/templates/Update-inventory-and-monitor-levels?appGuidString=722f8a69-cdbe-4e10-9a02-b55e63cce457)
- [Project Tracker](https://www.appsheet.com/templates/Track-project-tasks-or-issues-in-a-kanban-dashboard?appGuidString=535cf3aa-c081-47f6-a027-a24d2602c26a)
- [Facility Inspections](https://www.appsheet.com/templates/Inspect-points-throughout-various-properties?appGuidString=d8389191-0217-42c0-bd50-406993b660f6)

## ****Create a card view

To create a card view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
2.  Configure the card view, as follows:
    - Select **card** as the **View type** when configuring the card view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - Configure the [card view options](#configure-view-options).
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
3.  When you are done, save your changes by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## ****Configure the card view options

Configure the card **View options** by using the settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Sort by                                                                       | Sort the rows by one or more columns.                                         |
|                                                                               |                                                                               |
|                                                                               | Click **Add** and select the column name and whether to sort in **Ascending** |
|                                                                               | or **Descending** order. Repeat to configure additional sort by rules.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Group by                                                                      | Group rows by the values in one or more columns.                              |
|                                                                               |                                                                               |
|                                                                               | Click **Add** and select the column name and whether to sort in **Ascending** |
|                                                                               | or **Descending** order. Repeat to configure additional sort by rules.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Group aggregate                                                               | Display a numeric summary of the rows in each group.                          |
|                                                                               |                                                                               |
|                                                                               | Select the format to use for the display from the drop-down list.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Layout                                                                        | [Configure the layout](#configure-layout) for the card view.                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 

## ****Configure the layout

Configure the layout of the card view as described in the following sections.

- [Choose a layout](#choose-layout)
- [Configure the content blocks](#configure-content-blocks)

### Choose a layout

When creating and configuring your card view, you need to choose the layout that you want to use to display the content. Card views support the following layouts.

## Backdrop

Backdrop photo card that includes an image and title, and supports a single action when clicking the card.

Backdrop layout in card view

## Large

Full view of a card that includes an image, title, subtitle, header, subheader, and description and supports up to four actions, displayed using text (2) and icons (2).

Large layout in card view

## List

Compact view of a card that includes a thumbnail image, title, and subtitle, and supports up to three actions in the Actions drop-down menu.

List layout in a card view

## Photo

Photo card that includes an image, title, and subtitle, and supports a single action when clicking the card.

Photo layout in a card view

### Configure the content blocks

Based on the [layout](#choose-layout) that you choose there are a number of content blocks available that you can configure. The following figure highlights the full set of content blocks available when you choose the **large** layout.

Shows where content blocks appear in a card view

The following table summarizes the content blocks that are available in each layout.

Content blocks that are available based on the selected layout

Configure the content blocks available for your layout as described in the following sections:

- [Configure text blocks](#configure-text-blocks) including title, subtitle, header, subheader, and description
- [Configure image blocks](#configure-image-blocks) including main image and thumbnail
- [Configure action blocks](#configure-action-blocks) including text, icon, or menu item

### Configure text blocks

Text blocks in a card view layout include title, subtitle, header, subheader, and description.

To configure a text block:

1.  In the **Layout** structure, click the text block that you want to configure, such as **Title goes here**.
2.  Select a column in the **Column to show** drop-down list that will be used to populate the text block. To hide the text block, select **None**.

For example, the following shows the steps to configure the card view **title** in a **list** layout. In this case, the Inspection Point ID is used to populate the title block.

Configure text block in card view

### Configure image blocks

Image blocks in a card view layout include the main and thumbnail images.

To configure an image block:

1.  In the **Layout** structure, click the **image** block that you want to configure.

2.  Select a column in the **Column to show** drop-down list that will be used to populate the image block. To hide an image block, select **None** and skip any remaining steps.

3.  If available, select one of the following **Image Fit** options to configure the image display:

    - **Cover** - Uses the image as a background for the whole view (great for pattern images and some photos)

    - **Fit** - Scale the image to fit inside the header area (great for logos)

    - **Fill** - Crop the image to fit the area (great for photos)

4.  If available, select the **Image Shape**, square or round.

For example, the following shows the steps to configure the card view **thumbnail** image in a **list** layout. In this case, the **Point Image** is used to populate the image block.

Configure image blocks in card view

### Configure action blocks

Configure action blocks that are displayed as text, icon, or menu items.

To configure an action block:

1.  In the **Layout** structure, click the **text**, **icon**, or **menu item** action block that you want to configure.
2.  Select the action that you want to execute when the text, icon, or menu item is selected in the **On Click** drop-down. The drop-down includes includes actions defined for the selected table, Go to details, and None. To display details for an item in a detail view. select **Go to details**. To hide an action block, select **None**.

For **icon** action blocks, you select the icon when configuring the action, as described in [Actions: The Essentials](https://support.google.com/appsheet/answer/10107706).

For example, the following shows the steps to configure an **icon** action block in a **large** layout. In this case, the **Inspect** action is invoked when the **checkmark** icon is clicked.

Action blocks in card view

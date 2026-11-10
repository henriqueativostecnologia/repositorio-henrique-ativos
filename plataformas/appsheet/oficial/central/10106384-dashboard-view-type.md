---
fonte: https://support.google.com/appsheet/answer/10106384?hl=en
baixado: 2026-11-10
---

# Dashboard view type

The dashboard view allows you to show multiple views in one place. Currently calendars, maps, charts, gallery, deck, table, and detail views can be added to the dashboard.

Users can customize the dashboard view by repositioning views  in the grid. User can click  Dashboard grid  in the top toolbar to reset to the default grid layout.

If the view content is related or from the same table as data in other views, enabling [Interactive Mode](https://community.appsheet.com/t/interactive-dashboard/189) allows content to be dynamically updated as different entries are selected.

Dashboard view

Use a dashboard view in your app as described in the following sections:

- [Get started with a sample app](#get-started)
- [Create a dashboard view](#create-dashboard-view)
- [Configure the dashboard view options](#configure-dashboard-view-options)

See also [Views: The Essentials](https://help.appsheet.com/en/articles/943653-views-the-essentials) for more information about managing views.

## Get started with a sample app

See the [Interactive Dashboard](https://www.appsheet.com/templates/How-to-make-an-interactive-dashboard?appGuidString=1d06a130-fc0b-4733-837d-80bdf5ba9f2e) sample app to see how to create an interactive dashboard. 

This example includes a simple email client with two tables (`Folder` and `Message`). When you click on a folder, the messages in that folder are displayed. When you click on a message, the message details are displayed. 

## Create a dashboard view

To create a dashboard view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
2.  Configure the dashboard view, as follows:
    - Select **dashboard** as the **View type** when configuring the card view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - Configure the [dashboard view options](#configure-view-options).
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
3.  Save your changes.

## Configure the dashboard view options 

Configure the dashboard **View options** by using the settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| View entries                                                                  | Views that you want to appear on the dashboard                                |
|                                                                               |                                                                               |
|                                                                               | To add views entries:                                                         |
|                                                                               |                                                                               |
|                                                                               | 1.  Click **Add** and select an existing view in the list.                    |
|                                                                               | 2.  Select the size of the view in the dashboard: **Large**, **Small**,       |
|                                                                               |     **Tall**, or **Wide**. For example, large views will be twice the size of |
|                                                                               |     small views on the grid. On phones, this setting is ignored.              |
|                                                                               | 3.  Repeat to add additional views to the dashboard.                          |
|                                                                               |                                                                               |
|                                                                               | If the view entries are not all the same size, they may appear in a different |
|                                                                               | order for optimal fit on the current screen. The order of the view entries    |
|                                                                               | can only be guaranteed if the view entries are all the same size.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Use tabs in mobile view                                                       | On a tablet or desktop, the specified dashboard views will be shown in an     |
|                                                                               | automatically-sized grid that can be customized by the app user.              |
|                                                                               |                                                                               |
|                                                                               | Turn on **Use tabs in mobile view** to use the mobile-friendly dashboard tabs |
|                                                                               | for when the screen device is narrow, usually when the app is opened on a     |
|                                                                               | phone or small tablet.                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Interactive mode                                                              | When turned on, tapping rows will affect other views in the dashboard; it     |
|                                                                               | won't navigate to another view.                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

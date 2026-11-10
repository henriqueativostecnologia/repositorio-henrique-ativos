---
fonte: https://support.google.com/appsheet/answer/10106383?hl=en
baixado: 2026-11-10
---

# Calendar view type

The calendar view allows you to display data associated with dates and times in day, week or month formats. Additionally, you can display the calendar as a singular view or part of a [dashboard view.](https://support.google.com/appsheet/answer/10106384) 

- [Create a calendar view](#create-view)
- [Configure the calendar view options](#configure-view-options)
- [Structure your data for a calendar view](#structure-data)
- [Integrate with Google Calendar](#integrate-google-calendar)
- [Create recurring events](#create-recurring-events)
- [Customize the color of tasks in a calendar view](#customize-task-color)

## Create a calendar view

To create a calendar view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
2.  Configure the calendar view, as follows:
    - Select **calendar** as the **View type** when configuring the card view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - Configure the calendar view options.
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
3.   When you are done, save your changes by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

Calendar view example.

## ****Configure the calendar view options

Configure the calendar **View options** by using the settings described in the following table.

**Notes**:

- Calendar views have four **required** fields. All calendar views must specify a start (Start date, Start time) and an end (End date, End time). If you’re receiving an error in your calendar, a good place to start is by checking that these are all set.
- If you only have one date value in your data, use it as the start AND end date (likewise, you can use a single time value as the start and end values).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Start date                                                                    | Column that contains the start date for each row. Select a column from the    |
|                                                                               | drop-down.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Start time                                                                    | Column that contains the start time each row. Select a column from the        |
|                                                                               | drop-down.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| End date                                                                      | Column that contains the end date. Select the column from the drop-down.      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| End time                                                                      | Column that contains the end time for each row. Select a column from the      |
|                                                                               | drop-down.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Description                                                                   | Column that contains the text to display for the event.  Select a column from |
|                                                                               | the drop-down.                                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Category                                                                      | Column that defines the color for each category.  Select a column of type     |
|                                                                               | Color from the drop-down.                                                     |
|                                                                               |                                                                               |
|                                                                               | For tips on customizing the color of tasks in a calendar view, see this       |
|                                                                               | [community                                                                    |
|                                                                               | article](http                                                                 |
|                                                                               | s://www.googlecloudcommunity.com/gc/AppSheet-Q-A/Calendar-colors/m-p/222612). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Default view                                                                  | Default view to display when calendar loads. Select **Month**, **Week**, or   |
|                                                                               | **Day**.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Structure your data for calendar view

Because your data structure influences the interface and functionality of your application, it's important to ensure it's structured in a format that's easiest for AppSheet to read. Below are column header suggestions to help get you started. 

- Date: Start Date and End Date
- Time: Start Time and End Time

## Integrate with Google Calendar

AppSheet currently supports integration with Google Calendar, but not other Calendar platforms. To integrate with an existing Google Calendar, add your Google Calendar as a data source via the **Account \> Sources \> + Data Source \> Google Calendar**. Allow AppSheet to access your Google Account, and then create a calendar view. 

You can change the Google Calendar and it will sync across the app. You will need to create the blocks in Google Calendar for them to populate in AppSheet. 

## Create recurring events

The calendar view does not directly support a way to create recurring events. However, there are workarounds that you can implement. For example, you could create an [automation bot](https://support.google.com/appsheet/answer/11432969) to add events after a certain condition is triggered. 

## Customize the color of tasks in a calendar view

For tips on customizing the color of tasks in a calendar view, see this [community article](https://www.googlecloudcommunity.com/gc/AppSheet-Q-A/Calendar-colors/m-p/222612).

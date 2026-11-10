---
fonte: https://support.google.com/appsheet/answer/10106764?hl=en
baixado: 2026-11-10
---

# Use data from Google Calendar

You can use data from Google Calendar in your app to view and manage details for a meeting or event, including:

- Title and description
- Creator and attendees
- Start and end times
- Location
- Google Meet link
- Web link
- Status

Use data from a Google Calendar as described in the following sections:

- [Get started](#get-started)
- [Add a Google Calendar as a data source](#add-data-source)
- [Use the Google Calendar data in your app](#use-google-calendar-data)
- [Typical usage patterns](#typical-usage-patterns)

## Get started 

Watch this video to learn how to generate Google Meet links as part of an automation.

Video: https://www.youtube.com/watch?v=pBEGczlXbkM

## Add a Google Calendar as a data source

First, you must add a Google Calendar as a data source.

1.  Go to [appsheet.com](https://appsheet.com/) and sign in to your account.
2.  Select **My Account** in the top navigation bar.
3.  Select **Sources**.
4.  Click + **New Data Source**.
5.  Enter a name for the data source in the field provided.
6.  Click **Google Calendar** and follow the prompts to authenticate.

Your Google Calendar account is now available as a data source for tables in any of your apps.

## Use the Google Calendar data in your app

To use Google Calendar data in your app, [add a new table](https://support.google.com/appsheet/answer/10105821) to your app, select the Google Calendar data source you previously added, and select one of the calendars in your account.

**Note**: Typically, your Google account will have multiple calendars: a **primary** calendar as well as several secondary calendars (such as, **US National Holidays** calendar). Each calendar is modeled in AppSheet as a table whose entries have a *predetermined* column structure. The **primary** Google Calendar is most often used.

Like all other tables, calendar entries may be added, updated, or deleted depending on the table permissions chosen.

### Configure the locale

The Google Calendar API always provides dates and times in US/English locale, in the form: `MM/DD/YYYY `` `Consequently, it's important to ensure the AppSheet table for the Google calendar is also marked as having the **English (United States)** locale. For more information, see [Locale support in AppSheet](https://support.google.com/appsheet/answer/10106525). This has no effect on how dates are shown in the app; the format of dates in the app depends only on the locale of the user's device or browser.

## Typical usage patterns

Consider the following using Google Calendar data in your app:

- Most users will use the **primary** Google Calendar.
- To view calendar data, it's common to use add a virtual Thumbnail column to create a text icon image, using the app formula: **`TEXT_ICON(LEFT(TEXT([Start]), 10))`**
- AppSheet apps are best suited for viewing and modifying calendar entries that are associated with existing data in other tables; they are not meant to replace custom calendaring applications.

The most common associations between another table and a calendar table are via the `Creator` and `Attendees` columns. For example, consider an app with two tables: `Customers` (with a column called `Email`) and `Calendar`. We have provided two built-in formula functions to easily construct virtual columns in the `Customer` table that model related `Calendar` entries.

- `GCAL_MEETINGS_FROM("Calendar", [Email])`- Use in the app formula of a virtual column to find meeting requests sent by each customer. The generic structure is `GCAL_MEETINGS_FROM(`*`CalendarTable`*`, `*`SenderEmail`*`)`.
- `GCAL_MEETINGS_WITH("Calendar", [Email])`- Use in the app formula of a virtual column to find meeting requests where the customer is an attendee. The generic structure is `GCAL_MEETINGS_WITH(`*`CalendarTable`*`, `*`AttendeeEmail`*`)`.

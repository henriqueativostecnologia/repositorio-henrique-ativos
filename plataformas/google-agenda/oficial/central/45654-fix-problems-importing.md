---
fonte: https://support.google.com/calendar/answer/45654?hl=en
baixado: 2026-11-10
---

# Fix problems importing

If you're getting an error while importing information into Google Calendar, or if the results look wrong, use the tips below to help fix the problem.

**Note:** You can only follow these troubleshooting steps on a computer, not on a phone or tablet.

## First, check the steps you used to export & import

1.  Read the steps for [exporting from Google Calendar](https://support.google.com/calendar/answer/37111) or check for help information about exporting from another calendar application.
2.  Read the steps for [importing](https://support.google.com/calendar/answer/37118) into Google Calendar.

## Errors during importing

If you're seeing any of these errors, try these troubleshooting steps on your computer.

#### "Processed zero events"

### Import ZIP files

1.  Find the ZIP file on your computer.
2.  Double-click to open it. You'll see ICAL files (ending in “ics”) for each of your calendars.
3.  On your computer, open [Google Calendar](https://calendar.google.com/).
4.  In the top right, click Settings Settings   and then **Settings**.
5.  Open the **Calendars** tab.
6.  Click **Import calendars** (between the "My calendars" and "Other Calendars" sections).
7.  Click **Choose File** and select one of your ICAL files. You'll need to import each file that ends in “ics” individually.
8.  Choose the calendar where you want to add the imported events. By default, events will be imported into your main calendar.
9.  Click **Import**.  Repeat the import steps for each file that ends in “ics.” 

### Import CSV or ICAL files

You can also get the "Processed zero events" error if you clicked the **Import** button more than once. Because the file imported correctly after the first click, the error message pops up on the second click because there weren't any new events to process. Check your calendar to make sure all your events are there.

If this didn't fix your problem, check the formatting of your [CSV file](https://support.google.com/calendar/answer/37118#format_csv) or [ICAL file](https://support.google.com/calendar/answer/37118#format_ical).

#### "Processed x of y events"

This error usually happens when Google Calendar can't read some events in your file.

Google Calendar only works with files created by major calendar applications like Microsoft Outlook, Apple Calendar, and Yahoo Calendar. If you exported your file from one of these applications, try exporting it again and re-importing it into Google Calendar.

If this didn't fix your problem, check the formatting of your [CSV file](https://support.google.com/calendar/answer/37118#format_csv) or [ICAL file](https://support.google.com/calendar/answer/37118#format_ical).

#### "Google Calendar is temporarily unavailable"

### File size is too large

This usually happens when the file is too big. Google Calendar works with files that are one megabyte (1MB) or smaller.

If your file is too big, export a shorter date range from the original application. You can also separate the file into smaller files if you're comfortable [manually editing](https://support.google.com/calendar/answer/37118#advanced) CSV or ICAL code.

### Import started twice

You can also get the "Processed zero events" error if you clicked the **Import** button more than once. Because the file imported correctly after the first click, the error message pops up on the second click because there weren't any new events to process. Check your calendar to make sure all your events are there.

If this didn't fix your problem, check the formatting of your [CSV file](https://support.google.com/calendar/answer/37118#format_csv) or [ICAL file](https://support.google.com/calendar/answer/37118#format_ical).

#### "The connection to the server was reset"

This usually happens if the file isn't formatted correctly. To fix the format, check the formatting of your [CSV file](https://support.google.com/calendar/answer/37118#format_csv) or [ICAL file](https://support.google.com/calendar/answer/37118#format_ical).

## Errors after importing

If you're seeing any of these errors, use your computer to try these troubleshooting steps. 

#### Events show at the wrong time

### First, check your time zone

Check that the time zone in Google Calendar matches the time zone in the original calendar application:

1.  On your computer, open [Google Calendar](https://calendar.google.com).
2.  In the top right, click Settings Settings   and then **Settings**.
3.  In the "Your current time zone" section, select your time zone from the drop-down menu.
4.  Scroll to the bottom of the page, then click **Save**.

You also need to check the time zone settings in the calendar application you exported from. If you need help, check the application's help information.

### Next, try importing again

After you've checked your time zone, export your file again and re-import it into Google Calendar.

#### Recurring events don't work

Some calendar applications will export repeating events as a collection of single events. Because Calendar reads events as the other calendar application exported them, they will import as one-time events.

## Formatting errors

Imports might have errors because the formatting is wrong in the file. Choose your filetype below for tips for checking your file's formatting:

#### CSV file (file ends with "csv")

### Check that your file uses a comma as the delimiter

Google Calendar doesn’t work with files that use a semicolon ( ; ) or colon ( : ) to separate fields. Make sure all fields are separated by commas.

### Check your file for the correct field headers 

CSV files must be correctly formatted to import. [Learn more about creating or editing CSV files.](https://support.google.com/calendar/answer/37118#format_csv) 

### Check your file size 

Google Calendar only works with  files that are one megabyte (1MB) or smaller.

If your file is too big, export a shorter date range from the original application. You can also separate the file into smaller files if you're comfortable [manually editing](https://support.google.com/calendar/answer/37118#advanced) CSV code.

#### ICAL file (file ends with "ics")

### Check formatting of your headers and footers

ICAL files must be correctly formatted to import. [Learn more about creating or editing ICAL files.](https://support.google.com/calendar/answer/37118#format_ical)

### Check your file size

Google Calendar only works with  files that are one megabyte (1MB) or smaller.

If your file is too big, export a shorter date range from the original application. You can also separate the file into smaller files if you're comfortable [manually editing](https://support.google.com/calendar/answer/37118#advanced) ICAL code.

## I still need help

If you're still having issues, visit the [Google Calendar Help Forum](https://productforums.google.com/forum/#!forum/calendar) to get tips and suggestions from other users.

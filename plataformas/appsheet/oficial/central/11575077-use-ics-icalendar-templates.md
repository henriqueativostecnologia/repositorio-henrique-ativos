---
fonte: https://support.google.com/appsheet/answer/11575077?hl=en
baixado: 2026-11-10
---

# Use ICS/iCalendar templates

Most of us are used to receiving calendar invitations in an email message. Using AppSheet bots, you can customize and attach calendar invitations to your communications.

At a mechanical level, this involves creating a calendar invitation file that is sent along with your communication. The calendar invitation file uses a well-known format called ICS /iCalendar, and typically have an `.ics` extension.

Customize calendar invitations using an ICS/iCalendar template as described in the following sections:

- [Customize calendar invitation content using an ICS/iCalendar template](#customize-content)
- [View the template](#view-template)
- [Edit the template](#edit-template)
- [Manually create a calendar invitation template](#manually-create-template)

## Customize calendar invitation content using an ICS/iCalendar template

When configuring a [Send an email](https://support.google.com/appsheet/answer/11447614), [Call a webhook](https://support.google.com/appsheet/answer/11511244), or [Create a new file](https://support.google.com/appsheet/answer/11512511) task, customize the contents of a calendar invitation using an ICS/iCalendar template by performing one of the following tasks:

- Create an **ICS_CALENDAR** template, as described in [Create a template](https://support.google.com/appsheet/answer/11539957#create-template).
- [Manually create the calendar invitation template](#manually-create-template) in your cloud file system and use it, as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template). Ensure that the file is a text file with an **.**`ics` file extension and that contains valid ICS content.

For information about customizing the template, see [Customize content using templates](https://support.google.com/appsheet/answer/11539957#customize-content) and the tips provided below.

## View the template

After creating or selecting the template, click **View** adjacent to download the template file from your cloud system.

## Edit the template

Most cloud file systems like Google Drive will not let you edit an `.ics` file directly. To edit the template you must:

1.  Download the template file from your cloud file system to your computer.
2.  Edit the template file on your computer using the text editor of your choice (eg: Notepad).
3.  Upload the edited template file from your computer to your cloud file system.

## Manually create a calendar invitation template

Manually create an ICS/iCalendar template file by creating an empty `.ics` file, entering valid ICS content, and saving the file using the `.ics` extension.

The following provides a simple example of an ICS/iCalendar file. The `.ics` format is very rich and can construct very complex calendar invitations. For more information and examples, see: [https://icalendar.org](https://icalendar.org/)

`BEGIN:VCALENDAR`

`VERSION:2.0`

`PRODID:-//appsheet.com//appsheet 1.0//EN`

`CALSCALE:GREGORIAN`

`METHOD:PUBLISH`

`BEGIN:VEVENT`

`SUMMARY:Invitation from <<USEREMAIL()>> to talk about <<[MeetingTopic]>>`

`UID:c7614cff-3549-4a00-9152-d25cc1fe077d`

`SEQUENCE:0`

`STATUS:CONFIRMED`

`TRANSP:TRANSPARENT`

`DTSTART:<<[StartDateTime]>>`

`DTEND:<<[EndDateTime]>>`

`LOCATION:<<[MeetingAddress]>>`

`DESCRIPTION:<<[MeetingDescription]>>`

`END:VEVENT`

`END:VCALENDAR`

Notice that the template includes placeholders (for example, `<<[StartDateTime]>>`) that will be dynamically replaced by actual values when the action is executed. The actual placeholder expressions will depend on the specifics of your app.

To learn how fellow app creators are using this feature, see the [conversation about calendar invitations in the community](https://www.googlecloudcommunity.com/gc/Tips-Tricks/Creating-calendar-invites-using-ICS-attachments/m-p/324893).

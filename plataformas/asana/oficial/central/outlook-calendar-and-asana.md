---
fonte: https://help.asana.com/s/article/outlook-calendar-and-asana?language=en_US
baixado: 2026-11-10
---

# Outlook Calendar and Asana

**Available on Asana [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [pricing page](https://asana.com/pricing) for more information.**

The Outlook Calendar and Asana integration simplifies scheduling by automatically mapping tasks in your calendar, increasing visibility and accountability. Learn how to [connect Outlook Calendar with Asana](https://asana.com/apps/outlook-calendar).

## Sync Asana tasks to Outlook Calendar

You can sync Asana tasks to a calendar group in Outlook Calendar to create continuous visibility for members subscribed to the calendar group. Updates to Asana tasks are synced to the associated calendar events but not the other way around.

> The Data sync setting is configured at the individual user level. Each person must set up the integration for their own account.

### Configure Asana \> Outlook Calendar data sync setting 

1.  Navigate to **Customize** on the top-right in My tasks or the project you want to sync with Outlook Calendar.
2.  Select **Apps** and search and select **Outlook Calendar.**
3.  Select **Data sync setting** to start configuring how you want Asana and Outlook Calendar to remain in sync. 

You can configure the calendar group you want to sync Asana tasks to, the conditions for triggering sync, and the standard task fields that are synced to calendar events. 

### Select an existing calendar group or create a new one

The first step is to select a calendar group. By default, we select **Create new calendar** so the events created and updated from Asana do not interfere with the calendar group you regularly use for scheduling meetings. You also have the option to select any existing calendar groups as long as you have \`write\` access to them. 

### Define the conditions for triggering sync

If you select **When an Asana task is added → Create a new Outlook event,** you can define a condition in which sync is triggered. In an Asana project, the available conditions are “Tasks assigned to me,” “Tasks in section,” and “All tasks in project.” In My tasks, they are “Tasks assigned to me” and “Tasks in the section.” 

If you are looking for more customization on how sync is triggered, select **Custom rule**, and you can separately create custom rules that trigger calendar sync.

### Map task and event fields

**Task name**, **Start/Due dates**, and **Description** are required field mappings. You can optionally include or exclude **Collaborators**. By including **Collaborators**, the task collaborators are synced to the event guests list. 

### Initial bulk exports

Upon clicking **Save and close** after you have defined the Data sync setting, we perform an initial bulk export of all the tasks that meet the conditions for sync in My tasks or in projects. 

- In projects, bulk exports apply to all tasks that meet the sync conditions. 

- In My tasks, we only bulk export incomplete tasks with a due date of today and beyond, so your calendar only includes actions you need to complete.

## Grant required permissions to use Outlook Calendar integration

During app installation, if your Microsoft admin has not enabled user consent, you may be prevented from authorizing the required permissions to enable Outlook Calendar integration.

If you run into this problem, please pass along [this help article](https://help.asana.com/s/article/enabling-permissions-for-asana-and-microsoft-integrations?language=en_US) to your Microsoft admin to enable you to get the appropriate permissions. 

## Automate scheduling

Use rules to automatically create calendar events based on specific triggers. You can use one of the Outlook preset rules or create a custom one.

1.  Navigate to the **Customize** menu and click **Rules**
2.  Click **Outlook Calendar** on the left sidebar to see a list of preset rules or click **Create custom rule**
3.  Choose your trigger and conditions if needed
4.  Choose **Create a calendar event** as an action

From here, you can invite task collaborators to the event, attach files from the task, and generate a Teams meeting link.

The event title, date, and description will be based on the task's information. The events are added with a link to the associated Asana task in the description.

## Create one-off calendar events

You can create a calendar event directly from an Asana task to schedule a one-off event. The event's description and title will populate based on the task, and can also be edited.

To create a one-off event, go to the task, click **Add Outlook Calendar Event** under **Apps**, and select **Create new event**.

From here, you can edit the event's details, such as title, description, date range, start time, duration, and guests. When specifying the time, you can choose **First available time within date range** for start time and duration, to automatically find the best exact start and end time without having to manually look at your calendar.

## Link calendar events

 

You can link an existing calendar event to an Asana task by typing the event name in the **Outlook Calendar** field of your task. As you search for the event, the search typeahead looks through events from all the calendars you have access to, in order to find the best match.

## How to integrate Asana with Outlook calendar

In this video, we will show you how to integrate Asana with Outlook Calendar to automatically schedule and manage tasks by connecting them to calendar events.

Video: https://fast.wistia.net/embed/iframe/d7sbc7m4do?web_component=true&seo=true&videoFoam=false

## AI Meetings

[AI Meetings](https://help.asana.com/s/article/asana-meetings) helps you prepare for and follow up on your meetings. When you connect your Google Calendar or Outlook Calendar to Asana, AI Meetings can work with your upcoming calendar events so you can keep your related tasks and projects close at hand. Learn more about [AI Meetings](https://help.asana.com/s/article/asana-meetings).

[](https://forum.asana.com/c/forum-en/tips/6)

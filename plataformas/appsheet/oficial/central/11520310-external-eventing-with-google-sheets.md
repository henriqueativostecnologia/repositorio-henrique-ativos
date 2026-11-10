---
fonte: https://support.google.com/appsheet/answer/11520310?hl=en
baixado: 2026-11-10
---

# External eventing with Google Sheets

To set up a [bot](https://support.google.com/appsheet/answer/11432969) that triggers a [process](https://support.google.com/appsheet/answer/11445386) when a user changes data in a Google Sheet, perform the following steps:

1.  [Configure AppSheet Events on Google Sheets](#configure) to allow a data change event to be sent to your app when a user changes data.
2.  [Create the data change events in your AppSheet app](#create-data-change-events) that are triggered by Google Sheets.

**Note**: External data change events are triggered only when a **user** changes data in a Google Sheet, not when the data is changed programmatically, for example, by an app or an Apps Script. 

See [Troubleshoot](#troubleshoot) for tips on resolving issues.

## Get started

The following video demonstrates how to set up external eventing with Google Sheets, as described in this section.

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=dvA3r4BnoXc

## Configure AppSheet events on Google Sheets

To configure AppSheet Events on Google Sheets to allow a data change event to be sent to your app from the sheets when a user changes data:

1.  Install the [AppSheet Events Add-On](https://workspace.google.com/marketplace/app/appsheet_events/592572205846)from the Add-On marketplace.
2.  Open a spreadsheet and select **Extensions \> AppSheet Events \> Enable for document** to enable the add-on.
3.  Enable **Add-ons\> AppSheet Events \> Turn events on/off \> *sheet*** for each sheet from which you want to send events.

    Shows Extensions\> AppSheet Events \> Turn events on/off \> Sheet1 in the Sheets Extensions drop-down.

In addition, you can enable the add-on for [response sheets from Google Forms](https://support.google.com/appsheet/answer/10106596).

## Create the data change events in your AppSheet app

To create the data change [events](https://support.google.com/appsheet/answer/11445188) in your AppSheet app to be triggered by Google Sheets:

1.  Open the app in the editor.

2.   Go to **Data**, click **+** in the top header of the Data panel, and add tables for the Google Sheets that you enabled to send events in the previous section.

3.   We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Data \> Tables**, click **+ New Table**, and add tables for the Google Sheets that you enabled to send events in the previous section.

4.  Select **Data \> Table** and add tables for the Google Sheets that you enabled to send events in the previous section.

5.  Select **Automation \> Events** and create an event that triggers on **Data Change**.
    You can configure the event for adds or deletions only, as required. For example, the following event triggers when content is added to the **employees** table.

    Data change event triggered with an add to the employees table.

6.  [Create a bot](https://support.google.com/appsheet/answer/11432969#create-bot) that uses that event.

7.  When you modify the sheet in Google Sheet, you should see the event trigger after a few seconds. For Google Forms, new rows added to the [response sheet](https://support.google.com/appsheet/answer/10106596) through direct interaction with the Google Form can also trigger events.

    **Note**: Third-party (like IFTTT) or scripted interactions will not trigger events.

To learn more about events, see [Events: The Essentials](https://support.google.com/appsheet/answer/11445188).

## Troubleshoot

If the event hasn't triggered the bot after a few seconds, check that the event was received in the Automation Monitor. See [Monitor automation](https://support.google.com/appsheet/answer/11447502) for more information. You can also try removing and re-adding the event in the automation.

If the event doesn't show up, verify your table selection in Google Sheets and that you are logged into a Google account that has access to both the Google spreadsheet and the AppSheet app (from the **Users** tab).

If the event did show up but did not run, check that your Table, Condition, and data change type are all correct in the event configuration in AppSheet.

---
fonte: https://support.google.com/appsheet/answer/10104391?hl=en
baixado: 2026-11-10
---

# Smart Assistant view

This feature is available to **AppSheet Core** accounts and above. See [AppSheet pricing](https://about.appsheet.com/pricing/).

The assistant view allows you to interact with your app with your voice, similar to Siri or Google Assistant.

**Notes**:

- The assistant view currently works with English and Spanish language commands.
- When running your app in a desktop, the assistant view speech recognition only works in the Google Chrome browser.

## Get started

Learn how Smart Assistant works with your AppSheet app. 

**Note**: The steps to enable the Smart Assistant view are out of date in this video. See [Enable the Assistant view](#enable).

Video: https://www.youtube.com/watch?v=NGbOtnaug2w

## Sample template

Use the [Facility Inspections](https://www.appsheet.com/templates/Inspect-points-throughout-various-properties) template for an example of the Smart Assistant view.

## Enable the Smart Assistant

To enable the Smart Assistant:

1.  Open your app in the editor.
2.  Go to **Intelligence ** Intelligence icon  and click **Smart Assistant** under **Options.**
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to the **Intelligence \> Smart Assistant** pane.
3.  Turn on **Enable Smart Assistant.**
4.  Select the locale to use for Smart Assistant from the **Locale** drop-down.

This will create a new **Assistant view** in the menu of your app:

Assistant view in app menu

## Customize the Assistant view

To customize the Assistant view:

1.  Go to **App ** App icon **\> Views**.
2.  Select the **Assistant** view under Menu Navigation in the Views pane.
3.  Edit the Assistant view, as desired.
4.  Save the app.

## If you are using the legacy editor

To customize the Smart Assistant view, click **Show system views** on the  **UX \> Views** pane and expand and edit the **Assistant** view definition. 

## Use the Assistant view

Below is a summary of the types of commands that you can use in the Assistant view.

### View data

You can navigate to different tables and rows in your app using commands similar to the following:

- "Show me my customers" to navigate to a table called `Customers`
- "Go to orders" to navigate to a table called `Orders`
- "Go to Bob Barker" to navigate to the row with label `Bob Barker`

### Filter data

You can filter your data using commands similar to the following:

- "Show me all open orders" to navigate to the `Orders` table and display rows where the enum `Status` column equals **Open**
- "Show me orders from last week" to filter on a `Date` column in the `Orders` table
- "Products that cost at least \$5"

You can combine multiple filters in a single command:

- "Let me see Bob Barker's open orders from today"

You can also apply filters step by step:

- "Show me the open orders"
- "Just the ones from today"

If you have a `LatLong` column in your table, you can filter by distance:

- "Stores that are less than 5 miles away"

### Run actions

When viewing a particular record, you can use a voice command to run [actions](https://support.google.com/appsheet/answer/10107706).

- "Go to Bob Barker"
- "Send him an email"
- "Add a new order for Bob for November 1st"

## Limitations

Right now, you cannot filter by `Text` type columns. You can work around this limitation by converting your `Text` columns to `Enum`. For example, if you want to filter your data by State, make sure that your `State` column is an `Enum` with a list of states as its enum values.

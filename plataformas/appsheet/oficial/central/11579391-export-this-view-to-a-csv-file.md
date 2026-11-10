---
fonte: https://support.google.com/appsheet/answer/11579391?hl=en
baixado: 2026-11-10
---

# Export this view to a CSV file

This action downloads the rows of a [view](https://support.google.com/appsheet/answer/10106772) to a CSV file.

Export only works for applications that [require sign-in](https://support.google.com/appsheet/answer/10104975), and only when the app is running in a browser. It is not supported for public applications.

## Invoke an "export this view to a CSV file" action

Once you have created the Export action as described in the sections below, you can invoke it as follows:

1.  Open the application in a browser. Export only works when the app is running in a browser.
2.  Navigate to the table view having the Export action.
3.  Click the **Export** button. (If you do not see the **Export** button, you may need to edit the Export action and choose a different **Prominence** on the **Appearance** tab.)
4.  The Exported CSV file should appear at the bottom of the browser screen.

## Create an "export this view to a CSV file" action

To create an Export This View to a CSV File action:

1.  Open the app in the app editor.
2.  Go to **Actions**, click **+ **in the top header of the Actions panel, and click **Create a new action**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **Behavior \> Actions **and click **+ New Action**.
3.  Give the action a meaningful name by setting the **Action name** property.
4.  Use the **For a record of this table** dropdown to select the table from which the records should be downloaded. Views based on the table you select are eligible for export.
5.  In the **Do this** dropdown, select **App: export this view to a CSV file (not a row-level action)**
6.  Set the **CSV file locale** property as described in [configure the CSV locale](https://support.google.com/appsheet/answer/11512216).
7.  Expand the **Appearance** tab.
8.  Give the Export button a meaningful name by setting the **Display name** property.
9.  Select an **Action icon** for the export button.
    You can enter **export** in the search window and hit **Enter** to narrow down the list of icons. One of the icons showing an arrow leaving a document is often a good choice.
10. Select a **Position **to control how prominently the Export button is displayed.
11. Click **Save**.

## Row filtering

The app creator and app user can control which rows are exported by:

- The app creator can base the **View** on a **Slice** having a [Row filter condition](https://support.google.com/appsheet/answer/10106308). Only rows that match the Row Filter Condition are exported.
- The app creator can specify a [`LINKTOFILTEREDVIEW()` ](https://support.google.com/appsheet/answer/10107338)with a filter expression. Only rows that match the filter expression are exported.
- The app user can specify a **Search Term in** the **Search** box for the view while running the app. The app user can search any field for which [**Search?**](https://support.google.com/appsheet/answer/10106509) is true. Only rows that contain the **Search Term** are exported.
- The app user can specify one or more **Search Filter** conditions using the Filter drop-down in the **Search** box while running the app. The app user can search any field for which [**Search?**](https://support.google.com/appsheet/answer/10106509) is true. The app user can apply Search Filter conditions for any combination of searchable fields. Only rows that match all of the Search Filter conditions are exported.

These row filtering techniques can be combined. For example, the app creator could define a View on a Slice having a **Row Filter Condition**. The app creator could then define a `LINKTOFILTEREDVIEW()`** **using that slice which has its own filter expression. Finally, the app user could use the **Search** box to specify a **Search Term** or one or more **Search Filter** conditions while running the app. Only rows that match all of these filtering conditions are exported.

## Exported row sort ordering

You can control the exported row sort ordering by specifying **Sort by** for the **View**.

## Column filtering and column ordering

You can control which columns are exported and the order of those columns by basing the **View** on a **Slice** and specifying **Slice Columns** for the **Slice**.

**Note**: Specifying **Column Order** for a **Table View** currently has no effect on which columns are exported or the order of those columns.

## Private tables

CSV Export can be used to export data from [private](https://support.google.com/appsheet/answer/10106508) tables.

The app creator must first create an **App: export this view to a a CSV file** action for the Private table, as described above.

The app user can then sign-in to AppSheet using their account, invoke the application, and invoke the **App: export this view to a a CSV file** action, as described above. AppSheet will locate the Private table belonging to the signed-in user and export the contents of the Private table to the CSV file.

## Sample applications with an export action

- [Export CSV](https://www.appsheet.com/samples/How-to-export-data-to-csv?appGuidString=866b3f95-8d83-47a2-b015-872f0a029089)
- [Export CSV of filtered rows](https://www.appsheet.com/samples/This-app-shows-how-to-filter-your-data-using-a-form-and-export-it-to-CSV?appGuidString=1561bf63-ff85-4158-87e4-d29f7cab2c67)

## Troubleshoot

If CSV export fails see [Troubleshoot CSV export](https://support.google.com/appsheet/answer/11512215).

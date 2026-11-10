---
fonte: https://support.google.com/appsheet/answer/10106385?hl=en
baixado: 2026-11-10
---

# Detail view type

The Detail view type displays details about a record. You can configure the view to define the image presentation, column order, [quick edit columns](https://support.google.com/appsheet/answer/10106609), page navigation, and more.

This view type is used by default when an item is selected in the table, deck, and gallery view. See [System-defined reference views](https://support.google.com/appsheet/answer/10106516#system-generated-ref-view).

Detail view example

Create and configure a detail view as described in the following sections. 

- [Create a detail view](#create-view)
- [Configure the detail view options](#configure-view-options)
- [Control column order in a detail view](#control-column-order)
- [Configure card blocks in detail views to optimize the desktop design](#configure-card-blocks)

## Create a detail view

To create a detail view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10106688#create-view).
2.  Configure the detail view, as follows:
    - Select **detail** as the **View type** when configuring the detail view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
    - Configure the [detail view options](#configure-view-options).
    - Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
3.  When you are done, save your changes by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## ****Configure the detail view options

Configure the detail **View options** by using the settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Use Card Layout                                                               | Turn on to use a [card                                                        |
|                                                                               | view](https://support.google.com/appsheet/answer/11908538) layout for header  |
|                                                                               | items.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Main image                                                                    | Image column to display as main image for each row.                           |
|                                                                               |                                                                               |
|                                                                               | Select a column of type `Image` from the drop-down or select one of the       |
|                                                                               | following values:                                                             |
|                                                                               |                                                                               |
|                                                                               | -   Auto assign (*column*) - Let AppSheet auto-assign a value. The column     |
|                                                                               |     that is auto-assigned is shown in parentheses.                            |
|                                                                               | -   None - Don't display an image.                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Header columns                                                                | Columns to highlight at the top of each slide. For example:                   |
|                                                                               |                                                                               |
|                                                                               | Add header columns to a detail view                                           |
|                                                                               |                                                                               |
|                                                                               | Click **Add** and select the column name. Repeat to add another header        |
|                                                                               | column.                                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Quick edit columns                                                            | Columns that are editable directly from the detail view. To use this option,  |
|                                                                               | the data source of the detail view must allow edits. See [Quick edit          |
|                                                                               | columns](https://support.google.com/appsheet/answer/10106609).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Sort by                                                                       | Columns used to sort rows. Click **Add** and select the column name and       |
|                                                                               | whether to sort in **Ascending** or **Descending** order. Repeat to configure |
|                                                                               | additional sort by rules.                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Column order                                                                  | Order to display columns, if different from the original. See [Control column |
|                                                                               | order in a view](https://support.google.com/appsheet/answer/10107315).        |
|                                                                               |                                                                               |
|                                                                               | **Note**: Make sure that you add the [Show type                               |
|                                                                               | columns](https://support.google.com/appsheet/answer/12463320) that you want   |
|                                                                               | to be displayed.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Display mode                                                                  | Display mode for column data.                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Image style                                                                   | Style to use for the main image. See [Images in a detail                      |
|                                                                               | view](https://support.google.com/appsheet/answer/10107317#detail-view).       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Max nested rows                                                               | Maximum number of rows to show for related reference lists. Set the desired   |
|                                                                               | number.                                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Slideshow mode                                                                | Turn on to allow users to navigate to previous or next slides.                |
|                                                                               |                                                                               |
|                                                                               | Slideshow mode                                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Desktop layout                                                                | Layout to use when displaying details on a desktop device. Select one of the  |
|                                                                               | following options:                                                            |
|                                                                               |                                                                               |
|                                                                               | -   **Split view** - Detail views open in a new pane to the right of the      |
|                                                                               |     list. Users can click  to expand to full screen. For example:\            |
|                                                                               |     \                                                                         |
|                                                                               |     Split view desktop layout                                                 |
|                                                                               | -   **Full screen** - Detail views take up the full width of the page and     |
|                                                                               |     include a breadcrumb for navigating back up the nested list. For          |
|                                                                               |     example:\                                                                 |
|                                                                               |     \                                                                         |
|                                                                               |     Full screen desktop layout                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Desktop multicolumn layout                                                    | Turn on to display details using multiple columns in desktop browsers if      |
|                                                                               | space is available.                                                           |
|                                                                               |                                                                               |
|                                                                               | With the multicolumn layout, the headers, main image, and actions persist in  |
|                                                                               | the left column while the content in the right column can scroll.             |
|                                                                               |                                                                               |
|                                                                               | A maximum of three columns will be displayed.                                 |
|                                                                               |                                                                               |
|                                                                               | For example:                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Control column order in a detail view

Control the column order in a detail view if different from the original order. See [Control column order in a view](https://support.google.com/appsheet/answer/10107315).

## Configure card blocks in detail views to optimize the desktop design

 Configure card blocks in a detail view to optimize the display of information for the [desktop design](https://support.google.com/appsheet/answer/12407883), as shown below.

Detail view showing card blocks

Card blocks display only if there is sufficient width available on the page. You may need to resize the panel to view the content as card blocks.

To configure card blocks in detail views, add one or more `Show` type columns set as the `Page_Header` category to the associated table. Each `Page_Header` column creates a new card block that includes all columns below it until the next `Page_Header` column.

You can configure card blocks in two ways, using virtual columns or adding empty columns to your spreadsheet, as described in [*Improve the presentation of detail and form views using Show types*](https://support.google.com/appsheet/answer/12463320).

By default, `Show` type columns are only permitted in form views. To include `Show` type columns in detail views, when [configuring settings for detail views](https://support.google.com/appsheet/answer/10107387#detail-view) turn on **Include Show columns in detail views** in the **Detail view** section.

When turned on, the **Include Show columns in detail views** setting results in different behavior on mobile and desktop, as follows:

- Mobile: Shows `Section_Header` columns only.
- Desktop: Shows both `Section_Header` and `Page_Header` columns.

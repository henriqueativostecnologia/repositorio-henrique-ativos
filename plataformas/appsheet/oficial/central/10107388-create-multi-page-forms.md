---
fonte: https://support.google.com/appsheet/answer/10107388?hl=en
baixado: 2026-11-10
---

# Create multi-page forms

Create multi-page forms by performing the following steps:

1.  [Set up the table](#set-up-table) 
2.  [Configure the page headers](#configure-page-headers)
3.  [View the form in the app](#view-form-app)
4.  (Optional) [Change to use tabs](#change-to-tabs)

First, some basic information about forms in AppSheet

- A form allows the user to enter information into a table. Therefore, every form is connected to a table where the information is stored. 
- Each field on the form corresponds to a column in the underlying table. 
- By default, the form field will be labeled using the column header in your table.
- By default, the form fields will be displayed in the same sequences as they appear in your table.

See also: [Create multi-page forms with conditional branching](https://support.google.com/appsheet/answer/10107390)

## Set up the table

When creating a multi-page form in AppSheet, think of the page break as another field in your form. Each field in the form corresponds to a column in the table. Therefore, to create a page break, simply create a new column in your table at the location where you want the page break to appear. 

The screenshot below shows an example column structure for a Contact Us form. Columns `Page 1`, `Page 2`, and `Page 3` will be set as page breaks.

Contact Us Forms sheet showing Page 1, Page 2, and Page 3 columns

**Note**: You can call the column used for the page break anything you want. The name of the page break column is only visible to the app creator and will not be shown in the form.

## Configure the page headers

After adding the table to AppSheet, the page break columns will appear along with all the other columns for the table. Set these columns to be page breaks as follows:

1.  Open the app in the editor.
2.  Go to **Data**  and select the table you want to edit in the Data panel.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data**, click **Columns**, and expand the table you want to edit.
3.  Click **Edit** (pencil icon) next to the column name.
4.  Change the **Type** to **Show**.
5.  Change the **Category** to **Page_Header**.
6.  Optionally enter text to be displayed at the top of the page.

For example:

Configure multi-page column as Show type

## View the form in the app

The default form will add a **Next** button for the user to progress between pages. On the final page, the user will be shown the **Save** button.

Multi-page form viewed in app

## Change to use tabs

You can choose to break the form up with tabs. Change the **Form page Style** to **Tabs** when configuring the [form view](https://support.google.com/appsheet/answer/10107387#forms).

Set the Page Style for the UX to Tabs

Multi-page form in app using tabs

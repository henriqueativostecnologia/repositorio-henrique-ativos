---
fonte: https://support.google.com/appsheet/answer/10106787?hl=en
baixado: 2026-11-10
---

# Customize input forms

You can control the presentation of data.

If you choose to allow users to add or edit data from the Data section in the editor, your app will give users the ability to create or modify a data row using a form. The form is a sequence of labels (column names) and input fields (specific to the column data type). You can customize the form in the following ways:

- Column descriptions--you might want to provide a verbose description of each column for the user. If a comment is found, it is used in the label instead of the column name.
- Form style--configure the layout of the form and whether the individual fields are numbered as described in [Configure view settings](https://support.google.com/appsheet/answer/10107387#configure).
- Using Show-type columns.

Show-type columns are empty columns in your spreadsheet that serve the sole purpose of improving the presentation of data capture forms. There are six categories of Show types. 

**Categories**:

1.  **Page_Header**: Create a new page within the form
2.  **Section_Header**: Create a new section within the same form page
3.  **Text**: Show some descriptive text
4.  **Url**: Show a clickable URL. Here's an example of the **Content** field format: `{"Category":"URL", "Content":"http://www.your-url.com"}`
5.  **Image**: Show a static image. Here's an example of the image **Content** field format: `{"Category":"Image","Content":"http://www.your-url.com/your-image.png"}`  
    See also: [Display images and documents](https://support.google.com/appsheet/answer/10107317)
6.  **Video**: Show an MP4 video or Youtube video (for MP4 videos, use the hosted link; for Youtube videos, use the embed link). Here's an example of the video **Content** field format: `{"Category":"Video","Content":"https://www.youtube.com/embed/IdwbSNJwLAk"`

## Best practices

Here are some best practices for building effective forms in your app: 

1.  Do not change column names in AppSheet-- the column names should match 1:1 with the column headers in the sheet. If you change the column names and they no longer match the column headers in the sheet, subsequent attempts to regenerate column structure will cause you to lose information you had added to the app definition.
2.  Keep column names short. This makes it very convenient as you use column names in `Show_If` and other type qualifier conditions
3.  Do not use column names with positional indicators. For example, `Insulation Damaged?` is a good column name. But `(22) Insulation Damaged?` is not. This again is meant to protect your app edits when you regenerate column structure. For example, if you add a new column before this particular column and change its name to `(23) Insulation Damaged?`, AppSheet will not be able to correlate this to the previous column definition.
4.  Use the column `Description` (not the column `Name`) to provide long descriptive text. This is what is shown in the form as the question for the user. For example, `Is insulation damaged on any cables in the system? Including in electrical boxes and on roof? `The corresponding column `Name` on the other hand would probably be something compact like `Insulation Damaged?` If no `Description` is provided, AppSheet will use the column `Name` instead. 

## Input form as the only view in the app

You can choose to make your input form the only view in your app, so new users are not able to see past submitted data.

To do this, simply [delete any data view](https://support.google.com/appsheet/answer/10106688#delete), only keeping the form view.

---
fonte: https://support.google.com/appsheet/answer/10107664?hl=en
baixado: 2026-11-10
---

# Capture signatures and drawings

Capturing signatures and drawings is easy with AppSheet.

## Capture signatures

Insert a column in your spreadsheet and include the word **Signature** in the [column header](https://support.google.com/appsheet/answer/10099523). AppSheet will automatically detect this new column as a `Signature` type after you [regenerate](https://support.google.com/appsheet/answer/10106675) your columns. Alternatively, you can name the column anything you like and change the [column type](https://support.google.com/appsheet/answer/10106435) to `Signature` manually. See [View and edit columns](https://support.google.com/appsheet/answer/10106674#view-edit-columns).

When configuring a `Signature` column, optionally you can specify the folder where the signature files are stored using the **Image/File folder path** property in the Type Details section.

**Note**: The **Save externally** property has no effect on your app; its value is ignored.

A background image can be provided for signature capture by setting an image URL or `Image` type column value as the [Initial Value](https://support.google.com/appsheet/answer/10106437). 

Columns pane showing Signature field of Signature type

Signature field in the app

## Capture drawings

Capturing drawings is equally simple. The `Drawing` type provides a canvas and colored pens that allow you to capture free-form sketches within the app.

To capture drawings, insert a column in your spreadsheet and include the word **Drawing** in the [column header](https://support.google.com/appsheet/answer/10099523). AppSheet will automatically detect this new column as a `Drawing` type after you [regenerate](https://support.google.com/appsheet/answer/10106675) your columns. Alternatively, you can name the column anything you like and change the [column type](https://support.google.com/appsheet/answer/10106435) to `Drawing` manually in the **Data \> Columns** pane in the editor.

When configuring a `Drawing` column, optionally you can specify the folder where the drawings are stored using the **Image/File folder path** property in the Type Details section.

A background image can be provided for drawings by setting an image URL or `Image` type column value as the [Initial Value](https://support.google.com/appsheet/answer/10106437). The user can also take a photo or select an image to use as the background image with the camera button on the `Drawing` input.

## Troubleshoot

Some image urls will not work as background images due to the [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) policy of the server hosting the image. If the background image initially seems to work but disappears after syncing the app, this is most likely the problem. When this occurs, usually the only solution will be to find a different way to provide the image. For example, images hosted on Google Drive using the [export link](https://support.google.com/appsheet/answer/10107317) format do not work as background images due to CORS limitations. One alternative is to upload the image through the app itself using an [Image column](https://support.google.com/appsheet/answer/10106529), then use the value that is written into the sheet as the initial value of the Drawing column.

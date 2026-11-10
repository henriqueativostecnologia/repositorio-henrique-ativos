---
fonte: https://support.google.com/appsheet/answer/10105830?hl=en
baixado: 2026-11-10
---

# Display images and videos in your app

Display images and videos in your app as described in the following sections:

- [Supported image and video column types](#column-types)
- [Allow users to draw on an image](#allow-drawing-on-images)
- [Display images or videos using Show type columns](#show-type-columns)

## Supported image and video column types

The `Image` and `Thumbnail` types can be used to capture and display images in the app. The `Video` type can be used to display video (video capture is currently not supported).

These types should be used when image capture is needed or you want to display the [URL or file name values](https://support.google.com/appsheet/answer/10106610) that are stored within your table data. If you don't already have a column reserved for your image or video, you'll need to [add a new column](https://support.google.com/appsheet/answer/10106675) first and [change the column type](https://support.google.com/appsheet/answer/10106375). 

## Allow users to draw on an image

Allow users to draw on an image when editing an `Image` column by turning on the **Allow drawing on images** property.

Drawing tools include:

- Android devices only: Free draw, oval, rectangle, arrow, and text drawing tools, and standard color options for shape outlines and text
- Desktop and iOS mobile devices: Free draw and standard color options for shape outlines

See [Configure column properties](https://support.google.com/appsheet/answer/10106509).

## Display images or videos using Show type columns

You might want to show a particular image or video within a form view whenever users are creating or editing a record, but without including it in the data as part of the record. In this case, you can use the [Show](https://support.google.com/appsheet/answer/10106787) column type. In the **Category** field of the **Show** column choose **Image** or **Video**, then place an image link or video embed link in the **Content** field.

**Note**: The link must be a public URL for the media itself, not to a web page that displays it (an image URL will typically end with `.png` or `.jpg`, for example). This is a common problem when trying to use [images from Dropbox or Google Drive](https://support.google.com/appsheet/answer/10107317).

You can control whether Show type columns appear in other view types, such as detail views, when you [configure the view settings](https://support.google.com/appsheet/answer/10107387).

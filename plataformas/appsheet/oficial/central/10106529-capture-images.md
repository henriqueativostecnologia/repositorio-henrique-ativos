---
fonte: https://support.google.com/appsheet/answer/10106529?hl=en
baixado: 2026-11-10
---

# Capture images

Capture images in your app as described in the following sections:

- [Get started](#get-started)
- [Configure your app to capture images](#configure)
- [Capture images on mobile (Android/iOS) devices](#capture-images-mobile)
- [Capture images in a web browser](#capture-images-browser)
- [Control image size](#control-image-size)
- [Annote images](#annotate-images)
- [How image capture works](#how-image-capture-works)
- [Image storage in the cloud](#image-storage-in-cloud)

## Get started

Learn how to include an image in a form by using the [Images in forms](https://www.appsheet.com/template/showdef?appId=Imagesinforms-71626) feature sample

## Configure your app to capture images

To capture images, insert a column in your spreadsheet and include the word **Image** in the [column header](https://support.google.com/appsheet/answer/10099523). For example, if you want to capture three images, you might name your columns `Image1`, `Image2`, and `Image3`. When you [regenerate the table](https://support.google.com/appsheet/answer/10106675), AppSheet will automatically detect these columns and set their type to `Image`.

Alternatively, you can name the column anything you like and change the column type to `Image` when [configuring column properties](https://support.google.com/appsheet/answer/10106509).

For apps that need to exclusively work with small thumbnail images, we provide a `Thumbnail` type. AppSheet doesn't automatically detect the difference between a regular image and a thumbnail. To explicitly choose the `Thumbnail` type, change the `Column Type` to `Thumbnail`.

## Capture images on mobile (Android/iOS) devices

On mobile devices, the user is prompted with the choice to take a new photo or use the camera roll.

## Capture images in a web browser

Your app can be run directly in a web browser; however, this impacts the behavior of image capture.

When an app is run in a web browser on a desktop or laptop, the camera isn't used for image input. Instead, the user is prompted to pick an image from the filesystem. When an app is run in a web browser on a mobile device, the camera is used for image input.

In either case, it's important to note the new or updated record with the image must be synced to the backend *before* the browser tab is closed. Otherwise, the captured image content will be lost. If you expect to run your app in a browser and the app captures images, do not enable delayed sync. If you do enable delayed sync, please advise your users to explicitly sync their changes before closing the browser. If the browser is used on a mobile device, be aware that simply switching away from the browser app to another app on the device may cause the browser to automatically close.

## Control image size

You can control the captured image size by setting the **Image upload size** when [configuring general view settings](https://support.google.com/appsheet/answer/10107387#inputs).** **This sets the maximum image width to one of the following options:

- **Default**: 600px
- **Low**: 200px
- **Medium**: 800px
- **High**: 1600px
- **Full**: use the original image size

If you have issues with device crashes or hangs while taking photos, please look at the article about [troubleshooting application crashes and errors on mobile devices](https://support.google.com/appsheet/answer/10106237).

You can require that images captured in apps meet a minimum specified resolution using the Acceptable image resolution policy, as described in [Define governance policies](https://support.google.com/appsheet/answer/11948767).

## Annotate images

To enable users to annotate images they've captured or uploaded, use the [Drawing type](https://support.google.com/appsheet/answer/10107664).

## How image capture works

See how the camera function works in the [Inspection sample app.](https://www.appsheet.com/samples/A-mobile-app-for-manufacturing-equipment-inspections?appGuidString=52e893d8-dd9d-4fc9-aee6-9942c399c5c1)

Here's how AppSheet processes the photos taken with the camera:

- Any photo taken on a device with your app:
  - Uses the default camera settings on that device.
  - Is saved in full resolution in the camera roll on the device, unless the [Save images to gallery](https://support.google.com/appsheet/answer/10107387#save-images-to-gallery) option is disabled.
- If you use the app on the desktop, the image capture function only allows you to open an image file. Using the image function on a mobile device will allow you to either upload an image from your device's gallery or to manually take a photo.
- When the user presses the **Sync** button, the photo is uploaded at a reduced resolution to conserve network bandwidth. The image resolution used is controllable as described in [Control image size](#control-image-size).

## Image storage in the cloud

By default, the captured image is saved in a subfolder in the same location as the spreadsheet.

- The subfolder is called `{TableName}`*`_Images`* by default.

- You can optionally specify a custom folder name by using the `FolderLocation` property of the column definition. The custom folder is also relative to the location of the source spreadsheet. This custom folder name can be a constant value or an expression that uses the column values of the table. This means images captured for certain rows can be stored in a different folder from images captured for other rows.

- If your data source is a database (or some other data source that doesn't provide cloud storage), then there's no spreadsheet location to use. Instead, the platform uses the default app folder location (usually `/appsheet/data/{appName}`), or as configured under [App Properties](https://support.google.com/appsheet/answer/10106613#app-properties) when you customize the About page.

- It is also possible to store your images in a [cloud object store.](https://support.google.com/appsheet/answer/10106769)

Within the folder, each image is saved with a unique file name.

- Each image file name is prefixed by the key of the row being updated, the column name, and a short representation of a timestamp. The structure of the filenames is not changeable. However, you can use a computed-key if you would like to have more meaningful names for these files.
- The row in the spreadsheet is updated to contain the name of the image file just created. The image file name includes the row key as well as the column name so it can easily be correlated to the corresponding row.

---
fonte: https://support.google.com/appsheet/answer/10106610?hl=en
baixado: 2026-11-10
---

# Display images, documents, and audio files

The following sections provide guidelines relating to the display of images, documents, and audio files in your app:

- [Which column types are used to store images, documents, and audio files?](#where-stored)
- [URL values](#url)
- [File name values](#filename)
- [Display PDF files](#pdf-files)
- [Guidelines for custom image sizes](#custom-image)
- [Configure images in a detail view](#detail-view)
- [Turn on external URLs for image files](#external-url-images)
- [Show images in Smartsheet](#smartsheet)
- [Control document and image caching](#caching)

## Which column types can be used to store images, documents, and audio files?

In the app editor, the following column types can be used to store images, documents, and audio files:

- `Image` to store images.
- `File` or `Url` to store documents and audio files.

In your spreadsheet, image, document, or audio file values are stored as either a URL or a file name.

## URL values

If you have URLs in a column and they are publicly accessible, the app allows users to click on the URL and see the content in a hosted web browser window, or download the content if viewing is not supported (for example, zip files). Additionally, the users have the option of opening the content externally in the native web browser on the device (such as mobile Safari on iOS).

If you store the value as a URL, make sure that the URL is publicly accessible. 

Many users who choose this option provide image URLs that appear accessible to them, but are not really accessible to the public. Here are some examples of **bad** image URLs:

- **Facebook:**  You may be able to access images from your Facebook album because you are logged into Facebook, but when some other user tries to see the image, they will get an error. Whenever you are using an image from some kind of online storage provider, make sure that public access permissions are provided.

&nbsp;

- **Google Drive:** Viewing an image on Google Drive shows your image on a web page that hosts an image, but the URL of the web page will not work as a link to your image. We recommend using the solution described in [File name value](#filename).

&nbsp;

- **Dropbox:** Dropbox, like most cloud file systems, shows your image on a webpage, but the webpage itself is not actually an image. It is a web page that hosts an image. This [article](https://cantonbecker.com/etcetera/2014/how-to-directly-link-or-embed-dropbox-images/) explains how to construct a link to a Dropbox image. 

- **Local Computer:** An image URL from your local computer of the form `file://MyImages/MyImage.jpg` or `C:/MyImages/MyImage.jpg`. AppSheet has no access to your local computer, nor do you have the option to upload an image to AppSheet. Instead, place your images in your cloud storage provider and use one of the mechanisms described above.

## File name values

If you have files in a `File` column, the app opens the content in a hosted web browser. Depending on the device and operating system, there may be support for viewing a variety of file types-- for example, most browsers enable PDF viewing and playback of MP3 audio files.

If you store the value as a file name, the image or document must be stored in your cloud file system, not on your own computer.

Consider the following when using a file name value:

- In the app editor, AppSheet provides a file selector widget that lets you browse your cloud file system to find an image.

&nbsp;

- If you are specifying an image or document file name in your spreadsheet, the file should be in the same folder location as your spreadsheet. For example, if you use Google Drive and your spreadsheet is in the `/appsheet/data/MyApp` folder, then if you have the image `MyImage.jpg` in the same folder, you can just use the value, `MyImage.jpg`, in the appropriate cell.

&nbsp;

- It is sometimes easier to organize images in their own folder. For that reason, we allow image file names to be specified **relative to the location of the spreadsheet**. For example, if your images are in a subfolder called `Images`, you can use the cell value, `Images/MyImage.jpg` or `./Images/MyImage.jpg`.

See [IMAGE](https://support.google.com/docs/answer/3093333) in the Docs Editor Help Center if you need assistance with image sizing.

## Display PDF files

To display PDFs in your app, you will need to add either the file name or the URL where the document is hosted. if you are using URLs, make sure they are publicly accessible by placing them in a public folder. For more information about including PDFs in your app, see [Work with PDF files](https://support.google.com/appsheet/answer/10106523).

## Guidelines for custom images sizes

AppSheet downscales all images to 600 pixels (600px) wide, except for the app background image, which is 1000px wide. For custom images, we generally recommend using square images: 600x600px.

## Configure images in a detail view

The detail view has a *main* image. The main image is automatically selected but can be overridden with the **Main image** setting when [configuring the view](https://support.google.com/appsheet/answer/10106688#configure-view).

On the Views tab of the UX section, the Main image and Image style properties can be set

The **Image style** property can be used to control how the image is shown:

- **Fill** will crop the image to fit the header area (great for photos).
- **Fit** will scale the image down to fit inside the header area (great for logos).
- **Background** will use the image as a background for the whole view (great for pattern images and some photos).

In **Fill** mode, images shown at the top of the detail view will be a maximum of 768x400 pixels. On small screens (768 and below) the image will be 320px tall, otherwise it will be 400px tall. We recommend making a 768x400 image with the middle 375px as usable area, the sides will be cropped off on phones and other small screens. Here's a sample:

Usable area in the Detail view

## Turn on external URLs for image files

By default, app images and other files identified by name (such as, `MyImage.JPG`) or relative path (such as, `Images/MyImage.JPG`) will not have a predictable, meaningful URL that can be readily used outside of the app. If you would like the images stored by the app to be available for other uses, you will need to take extra steps.

For security reasons, AppSheet produces cryptic public URLs for images and files stored by the app. To instead produce URLs **that are less secure** but more friendly to external use, this default **security feature** must be disabled. To do so, go to **Security** Security icon ** \> Options** in the app editor and turn off **Require Image and File URL Signing**:

By disabling **Require Image and File URL Signing**, **you are making your app files less secure**. An app user could potentially modify an image or file URL in order to view any other image or file stored by the app. **This setting affects the security of all images and files stored by the app.** It is best to leave the feature enabled if possible.

Next, configure your app to produce a URL that is usable outside the app for each image or file that should be so accessible. Add another (optionally virtual) column to the same table as the column containing the image or file name, with an `App formula` expression like this:

    CONCATENATE(
      "https://www.appsheet.com/template/gettablefileurl",
      "?appName=", ENCODEURL(CONTEXT("AppName")),
      "&tableName=", ENCODEURL(CONTEXT("Table")),
      "&fileName=", ENCODEURL([image-or-file-column])
    )

Replace *`image-or-file-column`* with the name of the column containing the image or file name or relative path. 

## Show images in Smartsheet

Normally, images are stored as files in a cloud file system and the name of the file is put into a cell of the corresponding row in the data spreadsheet. If your data is in Smartsheet however, there are a couple of extra considerations. Smartsheet does not have a traditional 'file system'. Instead, the images associated with any row should be stored as a row attachment and the name of the attachment file should be stored in the corresponding cell.

Smartsheet allows an image to be saved and shown inline within a cell. Any images captured via an AppSheet app will be saved as a row attachment and will also additionally display inline with the specific cell. However, if you are creating a data set for use with an AppSheet app, the inline images cannot be read and processed by AppSheet. You will need to create the images as row attachments as described earlier.

## Control document and image caching

AppSheet caches documents and images in Cloud CDN (Content Delivery Network) because it is expensive to retrieve and serve images directly from AppSheet servers. It is even more expensive if AppSheet must resize the image before displaying it.

If you are reusing the document or image file URL and directly updating the contents of the document or image file, you will only see the updated value once the cached image ages out of the Cloud CDN cache.

To display a document or image without using the cached version (and without enabling secure access, as described below), see this [Community article](https://www.googlecloudcommunity.com/gc/Tips-Tricks/Open-File-Image-with-external-browser-without-looking-up-cache/m-p/228946). 

If you turn on **Secure PDF** or **Secure Image Access**, AppSheet doesn't cache the document or image in Cloud CDN, however retrieval performance will decline. You can turn on **Secure PDF** or **Secure Image Access** by going to **Security ** Security icon **\> Options** in the app editor:

The Security Options section enables yo8u to Secure PDF access and Secure Image access.

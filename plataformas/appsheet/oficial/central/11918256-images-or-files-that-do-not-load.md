---
fonte: https://support.google.com/appsheet/answer/11918256?hl=en
baixado: 2026-11-10
---

# Images or files that do not load

Many apps are used to capture images. Sometimes, apps are also used to display existing images or files. These images and files normally are stored in the cloud file system associated with the app (for example, Google Drive).

This should all work automatically, but it is not uncommon that somebody moves files around or wants to copy in new files from some other location, etc. These changes can cause images to stop showing in the app. You will see the symptoms of these problems as: (a) a missing image in a mobile/web app, or (b) a missing image in a PDF report generated as part of an automation.

## Basics

First, it is useful to understand how things are supposed to work.

- If your app captures images in an Image column of a table, the values stored in that column are partial path names. Something like `MyTable_Images/<someimagefilename>.jpg.`

- If your data table is called `MyTable` and is stored in a spreadsheet that lives in a particular folder (let's say the folder name is. `/appsheet/data/MyFolder`), then we expect images for that table to be in a sub-folder called `MyTable_Images` (with the folder path `/appsheet/data/MyFolder/MyTable_Images`) and files to be in a sub-folder called `MyTable_Files_ `(with folder path `/appsheet/data/MyFolder/MyTable_Files_`).

- Please note that every application has a default folder (usually something like `/appsheet/data/MyApp-123456`) but the sheets it uses do not need to be in that folder. Images and files are in sub-folders relative to the location of the sheet, not the location of the app default folder.

- If your data source is from something like a SQL database (something that doesn't let you save files to it directly), then by default, the image sub-folders are located within the app default folder (with folder path something like `/appsheet/data/MyApp-123456/MyTable_Images`).

When your app shows images (in a browser or app on a device), it is actually fetching an image from a HTTPS URL. The AppSheet service constructs the image url by combining: (a) the name/id of the app, (b) the name of the table, (c) the name of the file with a relative path within the table.

- These image urls usually take the format below if the app has been set up with the default secure image configuration. `https://www.appsheet.com/template/gettablefileurl?...<many details> ...`

- **If** you have set up your app to avoid using secure images, you may instead see a url that looks like this: `https://www.appsheet.com/get/?..<many details> ... `This format allows the images to be cached and served from CDN (which makes image delivery very fast but is only meant for public images). Most apps will not have this configuration. We'll focus the rest of this troubleshooting guide on the common case.

Using this information, AppSheet is able to respond to the URL `GET` request by:

1.  Going to the cloud file system.
2.  Traversing the folder hierarchy.
3.  Finding the file.
4.  Retrieving its contents.
5.  Serving it back to the caller as a HTTPS response.

Every step of this process can have an error. The most common errors are when the file is not found or there is something wrong with the folder hierarchy.

## Troubleshoot

There are some simple self-service debugging tools you can use to understand why an image doesn't display. The basic approach is to copy the image URL and open it in a browser window. If the image doesn't display, you will instead see an error trace. This will allow you to drill-down step-by-step to find the problem (almost always, a folder or a file is not found where it is expected to be).

Open image URL in a browser to see error trace.

How do you get the image URL? One simple way is to run the app in a browser window, and for images that do not load, right-click and choose **Inspect**. This shows you the details of the html used to render the image, and the image URL will be also present. Copy the image url and open it in a browser window.

Inspect image that does not load

Another approach is to [preview the data in a table](https://support.google.com/appsheet/answer/10105821#preview-table). This by default shows the first 1000 rows of the table and all the columns of each row. Any file or image column value is also shown along with a link to open the file or see the image full size. If you click the link, it will try to open the file or image in a separate browser tab. Once again, you can see a useful error trace.

View Data for a table

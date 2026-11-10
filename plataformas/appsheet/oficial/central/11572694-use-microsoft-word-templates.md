---
fonte: https://support.google.com/appsheet/answer/11572694?hl=en
baixado: 2026-11-10
---

# Use Microsoft Word templates

Customize content using Microsoft Word templates as described in the following sections:

- [Customize content using a Microsoft Word template](#customize-content)
- [Create a Microsoft Word template on Google Drive](#create-template-google-drive)
- [View the template](#view-template)
- [Edit the template](#edit-template)
- [How AppSheet processes a Microsoft Word template](#how)
- [Include an image in the template](#include-image)
- [Include an image URL in the template](#include-image-url)
- [Tips for formatting the template](#tips)
- [Customize the page layout](#customize-page-layout)
- [Add page breaks in PDF attachments](#add-page-breaks-pdf)
- [Unsupported features: Page headers, page footers, or page numbering](#unsupported-features)

See also [Use templates in a bot](https://support.google.com/appsheet/answer/11539957).

## Customizing content using a Microsoft Word template

When configuring a [Send an email](https://support.google.com/appsheet/answer/11447614), [Call a webhook](https://support.google.com/appsheet/answer/11511244), or [Create a new file](https://support.google.com/appsheet/answer/11512511) task, customize content using a Microsoft Word template by performing one of the following tasks:

- If your default data source is Box, Dropbox, Microsoft Office 365, or Microsoft OneDrive (in other words, *not* Google Drive), create a **Microsoft Word** or **PDF** template, as described in [Create a template](https://support.google.com/appsheet/answer/11539957#create-template).
- If your default data source is Google Drive, follow the steps described in [Create a Microsoft Word template on Google Drive](#create-template-google-drive).
- Manually create a Microsoft Word template in your cloud file system and use it, as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

For information about customizing the template, see [Customize content using templates](https://support.google.com/appsheet/answer/11539957#customize-content) and the tips provided below.

## Create a Microsoft Word template on Google Drive

By default, when your default data source is Google, the **Create** button will create a Google Docs template file on Google Drive.

To create a Microsoft Word template on Google Drive:

1.  [Create a template](https://support.google.com/appsheet/answer/11539957#create-template).
    A Google Docs template is created on Google Drive, by default.
2.  Click **View** to view the template.
3.  From the Google Docs **File** menu select **Download** \> **Microsoft Word (.docx)**.
4.  This will convert the Google Docs template to a Microsoft Word template and download it to your browser.
5.  Upload the Microsoft Word template to Google Drive.
    For consistency, upload the Microsoft Word template to the same folder where the newly created Google Docs template resides. Typically this is the **Content** folder beneath the **Default app folder.** The **Default app folder** location is set using the **Info \> Properties** \> **App Properties** tab.
6.  In the AppSheet Editor, click the **Browse** button and navigate to the Microsoft Word document you just uploaded to Google Drive.
7.  Delete the Google Docs template file from Google Drive, if desired.

## View the template

After creating or selecting the template, click **View** adjacent to the template property to view the template.

**Note**: We do not recommend that you edit the template in this view due to the built-in limitations in the way Microsoft Docs files can be opened and edited from the web.

## Edit the template

To edit the template, open the Microsoft Word template from your data source.

## How AppSheet processes a Microsoft Word template

AppSheet reads the Microsoft Word template in HTML format and replaces the template variables and expressions in the HTML template with the data values. The resulting HTML document becomes the email body or attachment. AppSheet converts the HTML document to PDF format before adding it as an attachment.

## Include an image in the template

Your Microsoft Word template can include one or more images.

To include an image:

1.  Open the template in Microsoft Word.
2.  Position the cursor where you want to insert the image.
3.  From the Microsoft Word menu bar select **Pictures** and select the image you wish to include.

When AppSheet exports the Microsoft Word template as HTML, it will include the image as an HTML `<img>` element. The image data is included inline in the **`src`** property of the **`<img>`** element.

When the template is used as an email body template, the resulting HTML email body contains the HTML `<img>` element. The email client that displays the HTML email body displays the image.

When the template is used as a PDF attachment template, the HTML-to-PDF conversion web service retrieves the image value from the HTML `<img>` element and includes the image in the resulting PDF file.

## Include an image URL in the template

Your Microsoft Word template can include one or more image URLs. Each image URL must refer to a publicly accessible image.

## Tips for formatting the template

The following tips may help you control the appearance of your PDF attachments. 

- [Change the line spacing in Word](https://support.microsoft.com/en-us/office/change-the-line-spacing-in-word-04ada056-b8ef-4b84-87dd-5d7c28a85712#:~:text=Change%20the%20line%20spacing%20in%20a%20portion,select%20the%20options%20you%20want%20under%20Spacing.), as follows:
  - Reduce the line spacing to **Single** if it is currently larger, such as 1.5, Double, and so on.
  - Remove space before and after paragraphs.
- Change the header formatting to **Normal Text** rather than Heading 1, Heading 2, and so on. Then apply formatting to control the header's font size, color, boldness, and so on.
- Remove any excess blank lines.
- Check the [page size](https://support.microsoft.com/en-us/office/change-page-size-paper-size-or-page-orientation-in-publisher-f5061db1-5431-4836-8c77-0f47f47d37df#bm2) and [margins](https://support.microsoft.com/en-us/office/change-the-margins-in-your-word-document-c95c1ea1-70b1-4dde-a1da-f5aa2042c829). For example, consider setting the page size to A4 and reducing the top and bottom margins.

## Customize the page layout

In the Word Document, you can specify the following:

- Page Orientation as either Landscape or Portrait.
- Page Width and Page Height.
- Page Margins for Top, Bottom, Left, and Right.

When AppSheet converts the Word Document into HTML, it honors these settings. The HTML body includes properties similar to the following:

    body {
        margin-top: 72pt;
        margin-bottom: 72pt;
        margin-left: 62pt;
        margin-right: 62pt;
        max-height: 612pt;
        max-width: 792pt;
    }

## Add page breaks in PDF attachments

You can include page breaks in the PDF file created from an attachment template file by manually inserting a page break in the Microsoft Word template.

1.  Select the **Insert** tab.
2.  Position the cursor where you want the page break to occur.
3.  From the Microsoft Word **Pages** menu, select **Page Break**.

## Unsupported features: Page headers, page footers, or page numbering

Email templates do not support automatic page headers, page footers, or page numbering. If your Word template file contains Word Headers, Word Footers, or Page Numbers they will be ignored. Instead, you should:

- Include your header contents at the start of your template as normal content. It will appear once at the start of the resulting document.
- Include your footer contents at the end of your template as normal content. It will appear once at the end of the resulting document.

To handle automatic page headers, page footers, and page numbering, we would need to implement a *page layout engine* that computes the page location of each element being displayed. We would need to be aware of page boundaries, so that we could:

- Insert a footer at the end of each page.
- Insert a bottom margin at the end of each page.
- Insert a top margin at the start of each new page.
- Insert a header at the start of each new page.
- Insert appropriate page numbers.

We do not support any of these features because implementing a page layout engine is a lot of work. It is not work that we have done.

---
fonte: https://support.google.com/appsheet/answer/11568965?hl=en
baixado: 2026-11-10
---

# Use Google Docs templates

Customize content using Google Docs templates as described in the following sections:

- [Customize content using a Google Docs template](#customize-content)
- [View and edit the template](#view-edit)
- [How AppSheet processes the Google Docs template](#how)
- [Include an image in the template](#include-image)
- [Include an image URL in the template](#includ-image-url)
- [Tips for formatting the template](#tips)
- [Add page breaks in PDF attachments](#add-page-breaks-pdf)
- [Use custom fonts](#use-custom-fonts)
- [Unsupported features: Page headers, page footers, or page numbering](#unsupported-features)

See also [Use templates in a bot](https://support.google.com/appsheet/answer/11539957).

## Customize content using a Google Docs template

When configuring a [Send an email](https://support.google.com/appsheet/answer/11447614), [Call a webhook](https://support.google.com/appsheet/answer/11511244), or [Create a new file](https://support.google.com/appsheet/answer/11512511) task, customize content using a Google Docs template by performing one of the following tasks:

Create a **Google Docs** or **PDF** template, as described in [Create a template](https://support.google.com/appsheet/answer/11539957#create-template).

Manually create a Google Docs template in your cloud file system and use it, as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

For information about customizing the template, see [Customize content using templates](https://support.google.com/appsheet/answer/11539957#customize-content) and the tips provided below.

## View and edit the template

After you create the template, click **View** to view and edit the template.

## How AppSheet processes the Google Docs template

AppSheet reads the Google Docs template in HTML format and replaces the template variables in the HTML template with the data values you specify. The resulting HTML document becomes the email body or attachment. For email attachments, AppSheet converts the HTML document to PDF format before adding it as an attachment.

When you are designing your Google Docs template, it can be helpful to see how it appears in HTML format so that you can fine tune its contents and ensure the best results.

For [Send an email](https://support.google.com/appsheet/answer/11447614) tasks, to preview the email click **Preview email** when configuring the task. The first record in the table is displayed, by default. You need to save the app to preview the latest changes.

To view the Google Docs template in HTML format:

1.  Open the template in Google Docs.
2.  In the Google Docs **File** menu, click **Download as** and select **Web Page (.html zipped)**.
3.  Locate the zip file in your Downloads folder.
    If you are using the Chrome browser in Windows, the browser downloads the file as a zip file. Open the file when the download completes.
4.  Extract the HTML file from the zip file.
5.  For example, on Windows, right-click on the zip file and select **Extract All....**
6.  Double-click on the extracted HTML file to view it in the browser.

## Include an image in the template

Your Google Docs template can include one or more images.

**Note**: Background and watermark images are not supported at this time.

To include an image:

1.  Open the template in Google Docs.
2.  Position the cursor where you want to insert the image.
3.  From the Google Docs menu select **Insert \> Image** and select the image you wish to include.

When Google Docs exports the template as HTML, it processes the image as follows:

1.  Saves the image on Google Drive.
2.  Creates a URL to the saved image file.
3.  Includes the URL in the exported HTML template in place of the image.

When the template is used as an email body template, the resulting HTML email body contains the image URL. The email client that displays the HTML email body uses the image URL to retrieve and display the image.

When the template is used as a PDF attachment template, the HTML-to-PDF conversion web service retrieves the image using the image URL contained in the HTML file and includes the image in the resulting PDF file.

## Include an image URL in the template

Your Google Docs template can include one or more image URLs. Each image URL must refer to a publicly accessible image.

## Tips for formatting the template

The following tips may help you control the appearance of your PDF attachments.

- Under **Format \> Line spacing**, reduce the line spacing to **Single** if it is currently larger, such as 1.5, Double, and so on.
- Under **Format \> Line spacing**, remove **Add space before paragraph** and **Add space after paragraph**.
- Under **Format \> Paragraph styles**, change the header formatting to **Normal Text** rather than Heading 1, Heading 2, and so on. Then apply formatting to control the header's font size, color, boldness, and so on.
- Remove any excess blank lines.
- Under **File \> Page setup...**, check the page size and margins. For example, consider setting the page size to A4 and reducing the top and bottom margins.

## Add page breaks in PDF attachments

You can include page breaks in the PDF file created from an attachment template file by manually inserting a page break in Google Docs.

1.  In Google Docs, position the cursor where you want the page break to occur.
2.  From the Google Docs **Insert** menu, select **Page break**.

## Use custom fonts

Use of custom fonts is not recommended. Some customers have reported problems when using custom fonts in templates. The PDF service sometimes fails to convert the HTML file to PDF correctly when custom fonts are present. The resulting PDF document may not display the text using the custom font. If you experience this problem, we recommend [remove all custom fonts from your Google Docs template](https://support.google.com/appsheet/answer/11572062#remove-all-custom-fonts).

## Unsupported features: Page headers, page footers, or page numbering

To handle automatic page headers, page footers, and page numbering, we would need to implement a *page layout engine* that computes the page location of each element being displayed. We would need to be aware of page boundaries, so that we could:

- Insert a footer at the end of each page.
- Insert a bottom margin at the end of each page.
- Insert a top margin at the start of each new page.
- Insert a header at the start of each new page.
- Insert appropriate page numbers.

Due to the complexity involved with managing this implementation, these features are not supported.

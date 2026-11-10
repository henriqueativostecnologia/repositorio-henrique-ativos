---
fonte: https://support.google.com/appsheet/answer/11568519?hl=en
baixado: 2026-11-10
---

# Troubleshoot file creation

Resolve the most common bot file creation problems using the guidance provided in the following sections. See also [Troubleshoot bots](https://support.google.com/appsheet/answer/11547467).

## Where is the file being saved?

Configure the file system where files are saved using the **File Store** property when [configuring the Create a new file task](https://support.google.com/appsheet/answer/11512511).

To understand the folder and file naming conventions, see [Archive files created from a bot](https://support.google.com/appsheet/answer/11568421). You can view the [saved folder and file names](https://support.google.com/appsheet/answer/11568421#view-file-folder-names-audit-history) in the Audit History.

## Why isn't the PDF file formatted correctly?

In your bot, you can define parameterized Google Doc templates that will be converted to PDF files. Occasionally, these files are not formatted identically to the original document template. To troubleshoot this problem, it is important to understand the steps used by AppSheet to process the file templates.

AppSheet performs the following steps when processing file templates:

1.  Exports the Google Docs template to HTML.
    This conversion is lossy --- in particular, HTML does not support the concept of pagination.

2.  Modifies the HTML by replacing all template variables and expressions in the HTML template with data values.

3.  Converts the HTML to PDF.
    This conversion reintroduces pagination constructs (such as margins and page breaks). However, they may not match the original pagination settings.

Formatting inconsistencies can be introduced at step 1 or step 3 because neither step maintains complete document fidelity. Most commonly, the problems are introduced at step 1 and can be fixed manually, as follows:

1.  Open the Google Docs template, export it to PDF, and view the results.
    Tweak the formatting options in the Google Docs template until it exports to PDF as required.

2.  Open the Google Docs template, export it to HTML, and view the results.
    Tweak the formatting options in the Google Docs template until it exports to HTML as required.

## Why are the images in the PDF file too large or too small?

You can control the size of images shown in the file. By default, columns/expressions of type `Image` are shown larger than columns/expressions of type `Thumbnails`.

You can specify a [format rule](https://support.google.com/appsheet/answer/10106703)  to further control the size of images in your file content. In the format rule, you choose the table, one or more columns, an optional condition, and the image size (Tiny, Small, Medium, Large). See [Display images, thumbnails, drawings, and signatures in templates](https://support.google.com/appsheet/answer/11547760). 

## How do I control when and how maps are shown in my PDF file?

You can control how geographic column values (Addresses and LatLongs) are shown in the file. By default, columns/expressions of type LatLong are shown as static maps with a pin, while columns/expressions of type Address are shown as text.

You can specify a [format rule](https://support.google.com/appsheet/answer/10106703) to further control the size of static maps in your file. In the format rule, you get to choose the table, one or more columns, an optional condition, and the image size (Tiny, Small, Medium, Large, or Text). Choosing **Text** results in the textual representation of the value being shown in the file. See [Display Address, LatLong, and XY values in templates](https://support.google.com/appsheet/answer/11547559).

## Why are app users not receiving emails with PDF attachments?

You may have reached the maximum number of PDF attachments allowed.  For each account, a maximum of 2500 PDF files are allowed to be created per day, at a rate of 20 per second. In this case, an exception similar to the following appears in the [Audit history](https://support.google.com/appsheet/answer/10104794):

`"Exception": "Document request failed with exception Status(StatusCode="ResourceExhausted", Detail="Resource has been exhausted (e.g. check quota)"`

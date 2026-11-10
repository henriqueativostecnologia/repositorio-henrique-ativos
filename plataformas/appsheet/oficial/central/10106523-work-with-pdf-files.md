---
fonte: https://support.google.com/appsheet/answer/10106523?hl=en
baixado: 2026-11-10
---

# Work with PDF Files

There are three ways you can include PDFs in your application. 

## Link to the PDF using a relative path

Using relative paths, you can create links to files relative to the spreadsheet that your app is using. This works in a similar way to links to images. For example, if the PDF is in the same directory as your spreadsheet, you can create a link to it just by putting in its name in your spreadsheet, such as `bovine.pdf`.

## Link to the PDF using a direct URL

Using direct URLs, you can link to a pdf that is somewhere on the internet. Just like you would link to an image, you can link to a pdf. For example: `http://www.mywebsite.com/path/super_pdf.pdf`

## Use a Google Drive URL

These are URLs that you copy from your address bar in your browser when you are previewing a PDF in Google Drive, such as `https://drive.google.com/view?id=1234`

Note that these are not direct or relative links, which means you are not supplying AppSheet with the actual PDF file. This means that you won’t be able to take full advantage of AppSheet’s PDF support.

## How does it work?

**iOS -** Regardless of the type of URL, the pdf will be opened in Safari. However, only relative and direct URLs are guaranteed to be cached for offline use.

**Android -** If you link to the PDF using a direct URL or relative path, the PDF will be downloaded to your phone, and you will be able to choose a viewer with which to view it. If you do not have a PDF viewer installed on your phone, AppSheet provides you with a link to the recommended viewer.

Downloading PDF message

You don't have a PDF viewer message

Google Drive URLs will open correctly. However, you will not be able to open them with a PDF viewer on your phone, and they are not guaranteed to be cached for offline use.

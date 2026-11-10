---
fonte: https://support.google.com/appsheet/answer/10104799?hl=en
baixado: 2026-11-10
---

# Optical Character Recognition (OCR)

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

This is a** preview** release of AppSheet OCR. See [product launch stages](https://cloud.google.com/products#section-23). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps.

Use AppSheet Optical Character Recognition (OCR) as described in the following sections:

- [What is OCR?](#what-is-ocr)
- [What kinds of images work with OCR?](#images)
- [How do I use OCR in my app?](#use)

## What is OCR?

OCR is a technology that allows you to access the text or writing that appears in an image. With AppSheet's OCR feature, you can speed up data entry by automatically filling out your forms from an image.

Watch a video to learn more about OCR.

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=iJvP7u1xyFA

## What kinds of images work with OCR?

AppSheet's OCR feature can be used when you need to scan multiple documents that all have a fixed layout. The image may contain printed text or handwriting. Some examples of this include:

- A standardized paper form
- USPS shipping labels
- Invoices from a single company

Some cases where AppSheet's OCR feature will not work include:

- Business cards (which do not adhere to a standard format)
- Forms that use checkboxes
- Apps that do not have an internet connection

## How do I use OCR in my app?

To get started with OCR, you will need between **4 and 10 example images** and the **values that should be extracted from them**. AppSheet will inspect the given examples and come up with a general template to match against new images.

Once you have your examples, you can create a new OCR model:

1.  Open your app in the editor.

2.  Go to **Security ** Security icon **\> Options** and ensure that **Secure Image Access** is turned off. AppSheet OCR doesn't work if this security option is turned on.

3.  Go to **Intelligence ** Intelligence icon .

4.  Click **+** adjacent to the **OCR Models** heading.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to the **Intelligence \> OCR Models** pane and click **+ New OCR Model**.

5.  Rename the OCR model by updating the name field.

6.  Select the table that contains the image examples in the **Table** drop-down.

7.  Choose the image column that has the examples inputs in the **Image Column** drop-down.

8.  Set the **Output Columns** to include the columns that contain the extracted data.

9.  Save the app.

Once you save your changes, your custom OCR model will be created. AppSheet will show the patterns that were found in each example and inform you of any issues that happened along the way.

For example, let's say we're extracting information from pictures of a conference badge. We'll create a new OCR model that will operate on the `Badges` table, extracting from the `Badge` image column, and returning the `First Name`, `Last Name`, `Organization`, `Twitter Handle`, and `Role` from the image.

After the OCR model has finished training, it's available for use in your app. Your columns will automatically be initialized using the extracted values from the image. Behind the scenes, AppSheet has added special OCR formulas to initialize the values of your columns.

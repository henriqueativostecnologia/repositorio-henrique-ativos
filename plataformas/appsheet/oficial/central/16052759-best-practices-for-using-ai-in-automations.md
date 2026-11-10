---
fonte: https://support.google.com/appsheet/answer/16052759?hl=en
baixado: 2026-11-10
---

# Best practices for using AI in automations

To improve the results when using AI in automations, apply the following best practices:

- [Best practices when leveraging AI](#leveraging-ai)
- [Best practices when building apps using AI](#building-apps)
- [Best practices for inputs to AI tasks](#inputs)

## Best practices when leveraging AI

The following lists some of the general, high-level best practices to use when leveraging AI. 

- [Set expectations and measure impact](#expectations)
- [Should I use AI in automations?](#should-i-use)
- [Have a human review the results and handle unexpected behavior](#review-results)

### Set expectations and measure impact

When using AI in automations, it is important to set expectations and measure its impact. That’s because AI doesn’t always get it right. Even when there are errors here and there, you’ll want to make sure it works in your favor overall and be able to tell others how it’s helping you,

As first steps, consider the following:

- What are you trying to accomplish using AI in automations?
- What are the expected outcomes?
- How can you measure the impact of AI? For example, you might track the cost and time savings, productivity gains, and so on.  
- What is the impact when AI gets it right?
- What is the impact when AI does not get it right?
- How often does AI get it right? How often does it not?

### Should I use AI in automations?

As an app creator, you can incorporate predefined AI capabilities as tasks in your automations. These AI tasks rely on Google’s Gemini models. You don’t need to train them, but that means they aren't tailored to your data.

To figure out if AI tasks are a good fit, we encourage you to try them out, first on a few examples and then on more data.

As a general guideline, consider the following:

- If your AI task does not require obscure knowledge, it might help you
- If the required knowledge to properly get the right response is difficult to find online, then your AI task might not return good results; for example, tasks that require industry-specific knowledge might impact the quality of the results

### Have a human review the results and handle unexpected behavior

Set up your automations to use AI and human expertise in a collaborative manner to ensure the accuracy of the results, by doing the following:

1.  Make sure humans can quickly review AI-generated results in your app.
2.  Add steps in the automation flow to handle unexpected behavior from AI tasks.

For example, if you've defined an `Enum` value named "Other" to catch any undefined values, you might send yourself a notification when the value is set so that you can update the `Enum` column to include the missing value.

## Best practices when building apps using AI

Use the following best practices when building apps using AI:

- [Add additional details](#additional-details)
- [Add column descriptions](#column-descriptions)

### Add additional details

Each AI task has an **Additional details** field. AppSheet recommends that you use this field to provide more information about the task and the expected results. 

The following provide guidelines specific to each AI task type:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **AI task**                                        | **Recommended additional details**                 | **Example**                                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Categorize                                         | -   Describe in more detail the requirements for   | Inexpensive: Less than 10 dollars\                 |
|                                                    |     each category value.                           | Moderately expensive: Between 10 and 50 dollars\   |
|                                                    | -   Indicate what values to set if results are not | Expensive: Over 50 dollars\                        |
|                                                    |     known.                                         | Other: Not sure of value                           |
|                                                    | -   Ensure that any recommended values match the   |                                                    |
|                                                    |     type and format of the column, for best        |                                                    |
|                                                    |     results.                                       |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | **Note**: Specifying a value that is not defined   |                                                    |
|                                                    | in the `Enum` type column selected for the Output  |                                                    |
|                                                    | setting may cause unexpected behavior unless       |                                                    |
|                                                    | you [allow other                                   |                                                    |
|                                                    | values](https://support.google.com                 |                                                    |
|                                                    | /appsheet/answer/10106509#allow-other-values) when |                                                    |
|                                                    | configuring the `Enum` column properties.          |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Extract                                            | -   Describe in more detail the information you    | If not sure of Make, Model, or year, make best     |
|                                                    |     want to extract.                               | guess\                                             |
|                                                    | -   Indicate what values to set if results are     | If not sure of Color, set to "Other"               |
|                                                    |     unknown.                                       |                                                    |
|                                                    | -   Ensure that any recommended values match the   |                                                    |
|                                                    |     type and format of the column, for best        |                                                    |
|                                                    |     results.                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Extract rows                                       | -   Describe in more detail the information you    | From the PDF file extract the items in the receipt |
|                                                    |     want to extract.                               | that are above fifty dollars                       |
|                                                    | -   Indicate what values to set if results are     |                                                    |
|                                                    |     unknown.                                       |                                                    |
|                                                    | -   Ensure that any recommended values match the   |                                                    |
|                                                    |     type and format of the column, for best        |                                                    |
|                                                    |     results.                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Summarize                                          | Describe in more detail the information you want   | Summarize the customer feedback, highlighting the  |
|                                                    | to include in the summary.                         | main areas for improvement                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

### Add column descriptions

For the columns that are used to save or temporarily store output from an AI task, AppSheet recommends that you add column descriptions to provide more information for Gemini to use in its data evaluation. See [Configure column properties](https://support.google.com/appsheet/answer/10106509).

Don't use expressions in column descriptions that are intended to be used with AI tasks in automations. The expressions in a column description won't be evaluated and might impact the quality of the results.  

## Best practices for inputs to AI tasks

Use the following best practices for input to AI tasks:

- [Use quality images](#quality-images)
- [Optimize PDF documents](#pdf-documents)

It might be useful to share this best practice guidance with your app users.

### Use quality images

The following provides guidelines to apply when using images with AI in automations:

- Use higher resolution images to improve result; avoid blurry images
  Consider setting the Image upload size to High, as described in [Control image size](https://support.google.com/appsheet/answer/10106529)
- If the text in an image is small in relation to the size of the image, it might impact the quality of the results
- If possible, modify the image as follows:
  - Rotate and crop images to include only the relevant subject matter
  - Mark up the image to highlight the relevant subject matter
- Images that require industry-specific knowledge might impact the quality of the results

See also [limitations and known issues with images](https://support.google.com/appsheet/answer/15999115#limitations-images).

### Optimize PDF documents

The following provides guidelines to apply when using PDF documents  with AI in automations:

- Consider splitting long PDF documents into multiple files
- Use PDFs created with text rendered as text instead of using text in scanned images
- Don't include low-resolution or small images in PDF documents

See also [limitations and known issues with PDF documents](https://support.google.com/appsheet/answer/15999115#limitations-pdf-documents).

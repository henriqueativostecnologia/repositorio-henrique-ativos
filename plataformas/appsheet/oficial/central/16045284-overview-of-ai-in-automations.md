---
fonte: https://support.google.com/appsheet/answer/16045284?hl=en
baixado: 2026-11-10
---

# Overview of AI in automations

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

With Gemini in AppSheet Solutions, you can use AI in automations to extract information from an image, PDF document, or text; and categorize information.

For example, imagine you are the owner of a car dealership and you need to frequently update your sales inventory. Using AI in automation, the process can be greatly simplified for the end user. Here’s what the experience could be for them:

1.  Take a photo of the new car on a mobile device.
2.  Upload the image to your AppSheet app.

Using AI, AppSheet extracts data from the photo, such as car make, model, color, year, and description.

Take a photo, upload it to the AppSheet app, and AppSheet extracts information using AI

Learn more about using AI in automations in the following sections:

- [Supported AI tasks](#supported-ai-tasks)
- [Get started using AI in automations](#get-started)

Consider the following when using AI in automations:

- Review [Limit and limitations with AI in automations](https://support.google.com/appsheet/answer/15999115).
- As an AppSheet admin, consider the following:
  - When you use Gemini in AppSheet Solutions, you consume *credits* based on the number and complexity of the AI tasks that are run by users of the apps owned by creators in your organization. For details, see [About credits and quotas with Gemini in AppSheet Solutions](https://support.google.com/appsheet/answer/16622530). 
  - You can define a governance policy to [control which app creators can use AI in automations](https://support.google.com/appsheet/answer/16052764)

## Supported AI tasks

The following table summarizes the AI tasks that are supported for AI in automations. Additional AI tasks will be supported in the future.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **AI task**                                        | **Description**                                    | **Example**                                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Categorize                                         | AI categorizes information into defined            | Categorize a support request                       |
|                                                    | categories.  You select the columns that you want  |                                                    |
|                                                    | to evaluate and the column that defines the        |                                                    |
|                                                    | allowed category values.                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | See [Use the Categorize AI task in an              |                                                    |
|                                                    | automation](htt                                    |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/15983005). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Extract                                            | AI extracts information from an image (such as a   | Upload photo to add car to sales inventory         |
|                                                    | photo), a file (PDF), or text. You select the      |                                                    |
|                                                    | information you want to extract and save to your   |                                                    |
|                                                    | data source.                                       |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | See [Use the Extract AI task in an                 |                                                    |
|                                                    | automation](htt                                    |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/15969430). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Extract rows                                       | AI extracts information from an uploaded image     | Upload PDF file and extract items in the receipt   |
|                                                    | (such as a photo) or file (PDF) and saves it to    | that are above fifty dollars and save to expenses  |
|                                                    | rows in an existing table.                         | table                                              |
|                                                    |                                                    |                                                    |
|                                                    | See [Use the Extract rows AI task in an            |                                                    |
|                                                    | automation](htt                                    |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/16411323). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Summarize                                          | AI summarizes long textual data into a shorter     | Summarize information for a specific customer,     |
|                                                    | summary.                                           | highlighting the main points of concern            |
|                                                    |                                                    |                                                    |
|                                                    | See [Use the Summarize AI task in an               |                                                    |
|                                                    | automation](htt                                    |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/16468184). |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## Get started using AI in automations

To get started using AI in automations:

- [Watch a quick tour video](#video)
- [Step through a quick start](#quick-start)
- [Explore an app template](#app-template)

### Watch a quick tour video

Watch a quick tour of using AI in automations.

Video: https://www.youtube.com/watch?v=Ktz2_bFcdfc

### Step through a quick start

Step through one of the following quick starts.

|                                                                                                                  |                                                                                                                                   |                       |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| **Quick start**                                                                                                  | **Description**                                                                                                                   | AI task               |
| [Quick start: Extract information from an image using AI](https://support.google.com/appsheet/answer/15985259)   | Build an automation using AI to extract information from a car photo and use it to update a car sales inventory.                  | Extract AI (image)    |
| [Quick start: Categorize information using AI](https://support.google.com/appsheet/answer/16338286)              | Extend the previous quick start to categorize the cars by body style using AI.                                                    | Categorize AI         |
| [Quick start: Extract information from a PDF file using AI](https://support.google.com/appsheet/answer/16227119) | Build an automation using AI to extract information from a service ticket request PDF file and use it to create a service ticket. | Extract AI (PDF file) |

### Explore an app template

Explore one of the Gemini-based app templates.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **App template**                                                              | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Acme Service Ticket                                                          | Logs a service ticket using information provided in a PDF document. Uses the  |
| Gemini](https://www.appsheet.                                                 | Extract AI task to get information from the PDF document, such as title,      |
| com//template/showdef?appId=ACMEServiceTicketGemini-2078346&quickStart=False) | ticket ID, description, department name, and more, and then sets the severity |
|                                                                               | based on the seriousness of the description.                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Book tracking with                                                           | Automates the input and categorization of books. Showcases use of the         |
| Gemini](http                                                                  | following AI tasks:                                                           |
| s://www.appsheet.com/templates/Gemini-gets-book-information-based-on-its-cove |                                                                               |
| r-For-my-personal-library?appGuidString=c7af20a4-6e35-4205-b537-863adbe28dda) | -   Extract AI task to get book-related information based on a photo of the   |
|                                                                               |     cover.                                                                    |
|                                                                               | -   Categorize AI task to group the books into fiction, history, mysteries    |
|                                                                               |     and thrillers, science fiction and fantasy, and so on.                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Car identification with                                                      | Identify a car's make, model, year, color, and more from a car photo.         |
| Gemini](https://www.appsheet.com/                                             | Showcases use of the Extract AI task to get car details from an uploaded      |
| /template/showdef?appId=CarIdentificationwithGemini-2078346&quickStart=False) | photo.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Gemini Support                                                               | Categorizes support ticket based on description. Showcases use of the Extract |
| Categorization](https://www.appsheet.com/                                     | AI task to categorize a support ticket based on its description.              |
| /template/showdef?appId=GeminiSupportCategorization-2078346&quickStart=False) |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

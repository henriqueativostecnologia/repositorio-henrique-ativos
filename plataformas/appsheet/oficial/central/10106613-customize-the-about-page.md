---
fonte: https://support.google.com/appsheet/answer/10106613?hl=en
baixado: 2026-11-10
---

# Customize the About page

Each app has an **About** page that your users can access from the menu at the top left. For example, the following provides an About page from one of the sample apps.

You can customize the information that is displayed, as described in the following sections.

- [Customize the page](#customize-page)
- [Configuration properties](#configure)

- To customize the app logo image that appears on the About page, see [Style: The Essentials](https://support.google.com/appsheet/answer/10106612).
- You can make the About page the app's initial launch page as described in [Choose the launch page for an app](https://support.google.com/appsheet/answer/10107319).

## Customize the page

 To customize the About page: 

1.  Open the app in the app editor.
2.  Select **Settings ** Settings icon **\> Information**.
3.  Expand each section and [configure the properties](#configure), as required.
4.  Save the app.
     

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy editor

To customize the About page: 

1.  Open the app in the app editor.
2.  Select **Info \> Properties**.
3.  Expand each section and [configure the properties](#configure), as required.
4.  Save the app.
     

## Configuration properties

Configuration properties that you can use to customize the About page are summarized in the following sections:

- [App Properties](#app-properties)
- [Information for App Users](#information-for-app-users)
- [App Documentation](#app-documentation)

### ****App Properties

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Property**                                       | **Description**                                    | **Example**                                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Short Name                                         | Unique short name for the app.                     | My App                                             |
|                                                    |                                                    |                                                    |
|                                                    | For [Chat                                          |                                                    |
|                                                    | apps](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/12860535), |                                                    |
|                                                    | the Short Name can't exceed 25 characters; the     |                                                    |
|                                                    | information will be be truncated by Google Chat.   |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Version                                            | Version of app.                                    | 1.000005                                           |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Short description                                  | Short description of the app.                      | Sample App                                         |
|                                                    |                                                    |                                                    |
|                                                    | For [Chat                                          |                                                    |
|                                                    | apps](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/12860535), |                                                    |
|                                                    | the Short description can't exceed 40 characters;  |                                                    |
|                                                    | the information will be be truncated by Google     |                                                    |
|                                                    | Chat.                                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Category                                           | Category of the app.                               | Tracking Apps                                      |
|                                                    |                                                    |                                                    |
|                                                    | **Note**: Category is not currently used in the    |                                                    |
|                                                    | app.                                               |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Function                                           | Function of the app.                               | Inventory Management                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Industry                                           | Industry for the app.                              | Retail                                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Description                                        | Description of the app.                            | A sample app with sample data                      |
|                                                    |                                                    |                                                    |
|                                                    | For [Chat                                          |                                                    |
|                                                    | apps](htt                                          |                                                    |
|                                                    | ps://support.google.com/appsheet/answer/12860535), |                                                    |
|                                                    | the Description can't exceed 200 characters; the   |                                                    |
|                                                    | information will be be truncated by Google Chat.   |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Personal use only?                                 | Flag that indicates app is meant for personal use  |                                                    |
|                                                    | only.                                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Default app folder                                 | Default location for all app files.                | /appsheet/data/MyApp-1234                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

### ****Information for App Users

|                  |                                                                                                                                        |                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| **Property**     | **Description**                                                                                                                        | **Example**                  |
| User Guidance    | App user guidance.                                                                                                                     | Some user guidance           |
| About Url        | URL for about app information.                                                                                                         | about.example.com            |
| Use Public Owner | Flag that specifies whether to display your team's [public app owner](https://help.appsheet.com/en/articles/5542043-public-app-owner). |                              |
| Privacy policy   | Privacy policy for the app.                                                                                                            | Some privacy policy details. |
| Terms of use     | Terms of use for using the app.                                                                                                        | Some terms of use.           |

### ****App Documentation

|                     |                                                                                                               |                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| **Property**        | **Description**                                                                                               | **Example**                                                         |
| Purpose             | Purpose of the app.                                                                                           | Track item details and log incoming and outgoing inventory amounts. |
| Design Details      | App design details.                                                                                           | Some design details                                                 |
| Readme PDF document | Upload a PDF file that contains a description of the app. This information is available to app creators only. |                                                                     |
| Reference Url       | URL for app reference information. This information is available to app creators only.                        | reference-url.example.com                                           |

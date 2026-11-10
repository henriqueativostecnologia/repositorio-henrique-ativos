---
fonte: https://support.google.com/appsheet/answer/10106596?hl=en
baixado: 2026-11-10
---

# Use data from Google Forms

You must be a **Google Workspace user** to build AppSheet automations with Google Forms. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Google Forms. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

Use data from Google Forms with AppSheet in the following ways:

- To build an automation using Google Forms to trigger events based on a form response, see [Build an automation using Google Forms](https://support.google.com/appsheet/answer/14634161).
- If you have an existing form in Google Forms that you want to convert into an AppSheet app that *replaces* the Google Forms UI, [use the Google Forms AppSheet add-on](#add-on) (described below).

## Use the Google Forms AppSheet add-on

Google Forms can be used as a data source through the [Google Forms AppSheet add-on](https://workspace.google.com/marketplace/app/appsheet/865237847665), which automatically converts a Google Form to an AppSheet app. It does this in two steps:

1.  **Prepare** analyzes the form and takes information from the form questions and adds it to the response spreadsheet as notes on the column headers.
2.  **Launch** creates an AppSheet app from the response spreadsheet.

Understand that the AppSheet service cannot access the form directly; only the add-on (web component running in your browser) can access the form.

### Caveats and limitations

#### Stuck on Analyzing step

Due to a limitation in Google Forms, AppSheet assumes that your response sheet is the first sheet in your workbook. If your response sheet is not the first sheet, the add-on will be stuck on the Analyzing step. Ensure that the first sheet in your workbook is your response sheet.

#### Add or move questions

If you add new questions or move existing questions around, the order of columns in the response spreadsheet may no longer correspond to the latest form content. You'll need to create a new response spreadsheet (using the **Responses** menu), **Prepare**, and then **Launch** again.

#### Choose AppSheet types

A subset of AppSheet [column data types](https://support.google.com/appsheet/answer/10106435), like `Photos` and `Signatures`, can't be specified in a form using Google Forms. So what can you do? The simple approach is to specify a question of `Text` type and add a title that is suggestive of the type (for example, `Customer Photo` or `Manager Signature`). AppSheet attempts to predict the type based on the titles. You can also [change the column type](https://support.google.com/appsheet/answer/10106375) manually.

#### Images and videos

Google Forms can contain embedded images and videos. Although AppSheet forms can as well, the Forms add-on is unable to extract embedded image and video data during the automatic app creation process. These fields will be given variable URLs in the generated app that you should update in the app editor with correct URLs pointing to your image or video content. If you intend to use a YouTube video, provide the `embed` link, for example:  `http://www.youtube.com/embed/{your-video-id})`

#### Form navigation

Google Forms has a powerful mechanism to chain sections together using a "go-to-next" navigation model tied to answers of specific questions. At the end of every section, you can also specify to jump to another section or submit the form.

AppSheet uses a different mechanism. In AppSheet, you can specify a conditional expression that controls whether a form page should be shown. The Forms add-on attempts to automatically generate the appropriate expressions based on the structure of your form.

Most form navigation can be correctly converted to AppSheet apps automatically, but there are three main limitations:

1.  Reverse navigation is not supported by AppSheet. Try to arrange your form such that all navigation proceeds to higher section numbers.
2.  In Google Forms, you can include a special **Other** option for Multiple choice questions and assign it specific navigation behavior. However, the navigation associated with this choice is not made available to the AppSheet add-on. We recommend avoiding use of **Other** on questions where **Go to section based on answer** is enabled.
3.  There is a practical limit to how much branching navigation can occur in a single form. Part of the process of converting to AppSheet's `Show_If` navigation model requires building the set of all distinct paths through the form. The total number of paths through a form can quickly become unmanageable when there are many sections with redundant navigation options, such as multiple questions in the same section that can send the user to the same place. Therefore, we strongly recommend using at most one navigating question per section, and marking these required whenever possible. Note that when more than one navigating question occurs in one section of a Google Form, only the last answered question will affect navigation anyway, and any others will be ignored.

For more information about building conditional branching forms in Google Forms and in AppSheet, see [Create multi-page forms with conditional branching](https://support.google.com/appsheet/answer/10107390).

#### Advanced options

Questions in Google Forms have Advanced options that let you constrain the type of the response. This information is unfortunately not made available to the add-on. However, you can explicitly set up equivalent behaviors in the app editor.

#### Response summary

To analyze the information captured in a form and stored in a Google Sheets spreadsheet, you have the following options:

- Gemini in Google Sheets allows you to generate data analysis and insights, and build charts and graphs (currently only available through Gemini Beta and Workspace Labs programs). See [Collaborate with Gemini in Google Sheets.](https://support.google.com/docs/answer/14356410)
- Gemini Advanced provides data analysis capabilities for Google Workspace. See [Upgrade to Gemini Advanced](https://support.google.com/gemini/answer/14517446).

#### Triggers

If you have `formSubmit` triggers on the spreadsheet, they do not fire when updates are made via AppSheet. As with `onEdit` triggers, we recommend moving this logic to a timed trigger.

#### Scale questions

If your Google form has a `Scale` question with just two choices, there is a bug in Google AppScript that causes the AppSheet add-on to fail. In any case, a `Scale` question with just two choices isn't very meaningful, so we advise changing it to have at least three choices or switching to another question type.

#### Grids

Grids are not supported.

---
fonte: https://support.google.com/docs/answer/16813283?hl=en
baixado: 2026-11-10
---

# Learn how to use sources with Google Workspace with Gemini

When you use Gemini in Workspace apps like Docs and Drive, you use sources to tell Gemini exactly which information to use in its response.

Sources are files, documents, or contextual info that Gemini uses to provide more relevant and focused answers to your prompts.

With sources, Gemini can:

- **Find information:** Get tailored responses or ask for data points found in your files.
- **Summarize documents:** Get a summary or extract key points from a file you have as a source.
- **Compare facts between files:** Use multiple source files to compare data, insights, or findings across them.

## Understand your sources

When you interact with Gemini, you can manage the content that it can access to inform its response. You can:

- [Add a source from Drive](#add_source_drive)
- [Manage source settings](#manage_source_settings)
- [Add a missing source](16813283#add_missing_source)
- [Use cell ranges as a source in Sheets](#use_cell_ranges)
- [Check sources that contribute to Gemini’s response](#check_sources)

## Add a source from Drive

You can add specific files in Drive when you want Gemini to prioritize these files before it consults other options. When you add a source, it remains active for your entire conversation, providing consistent context for Gemini's responses. You can add:

- Google Docs
- Google Sheets
- Google Slides
- PDFs

#### Add a source in Docs, Gmail, or Slides

1.  Go to:
    - Docs: [docs.google.com](https://docs.google.com)
    - Gmail: [mail.google.com](https://mail.google.com)
    - Slides: [slides.google.com](https://slides.google.com)
2.  At the top right corner, click Ask Gemini .
3.  At the bottom of the panel, click Add sources .
4.  Click **Add from Drive**.
5.  Select a file.
6.  Click **Add**.

#### Add a source in Drive

1.  Go to [drive.google.com](https://drive.google.com/).
2.  At the top right, click Ask Gemini .
3.  In the left panel, under "Your sources" or "Project sources," click **Add**.
4.  Select the files, folders, or emails you want to add as sources.
5.  Click **Add**.

[Learn how to manage your sources and search settings in Drive](https://support.google.com/drive/answer/16963068#source_and_search_settings).

#### Add a source in Sheets

1.  Go to [sheets.google.com](https://sheets.google.com).
2.  At the top right, click Ask Gemini .
3.  At the bottom of the panel, click Sheet .
    - If your sheet is not empty, click Sources .
4.  Click **Add from Drive**.
5.  Select a file.
6.  Click **Add**.

**Tips:**

- To add a file, you need permission to access it. You can only use files you have permission to view in Drive as sources. If you lack file access, you get this alert: “You need access to some files.” [Learn how to get permission to open a file or folder](https://support.google.com/docs/answer/6211862).
- Before you can add a PDF as a source, upload it to Drive. [Learn how to upload files and folders to Google Drive](https://support.google.com/drive/answer/2424368).

## Manage source settings

**Important:**

- Gemini only searches the sources you have selected, but may use any app data enabled by an administrator as well as activity from across Workspace apps to prioritize the most relevant information from available sources. Some sources are on by default, and you can disable them in your source settings at any time.
- Gemini can reference sources from a previous turn in your current conversation. To exclude a source you had previously included, start a new conversation and go to your source settings to select the sources you want.

#### Manage source settings in Docs, Gmail, or Slides

1.  Go to:
    - Docs: [docs.google.com](https://docs.google.com)
    - Gmail: [mail.google.com](https://mail.google.com)
    - Slides: [slides.google.com](https://slides.google.com)
2.  At the top right corner, click Ask Gemini .
    - In Docs, you can also add sources from the bottom bar.
3.  Click Add sources .
4.  Click **Gemini search settings**.
5.  Turn specific search locations on or off:
    - **Drive search**
    - **Gmail search**
    - **Chat search**
    - **Web search**

#### Manage source settings in Drive

**Important:** When you start a conversation from scratch, search settings for Drive, Gmail, Chat, and Calendar are turned on by default. Gemini uses these default search settings to answer questions. Web search remains off by default. [Learn how to manage your sources and search settings in Drive](https://support.google.com/drive/answer/16963068#source_and_search_settings).

1.  Go to [drive.google.com](https://drive.google.com/).
2.  At the top right corner, click Ask Gemini .
3.  In the left panel, toggle on **Let Gemini search for sources**. This enables Gemini to pull broader context from across Google Workspace.
4.  If you want to limit locations, leave the primary toggle on but uncheck specific locations:
    - Select **Drive** to search your wider Drive content beyond pinned sources.
    - Select **Chat**, **Calendar**, or **Gmail** to search recent communications and meeting schedules.
    - Select **Web** to search the internet for supplemental public data.

#### Manage source settings in Sheets

1.  Go to [sheets.google.com](https://sheets.google.com).
2.  At the top right, click Ask Gemini .
3.  At the bottom of the panel, click Sheet .
    - If your sheet is not empty, click Sources .
4.  Click **Gemini search settings**.
5.  Turn specific search locations on or off:
    - **Drive search**
    - **Gmail search**
    - **Chat search**
    - **Web search**

#### Manage source settings for skills in Workspace Studio

**Important:** When you build a skill, search settings for Drive and Web are turned on by default. Gemini uses these default search settings to build the skill.

1.  Go to [Google Workspace Studio](https://studio.workspace.google.com/).
2.  On the left, select **Skills**.
3.  At the top right, click **Create**.
4.  At the bottom of the skill builder, click Add files & more .
5.  Select **Gemini search settings**.
6.  Under "Where Gemini can search," check or uncheck the sources you want Gemini to access:
    - **Drive**
    - **Gmail**
    - **Chat**
    - **Calendar**
    - **Web**

## Add a missing source

If a prompt requires a source you haven't selected in your Gemini search settings, you’ll get a message: “To complete this request, Gemini needs access to \[service\].”

To fix this issue:

1.  In the Gemini in Workspace side panel, click Add and then **Gemini search settings**.
2.  Under “Where Gemini can search,” check the box next to the missing source.

## Use cell ranges as a source in Sheets

In Sheets, if you want Gemini to use a specific range or table in the file instead of the entire sheet:

1.  Highlight the cell range in your sheet.
2.  Ask Gemini a question that references the range.

**Tips:**

- Cell ranges are only for the sheet tab you are currently on.
- Gemini in Sheets might automatically select existing sources, such as other Sheet tabs. If you want to ask a question only about your selected cell range, make sure to deselect the other sources first.

## Check sources that contribute to Gemini’s response

After Gemini generates a response, you can review a list of the files that contributed to its answer. Below the response from Gemini, select **Sources** to find the list of sources.

For all requests that you make to Gemini, there’s a limited processing capacity, often referred to as a context window. If you have too many sources, or include sources with too much text, they may exceed this capacity. In these cases, Gemini might base its response on some, but not all, of the content.

Even when Gemini shows sources, it can still get things wrong. For example:

- Gemini might miss a source it used, or it may cite a document that is not directly used for a specific piece of information.
- In some cases, Gemini can make up a source, presenting it as factual even if it wasn't part of the request.

Make sure to double-check the response and verify information with the listed sources, and with other sources you trust, before you rely on the generated content.

## Get more help with sources in Docs, Drive & more

Find instructions for how to use Gemini and sources in Docs, Drive, and other Workspace apps that support sources:

- [Collaborate with Gemini in Docs](https://support.google.com/docs/answer/14355406)
- [Collaborate with Gemini in Gmail](https://support.google.com/mail/answer/14355636)
- [Collaborate with Gemini in Sheets](https://support.google.com/docs/answer/14356410)
- [Collaborate with Gemini in Slides](https://support.google.com/docs/answer/14355071)
- [Draft emails with Gemini in Gmail](https://support.google.com/mail/answer/13955415)
- [Generate a slide with Gemini in Google Slides](https://support.google.com/docs/answer/16961475)
- [Use Gemini in Drive for research & analysis](https://support.google.com/drive/answer/16963068)
- [Use Suggested Replies in Gmail](https://support.google.com/mail/answer/15464729)
- [Write & edit with Gemini in Google Docs](https://support.google.com/docs/answer/13447609)
- [Learn how skills work in Google Workspace & Google Workspace Studio](https://support.google.com/workspace-studio/answer/17307546)

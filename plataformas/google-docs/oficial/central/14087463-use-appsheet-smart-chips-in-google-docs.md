---
fonte: https://support.google.com/docs/answer/14087463?hl=en
baixado: 2026-11-10
---

# Use AppSheet smart chips in Google Docs

Use AppSheet smart chips in Google Docs as described in the following sections:

- [Overview](#overview)
- [Install the AppSheet add-on](#install)
- [Share the app](#share)
- [Insert an AppSheet smart chip into a Google Doc](#insert)
  - [Use the app view URL](#app-view-url)
  - [Use the smart chips @ menu](#smart-chips-menu)
- [View and interact with the AppSheet app](#interact)
- [Troubleshoot AppSheet smart chips](#troubleshoot)

See also:

- [Summary of features supported for Workspace integration](https://support.google.com/appsheet/answer/14102086) to understand the AppSheet features that can be used with smart chips
- [AppSheet smart chips in Docs FAQ](https://support.google.com/appsheet/answer/14088329) for answers to common questions.

## Overview

App creators and users can use AppSheet smart chips to embed a card-based view of their app in a Google Docs document. Google Docs users with access to the app can then see supported app views, trigger actions, and update data without ever needing to leave Google Docs. 

In order to use AppSheet smart chips, you must first [install](#install) the **AppSheet for Google Docs** add-on.

The following illustration shows an AppSheet app being rendered as a smart chip simply by pasting the app URL. The smart chip displays an icon and short title or description of the app's content. When the user hovers over the smart chip, it displays the app using the Google Workspace card framework.

Animation showing how to insert an AppSheet smart chip and then interact with the app

AppSheet policies and access permissions apply when using AppSheet smart chips. See [Summary of features supported for Workspace integration](https://support.google.com/appsheet/answer/14102086).

To use AppSheet smart chips in Google Docs, do the following:

1.  [Install the AppSheet add-on](#install) from Google Workspace Marketplace.
2.  (Optional) [Customize the name of the AppSheet smart chip](#customize-name).
3.  [Share the app](#share) with Workspace users or domains.
4.  [Insert an AppSheet smart chip into a Google Doc](#insert).
5.  [View and interact with the AppSheet app](#interact).

## Install the AppSheet for Google Docs add-on

Before you can insert an AppSheet smart chip in a Google Doc, you or your Workspace administrator need to install the **AppSheet for Google Docs** add-on. 

If you already installed the AppSheet for Google Docs add-on, you don't need to reinstall it; the AppSheet smart chip functionality will be available to you by default.

If you’re unable to install the add-on, contact your administrator. 

To install the AppSheet add-on, perform the following steps:

1.  Go to **Extensions \> Add-ons \> Get Add-ons**. 
2.  Search for **AppSheet for Google Docs** and click the card when found.
3.  Click **Install**.

For more information, see this [article](https://support.google.com/docs/answer/2942256).

## Customize the name of the AppSheet smart chip

 Customize the name of the AppSheet smart chip by changing the **Display Name** setting for the app view in the Display section when you [configure the view.](https://support.google.com/appsheet/answer/10106688#configure-view)  

The name of the AppSheet smart chip defaults to the the **Label** column set in the associated table for detail views or the app view name for all other view types. 

Display name app view setting

## Share the app

In AppSheet, share the app to allow access by Workspace users or domains. See [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

This ensures that the collaborators in your Google Docs document can see the app content you add. If not, they'll get an error message, as described in [Troubleshoot smart chips](#troubleshoot).

**Note**: Public access is not supported; the app must require sign-in.

## Insert an AppSheet smart chip in Google Docs

You can insert an AppSheet smart chip in Google Docs in one of the following ways:

- [Use the app view URL](#app-view-url)
- [Use the smart chips @ menu](#smart-chips-@-menu)

### Use the app view URL

When app users type or paste an AppSheet app URL into a document, Google Docs prompts them to replace the link with a smart chip. The smart chip displays an icon and short title or description of the app's content. When the user hovers over the chip, they see a card interface that previews more information about the app, and can interact with the [supported features](https://support.google.com/appsheet/answer/14102086) directly in Google Docs.

To insert an AppSheet smart chip in Google Docs using the app view URL, do the following: 

1.  Copy the URL of the AppSheet app view by doing the following: 

    1.  Open the app that you want to insert as a smart chip in a browser.
    2.  Navigate to the desired view in your app, right-click the browser URL, and select **Copy** to copy the URL of the app view.
        For detail views, make sure that you include the `row` parameter in the URL; it is required to render the detail view in the smart chip.

        Copy URL of app view in browser

2.  (Optional) [Customize the name of the AppSheet smart chip](#customize-name).  

3.  Sign in to Google Docs using the same Google Workspace account that has permissions to access the app.

4.  Open a [Google Docs document](https://docs.google.com/document/u/0/?tgif=d).

5.  In the document, paste the URL to the AppSheet app view (that you [copied](#copy) previously) at the desired location. For example:

    Paste URL in doc and see message about using tab

6.  Click the **Tab** key to insert an AppSheet smart chip. For example:

    Smart chip inserted in a doc

7.  Hover over or click the smart chip to [view and interact with the AppSheet app view](#interact).

### Use the smart chips @ menu

Use the smart chips @ menu to embed an app view as a card interface and allow users to interact with the [supported features](https://support.google.com/appsheet/answer/14102086) directly in Google Docs. For example, you can capture user input or show app details by embedding an AppSheet form or deck view, respectively.

To insert an AppSheet smart chip in Google Docs using the smart chips @ menu, do the following: 

1.  (Optional) [Customize the name of the AppSheet smart chip](#customize-name).
2.  Sign in to Google Docs using the same Workspace account that has permissions to access the app.
3.  Open a [Google Docs document](https://docs.google.com/document/u/0/?tgif=d).
4.  Type **@** in the document and under **Integrations** select **Open form** or **Open deck** to insert an AppSheet app form or deck view, respectively:

    Smart chips @ menu with Open form and Open deck
     
    You may be prompted to authorize access to your Google account by the AppSheet for Google Docs add-on.

    A list of apps with an app view of the selected type (form or deck) is displayed. A maximum of 25 apps are listed, but you can search for any app that includes an app view of the selected type in the search form 
5.  Click **Select** associated with the form or deck view that you want to insert.

    List of apps that have app view
     
6.  Select an app view from the **App view** drop-down, then click **Open**.

    Select app view and click Open

    The app view is inserted into the document.

     
7.  [View and interact with the AppSheet app view](#interact).

## View and interact with the AppSheet app

Make sure of the following:

- You are signed in to AppSheet and Google Docs using the same Workspace account.
- Your Workspace account has permissions to access the app.

View and interact with the inserted AppSheet app view as you would in the app.

In the following example, the Inspections deck view is displayed. You can click **Details** to open the detail view for any inspection directly in the Google Docs document. 

Smart chip with app displayed in a Doc

 

**Note**: At this time, adding or editing data, such as an inspection, using a form view is only supported when using the [smart chips @ menu](#smart-chips-@-menu). See [supported features](https://support.google.com/appsheet/answer/14102086).

If the AppSheet app view is not yet supported with smart chips, users are provided the option to open the app in a browser, as shown:

Smart chip open in app

## Troubleshoot AppSheet smart chips

If you don't have permission to use an app, the message **Failed to load** displays as the chip label.

Failed to load error in smart chip

Make sure of the following:

- You are signed in to AppSheet and Google Docs using the same Workspace account.
- Your Workspace account has permissions to access the app.

After you correct the error, click **Refresh** to refresh the smart chip.

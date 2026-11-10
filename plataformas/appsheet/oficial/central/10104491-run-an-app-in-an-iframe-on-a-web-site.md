---
fonte: https://support.google.com/appsheet/answer/10104491?hl=en
baixado: 2026-11-10
---

# Run an app in an iframe on a web site

In some cases, you may want to host an app within an existing web site. Technically, the app is hosted within an iframe (inline frame) element that is embedded on the web site. In fact, this is how the app emulators work on the AppSheet web site.

**Note**: Some functionality will not work when an app is hosted in an iframe, such as the scanner and mobile-only features like push notifications. In addition, offline behavior is limited and the behavior of the camera is altered.

To run an app in an iframe on a web site, you must:

1.  [Turn on app embedding](#turn-on-app-embedding)
2.  [Embed an app in an iframe](#embed-in-iframe)

To prevent app creators from running their apps in an iframe, see [Prevent app creators from embedding apps in an iframe](#prevent-embedding-apps).

For troubleshooting tips, see [Troubleshoot issues with embedded apps in Google Sites](#troubleshoot).

## Turn on app embedding

To allow an app to run in an iframe on a web site, turn on app embedding as follows:

1.  Open the app in the app editor.
2.  Select **Security** Security icon ** \> Options**.
3.  Turn on **Allow app embedding**.

## Embed an app in an iframe

The following sections describe how to embed an app in an iframe based on whether the app is public or restricted.

- [Embed a public app in an iframe](#embed-public-app-in-iframe)
- [Embed a restricted app in an iframe](#embed-restricted-app-in-iframe)

### Embed a public app in an iframe 

Public apps can be embedded in an iframe on any web site.

To embed a public app in an iframe, do the following:

1.  Get the ID of the app by using one of the following options:

    - Open the Share dialog, click **Share links**, and copy the **Open in browser** link, as described in [Notify users about your app](https://support.google.com/appsheet/answer/10104983#notify-users).

      Open in browser link in Share links dialog

    - Open the app in the app editor and copy the `appId` value in the URL:

      `https://www.appsheet.com/template/AppDef?appName=NewApp-2959733&appId=`**`f88b2122-4e1c-4e1f-111f-12eb567c89cf`**` `

    - View and copy the App ID by selecting **Settings ******Settings icon****** \> Integrations.**

2.  Add an HTML iframe element to the web site. Use the following iframe code structure and replace the *appId* value with the app ID copied in step 1:
    `<iframe src="https://www.appsheet.com/start/`*`appId`*`" />`

3.  Optionally, set `width` and `height` settings. For example, to display using the approximate dimensions of a mobile phone, try the following settings: `<iframe src="https://www.appsheet.com/start/b3756bde-b741-4609-bf7d-e2eee77852d6" width="320" height="568"/>`.

4.  Optionally, configure the following options:

    - If you want the hosted app to automatically refresh the app definition and the data every time the web site is opened, you can turn on the `refresh` option.
    - If you want the hosted app to abandon any unsaved data every time it is opened, you can turn on the `wipe` option.

    The following shows an example iframe element with both options enabled:
    `<iframe src="https://www.appsheet.com/start/b3756bde-b741-4609-bf7d-e2eee77852d6?refresh=1&wipe=1" width="320" height="568"/>`

### Embed a restricted app in an iframe 

Restricted apps [*require user sign-in*](https://support.google.com/appsheet/answer/10104975).

Consider the following when running a restricted app in an iframe:

- At this time, restricted apps can only be embedded in a [Google Sites](https://support.google.com/sites/answer/6372878) web site. Use of a [custom domain for your site](https://support.google.com/sites/answer/9068867) isn't supported.
- App users must use a web browser that doesn't block third-party cookies.
  Restricted apps use [third-party cookies](https://developers.google.com/privacy-sandbox/cookies/basics/third-party-cookies) to track user activity across domains without user consent. Browsing in [Incognito mode](https://support.google.com/chrome/answer/95464?hl=en&co=GENIE.Platform%3DDesktop) in Chrome or setting your browser to block third-party cookies will prevent credentials from being passed in an embedded context. If using Chrome, it's recommended to be in a standard user profile session.
- [Embedding content as a full page in a site](https://workspaceupdates.googleblog.com/2022/05/embed-content-as-full-page-in-new.html) is not supported at this time.

For troubleshooting tips, see [Troubleshoot issues with embedded apps in Google Sites](#troubleshoot).

To embed a restricted app in an iframe, do the following:

1.  Get the app URL or ID by using one of the following options:

    - **Copy the app URL**: Open the Share dialog, click **Share links**, and copy the **Open in browser** link, as described in [Notify users about your app](https://support.google.com/appsheet/answer/10104983#notify-users).

      Open in browser link in Share links dialog

    - **Copy the app ID **by doing one of the following:

      - Open the app in the app editor and copy the `appId` value in the URL:

        `https://www.appsheet.com/template/AppDef?appName=NewApp-2959733&appId=`**`f88b2122-4e1c-4e1f-111f-12eb567c89cf`**` `

      - View and copy the App ID by selecting **Settings **Settings icon** \> Integrations.**

2.  Create or open a [Google Sites](https://support.google.com/sites/answer/6372878) site.

3.  To add an HTML iframe element to the web site, select **Insert \> Embed \>** **By URL** and paste the app URL.
    If you copied the app ID in the previous step, enter the following URL and replace the *appId* value with the app ID copied:
    `https://www.appsheet.com/start/`*`appId`*

4.  Select **Whole page**. 
    Don't select **Preview**.

5.  Resize the iframe in the Google Sites editor.

6.  Optionally, configure the following options:
    - If you want the hosted app to automatically refresh the app definition and the data every time the web site is opened, you can turn on the `refresh` option.
    - If you want the hosted app to abandon any unsaved data every time it is opened, you can turn on the `wipe` option.

7.   Optionally, you can delete the following reauthorization block at the bottom of the iframe.

    Reauthenticate block in sites

## Prevent app creators from embedding apps in an iframe

Prevent app creators from being able to run their apps in an iframe by using the "Disallow apps in iframes" policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To prevent app creators from being able to run their apps in an iframe:

1.  Select **My account \> Policies**.

2.  Click **+ Organization Policy** or **+ Team Policy** to add an account or team policy, respectively.

3.  Select **Disallow apps in iframes** from the **Policy Template** drop-down.

4.  Click **Next**.

5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 

    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `NOT([AllowAppInIFrame])`

6.  Click **Save**.

## Troubleshoot issues with embedded apps in Google Sites

Troubleshoot issues with embedded apps in Google Sites, as described below:

- [Embedding content as a full page in a site](https://workspaceupdates.googleblog.com/2022/05/embed-content-as-full-page-in-new.html) is not supported at this time.
- After embedding an AppSheet app in an iframe on a Sites page, the Edit  Edit icon  icon might not appear in the iframe's toolbar. As a workaround, publish the site, open the published site, and click Edit  in the bottom right corner of the page.

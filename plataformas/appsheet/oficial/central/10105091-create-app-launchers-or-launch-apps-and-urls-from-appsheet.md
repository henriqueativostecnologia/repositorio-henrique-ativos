---
fonte: https://support.google.com/appsheet/answer/10105091?hl=en
baixado: 2026-11-10
---

# Create app launchers or launch apps and URLs from AppSheet apps

If you have used AppSheet's App Gallery, you know the value of having a list of apps that you can easily access from a single app. 

You can create your own app launcher that launches AppSheet apps. This allows you to create a suite of solutions. It simplifies deployment because you can now deploy one app and simply change a back-end spreadsheet to add or update other apps.

- [Get started by using the sample app launcher](#get-started-sample)
- [Create an an app launcher](#create)
- [Use deep links in an app launcher](#deep-links)
- [Create a URL launcher](#create-url-launcher)
- [Launch an app by using the URL](#launch-url)

## Get started by using the sample app launcher

The [App Portal](https://www.appsheet.com/templates/Custom-app-launcher-for-sharing-apps--tracking-usage?appGuidString=842a6ea2-7c8d-431f-a16f-8ab0c4ec7a3b) is a sample app launcher that you can use as an example to build your own.

App launcher example

## Create an app launcher

1.  Create a spreadsheet table for the app launcher.
    An app launcher table has three fields.
    - **App Name**: Name of the app.
    - **Image**: Public URL for the image or a reference to a file in your cloud provider. See [Display images and documents](https://support.google.com/appsheet/answer/10107317).
    - **App Link**: App name you obtain from the link to the app. For example, if the link to the application URL is `https://www.appsheet.com/template/showdef?appName=ClassAssignments-71626`, enter **ClassAssignments-71626** in this field.

      Table including App Name, Image, and App Link columns

2.  Create the app launcher app using the spreadsheet. See [Create apps: The Essentials](https://support.google.com/appsheet/answer/11980957).

3.  Open the app launcher in the editor.

4.  Go to **Data **.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

     

    Go to **Data \> Tables** and expand the table.

5.  Make sure that the column types are configured as follows:

    |            |                        |
|------------|------------------------|
| **Column** | **Type**               |
| App Name   | `Name`                 |
| Image      | `Image` or `Thumbnail` |
| App Link   | `App`                  |

6.  [Create a view](https://support.google.com/appsheet/answer/10106688#create-view) of type gallery, table, or deck.

7.  Save the application.

The linked app will load when you click or tap on the image in the app launcher application.

## Use deep links in an app launcher

The app name (for example, `ClassAssignments-71626`) is actually a link to the initial view of the named app. Instead of starting with the initial view, you can specify deep links to specific views of the app. For example, you can:

- Open the app with a specific view displayed
- Navigate to a different view in the current app

See [App column type (deep link)](https://support.google.com/appsheet/answer/10106757).

## Create a URL launcher

You can create your own URL launcher application that launches web sites based on the web site's URL.

To create a URL launcher:

1.  Create a spreadsheet table for the URL launcher.
    The URL launcher table has three fields.
    - **URL Name**: Name of the URL.
    - **Image**: Public URL for the image or a reference to a file in your cloud provider. See [Display images and documents](https://support.google.com/appsheet/answer/10107317).
    - **URL Link**: URL you wish to launch.

2.  Create the URL launcher app using the spreadsheet. See [Create apps: The Essentials](https://support.google.com/appsheet/answer/11980957).

3.  Go to **Data **.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

     

    Go to **Data \> Tables** and expand the table.

4.  Make sure that the column types are configured as follows

5.  |            |                        |
|------------|------------------------|
| **Column** | **Type**               |
| URL Name   | `Name`                 |
| Image      | `Image` or `Thumbnail` |
| URL Link   | `URL`                  |

6.  [Create a view](https://support.google.com/appsheet/answer/10106688#create-view) of type gallery, table, or deck.

7.  Save the application.

The website will load when you click/tap on the web site's image in the URL Launcher application.

## Launch an app by using the URL

You can provide a URL to users of an app by email or other media and direct them to a given view in an app that is already installed. This can be accomplished by providing an AppSheet URL.

To access the AppSheet URL, perform the following steps:

1.  Go to App** ** App icon **\> Views**.
2.  Select the view in the left navigation that you want to link to.
3.  Under **Behavior**, copy the URL provided in the **App Link** field.

    App view URL

See also: [App Column type (deep link)](https://support.google.com/appsheet/answer/10106757)

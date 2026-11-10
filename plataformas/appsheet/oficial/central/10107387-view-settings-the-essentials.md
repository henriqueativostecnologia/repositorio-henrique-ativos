---
fonte: https://support.google.com/appsheet/answer/10107387?hl=en
baixado: 2026-11-10
---

# View settings: The Essentials

Configure view settings to tailor the app's [user experience](https://support.google.com/appsheet/answer/10107307).

- [Configure view settings](#configure)
- [General settings](#general-settings)
- [View type settings](#view-type-settings)
- [Localization settings](#localization-settings)

To configure the theme and brand to control the appearance of your app, including font style and size, see [Style: The Essentials](https://support.google.com/appsheet/answer/10106612).

## Configure view settings

To configure view settings:

1.  Open the app in the app editor.
2.  Go to one of the following: 
    - Settings** ** Settings icon ** \> Views: General** to configure [configure general settings](#general-settings)
    - Settings Settings icon ** \> Views: View type options** to [configure view type settings](#view-type-settings)
    - Settings Settings icon ** \> Views: Localization** to [configure localization settings](#localization-settings)
3.  [Configure the settings](#settings).
4.  Save the app.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy editor

 To configure view settings:

1.  Open the app in the app editor.
2.  Select **UX \> Options**.
3.  Configure the settings described in the following sections.
4.  Save the app.

## Configure general settings

Configure the General settings that apply across the entire app.

- [Data Formats](#data-formats)
- [General](#general)
- [Inputs](#inputs)
- [System Buttons](#system-buttons)

### Data formats

Configure the data formats that apply across the entire app.

|                       |                                                |
|-----------------------|------------------------------------------------|
| **Setting**           | **Description**                                |
| Use accounting format | Display price columns using accounting format. |

### General

Configure general settings that apply across the entire app.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Starting view                                                                 | Identify which view the user sees when the app is launched. See [Choose the   |
|                                                                               | launch page for an app](https://support.google.com/appsheet/answer/10107319). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Start with About                                                              |  Turn on to display the app's **About** page the *first time* the app is      |
|                                                                               | started after installation, before any configured view is shown. The user     |
|                                                                               | will need to click **OK** to access app functionality.                        |
|                                                                               |                                                                               |
|                                                                               | The app's About page may be accessed within the app from the app main menu.   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Show name and email in the side menu                                          |  Turn on to display the name and email address of the app user in the app's   |
|                                                                               | main menu. This information is only known and displayed if the app [requires  |
|                                                                               | user sign-in](https://support.google.com/appsheet/answer/10104975).           |
|                                                                               |                                                                               |
|                                                                               | Show name and email in side menu                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Pull to refresh                                                               | Turn on to allow users to initiate a sync by dragging down.                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Preview new features                                                          | Turn on the **Preview new features** option to gain access to app features    |
|                                                                               | that are in the [Preview                                                      |
|                                                                               | Program](https://www.googlecloudcom                                           |
|                                                                               | munity.com/gc/Announcements/Preview-Program-for-new-app-features/m-p/335898). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Desktop mode                                                                  | Turn on the [new desktop                                                      |
|                                                                               | design](https://support.google.com/appsheet/answer/12407883) to optimize the  |
|                                                                               | desktop experience.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Inputs

Configure the input settings that apply across the entire app.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Image upload size                                                             | Automatically downscale images uploaded with the app. See                     |
|                                                                               | [Capture images](https://support.google.com/appsheet/answer/10106529) for     |
|                                                                               | more information. Choose **Full** to disable down-scaling.                    |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting applies throughout the app and can't be overridden     |
|                                                                               | elsewhere.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Save images to gallery                                                        | Turn off this setting to prevent images taken within the app on a mobile      |
|                                                                               | device from being saved to the device photo gallery/camera roll or from being |
|                                                                               | accessed outside of the app.                                                  |
|                                                                               |                                                                               |
|                                                                               | This option is available to the following mobile app versions and above: 15.7 |
|                                                                               | on Android or 15.2 on iOS. On earlier versions, images are always saved to    |
|                                                                               | the gallery.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: In some rare cases, a sync might be processed without an image. In  |
|                                                                               | this case, a copy of the image device’s gallery could be used as a backup,    |
|                                                                               | but only if this option is on.                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Allow image input from gallery                                                | Turn on to allow the app user to choose an existing image or use the device's |
|                                                                               | camera to capture a new one. If you turn this setting off, existing images    |
|                                                                               | aren't available to the app.                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting applies throughout the app and can't be overridden     |
|                                                                               | elsewhere.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Allow scan input override                                                     | Turn on to allow the app user the opportunity to edit the value scanned from  |
|                                                                               | a [barcode](https://support.google.com/appsheet/answer/10106618) or with      |
|                                                                               | [NFC](https://support.google.com/appsheet/answer/10106790). If you turn this  |
|                                                                               | setting off, the scanned value can't be edited by the app user.               |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting applies throughout the app and can't be overridden     |
|                                                                               | elsewhere.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### System Buttons

Configure the system button settings that apply across the entire app.

|                                               |                                                                                                                                                         |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Setting**                                   | **Description**                                                                                                                                         |
| Allow five views in the bottom navigation bar | Turn on to display the sync button in the top header bar and the share button in the side menu.                                                         |
| Disable share button                          | Turn on to prevent users from sending app install links to other individuals.                                                                           |
| Allow users to provide feedback               | Turn on to allow signed-in users to provide feedback to the app required. [Requires user sign-in](https://support.google.com/appsheet/answer/10104975). |

## Configure view type settings

Configure the settings that apply to specific view types.

- [Dashboard view](#dashboard)
- [Detail view](#detail-view)
- [Form view](#forms)
- [Map view](#map-view)
- [Table view](#table-view)

### Dashboard view

Configure the settings for [dashboard views](https://support.google.com/appsheet/answer/10106384).

|                                    |                                                                  |
|------------------------------------|------------------------------------------------------------------|
| **Setting**                        | **Description**                                                  |
| Show overlay actions in dashboards | Turn on to show overlay actions in all views within a dashboard. |

###  Detail view

Configure the settings for [detail views](https://support.google.com/appsheet/answer/10106385).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Detail style                                                                  |  Set the default detail style, either **Normal**, **Centered**, **No          |
|                                                                               | Headings**, or **Side-by-side**.                                              |
|                                                                               |                                                                               |
|                                                                               | **Note**: The default detail style may be overridden for each [detail         |
|                                                                               | view](https://support.google.com/appsheet/answer/10106385) in the detail      |
|                                                                               | view's configuration.                                                         |
|                                                                               |                                                                               |
|                                                                               | Detail style setting examples                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Detail image style                                                            | Set the default image style for details views. Valid options include:         |
|                                                                               |                                                                               |
|                                                                               | -   **Fill** - Enlarge or shrink an image to completely fill the screen area. |
|                                                                               |     Some content might be hidden or distorted.                                |
|                                                                               | -   **Fit** - Enlarge or shrink an image to fit within the screen area        |
|                                                                               |     without cropping or distortion.                                           |
|                                                                               | -   **Background** - Set as background image.                                 |
|                                                                               |                                                                               |
|                                                                               | You can override this setting when you [configure the detail                  |
|                                                                               | view](https://support.google.com/appsheet/answer/10106385).                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Include Show columns in detail views                                          | Turn on this setting to include [Show                                         |
|                                                                               | type](https://support.google.com/appsheet/answer/10106435#show) columns in    |
|                                                                               | detail views. By default, Show type columns only appear in form views.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Nested row display                                                            | Set the maximum number of rows to display without further user interaction    |
|                                                                               | for related reference lists.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Form view

Configure the settings for [form views](https://support.google.com/appsheet/answer/10107846).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Form page style                                                               | Set the default form page style: **Default** , **Page Count**, or **Tabs**.   |
|                                                                               |                                                                               |
|                                                                               | **Note**: The default form page style may be overridden for each [form        |
|                                                                               | view](https://support.google.com/appsheet/answer/10107846) in the form view's |
|                                                                               | configuration.                                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Form style                                                                    |  Set the default form style, either **Default** or **Side-by-side**.          |
|                                                                               |                                                                               |
|                                                                               | **Note**: The default form style may be overridden for each [form             |
|                                                                               | view](https://support.google.com/appsheet/answer/10107846) in the form view's |
|                                                                               | configuration.                                                                |
|                                                                               |                                                                               |
|                                                                               | Form style, default and side-by-side                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Hide from numbering                                                           | Turn on to hide numbering for fields in a form.                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Advanced forms automatically                                                  | Turn on to automatically advance to the next field or page after completing a |
|                                                                               | field.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apply show-if constraints universally                                         | Turn on to apply the [Show_If column                                          |
|                                                                               | constraint](https://support.google.com/appsheet/answer/10106628) everywhere   |
|                                                                               | within the app. If you turn off this setting, `Show_If` applies only within   |
|                                                                               | [form views](https://support.google.com/appsheet/answer/10107846). Most app   |
|                                                                               | creators will prefer this option to be **on**                                 |
|                                                                               |                                                                               |
|                                                                               | **Note**: This setting applies throughout the app and can't be overridden     |
|                                                                               | elsewhere.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Map view

Configure the settings for [map views](https://support.google.com/appsheet/answer/10106601).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Use my Google Maps integration                                                | Turn on to use the Google Maps key from the account settings for geocoding    |
|                                                                               | requests.                                                                     |
|                                                                               |                                                                               |
|                                                                               | **Note**: You must turn on this setting if you have more than 1000 geocoded   |
|                                                                               | addresses per month.                                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Max pin limit                                                                 | Set the maximum number of pins to show in map views.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Hide points of interest                                                       | Turn on to hide icons for local businesses, restaurants, and attractions.     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Table view

Configure the table view settings.

**Note**: The table view settings apply throughout the app and can't be overridden elsewhere.

|                             |                                                                            |
|-----------------------------|----------------------------------------------------------------------------|
| **Setting**                 | **Description**                                                            |
| Show column headers         | Turn on to show column headers at the top of table views.                  |
| Keep original column order  | Turn on to prevent AppSheet from intelligently reordering columns          |
| Right-align numeric columns | Turn on to display all numeric types as right-aligned.                     |
| Disable user sorting        | Turn on to prevent users from sorting tables by clicking the table header. |

The following illustrates the impact of the various settings in the table views.

Table view settings examples

## Configure localization settings

Customize the text shown in system buttons and notifications. Enter text or click the flask icon to enter an expression.

See also [Localize: The Essentials](https://support.google.com/appsheet/answer/10106393).

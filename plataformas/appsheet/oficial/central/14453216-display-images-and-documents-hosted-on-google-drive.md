---
fonte: https://support.google.com/appsheet/answer/14453216?hl=en
baixado: 2026-11-10
---

# Display images and documents hosted on Google Drive

Last updated: February 5, 2024

Check back regularly for updated guidance.

From **January 2, 2024**, Google began [changing how files, including images, are accessed in Google Drive](https://workspaceupdates.googleblog.com/2023/10/upcoming-changes-to-third-party-cookies-in-google-drive.html).

If you are relying on Google Drive download URLs (for example, `drive.google.com/uc?export=view&id=File_ID`) your AppSheet app will not display these files, especially images and videos, to your users when these changes are fully in effect.

- [What type of app is most likely to face this issue?](#type-of-app)
- [What action is required?](#action)
- [Tip for finding occurrences in your app definition](#find)

**Note**: Other `drive.google.com` URLs, such as `drive.google.com/file`, are also not supported for displaying images and documents hosted on Google Drive.

## What type of app is most likely to face this issue?

Apps where app creators customize their apps by:

1.  Including images using app settings.
2.  Adding read-only records containing images to help structure the app (such as a Menu table).

## What action is required?

**You need to update immediately any occurrences of the Google Drive download URL in content that is loaded outside of AppSheet. **For example, an [email automation](https://support.google.com/appsheet/answer/11447614) sent to an email client.

**Before May 1, 2024, you need to update occurrences of the Google Drive download URL **in all of the following locations:

- Data sources, for example, Google Sheets and Cloud SQL
- App definition
  - An expression used to create the URL

In your data sources, update all references to the Google Drive download URL using the solution described in [File name value](https://support.google.com/appsheet/answer/10107317#filename).

In the app (outside of your data sources), the Google Drive download URL might be used in one or more of the following locations:

- [Theme & Brand](https://support.google.com/appsheet/answer/10106612) settings, including:
  - App logo
  - Launch image
  - Background image
- Data configuration, including:
  - Columns with `XY` data types in the **Background image for the XY coordinates** setting, as described in [Mappable types](https://support.google.com/appsheet/answer/10106435#mappable)

  - [Virtual columns](https://support.google.com/appsheet/answer/10106758) that are computed using an expression like `CONCATENATE(“drive.google.com/uc?id=”, [fileID])`
- Automations, including:
  - [Send an email](https://support.google.com/appsheet/answer/11447614) automation and potentially the [email body template](https://support.google.com/appsheet/answer/11539957) used
  - [Create a new file](https://support.google.com/appsheet/answer/11512511) automation and potentially the [template](https://support.google.com/appsheet/answer/11539957) used
  - [Call a script](https://support.google.com/appsheet/answer/11997142) automation and potentially the Apps Script code

## Tip for finding occurrences in your app definition

To find occurrences of Google Drive download URL in the app definition, do the following:

1.  Open the app in the AppSheet app edtor.
2.  Go to **Settings **Settings icon**  \> Information**.
3.  At the bottom of the **App documentation** section, click the link to the documentation page for the app, as shown in the following figure: 

4.  Search the page for the URL: **drive.google.com/uc**
5.  Update any occurrences found directly in the app editor.

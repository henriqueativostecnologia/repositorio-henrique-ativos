---
fonte: https://support.google.com/appsheet/answer/10104999?hl=en
baixado: 2026-11-10
---

# Integrate AppSheet with external services

AppSheet seamlessly integrates a number of external services that are used in apps. Some of the commonly used external services are: 

- Email in an automation
- SMS in an automation
- PDF conversion in an automation
- Barcode scanning
- Address geocoding (converting street addresses to lat-long locations that can be shown on a map)
- Mapping using Google Maps
- MixPanel for usage tracking

Each external service is a paid service that charges AppSheet based on usage. However, AppSheet makes these services available out-of-the-box seamlessly to all our users.

**Note**: In rare situations, if an AppSheet account makes excessive use of one of the external services, AppSheet will apply usage limits to the account and provide reasonable alternatives.

See also: [API integration points with AppSheet](https://support.google.com/appsheet/answer/11628886)

## Configure AppSheet integrations

To configure AppSheet integrations:

1.   Open the app in the app editor.
2.  Select **Settings \> Integrations**.
3.  [Configure the settings](#configuration-settings).
4.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy navigation

 To configure AppSheet integrations:

1.  Open the app in the app editor.
2.  Select **Manage \> Integrations**.
3.  [Configure the settings](#configuration-settings).
4.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

## Configuration settings for AppSheet integrations

Configure the settings for AppSheet integrations.

- [IN: from cloud services to your app](#cloud-services-to-app)
- [External services](#external-services)

### IN: from cloud services to your app

Configure the settings to allow cloud-based services like Looker Studio and Zapier to communicate with your app. See [Enable the API.](https://support.google.com/appsheet/answer/10105769)

### External services

**Note**:

- External services are available for Core subscriptions and above. See [AppSheet pricing](https://about.appsheet.com/pricing/).
- At this time, external services can be configured using the legacy editor only. (This is a known issue that will be addressed in the future.) You are opted in to the new navigation by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at anytime.

Configure the integration of external services with AppSheet.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Allow Firebase                                                                | Enable to allow integration with Firebase and allow push notifications in     |
|                                                                               | branded apps. See [Create a Firebase                                          |
|                                                                               | account](https://support.google.com/appsheet/answer/10104995).                |
|                                                                               |                                                                               |
|                                                                               | If you disable this setting, apps can only run as a branded app or in a       |
|                                                                               | browser.                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Allow maps and geocoding                                                      | Enable maps and geocoding in your app.                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Allow barcode/QRcode scanning                                                 | Enable barcode scanning. See [Use a barcode                                   |
|                                                                               | scanner](https://support.google.com/appsheet/answer/10106618).                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Barcode/QRcode scanning service                                               | Select the barcode scanning service. See [Supported barcode                   |
|                                                                               | scanners                                                                      |
|                                                                               | ](https://support.google.com/appsheet/answer/10106618#supported-scanners) and |
|                                                                               | [Configure Scandit for barcode scanning in your                               |
|                                                                               | app](https://support.google.com/appsheet/answer/11628210#configure-scandit).  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

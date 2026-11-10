---
fonte: https://support.google.com/appsheet/answer/11628210?hl=en
baixado: 2026-11-10
---

# Use Scandit

**Note**: Barcode scanning is supported for Core plans and above. See [AppSheet pricing](https://about.appsheet.com/pricing/).

AppSheet can read data from a [barcode](https://en.wikipedia.org/wiki/Barcode) or [QR code](https://en.wikipedia.org/wiki/QR_code) using the camera on your phone or tablet, or an external barcode reader. AppSheet supports multiple options for barcode scanning on your mobile device, as described in [Use a barcode scanner](https://support.google.com/appsheet/answer/10106618). This section describes how to use Scandit for barcode scanning.

Scandit provides advanced scanning software for mobile devices. Especially in situations where scanning is frequent, when the conditions are not ideal in terms of lighting, or the barcodes you need to scan are challenging (damaged, warped, worn, small, and so on), Scandit provides a robust solution that runs on any Android (requires AppSheet version 14.8 or higher) or iOS device (requires AppSheet version 14.5 or higher) supported by AppSheet.

For a list of barcode formats supported using Scandit, see [Supported barcode formats](https://support.google.com/appsheet/answer/10106618#supported-formats).

The following shows how to use the Scandit barcode scanner in your app.

animation showing how to use Scandit

To use Scandit for barcode scanning with AppSheet, you need to:

1.  [Sign up for a Scandit account](#scandit-account), if you have not already.
2.  [Register a Scandit license key with AppSheet](#register-scandit-license-key).
3.  [Configure Scandit for barcode scanning in your app](#configure-scandit).
4.  Enable barcode scanning, as described in [Enable barcode scanning](https://support.google.com/appsheet/answer/10106618#enable).

Note that Scandit is a third-party service and not part of AppSheet. Use of Scandit and its functionality and data collection is subject to Scandit's [terms of service](https://ssl.scandit.com/terms-archive) and [privacy policy](https://www.scandit.com/privacy/).

## ****Sign up for a Scandit account

Sign up for a Scandit account and create a license key on the [Scandit](https://ssl.scandit.com/dashboard/sign-up?p=test&source=appsheet) site.

Scandit requires you to specify an **App ID** (Android) or a **Bundle ID** (iOS). Unless you are [create and deploy your own branded app](https://support.google.com/appsheet/answer/10105390), you should specify the following values:

- App ID (Android): **x1Trackmaster.x1Trackmaster**
- Bundle ID (iOS): **com.1track.nearsight**

For branded apps, you'll need your unique **App ID** (Android) or **Bundle ID** (iOS) when creating a license key with Scandit. To obtain the values:

- App ID (Android): Copy the **App ID** on the **Manage \> Deploy** page by expanding the **White-Label** section.
- Bundle ID (iOS): Use the same value that you specified in the **White-Label** section when [configuring the branded app for iOS](https://support.google.com/appsheet/answer/10105764). Note that this is not yet supported \[as of December 7, 2021\].

Manage white label app deployments for Android and iOS, showing fields where you copy the IDs

## ****Register a Scandit license key with AppSheet

To register a Scandit license key with AppSheet:

1.  Open AppSheet.
2.  Select **My account**.
3.  Select **Integrations \> App Services**.
4.  Click **New App Service**.
5.  Click **Scandit Mobile Barcode Scanning**.

    Add a new app service dialog showing Scandit Mobile Barcode Scanning button.

    The **Add Scandit Mobile Barcode Scanning** dialog displays.

    AppSheet Scandit Mobile Barcode Scanning dialog with fields to enter a name and access key
6.  Enter a unique and recognizable name for the license key in the **Name** field.
    The name is useful if you have multiple license keys.
7.  Enter the license key in the **Access Key** field.
8.  Click **Save**.
9.  Optionally, share the Scandit barcode scanner with your team by expanding the collapsed menu and selecting **Share with my team**.

    Share with team option in the three dot menu.

## ****Configure Scandit for barcode scanning in your app

To configure Scandit for barcode scanning in your app:

1.  Open your app in the app editor.
2.  Select **Settings \> Integrations**.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Select **Manage \> Integrations**.
3.  Click **External Services** to expand the component.
4.  Ensure **Allow barcode/QRcode scanning** is enabled.
5.  In the **Barcode/QRcode scanning service** drop-down, select the Scandit service that you want to enable for your app.

    Dropdown for selecting MyScanditService for barcode scanning
6.  Save your app.

## ****Enable barcode scanning

Enable barcode scanning in your app, as described in:

- [Enable barcode scanning using the camera on a mobile device](https://support.google.com/appsheet/answer/10106618#enable-using-mobile-device)
- [Enable barcode scanning using an external barcode scanner](https://support.google.com/appsheet/answer/10106618#enable-using-external-scanner)

## ****Scandit pricing and commercials

Scandit offers subscription-based pricing that varies based on use case, bundling, support requirements, etc. For more information, reach out to Scandit directly using the contact form on the [Scandit](https://www.scandit.com/partners/appsheet/?utm_source=appsheet&utm_medium=website&utm_campaign=partner-appsheet) site.

## ****Scandit FAQ

The following provides a list of frequently asked questions (FAQ).

## How can I tell if my app is using the Scandit scanner or the system default?

While the scanner is open, the Scandit scanner will have the **Scandit** logo in the bottom right part of the screen.

Scandit logo in lower right corner

## How do I monitor the Scandit barcode scanning usage?

App creators can access the [Scandit portal](https://ssl.scandit.com/) to monitor barcode scanning usage for each of their Scandit licenses.

## I have entered my license key and selected it for use by my app, but I get an error message when scanning

1.  Make sure to sync your app after you save your changes in the Editor.

2.  Check that your license key is valid.

    - For non-branded apps (most cases), make sure you use the AppSheet App ID and Bundle ID, as described in [Sign up for a Scandit account](#scandit-account).

    - For a branded app for Android, make sure you follow the instructions provided above when [signing up for an account](#scandit-account) to specify the right App ID (for your Android app).

    - For a branded app for iOS, the Scandit SDK is not yet integrated.

3.  Otherwise, contact [AppSheet Support](https://www.appsheet.com/Support) and include a screenshot of the error message.

## My app suddenly stopped scanning barcodes with Scandit

- If you have a trial license key, it may have expired. Contact [Scandit Support](https://support.scandit.com/hc/en-us/requests/new) if you want to continue to use Scandit.
- If you have a production license key, it may have expired. Contact [Scandit Support](https://support.scandit.com/hc/en-us/requests/new) for assistance.
- If your license key is valid and has not expired, contact [AppSheet Support](https://www.appsheet.com/Support) and include a screenshot of the error message.

## My app cannot scan certain barcode formats

Your app is able to scan barcodes, but it does not work with all formats. Contact [AppSheet Support](https://www.appsheet.com/Support) and provide an image of the barcode and its format.

## Who do I contact for support with an issue?

- If you have issues with your Scandit license, contact [Scandit Support](https://support.scandit.com/hc/en-us/requests/new).
- For all other issues using Scandit with your AppSheet app, contact [AppSheet Support](https://www.appsheet.com/Support).

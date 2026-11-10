---
fonte: https://support.google.com/appsheet/answer/10106618?hl=en
baixado: 2026-11-10
---

# Use a barcode scanner

Use a barcode scanner with AppSheet as described in the following sections:

- [Overview of barcode scanning with AppSheet](#overview)
  - [Supported barcode scanners](#supported-scanners)
  - [Supported barcode formats](#supported-formats)
  - [General limitations of barcode scanning using AppSheet](#general-limitations)
- [Get started with a sample template](#get-started)
- [Enable barcode scanning](#enable)
  - [Enable barcode scanning using the camera on a mobile device](#enable-using-mobile-device)
  - [Enable barcode scanning using an external barcode scanner](#enable-using-external-scanner)
- [Test barcode scanning](#test)

## ****Overview of barcode scanning with AppSheet

**Note**: Barcode scanning is supported for Core and Enterprise plans only.

AppSheet can read data from a [barcode](https://en.wikipedia.org/wiki/Barcode) or [QR code](https://en.wikipedia.org/wiki/QR_code) using the camera on your phone or tablet, or an external barcode reader.

The following sections provide more details about barcode scanning with AppSheet:

- [Supported barcode scanners](#supported-scanners)
- [Supported barcode formats](#supported-formats)
- [General limitations of barcode scanning using AppSheet](#general-limitations)

### Supported barcode scanners

AppSheet supports two options for barcode scanning on your mobile device.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Barcode scanner**                                                           | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| System default                                                                | Provides barcode scanning out of the box.                                     |
|                                                                               |                                                                               |
|                                                                               | Requires no additional set up after you [enable barcode scanning](#enable) in |
|                                                                               | your app.                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Scandit                                                                       | Delivers a robust set of barcode scanning features and formats for situations |
|                                                                               | where scanning conditions are more challenging (such as, poor light, damaged  |
|                                                                               | or bent barcodes) or when you need to scan a lot of codes.                    |
|                                                                               |                                                                               |
|                                                                               | You must have a Scandit account and register a license key with AppSheet in   |
|                                                                               | order to use Scandit for barcode scanning. See                                |
|                                                                               | [Use Scandit](https://support.google.com/appsheet/answer/11628210).           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Supported barcode formats

AppSheet supports the barcode formats, or *symbologies*, out of the box.

**Note**: If your app requires a barcode format that isn't currently supported out of the box, contact [AppSheet Support](https://www.appsheet.com/Support) or consider [using Scandit](https://support.google.com/appsheet/answer/11628210) for barcode scanning.

- Codabar
- Code 39
- Code 93
- Code 128
- Data Matrix
- EAN-8 and EAN-13
- Interleaved 2 of 5 (ITF)
- PDF417
- QR Code
- UPC-A and UPC-E

The Scandit barcode scanner also supports the following formats:

- Code 11
- Code 25
- Dotcode
- EAN 13+2
- EAN 13+5
- GS1 Databar
- MaxiCode
- Micro PDF417
- MicroQR
- Truncated PDF417

**Note**: Not all formats supported by Scandit are enabled in AppSheet at the moment. Contact [AppSheet Support](https://www.appsheet.com/Support) if you are interested in a particular format.

### General limitations of barcode scanning with AppSheet

The limitations of barcode scanning with AppSheet include the following:

- Scanning is supported only when running an app on mobile devices.
- Scanning is not supported:
  - When running an app in a web browser. The **Scan** button is not shown.
  - In the app editor's emulator window. The **Scan** button is displayed to show you how the app would look like on a mobile device, but it is not operational and always generates the same value: 111122333.
- Line breaks in multi-line QR codes will be removed.

## ****Get started with a sample template

To get started using barcode scanning, check out the [Inventory Management](https://www.appsheet.com/templates/Manage-inventory-levels-stock-value-and-vendor-details) sample template. The Inventory Management template manages inventory items and enables you to use a barcode scanner to generate the Item ID when adding a new item.

## ****Enable barcode scanning

Enable barcode scanning as described in the following sections:

- [Enable barcode scanning using the camera on a mobile device](#enable-using-mobile-device)
- [Enable barcode scanning using an external barcode scanner](#enable-using-external-scanner)

By default, the **System default** barcode scanner is enabled. **To use Scandit for barcode scanning**, you also need to register your Scandit account with AppSheet and enable Scandit for barcode scanning. See [Use Scandit](https://support.google.com/appsheet/answer/11628210).

### ****Enable barcode scanning using the camera on a mobile device

To enable barcode scanning using the camera on a mobile device:

1.  Sign in to [*AppSheet*](https://appsheet.com/)**.**

2.  Open the app in the app editor.

3.  Go to **Data**  and select the table to which you want to add barcode scanning in the list.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data**, click **Columns**, and expand the table to which you want to add barcode scanning.

4.  Perform one of the following tasks:

    - Enable the **Scan** setting for the desired column in the column list.

      Scan toggle in the column list.

      Optionally, enable **Search** to enable scanned input in the app's built-in search box at the top of the app screen.

    - Click the **Edit (pencil)** icon to open the row configuration dialog, expand Other Properties, and enable Scannable.

      Scannable property

      Optionally, enable **Searchable** to enable scanned input in the app's built-in search box at the top of the app screen.

5.  Save your changes.

After you enable barcode scanning, within the app the column will include an icon to indicate its input may be scanned:

Scan icon in the app

When the icon is tapped, the device's camera will be activated to read the [barcode](https://en.wikipedia.org/wiki/Barcode) or [QR code](https://en.wikipedia.org/wiki/QR_code) . The scanned data will be entered as the column value.

If a column that is scannable is also searchable, the app's built-in search box at the top of the app screen will also allow scanned input, as indicated by the scan icon:

Scan icon and search field

### Enable barcode scanning using an external barcode scanner

Set the type of the column to **Text**. Any supported external barcode scanner that interacts with your mobile device as a keyboard when a barcode is scanned will insert the barcode into the text field on the input form.

If app users use a device with an external barcode scanner, the column **should not** be set as scannable. It won't work with the image scanner at the same time.

## ****Test barcode scanning

Test barcode and QR code scanning by running your AppSheet app on a mobile device.

**Note**: Barcode scanning is not available from within the browser-based app or the app editor's emulator window. See [General limitations of barcode scanning with AppSheet](#general-limitations).

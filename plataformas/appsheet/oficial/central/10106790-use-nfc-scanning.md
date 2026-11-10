---
fonte: https://support.google.com/appsheet/answer/10106790?hl=en
baixado: 2026-11-10
---

# Use NFC scanning

Near Field Communication (NFC) is a short-range protocol of communication between devices, typically between an NFC tag and a scanner.

Most modern smartphones are capable of writing to and reading from NFC tags. This, combined with the affordable price of tags (from ~0.5 USD per piece), is making NFC an attractive feature for some app creators.

A tag can be read by physically touching it with a NFC supported phone or device.

While NFC has many capabilities and formats, AppSheet is currently supporting reading records from NDEF tags such as the NTAG215.

The use of NFC in your AppSheet app falls into two categories: [data capture](#data-capture) and [links](#links)

## Data capture

You can write some part of data into your tag (typically an ID) and then use your app to read the value from the tag into a field in a form or the search bar.

Enabling data capture is very simple. In the app editor, go to the definition of the column you would like to scan, and mark it as NFC scannable. Once enabled, an NFC button will appear next to the text field of that column when running the app on a mobile device. Since scanning NFC tags is possible only from mobile devices, the NFC button won't appear when accessing your app from a browser. When your users click the NFC button they will be prompted to scan a tag. When they do, the tag's value will be filled in the relevant text field.

While it is possible to write multiple records to a single NFC tag, in order to keep the UI simple, AppSheet will only use the first record in the tag.

In the editor, the button is enabled so the app creator will be able to see how the app will look like on mobile while editing. Clicking the button when you're editing the app will simulate a scan of a meaningless value.

## Links to apps and deep links (Android only)

Currently, iOS devices do not support reading URLs from NFC tags. This feature is only supported for Android devices.

You can write URLs to NFC tags. When those tags are later scanned with an Android device, Android will try to open the URL with an app that can handle it -- usually the mobile device's default browser.

You can use this functionality to write your app's URL to a tag. When users scan the NFC tag, your app will be opened on their browser. If AppSheet is installed on the device and the system settings allow it, your app will open on the user's AppSheet app itself.

To get a link to a specific view in your app simply open it in a browser, navigate to the view you wish to link, and copy the URL from the address bar in your browser.

## Requirements for NFC

There are a few components you need to get started with using NFC tags in your app.

You'll need:

- An NFC tag. While any tag that supports NDEF messages should work, AppSheet NFC was tested primarily on NTAG215.
- An NFC enable mobile device to read and write tags. On iOS NFC is supported from iPhone 7 (currently not on tablets) and from OS 11.0.
- A third party app for writing tags. For now, AppSheet only supports reading tags so you'll need to get another app for writing. The app stores have several free NFC apps for Android that you might find useful. It's a little trickier for iOS: keep in mind that if you're using an iOS device, you'll need an external NFC writer.

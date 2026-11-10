---
fonte: https://support.google.com/appsheet/answer/10106789?hl=en
baixado: 2026-11-10
---

# Capture GPS location

You can use a `LatLong` or `ChangeLocation` column to capture a GPS location. In apps that include these column types, **the current location is polled once per minute**.

There are four ways to capture the GPS location in a form:

1.  You can assign the `LatLong` column an AppFormula value of `HERE()`. This will automatically populate the `LatLong` column with **the most recent polled location** each time a new entry is added or an existing entry is edited.
2.  You can assign the `LatLong` column an Initial Value of `HERE()`. This will automatically populate the `LatLong` column with **the most recent polled location** when an entry is first added, but not when the entry is edited.
3.  You can use a `ChangeLocation` column to automatically capture **the most recent polled location** when a particular data change occurs. Read more on [Change column types](https://support.google.com/appsheet/answer/10106375).
4.  You can manually capture the current location. The input field for a `LatLong` column has a clickable icon that lets you capture the device's current GPS location. Rather than using the polled location, with each button press the app will try to obtain the most accurate current location it can for up to 30 seconds or until an estimated accuracy of 10m is reached. **This method offers the highest accuracy** and displays an estimate of the accuracy (in meters) within the app.

Additionally, you can explicitly type in a `LatLong` value, such as `46.34,-32.34`.

## Troubleshoot GPS location

Whether on a mobile device or in a browser, the system will probably ask you to give AppSheet permission to access your current location.

- If you are running your app within a browser, this permission request may not be very prominent. For example, some browsers bring up a subtle request near the address bar which can be easy to overlook.
- If you have ever denied Location Services for AppSheet, the system will remember this and block AppSheet from retrieving location information.

Ensure that Location Services is enabled for AppSheet on your device.

- For iOS devices do [this](https://support.apple.com/en-us/HT207092).
- For Android devices do [this](https://support.google.com/nexus/answer/6179507?hl=en).

If you are still having trouble getting GPS location to work, try the following:

1.  Add a new `LatLong` column to your worksheet.
2.  Regenerate the table containing the new `LatLong` column.
3.  Verify that the new `LatLong` column is present in the table and that it has type `LatLong`.
4.  Open the updated application on the device that is having trouble capturing GPS location.
5.  Edit one of the rows in the table having the `LatLong` column.
6.  When the `LatLong` column is displayed, click the icon to the right of the `LatLong` column. The icon contains a blue box with a map pin inside it. This should insert the current GPS location in the `LatLong` field.
7.  Ensure the `LatLong` field is populated with the current geolocation.

## Accuracy of results

AppSheet captures location using the [HTML5 geolocation API](https://www.w3.org/TR/geolocation-API/), which draws from a variety of available mechanisms to estimate the current location of the device:

"The Geolocation API defines a high-level interface to location information associated only with the device hosting the implementation, such as latitude and longitude. **The API itself is agnostic of the underlying location information sources**. Common sources of location information include Global Positioning System (GPS) and location inferred from network signals such as IP address, RFID, WiFi and Bluetooth MAC addresses, and GSM/CDMA cell IDs, as well as user input."

Since the actual location capture mechanisms are device dependent, maximum available accuracy may vary depending on local conditions such as network or GPS availability and reception, device hardware or operating system, and the browser running the app. As such, a consistently high accuracy cannot be guaranteed. The manual capture mode of the `LatLong` input provides the highest available accuracy and is recommended over use of the `HERE()` function in cases where high accuracy is especially important.

## Coordinate system

AppSheet uses [WGS84 standard](https://en.wikipedia.org/wiki/World_Geodetic_System) for the latitude and longitude.

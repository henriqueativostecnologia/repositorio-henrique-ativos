---
fonte: https://support.google.com/appsheet/answer/10105388?hl=en
baixado: 2026-11-10
---

# Deploy from an install link

Deploy your app to users by sending an install link.

How does a user install your app with the install link? The link points to a page with instructions depending on the combination of platform and web browser they're using.

- [Chrome and Firefox on Android](#chrome-firefox-android)
- [Other browsers on Android](#other-browsers-android)
- [Chrome and Safari on iOS](#ios)

## Chrome and Firefox on Android

Chrome and Firefox on Android have features that allow AppSheet to detect whether it is installed on a user's device, greatly simplifying the installation process. First, the user is taken to a landing page for the app with the app name and description (if available). 

If AppSheet is already installed, tapping **Install** opens the app and creates a shortcut on the user's home screen.

If AppSheet is not already installed, tapping **Install*** *takes the user to a page prompting them to install AppSheet. Then, tapping **Go** will open the Play Store where they can install AppSheet. When the user opens AppSheet for the first time, it opens the app and creates a shortcut on the user's home screen

**Note**: For managed accounts (such as `@companyname.com`), after AppSheet is installed users will need to tap **Install** again to open the app in AppSheet.

## Other browsers on Android

In browsers other than Chrome or Firefox on Android, the user is taken to a landing page for the app with the app name and description (if available) and presented with two options: one for when AppSheet is installed, and one for when it isn't.

If AppSheet isn't installed, tapping **Install from PlayStore** will open the Play Store where the user can install AppSheet. When the user opens AppSheet, they'll be taken to your app and a shortcut to the app will be placed on their home screen.

**Note**: For managed accounts (such as `@companyname.com`), after AppSheet is installed users will need to tap **Install *appname*** to open the app in AppSheet.

If AppSheet is already installed, tapping **Install *appname*** will launch AppSheet, open the app, and create a shortcut on the home screen.

## Chrome and Safari on iOS

On iOS, the email the user receives will contain a button to install your app.

For Chrome browsers, clicking **Install** opens the app in a web page.

For Safari browsers, clicking **Install** opens a landing web page that describes the app and displays a banner recommending that the user download the app. If AppSheet is not already installed, clicking the banner will take the user to the App Store to install AppSheet where they can install the app. Once your app is installed, the user will be given the option to create a shortcut to it on their home screen.

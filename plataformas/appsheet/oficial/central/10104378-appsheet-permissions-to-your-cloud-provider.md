---
fonte: https://support.google.com/appsheet/answer/10104378?hl=en
baixado: 2026-11-10
---

# AppSheet permissions to your cloud provider

AppSheet uses the industry-standard OAuth protocol to secure access to your cloud file system. Let us describe the process when you sign up with AppSheet through your Google account. The process is similar if your account is through Dropbox, Box, and so on.

There are different permissions requested of app creators (people who build apps) and app users (people who use those apps on browsers or devices).

Under no circumstance does AppSheet:

- Read irrelevant information utilizing these permissions
- Sell this information to any other party
- Utilize these permissions for any reason other than providing our app platform service

## **App creators**

On sign up on the AppSheet website, you are redirected to a Google page where you are asked if you are willing to authorize AppSheet with a requested set of permissions. Here is what you are agreeing to and why:

- You let AppSheet verify your identity. This is so that AppSheet can associate a unique identity with each user.
- You let AppSheet know your email. This is so that AppSheet can send you email as you create apps.
- You let AppSheet read your files and folders. This is so that you can select spreadsheets and images to use in the app.
- You let AppSheet make copies of data into your cloud file system and edit that data. This is so that you can make copies of apps.
- You let AppSheet read and write your spreadsheets. This is what it is all about after all.

We really do not like asking for permissions to your data and have worked to try to keep this minimal while still keeping it simple and providing useful functionality.

Once you go through the auth process, Google and AppSheet use internal identifiers (called access tokens) to allow AppSheet software to act on your behalf. To explain this simply:

- Whenever one of your apps is used, AppSheet has to read and write your data from Google. It does this using your access token. Your access token is never used with anyone else's apps so your data is appropriately protected.
- You can completely revoke permissions by going to your Google Drive options and disabling AppSheet.

## **App users**

If your app is a Public app, then the users are not asked to sign in and AppSheet does not ask them for any permissions.
If your app requires sign-in (such as using a Google Account), then as part of signing in, the users are asked to provide AppSheet some permissions.

Here is what they are agreeing to and why:

- They let AppSheet verify their identity. This is so that AppSheet can associate a unique identity with each user.
- They let AppSheet know their email. This is so that AppSheet can match their account to your app user list to provide security and access control for your app.

We call this a "basic" authorization scope, and is currently implemented for Google Drive, Office365, and Dropbox providers. Other providers will ask the app user for the same permissions as the app creator (full scope).

If your app utilizes some specific features (like Private Tables or run As-App-User), then AppSheet needs to ask the user for the same permissions as an app creator (full scope). These features are not used very often.

---
fonte: https://support.google.com/appsheet/answer/10104802?hl=en
baixado: 2026-11-10
---

# Google sign in warning

Google verifies its third-party apps to ensure valid data access. As a result, for some users a warning screen might be displayed when you sign in informing you that AppSheet is unverified and not to proceed. This might occur if permissions that you may have provided to AppSheet in the past are no longer valid, and when AppSheet tries to sign you in, Google’s security system displays this warning.

To resolve this issue, do one of the following:

- If the warning screen has an Advanced option, you can click it and proceed with your sign in. 
- Perform the following steps:

1.  Go to [https://myaccount.google.com/permissions](https://myaccount.google.com/permissions)
2.  Under **Third party apps with account access**, find **AppSheet**, click on it, and then **Remove Access.**
3.  Go to [https://www.appsheet.com/account/login](https://www.appsheet.com/account/login) and sign in via Google.
    You should be able to successfully sign in.
4.  If you had set up any Google Calendar data source, or any Google Domain auth source, go to your account page in AppSheet, find the appropriate Calendar data source or Domain auth source, click on its icon, and go through its sign-in process again.

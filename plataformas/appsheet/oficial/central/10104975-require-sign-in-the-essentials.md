---
fonte: https://support.google.com/appsheet/answer/10104975?hl=en
baixado: 2026-11-10
---

# Require sign-in: The Essentials

Restrict access to your app by requiring users to authenticate by signing in to the app.

- [When to require user sign-in](#when-to-require)
- [How to require user sign-in](#how-to)
- [Alternatives to requiring sign-in](#alternatives)

Review the frequently asked questions (FAQ) for more information:

- [Which subscription plans support user sign-in?](#which-plans)
- [How public is an app on a Publisher Pro plan?](#publisher-pro-plan)
- [Can I secure an app without making a user sign-in?](#secure-without-sign-in)
- [Why is `guest_-956001730` user accessing my app?](#guest-user)

See also [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

## When to require user sign-in

Require user sign-in if your app:

- Has any confidential data. 
- Needs to distinguish between users in a secure and reliable way. 

There are five levels of security afforded to apps that require users to sign-in:

1.  **Requiring sign-in with a specific authentication provider**
    Only users with an account hosted by a specific authentication provider (such as, Google, Dropbox, or Microsoft) can access the app.

2.  **Specifying a user allowlist**
    Only users explicitly listed in an allowlist can access the app. Learn more about [sharing application access](https://support.google.com/appsheet/answer/10104983). One approach to this is using [domain groups](https://support.google.com/appsheet/answer/10105757). 

3.  **Using [security filters](https://support.google.com/appsheet/answer/10104488)**
    The app can be configured to show different subsets of data to different users.

    Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

4.  **Using expression logic within the app** based on the user's information
    Use `USEREMAIL()` and `USERNAME()` functions to customize the app on a per-user basis.

5.  **[Auditing](https://support.google.com/appsheet/answer/10104794#audit-changes-by-user)**
    The app can explicitly capture the identity of each user that makes a change to the app. Additionally, the audit history automatically captures the identity of every user who interacts with the app.

**Note**: The security mechanisms described above are **not available** to apps that do not require user sign-in.

## ****How to require user sign-in

To require user sign-in:

1.  Open your app in the app editor.
2.  Select **Security \> Require sign-In**.
3.  Enable **Require user sign-in?**
4.  From the Authentication provider drop-down, select an authentication provider or **Any provider** to enable sign-in using any of the supported authentication providers. Supported authentication providers include:
    - Apple
    - Box
    - Dropbox
    - Google
    - Microsoft
    - Salesforce
    - Smartsheet
5.  [Share your app with users](https://support.google.com/appsheet/answer/10104983).

Your app users must have an account with the selected authentication provider. For example, all users using Google Drive have a Google account. This applies to consumers with a @gmail.com email address and corporate accounts that are hosted by Google. Most corporate and consumer email accounts are hosted by one of the supported authentication providers.

If you select **Any provider**, each of your app users must have an account with at least one of the authorization providers supported. For example, one of your app users might have a Google account while another might have a Microsoft account.

**Note**: Restricting the authentication provider applies to app users, but not app editors. So, it is possible to collaborate with editors using other authentication providers while still restricting app users.

## ****Alternatives to requiring sign-in

For reasons of cost, some app creators may want to stay with a Publisher Pro plan. We want to emphasize that these apps are **inherently insecure**. However, if the main goal is to acquire the user's email address rather than data/app security, here are some aspects of the functionality that can still be achieved:

1.  In forms, instead of using [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) to automatically fill in a column value, the user can explicitly type in their email address. This will not be verified, but an email can still be captured and used.

2.  The app can utilize the `UserSettings` feature to ask the user to provide their email address. The benefit of this approach is that the email address is typed in once and then can be used in formulas (for example, `UserSettings("MyEmail")`). This email is not authenticated (any user could claim to be `bill.gates@microsoft.com`), so this is not a security mechanism.

3.  If you have a fixed list of users in a `Lookup` table, you could assign each user an ID and ask them to provide their ID via the `UserSettings` feature. This ID can be used with the `Lookup` table. Note that this is not a password. It is not encrypted and all users will have access to the `Lookup` table, so this approach is in some ways even less secure than the other options.

## Frequently asked questions (FAQ)

### Which subscription plans support user sign-in?

AppSheet provides the following plans: Starter, Core, Enterprise Plus, and Publisher Pro. **Only Starter, Core, and Enterprise Plus plans support user sign-in.** Publisher Pro only supports creation of publicly accessible applications that don't contain sensitive data and don't require sign-in.

If your app's data is sensitive, then you should require sign-in, and therefore sign up for the Starter, Core, and Enterprise subscriptions. See [How to choose a subscription plan](https://support.google.com/appsheet/answer/10105400).

## ****How public is an app on a Publisher Pro plan?

If you deploy an app on a Publisher Pro plan, you should assume that all the data in the app is visible to anybody. Furthermore, you should assume that anybody who wants can run the app. If the app permits data changes, then anybody can make those changes.

### Can I secure an app without making a user sign-in?

This question comes up occasionally from app creators who want to use one of the public Publisher plans. The answer is **no**.

Some app creators try to create their own workarounds for each of these levels of security. However, these approaches all have their shortcomings.

1.  **Instead of a user allowlist, can I control distribution of the app install link?**

    While this is possible initially when the app creator sends the install link to users, there is no way to control whether the link is forwarded. Anybody with the link has access to the app.

    We have had multiple instances where an employee of a company has access to the app and then that person leaves the company. At this point, the company requests us to disable access and there is no way to do this.

    If the link is ever placed on a publicly accessible site, it may be crawled by a search engine. And the content of the app (the data shown in the app) could also be indexed by the search engine. This is because the intent for Publisher Pro apps is to have broad public access to the app.

2.  **Can slices be used instead of a security filter?**

    Slices are a mechanism used to define *virtual tables*. Even if the user was identified and used in the filter condition of a Slice, this doesn't guarantee that the entire data set isn't accessible as well.

    When the app is opened in a browser, all of the data used by the app is accessible to anyone who opens the developer console and examines the data of the running application. There is no guarantee that the entire table isn't available even if a slice is defined on that table. The only way to ensure this is to use a security filter for the table.

3.   **Can I create my own username/password mechanism?**

    Not really. If you want to implement your own security, you need to worry about authentication (is the person who they claim they are), and a secure implementation (encrypted capture, transmission, and storage of passwords, as well as mechanisms to handle forgotten passwords, revocation, and so on). This is a huge and complex undertaking. In fact, this is why AppSheet does not provide its own username and password mechanism. Instead, we utilize third party authentication via highly credible providers like Google, Dropbox, and Office365.  

4.  **Can I verbally tell people to sign-in and use expressions with** [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) **to control app behavior? **

    No. [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) and [`USERNAME()`](https://support.google.com/appsheet/answer/10108211) do not have a defined value if the app does not enforce user sign-in. The **Login** option in the app menu will also only be visible for apps that require sign-in. Apps should either assume all users are signed in, or assume that no users are signed in.

## Why is `guest_-956001730` user accessing my app?

You may see `guest_-956001730` in your log files even if your app requires sign-in. This system user account is used to log system events, and is not an indication that your app security has been compromised.

This system user account does not count towards your active users.

**Note**: In the future, system events will be tracked using the `AppSheet System User` account.

---
fonte: https://support.google.com/appsheet/answer/10105090?hl=en
baixado: 2026-11-10
---

# Users: The Essentials

## What is an active user? 

Whenever we refer to users, we mean **active** **users**. 

AppSheet counts active users when determining the number of licenses you need to purchase for your app. Starting from when your app is first fully deployed, Appsheet tracks the number of users that access the app for recurring trailing periods of 30 days. Anyone that opens the app within these trailing periods is an **active user**. For each trailing period, AppSheet will track the number of active users and then determine how many licenses you need to purchase.  

Suppose your company has 200 employees, but you only plan on having 50 employees actively use your app. Then, you'd purchase 50 licenses.

Your number of active users can vary, depending on whether your subscription plan is **secure** or **public**. 

### Secure

If the app is secure, it [requires users to sign in](https://support.google.com/appsheet/answer/10104975) with their e-mail. AppSheet will count each individual e-mail as one user. For example, if an employee signs into an app with the same e-mail on two devices, they will still be considered only one user. AppSheet supports having the same user logged in on up to five devices at a time.

### Public

If an employee opens a public app on two devices, AppSheet will count two guest users rather than one.

**Note**: If you are on a **secure** subscription plan, make sure that all your deployed apps [require users to sign in](https://support.google.com/appsheet/answer/10104975) so you aren't paying more for guest usage. 

## How many users can I have?

While you are prototyping your app for free, you can have up to 10 active users. Once you fully deploy an app, you will need to subscribe to either a secure or public plan. With a secure plan, you will need a subscription with as many licenses as active users. Note that your license count will not automatically adjust with your number of active users, you will need to adjust your license count as your user base fluctuates. With a public plan, you will pay a fixed amount per month per app. If you start to increase the number of people using your deployed app, you will need to update your pricing plan. Details can be found on [our pricing page](https://www.appsheet.com/Pricing). 

**The license required to *use* an app depends exclusively on the app creator's license.** AppSheet Core creators require users to have an AppSheet Core or AppSheet User Pass license. AppSheet Enterprise Plus creators require users to have an AppSheet Enterprise Plus or AppSheet User Pass license. See also [About licensing in AppSheet for organizations](https://support.google.com/appsheet/answer/16563370).

## Connecting with your app users

Share your app with users, as described in [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

In the Users pane of the app editor, you can control user access to your app and interact with your users. There are two tabs in the Users pane:

- **Users** - Set the authentication provider, [manage roles and app versions for individual users](https://support.google.com/appsheet/answer/10104983#manage-roles-app-versions), or [send a reminder notification to individual users](https://support.google.com/appsheet/answer/10104983#send-reminder).
- **Broadcast Notifications** - Send a push notification to your users. See [Broadcast notifications to your users](https://support.google.com/appsheet/answer/10104701).

## Tips and tricks

Learn tips and tricks for user access from the AppSheet Community:

- [Users tips and tricks](https://www.googlecloudcommunity.com/gc/forums/filteredbylabelpage/board-id/appsheet-tips-tricks/label-name/Users)
- [Users Q&A](https://www.googlecloudcommunity.com/gc/forums/filteredbylabelpage/board-id/appsheet-questions/label-name/Users)

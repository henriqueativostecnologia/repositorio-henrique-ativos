---
fonte: https://support.google.com/appsheet/answer/11512233?hl=en
baixado: 2026-11-10
---

# Troubleshoot notifications

Resolve the most common bot notification problems using the guidance provided in the following sections. See also [Troubleshoot bots](https://support.google.com/appsheet/answer/11547467).

## Why are notifications only sent to the app creator?

While the app is in test mode (that is, it has not passed a [deployment check](https://support.google.com/appsheet/answer/10104389)), any notifications sent from a bot are delivered to the app creator only. This ensures that you do not inadvertently send email messages, SMS messages, or notifications, or post HTTP messages while debugging your bot.

## Why is there no Notification Device Token present for a user?

If a notification recipient does not have a Notification Device Token, the following error is returned in the [audit history log](https://support.google.com/appsheet/answer/10104794): `Warning: No notification sent to 'someuser@somesite.com' because no Notification Device Token is present for this user.` 

For more information about this error, see [How AppSheet processes notifications](https://support.google.com/appsheet/answer/11513089#how-appsheet-processes-notifications).

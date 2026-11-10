---
fonte: https://support.google.com/appsheet/answer/10108291?hl=en
baixado: 2026-11-10
---

# USERSETTINGS()

Specified user setting value

Returns the value of the user setting.

To learn how to configure user settings to customize the behavior of your app, see [User Settings: The Essentials](https://support.google.com/appsheet/answer/10106760).

## Sample usage

`USERSETTINGS("Team")` returns the value of the `Team` user setting

## Syntax

`USERSETTINGS("`*`user`*`-`*`setting`*`")`

- *`user-setting `*- Name of the user setting. To view and configure the users settings, see [Configure user settings](https://support.google.com/appsheet/answer/10106760#configure-user-settings).

## Notes

Equivalent to: `[_THISUSER].[`*`usersetting`*`]`

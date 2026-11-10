---
fonte: https://support.google.com/appsheet/answer/10106760?hl=en
baixado: 2026-11-10
---

# User Settings: The Essentials

The user settings allow the user to customize the behavior of the app. 

You can change the names, types, and other properties of one or more user settings. User settings may be used in expressions ([security filters](https://support.google.com/appsheet/answer/10104488), [slice filters](https://support.google.com/appsheet/answer/10106308), [app formulas and initial values](https://support.google.com/appsheet/answer/10106437), [column constraints](https://support.google.com/appsheet/answer/10107948), [format rules](https://support.google.com/appsheet/answer/10106703), and so on) to control the behavior of the app.

When you show at least one user setting, AppSheet adds a new **Settings** view to the menu navigation that you can customize. For example, you can prompt users to set their language preference. Then modify the user interface using `DisplayName` expressions based on the chosen language.

Setting menu added when User Settings are set to Show

Other common use cases for user settings include:

- Your app has data analytics for 10 different countries. Ask the user to select a country using the User Settings, and filter the data (using a security filter or slice) to show just the appropriate information for that country.
- Your app is for members of a soccer league to see the upcoming matches for their team. Ask the user to choose their team using the User Settings, and filter the data appropriately.
- Just as in the Display Jobs sample, your app is for members of a team to pick up tasks to work on. Each team member provides an identifier or name using the User Settings, and the app filters the data appropriately. 

For security reasons, do not use User Settings to create a custom user sign-in process in your app. For more information about user sign-in, see [Require sign-in: The Essentials](https://support.google.com/appsheet/answer/10104975).

 

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

Learn more about user settings in the following sections:

- [Configure user settings](#configure-user-settings)
- [How user settings are stored](#how-stored)

## Configure user settings

To configure user settings:

1.  Open the app in the editor
2.  Go to **Data**  and select **User Settings** under **Options** in the Data panel. There are a fixed number of options, each of which is initially hidden.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data \> User settings**.
3.  Edit any of the users settings. This is identical to the way you refine the [column structure](https://support.google.com/appsheet/answer/10106674) of regular tables in the app. You can use many of the same mechanisms: [column constraints](https://support.google.com/appsheet/answer/10107948), [initial values](https://support.google.com/appsheet/answer/10106437), and so on.
4.  Click **Edit**  to view the full set of properties for a specific user setting.See [Configure column properties](https://support.google.com/appsheet/answer/10106509) for more information about the properties that you can configure.
5.  Click **Show?** to make a user setting available to app users in the menu navigation.
    When you show at least one user setting, AppSheet adds a new **Settings** view to the menu navigation that you can customize.

## How users settings are stored

Each individual user setting is a row in a hidden table. The columns of this hidden table have the same column features as normal table columns, such as column types, column constraints, app formulas, initial values, and display names. Column values from the user settings table are available within expressions using the [`USERSETTINGS()`](https://support.google.com/appsheet/answer/10108291) function or `[_THISUSER].[`*`usersetting`*`]`.

Unlike normal tables, the user settings are stored on the device itself, not in the cloud. Consequently, user settings do not follow the user between devices. If multiple users *sign in* on the same device, each will have their own user settings, and one user may not access another's user settings. User settings can be used even if not signed in, but will no longer be scoped to a particular user.

User settings are calculated when the app is opened for the first time, even if you never open the Users Settings panel. All user settings are readable by the app, regardless of the **Show?** setting.

#### Lifetime

The user settings option values are saved in the app on each device or browser in which the app is running. The user settings are unique to each user device. These values persist across restarts of the app.

However, when the app is being run in the emulator within the app editor, user settings (along with all other cached information) are deleted every time the page is refreshed. This allows the app creator to work with a clean state each time the app is run.

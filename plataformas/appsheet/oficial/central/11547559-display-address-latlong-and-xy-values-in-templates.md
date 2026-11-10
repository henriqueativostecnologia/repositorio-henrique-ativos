---
fonte: https://support.google.com/appsheet/answer/11547559?hl=en
baixado: 2026-11-10
---

# Display Address, LatLong, and XY values in templates

Display `Address`, `LatLong`, and `XY` values in your templates as described in the following sections:

- [Display an Address in a template](#display-address)
- [Display a LatLong in a template](#display-latlong)
- [Display an XY in a template](#display-xy)

## Display an Address in a template

Display an `Address` in a template by specifying its name.

For example, if your `Address` column is called `Home Address`, you can display it as follows:

    Name: <<[Name]>>
    Address: <<[Home Address]>>

 

An `Address` is displayed as text by default. You can create a [format rule](https://support.google.com/appsheet/answer/10106703) to control how the `Address` is displayed.

To create a format rule to control the display of the `Address` column:

1.  Open the AppSheet editor.
2.  Go to **App** App icon **\> Format Rules**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **UX \> Format Rules**.  
3.  Click + **New Format Rule**.
4.  Choose the table containing the `Address` in the **For this data** field.
5.  Select the `Address` column in the **Format these columns and actions** field.
    For example, `HomeAddress` or `_ComputedAddress`.

## Display a LatLong in a template

Display a `LatLong` in a template by specifying its name.

For example, if your `LatLong` column is called `Location`, you can display it as follows:

    Name: <<[Name]>>
    Location: <<[Location]>>

 

A `LatLong` is displayed as a Google Map by default. You can control how the `LatLong` is displayed using a [format rule](https://support.google.com/appsheet/answer/10106703).

To create a format rule to control how the `LatLong` is displayed:

1.  Open the AppSheet editor.
2.  Go to **App** App icon **\> Format Rules**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **UX \> Format Rules**.  
3.  Click **New Format Rule**.
4.  Choose the table containing the `LatLong` column in the **For this data** field.
5.  Select the `LatLong` column name in the **Format these columns and actions** field.

## Display an XY value in a template

You can display an `XY` value in a template by specifying its name. An XY is always displayed as text in templates.

For example, if your `XY` column is called `FloorPlan`, you can display it as follows:

    Name: <<[Name]>>
    Floor Plan: <<[FloorPlan]>>

**Note**: We hope to provide you with the option of displaying an `XY` value as an image in the future.

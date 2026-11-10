---
fonte: https://support.google.com/appsheet/answer/10106703?hl=en
baixado: 2026-11-10
---

# Format Rules: The Essentials

Format rules enable you to change the way information is displayed throughout your app.

- [About format rules](#about)
- [Add format rule](#add)
- [Add format rule to your favorites](#favorites)

## About format rules

Format rules allow you to customize icons, text, and more. This helps you make your app more unique. You can also make different formatting rules for each row, creating different formatting for different data.

An app can define more than one format rule and, in fact, more than one rule can match the same data at the same time. In such cases, the order of the formatting rules in the app determines the actual behavior.

The rules are processed in order from the first to the last. If two matching rules conflict in their formatting information, the last rule takes precedence. So for example, if Rule 1 matches and sets the Text Size to 1.5 and Rule 2 also matches and sets the Text Size to 2.5, the final Text Size will be 2.5.

In the case of icons, the rules are additive. So if Rule 1 matches and assigns an icon and Rule 2 also matches and assigns an icon, both icons are shown for the data.

Expensive format rules that require a lot of computation each time a screen is scrolled can affect the app's interactivity and performance.

 

Format rules are not supported for [onboarding views](https://support.google.com/appsheet/answer/11911809) at this time.

## Add format rules

To add format rules:

1.  Open your app in the app editor.

2.  Go to **App ** App icon **\> Format Rules** and click **+** in the Format rules header.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **UX \> Format Rules** and click **+ New Format Rule**.

3.  Configure the following properties:

    |                                  |                                                                                                                                                                                                                                                                  |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Property**                     | **Description**                                                                                                                                                                                                                                                  |
| Rule name                        | Name of the format rule.                                                                                                                                                                                                                                         |
| For this data                    | Table that the rule applies to.                                                                                                                                                                                                                                  |
| If this condition is true        | Condition that must be satisfied for the formatting rule to take effect. If you leave this blank, the rule applies to all rows in the table. However, you could specify a simple formula like `[Country] = "USA"` or a more complex formula for richer behaviors |
| Format these columns and actions | Columns in the table that you want formatted. Hold down the `Ctrl` key to select multiple items.                                                                                                                                                                 |

    Configure format rule

     

4.  Optionally, you can customize the visual, text, and workflow template formats, or provide a descriptive comment for the format rule by expanding the additional sections. For example:

    - Show an icon next to the row, inside the map pin, or on any view.
      Expand the **Visual Format** section to set icons based on rules for the data in your app. Make sure to select any column where you would like the icon featured (choose your location column to feature icons inside map pins instead of numbers). You can browse through the icons and click on the one you want to use, or search for a specific icon using the text box.

      **Note**: Adding icons will affect the size of columns in the table view. 

    - Customize the text and highlight colors from the list of theme-based colors.
      Highlight color determines the color of the icon. You can also manually type in any hex-based color code you want, such as `#0F77FF`. You can use this tool to find color codes: [http://www.colorpicker.com](http://www.colorpicker.com/)

      The image below shows the results of the visual customizations in the format rule.

      Results of the visual customizations in the app

      For [desktop browsers](https://support.google.com/appsheet/answer/12407883), you can customize the color of individual icons using format rules. For example:

      Individually colored icons

    - Customize the text size and style (such as underline, bold, and so on).

Individual format rules can be disabled. If so, they remain in the app definition but they don't run. This is useful if you want to define and test a format rule, but aren't ready to enable it for live use.

##  Add a format rule to your favorites

To easily access frequently used format rules, add them to your favorites. 

 To add a format rule to your favorites:

1.  Open the app in the app editor.
2.  Go to **Apps** App icon **\> Format Rules**.
3.  Position your cursor over the format rule in the Format rules pane and select **More ********************************************************************************************************************************************************************************************************************************************************\> Add to favorites**.

Remove an format rule from your favorites by positioning your cursor over the format rule in your favorites and clicking **x**.

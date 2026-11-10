---
fonte: https://support.google.com/appsheet/answer/15831909?hl=en
baixado: 2026-11-10
---

# About the new mobile framework

This is a **preview release** of the mobile design framework. See [product launch stages](https://cloud.google.com/products#section-23). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps.

To access your app using a mobile device, you have the option of using the new mobile framework or the current mobile framework (set by default). Eventually, the new mobile framework will replace the current mobile framework. We encourage you to test out this feature in a non-production environment — by making a copy of your apps — and provide your feedback.

Learn more about the new mobile framework in the following sections:

- [About the new mobile framework](#about)
- [Turn on the new mobile framework](#turn-on-new-mobile-design)

###  Provide your feedback

 Your feedback is invaluable in helping us shape the future of this framework for general availability. Follow the steps described in [Send feedback about AppSheet](https://support.google.com/appsheet/answer/14663970#product). Be sure to indicate you are using the** new mobile framework** in the description.

## About the new mobile framework

AppSheet's new mobile framework:

- Improves the overall mobile experience with a more responsive app, enhanced stability, and modernized user experience
- Unifies the mobile app experience with the [desktop experience](https://support.google.com/appsheet/answer/12407883)

The following table describes the modernized user interface (UI) improvements.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **UI improvement**                                 | **New mobile framework**                           | **Current mobile framework**                       |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Floating navigation buttons**\                   | Action button More menu in new mobile design       | Action bar overlay in legacy mobile                |
| \                                                  |                                                    |                                                    |
| More  menu when 3 or more primary actions          | Action bar with expanded More menu in new mobile   | Action buttons overlay content, maximum of 4       |
|                                                    | design                                             |                                                    |
| -   Allows for multiple actions without losing     |                                                    |                                                    |
|     visibility of view content                     |                                                    |                                                    |
| -   Supports up to 6 actions                       |                                                    |                                                    |
| -   Includes tooltips                              |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Bottom navigation bar**                          |                                                    |                                                    |
|                                                    |                                                    |                                                    |
| More  menu when 5 or more buttons in bottom        | Bottom navigation bar in new mobile design showing | Bottom navigation bar in legacy mobile showing 7   |
| navigation bar                                     | 4 buttons and More menu                            | buttons and More menu scrolled out of view         |
|                                                    |                                                    |                                                    |
| -   Adapts to different screens sizes              |                                                    | More menu scrolls out of view, up to 7 buttons     |
| -   Improves legibility of icons and titles        |                                                    | shown                                              |
| -   Minimizes scrolling                            |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Sync**                                           | Icon:  Sync icon                                   | Icon:                                              |
|                                                    |                                                    |                                                    |
| Improved sync functionality                        | Sync status in bottom panel                        |                                                    |
|                                                    |                                                    |                                                    |
| -   Modernizes icon                                |                                                    |                                                    |
| -   Displays additional information about sync     |                                                    |                                                    |
|     status in bottom panel                         |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Drill-down bar in group-by views**               | New mobile side navigation                         | Legacy mobile side navigation                      |
|                                                    |                                                    |                                                    |
| Persistent access to menu navigation (no need to   |                                                    |                                                    |
| navigate back)                                     |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Bottom sheets for secondary actions**            | Secondary actions in bottom menu on new mobile     | Secondary actions in drop-down on legacy mobile\   |
|                                                    |                                                    |                                                    |
| Secondary actions shown in menu at bottom of       |                                                    |                                                    |
| screen for easier access and improved legibility   |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Search**                                         | Search in new mobile framework                     | Search current mobile framework                    |
|                                                    |                                                    |                                                    |
| Modernized search field and filter control         |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Header columns in detail views**                 | Header column in detail view in new mobile design  |                                                    |
|                                                    |                                                    |                                                    |
| Header columns in detail views don't obscure the   |                                                    |                                                    |
| main image                                         |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Custom color icons**                             | Individually colored icons                         |                                                    |
|                                                    |                                                    |                                                    |
| Customize the color of individual icons using      |                                                    |                                                    |
| [format                                            |                                                    |                                                    |
| rules](htt                                         |                                                    |                                                    |
| ps://support.google.com/appsheet/answer/10106703)\ |                                                    |                                                    |
|                                                    |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

Other changes that further align the mobile experience with the desktop experience include:

- When using custom app launchers or navigating between apps that use different mobile frameworks you might experience unexpected results with the navigation patterns.
- For [grouped actions](https://support.google.com/appsheet/answer/10107706#composite&zippy=%2Cgrouped-execute-a-sequence-of-actions):
  - Only one [navigation action](https://support.google.com/appsheet/answer/10107706#navigate) or [external action](https://support.google.com/appsheet/answer/10107706#external-communication) is executed, even if you specify more than one. It also ends the execution of the grouped action.
  - [Validations rules](https://support.google.com/appsheet/answer/10107949) are enforced in each step of the grouped action.

## Turn on the new mobile framework

To turn on the new mobile framework, when [configuring general settings for views](https://support.google.com/appsheet/answer/10107387#general-settings) **turn on **the **New mobile framework **setting in the **General** section. This setting is turned off by default.

You can continue to use the current mobile framework in your app by turning off the new mobile framework at anytime.

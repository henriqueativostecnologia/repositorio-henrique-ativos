---
fonte: https://support.google.com/appsheet/answer/15990700?hl=en
baixado: 2026-11-10
---

# How to limit AppSheet license consumption

Customers can license app users through any of the available license tiers, including AppSheet Core, AppSheet Enterprise Plus, and AppSheet User Pass, as described in [How to Choose a subscription](https://support.google.com/appsheet/answer/10105400).

In some cases, it is necessary to restrict license consumption in an organization. AppSheet provides the following options to accomplish this goal.

------------------------------------------------------------------------

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/15990700)

#### Advise app owners on how to adjust sharing settings in their apps

A license is consumed whenever an app user accesses an app. The license that the app user consumes is based on the license of the app owner. For example, if an app owner with an enterprise license shares an app with a user that has an AppSheet Core entitlement through their Google Workspace license, then that Core user will consume an enterprise license that month--or a User Pass license if purchased. If the enterprise app owner restricts how the app is shared, then the Core user will not consume that license. To learn more about app sharing settings, go to [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

#### Use the Core security setting to restrict sharing with external users

If the Core security setting is turned off, it is possible for Core app owners to share their apps with users outside of the organization that don't have an [*entitlement to AppSheet Core through their Workspace license*](https://support.google.com/appsheet/answer/10105400#core-editions). AppSheet provides controls to admins to limit sharing outside of the organization when the Core security setting is turned on. To learn more about how to control this setting for your Core app owners, go to [Control access to AppSheet](https://support.google.com/a/answer/16018438). 

#### Turn AppSheet on or off for Google-authenticated users

You can control which Google-authenticated users are allowed to use the AppSheet editor and AppSheet apps. Admins with the necessary privileges can turn AppSheet on and off using the Google Admin console. To learn more about how to turn AppSheet on or off for specific users, groups, or organization units, go to [Turn AppSheet on or off for users](https://support.google.com/a/answer/10216943).

#### Use policies to restrict app sharing (requires AppSheet Enterprise Plus)

You can use AppSheet policies to [*restrict who is allowed to use your organization’s apps*](https://support.google.com/appsheet/answer/12282002?hl=en). It is also possible to define exceptions to these policies based on the app owner, app user, or app itself. To learn more about how to restrict usage using policies, go to [Define governance policies](https://support.google.com/appsheet/answer/11948767).

#### Define the group of users allowed to create apps (requires AppSheet Enterprise Plus)

AppSheet allows admins to define the group of users that are allowed to create apps. Currently, only Google Groups are supported, but in the near future, Microsoft groups will also be supported. To learn more about restricting who can build apps, go to [Restrict who can create apps](https://support.google.com/appsheet/answer/11918568#restrict-create-apps). 

#### Define the group of users able to use pooled enterprise licensing (requires AppSheet Enterprise Plus)

If you have pooled enterprise licensing turned on, then any user of your verified domains can consume your pooled enterprise licenses by default. When configuring pooled licensing, you can define the group of users that are allowed to consume your pooled enterprise licenses. Only users in that group will be able to use your enterprise licenses. Both Google and Microsoft groups are supported. See [Turn on or off pooled licensing for AppSheet Enterprise Plus](https://support.google.com/appsheet/answer/15617758#pooled-licensing).

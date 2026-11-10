---
fonte: https://support.google.com/appsheet/answer/16003327?hl=en
baixado: 2026-11-10
---

# About license warnings

You may see warnings in the AppSheet Admin Console if one or more of the following are true:

- Your organization has exceeded the number of licenses purchased
- Users of your organization's apps have accessed apps without a sufficient license

This section provides more information about the license warnings and sharing violations:

- [License warnings](#license-warning-scenarios)
- [Sharing violations](#sharing-violations)
- [Additional context on why licenses were used](#additional-context)
- [License warnings FAQ](#faq)

- **Note:** License warnings are not shown to app creators or app users—warnings are only visible to admins. However, your AppSheet service may be interrupted after multiple consecutive months of unresolved license warnings. If service interruption becomes necessary, AppSheet will provide at least 30 days of advanced notice to admins.

On the Used tab on the [Licenses](https://support.google.com/appsheet/answer/14960110) page, you will see a *historical report* of users and the licenses they have used in the most recent calendar month.

**Reporting on the Licenses \> Used tab** **is historical. **Any changes made to your subscription or to app sharing settings won't cause the warnings to be removed until the following month. However, changes to license assignment or pooled licensing will take effect within 24 hours.

 

**Verify license assignment on Licenses \> Assigned tab. **Note that changes may take 24 hours to be reflected in the AppSheet Admin Console.

Learn more about [how to limit AppSheet license consumption](https://support.google.com/appsheet/answer/15990700).

## License warning scenarios

The following lists common license warning scenarios. See also [Additional context on why licenses were used](#additional-context) and the [License warnings FAQ](#faq).

------------------------------------------------------------------------

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/16003327)

#### Number of Core licenses used is more than number purchased

This warning will appear when there are more Core app users and app owners than Core licenses purchased. This can happen when the Core security setting is off and your Core app owners share their apps with users (for example, external or unauthenticated users) that do not have a Core entitlement through your organization’s Workspace license.

#### Number of Enterprise Plus licenses used is more than number purchased

This warning will appear when there are more Enterprise Plus app users and app owners than Enterprise Plus licenses purchased. This can happen when your Enterprise Plus app owners share their apps with users that have a Core license or with external users. It can also happen when you have pooled licensing turned on without purchasing sufficient enterprise licenses with an annual commitment.

#### Number of User Pass licenses used is more than number purchased

This warning will appear when you have more users consuming User Pass licenses than have been purchased. This can happen when your Core or Enterprise apps have been shared more broadly than initially estimated.

## Sharing violations

The following lists the sharing violations.

------------------------------------------------------------------------

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/16003327)

#### Users are accessing Core apps without a Core or User Pass license

This warning will appear when a user does not have a Core license and accesses an app created by a Core app owner. This can happen when a Core app owner shares an app with a user outside the organization or within the organization but without a Core license. Note that this scenario is different from exceeding the number of Core licenses purchased. It is possible for your organization to have unused Core licenses, but still have a sharing violation because the app user does not have a Core entitlement or because your organization has not purchased User Pass licenses. Learn more about the [*Google Workspace editions that include AppSheet Core*](https://support.google.com/a/answer/10100275?hl=en#core-editions).

#### Users are accessing Enterprise apps without an Enterprise or User Pass license

This warning will appear when a user does not have an Enterprise Plus license and accesses an app created by an Enterprise Plus app owner. Note that this scenario is different from exceeding the number of Enterprise licenses purchased. It is possible for your organization to have unused Enterprise licenses, but still have a sharing violation because the app user does not have an Enterprise Plus license or because your organization has not purchased User Pass licenses.

## Additional context on why licenses were used 

Licenses can be consumed for any of the following reasons:

- **Enterprise admin**: The user was assigned AppSheet admin privileges and has an AppSheet Enterprise Plus license.
- **Enterprise app owner**: The user owned active enterprise apps in the calendar month. This will be the reason that a user consumes an enterprise license even if they have also used enterprise apps - or in other words, enterprise app ownership takes precedence over enterprise app consumption.
- **Used Enterprise app**: The user accessed an enterprise app in the calendar month. Note that it is possible for a user with a lower license tier (for example, Core or external user) to consume an enterprise license because an enterprise app owner shared one of their apps with the user.
- **Core app owner**: The user owned active Core apps in the calendar month. This will be the reason that a user consumes a Core license even if they have also used Core apps - or in other words, Core app ownership takes precedence over Core app consumption.
- **Used Core app**: User accessed a Core app in the calendar month. Note that it is possible for a user with a lower license tier (for example, Free or external user) to consume a Core license because a Core app owner shared one of their apps with the user.
- **Assigned or pooled**: The user was granted an enterprise license - either assigned through the Google Admin Console or automatically granted through pooled licensing. This will only occur when the user is accessing apps owned by a non-enterprise app owner.

## License warnings FAQ 

 The following lists the frequently asked questions.

------------------------------------------------------------------------

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/16003327)

 

#### I purchased User Pass licenses, why do I still see license warnings?

- Once a license is used, the license remains with the user through the end of the calendar month. For example, if users have already used an Enterprise license earlier in the month, then they can't be granted a User Pass license until the following month. In other words, User Pass licenses can't be retroactively applied to users that already used an Enterprise or Core license.

- After User Pass licenses have been purchased, external users that haven't already used an Enterprise license, will be granted User Pass by default. External users that have already used an Enterprise license earlier in the month will be granted a User Pass license the following month as long as the organization has purchased User Pass licenses.

#### I changed my pooled license settings, why do I still see license warnings?

Once a license is used, the license remains with the user through the end of the calendar month. Changes to pooled license settings will immediately take effect for new users that haven't been granted a license, but users that have already used a license will only see an impact the following calendar month. For example, if your organization has pooled licensing turned on for any app user and you change those settings to restrict pooled licensing to a group of users, any users outside of the group that have already used an Enterprise license will continue to produce license warnings until the end of the calendar month. The following month, the license warnings will be removed.

#### How can I resolve the license warnings immediately? When will I have to wait until the following calendar month?

- If you have used more Enterprise licenses than you have purchased, then purchasing additional Enterprise licenses will resolve the license warnings within 24 hours (you can view the last update in the upper right-hand corner of the AppSheet Admin Console). The only way to immediately resolve license warnings for a given license type (such as, Core, Enterprise, User Pass) is to purchase licenses of that license type. 

- If you change your license settings or want a user to consume a different license type, then those changes will only apply for the following calendar month because once a license is used, it remains with the user.

#### How do I assign users to only use my User Pass licenses?

- User Pass licenses are pooled - they are not assigned in the Google Admin console. Attempting to assign the licenses to a user in the Google Admin Ccnsole will have no effect. After User Pass licenses are purchased, they are automatically granted to external users, unauthenticated users, and users with a Core or Free license that access an app created by an Enterprise user.

- If your organization needs to limit usage of User Pass licenses, you can use AppSheet policies to restrict who can share apps with external users. Exceptions can be added to the policy for the app creators that need to share their apps with external users.

#### How do I prevent users from consuming my Enterprise licenses?

You have two options:

- Option 1: Assign your Enterprise licenses in the Google Admin console and apply AppSheet policies to restrict app sharing with external users. If you plan to assign your licenses, make sure pooled licensing is turned off. If you have apps that require sharing with external users and you don't want them to consume an Enterprise license, then you can purchase User Pass licenses. Keep in mind that any existing users that have used an Enterprise license prior to this change will have used that license for the month. They will only use a User Pass license the following month.

- Option 2: Configure your pooled license settings to restrict access to members of a group you have selected. This will ensure that only users within the group you define will use your Enterprise licenses.  Keep in mind that any existing users that have used an Enterprise license prior to this change will have used that license for the month.

#### Why does the AppSheet Admin Console show my organization using more licenses than I have paid for in the Google Admin console?

A license is used anytime someone accesses an app owned by a member of your organization. If an app creator shares their app with users that have not been assigned a license, then your organization could use more licenses than they have paid for. Warnings will be displayed in the AppSheet Admin Console if your organization's usage exceeds the licenses purchased. If the Core security setting is turned on, then your app creators with a Core license will be limited to sharing their apps with Core users. For app creators with an Enterprise license, you can use AppSheet policies to restrict sharing with external users and you can configure a pooled license group to restrict sharing with internal users with a Core or Free license.

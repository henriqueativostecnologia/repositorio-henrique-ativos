---
fonte: https://support.google.com/appsheet/answer/15342373?hl=en
baixado: 2026-11-10
---

# AppSheet Admin Console FAQ

Find answers to your questions about the AppSheet Admin Console.

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/15342373)

#### Are there any limitations for admins without an AppSheet Enterprise Plus license?

Yes, non-Enterprise Plus admins **do not** have the ability to do the following:

- View account or app detail pages
- Adjust governance polices or team settings

#### What does it mean when I see "Guest \#######" on the App usage or Licenses page?

When app creators create [public apps](https://support.google.com/appsheet/answer/10104983#share-anyone) (apps that do not require sign-in), an email address is not collected. The only identifying information is the device id. These guest sign ins are represented as `Guest #######`.

#### What will happen to the My team page?

The [My team](https://support.google.com/appsheet/answer/10104796) page will remain available for now until all of the primary functionalities are migrated to the AppSheet Admin Console. 

#### I am seeing users with AppSheet Enterprise Plus licenses that I have not assigned in the Google Workspace Admin console?

- This can happen when an AppSheet Enterprise Plus app creator has shared an app with a user without a license or the organization has been provisioned with the [team licensing model](https://support.google.com/appsheet/answer/14101111). AppSheet supports two provisioning models, as described in [How AppSheet Enterprise Plus licenses are provisioned](https://support.google.com/appsheet/answer/14101111). We will soon allow customers to select their provisioning method self-serve. In the meantime, if you need to switch your provisioning model, your admin can submit a request to [AppSheet Support](https://support.google.com/appsheet/gethelp).
- Keep in mind, any user of an app created by an app creator with an AppSheet Enterprise Plus license will also need that same license (in other words, AppSheet Enterprise Plus app creator -\> AppSheet Enterprise Plus app user).

#### Why aren't all of the purchased licenses listed on the Licenses page?

The AppSheet Admin Console provides information on the licenses purchased through Google Workspace, including AppSheet Core, AppSheet Enterprise Plus, and AppSheet External User.

Licenses might not be listed in the AppSheet Admin Console for the following reasons:

- The license was purchased using either of the following methods:
  - Offline or from a reseller prior to June 2024
  - Through a consumer billing account on [appsheet.com](https://appsheet.com)
- The license was a legacy type (such as, AppSheet Business) and has been consolidated into AppSheet Enterprise Plus.

If you don't see the correct number of licenses purchased from Google Workspace or a reseller, click **Send feedback** in the AppSheet Admin Console and report this to AppSheet.

#### My usage is greater than the license purchased? Will my users get blocked?

This can happen when your organization was provisioned with the [team licensing model](https://support.google.com/appsheet/answer/14101111) or when app creators have shared their apps with unlicensed users.

In the short team, no users will be blocked. Admins will be given several months advanced notice before stricter license enforcement. In the meantime, you can review the features included in each plan by reviewing the [AppSheet pricing page](https://about.appsheet.com/pricing/) and [How to choose a subscription](https://support.google.com/appsheet/answer/10105400), and [adjust your licenses](https://support.google.com/a/answer10569787) in the Workspace Admin Console.

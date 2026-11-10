---
fonte: https://help.asana.com/s/article/automatic-guest-removal?language=en_US
baixado: 2026-11-10
---

# Automatic guest removal

**Available for organizations and divisions on Asana [Enterprise+](https://asana.com/enterprise) tiers.**

**Visit our [pricing page](https://asana.com/pricing) for more information.**

Automatic guest removal allows super admins to automatically remove guests after a certain period of time of inactivity, reducing security risks for organizations. Automatic guest removal reduces manual work for super admins and makes guest management easier.

## Inactivity time limits

Super admins can set the following domain-wide inactivity time limits for guests:

- 15 days
- 30 days
- 60 days
- 90 days
- 120 days
- 180 days

Inactive guests will be automatically removed from the organization unless they've been [exempted](#h_01HSTGTM7QC3FT1YHT2KPPMDQH).

> A user will be defined as active if they have engaged with Asana via mobile, web, or email. Read more about [how last activity is defined](#h_01HSXRHCRA6SKNP3NCZ368Y8K3).

## Setting inactivity day limits

To set inactivity day limits, you must enable this control from the admin console’s security tab.

1.  Navigate to the **Security tab** in the admin console
2.  Scroll down to **Admin controls,** and click **Guest settings**
3.  Turn on the toggle for automatic guest removal
4.  From the drop-down, select the number of days you want to remove inactive guests after
5.  Click **Save**

> Changes to automatic removal settings will be applied within 24 to 48 hours. Afterward, automatic removals will happen once per day.

Newly invited or recently restored guests will have a grace period to become active. They will be automatically removed if they do not become active within this timeframe.

## Individual guest exemptions

Admins and super admins can set exceptions for individual guests so their access never expires.

To set individual guest exemptions:

1.  Navigate to the **Members tab** in the admin console and click the three dot icon next to the member’s name
2.  Head to the **Security tab**
3.  Turn on the toggle for “Exclude from automatic guest removal”

The user won’t be automatically removed even if they were last active beyond the limit.

## Monitoring last activity

Admins can monitor guests’ last activity through the admin console. To see their last activity, navigate to the **Members tab** in the admin console and look for the **Last activity** column.

> Asana will not send notifications to admins or guests regarding the removal.

## Tasks of removed guests

When you remove guests, their tasks are added to a project, which is owned by the super admin you’ve assigned in the **[Member removal settings](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim?language=en_US)** in the admin console.

## Defining last activity

The following are triggers which update the guest’s last activity:

- Loading the mobile app
- Clicking or making keystrokes in the web or desktop app
- Creating, completing, liking a task, or generating a comment via email

[](https://forum.asana.com/c/forum-en/tips/6)

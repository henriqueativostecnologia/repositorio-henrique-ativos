---
fonte: https://help.asana.com/s/article/manage-session-duration?language=en_US
baixado: 2026-11-10
---

# Sessions management

**Available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.** **Visit our [*pricing page*](https://asana.com/pricing) for more information.**

The ability to choose a **session duration** is available to super admins of organizations and divisions. A **session’s duration** is the amount of time a user can spend logged into Asana before they are logged out automatically by the system. To allow more control and flexibility super admins can control the session duration for Asana web and Desktop users. Setting **Session Duration Controls** allows the super admin to determine session durations with their companies’ standards in mind, and can select whether they would like the session duration for users to be 14 days or infinite (where the users are never automatically logged out).

Like what you see? Get started with a free Asana trial today. [Try for free](https://asana.com/create-account "Try for free")

## Session duration

#### Super admins of organizations can manage session durations by:

#### Super admins of organizations can manage session durations by:

1.  Navigating to the admin console
2.  Go to the **Security** section of your admin console and scroll to **Session Duration**
3.  Here, you can select from two options: **Never automatically log out**, where users are logged in for an infinite amount of time **Log out after 14 days**
4.  Once you have selected from the two options, click **Save configuration**

> As a super admin of a **division** please reach out to [Asana Support](https://asana.com/support "Asana Support") to set your divisions’ **Session Duration**

### How this works for an existing user

If the super admin **modifies** the session duration for their organization, then all existing user sessions will be terminated. When users login again they will get new session duration going forward. For instance, if a super admin chooses a 14-day auto-logout, then all existing user sessions will expire immediately and when users login again they will have 14 days session expiration.

> A user who is in multiple domains will have their timeout set to the lowest session duration across all domains.

### How this works with SAML login

Users governed by an organization’s SAML login will not be subject to the domain's session duration setting. Instead, their session duration will continue to be defined by the [SAML configuration](https://help.asana.com/s/article/global-authentication-settings?language=en_US "SAML configuration").

## Idle timeout duration 

Super admins of organizations can manage idle session duration.

1.  Navigate to the admin console
2.  Click **Security** from the sidebar and scroll down to **Authentication**
3.  Click** Session management**
4.  Here, you can select from two options: 
    1.  Allow unlimited idle time where users are not logged for an infinite amount of time
    2.  Log out after idle time defined (please note the time mentioned here must be between 1 and 14 days)
5.  Once you have selected, click **Save changes**

### How this works for an existing user

They are logged out immediately. We can't enforce ABSE until a user logs in after it is enabled. As for guest users, we will apply the most strictest setting to the guests based on the home vs guest domain they are collaborating in.

### How this works with SAML login

Users in SAML domains WILL be subject to idle session timeout.

## How session duration and idle timeout duration interact

If an admin sets both a session duration and an idle timeout duration, both will be enforced. A user's session will remain valid as long as they are active up to a maximum session length defined by the session duration

## How SAML sessions work with these

- Session durations defined in the SAML configuration will override the session duration for users who log in with SAML.
- Users who log in with SAML will still be subject to Idle timeout duration if it is set by the domain.
- If the SAML session duration is shorter than the idle timeout duration, the idle session duration will not be honored and the user will automatically be logged out due to the SAML session duration length.
- SAML sessions are not enforced on guests since they are not required to login through SAML.

[](https://forum.asana.com/c/forum-en/tips/6)

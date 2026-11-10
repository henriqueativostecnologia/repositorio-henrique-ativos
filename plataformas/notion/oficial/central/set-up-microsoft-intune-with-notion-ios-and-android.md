---
fonte: https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android
baixado: 2026-11-10
---

# Set up Microsoft Intune with Notion (iOS and Android)

In this help doc

## Set up Intune to manage Notion on iOS and Android mobile devices.

[Jump to FAQs](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#faq)

------------------------------------------------------------------------

**Note:** This is available for Enterprise plans only. Notion supports Microsoft Intune for the Notion mobile apps.

Microsoft Intune can apply security policies to the Notion mobile app. This helps IT teams protect company data in Notion on iOS and Android devices.

Notion supports Intune app protection policies (also called MAM without device enrollment). That means Intune manages the app and its data, not the entire device.

------------------------------------------------------------------------

## [What you’ll need to start](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#what-you%E2%80%99ll-need-to-start)

To configure Notion with Microsoft Intune, you’ll need:

- A Notion Enterprise plan

- Admin access in Microsoft Intune

- Admin access in Microsoft Entra ID (formerly Azure AD)

- Intune licenses for for all members who will use Notion on mobile devices

- The Notion mobile app installed on iOS or Android

------------------------------------------------------------------------

## [What policies are supported](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#what-policies-are-supported)

Notion supports the following app protection controls through Intune:

- Restrict cut, copy, and paste

- Restrict screen capture

- Restrict sharing to other apps

- Restrict backups

- Require corporate credentials

- Require a PIN or biometrics

- Require re-authentication after a timeout

- Conditional launch checks (minimum OS version, app version, offline grace period, or blocked rooted/jailbroken devices)

- Selective wipe (remove work data from Notion)

- Block multiple accounts (restrict to one workspace at a time on managed devices)

## [Set up Notion with Microsoft Intune](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#set-up-notion-with-microsoft-intune)

### [Step 1: Add Notion to Intune](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#step-1-add-notion-to-intune)

First, you’ll need to add Notion to Microsoft Endpoint Manager.

1.  Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com).

2.  Go to **`Apps`** → **`All apps`** → **`Add`.**

3.  Add Notion from the iOS store app or Android store app.

4.  Assign the app to the right users or groups.

5.  Click **`Create`** to add the app.

### [Step 2: Create and assign app protection policies](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#step-2-create-and-assign-app-protection-policies)

App protection policies control how corporate data is handled within Notion. You'll need to create separate policies for iOS and Android.

1.  In the Intune admin center, go to **`Apps`** → **`App protection policies`.**

2.  Click **`Create policy`** and select **`iOS/iPadOS`** or **`Android`.**

3.  Under `Apps`, select Notion from the list of managed apps. Alternatively, click `Add` and select `Custom apps`. Then, enter the bundle identifier "notion.id."

4.  Choose the protection settings you want.

5.  Assign the policies to the right users or groups.

6.  Review and create the policy. Then, repeat for the other platform.

### [Step 3: Enable Microsoft Intune in Notion](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#step-3-enable-microsoft-intune-in-notion)

An organization owner must turn on Intune in Notion.

1.  Open the admin console in Notion.

2.  Find the Microsoft Intune setting.

3.  Turn it on.

Once you switch on this setting, members may see a one-time Microsoft sign-in the first time they open Notion on mobile.

**Note:** Policies only apply to users who are assigned an Intune license and targeted by your Intune policy assignments.

------------------------------------------------------------------------

## [What users will see on mobile](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#what-users-will-see-on-mobile)

After Intune is set up, users keep using the standard Notion mobile app. Depending on your policies, users may:

- Need to sign in with Microsoft

- Be blocked from copying or pasting content outside of Notion

- Be blocked from sharing content to other apps

- Be required to set up a PIN or biometrics for access

**Note:** When signed into an Intune-managed workspace, users will see a "Managed" badge in the workspace switcher.

------------------------------------------------------------------------

## [Troubleshooting](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#troubleshooting)

- Policies aren’t applying

  - Confirm the user is included in the Intune policy assignment

  - Confirm the user has an Intune license

  - Wait a few minutes for policy changes to propagate, then have the user sign out and sign back in

  - Confirm the user is on the latest Notion mobile app

- Users can’t access Notion

  - Check conditional access settings (if your org uses them)

  - Confirm required Microsoft apps are installed if your setup requires them (like Microsoft Authenticator or Company Portal)

- Unexpected policy behavior

  - Check whether multiple policies apply, and whether policy priority is affecting results

  - Contact Notion support with details about expected vs. actual behavior

------------------------------------------------------------------------

## [FAQ](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#faq)

- Which Notion plans support Intune?

  Intune support is available on the **Enterprise** plan only.

- Do users need a separate Notion app?

  No. Users can use the standard Notion mobile app.

- Can I use Intune with personal Notion accounts?

  Intune policies apply to work accounts managed through your organization.

- What happens during selective wipe

  Work data on the device is removed from Notion. The Notion app stays installed.

------------------------------------------------------------------------

## [Related resources](https://www.notion.com/help/set-up-microsoft-intune-with-notion-ios-and-android#related-resources)

- [Microsoft Intune documentation](https://learn.microsoft.com/en-us/mem/intune/)

- [App protection policies overview](https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policy)

- [Conditional Access documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

------------------------------------------------------------------------

## FAQs

Which Notion plans support Intune?

Intune support is available on the Enterprise plan only.

Do users need a separate Notion app?

No. Users can use the standard Notion mobile app.

Can I use Intune with personal Notion accounts?

Intune policies apply to work accounts managed through your organization.

What happens during selective wipe?

Work data on the device is removed from Notion. The Notion app stays installed.

Still have more questions? Message support

## Contents

- [What you’ll need to start](#what-you’ll-need-to-start)
- [What policies are supported](#what-policies-are-supported)
- [Set up Notion with Microsoft Intune](#set-up-notion-with-microsoft-intune)
- [Step 1: Add Notion to Intune](#step-1-add-notion-to-intune)
- [Step 2: Create and assign app protection policies](#step-2-create-and-assign-app-protection-policies)
- [Step 3: Enable Microsoft Intune in Notion](#step-3-enable-microsoft-intune-in-notion)
- [What users will see on mobile](#what-users-will-see-on-mobile)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Related resources](#related-resources)

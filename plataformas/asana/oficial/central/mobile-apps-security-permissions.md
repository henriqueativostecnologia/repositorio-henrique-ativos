---
fonte: https://help.asana.com/s/article/mobile-apps-security-permissions?language=en_US
baixado: 2026-11-10
---

# Mobile apps security permissions

**Mobile data controls are available on the Asana [*Enterprise+*](https://asana.com/enterprise) tier, as well as [*legacy tier*](https://asana.com/pricing-legacy) Legacy Enterprise.** **Mobile app management is available on the Asana *[Enterprise](https://asana.com/enterprise)* and *[Enterprise+](https://asana.com/enterprise)* tiers, as well as *[legacy tier](https://asana.com/pricing-legacy)* Legacy Enterprise.**

**Mobile app management is not available on Division plans.**

Add additional security to the Asana mobile apps ([iOS](https://help.asana.com/s/article/asana-for-ios?language=en_US) and [Android](https://help.asana.com/s/article/android-basics?language=en_US)) to protect your organization’s data while enabling your team to work and collaborate from anywhere.

#### Related articles

- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Managing password settings in the admin console](https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US)
- [Profile field editability controls](https://help.asana.com/s/article/profile-field-editability-controls?language=en_US)
- [Global authentication settings](https://help.asana.com/s/article/global-authentication-settings?language=en_US)
- [Managing teams through the admin console](https://help.asana.com/s/article/managing-teams-through-the-admin-console?language=en_US)
- [Billing settings in the admin console](https://help.asana.com/s/article/billing-settings-in-the-admin-console?language=en_US)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls?language=en_US)
- [Managing organization settings](https://help.asana.com/s/article/managing-organization-settings?language=en_US)
- [Managing members in an organization](https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US)
- [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations?language=en_US)

Super admins can manage the following mobile data controls for their organization:

## Biometric authentication

By activating biometric authentication, you can allow users to unlock Asana on mobile devices using their fingerprint or facial recognition. You can set the frequency at which users will need to re-authenticate. Device passcode will be used in the event biometrics are unavailable.

## Widget permissions

Restrict the Asana home widget on mobile devices, so users are unable to view tasks directly from the phone’s home screen.

## Attachment permissions

Restrict downloads or the ability to share attachments in Asana on mobile devices.

## Screen capture permissions

This data control is available on Android only.

Choose whether users in your organization can take screenshots of the mobile app.

## Copy and paste permissions

Limit copy and paste permissions in the mobile app.

## Mobile application management

### Microsoft Intune integration

**Available on the Asana [Enterprise](https://asana.com/enterprise) and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tier](https://asana.com/pricing-legacy) Legacy Enterprise.**

Asana's Microsoft Intune integration enables IT admins to protect corporate data by applying security policies like restricting downloads, restricting data transfer between apps, and requiring PIN or biometric authentication.

The integration applies to Asana’s [iOS ](https://help.asana.com/s/article/asana-for-ios?language=en_US)and [Android](https://help.asana.com/s/article/android-basics?language=en_US) mobile apps, and is not relevant to [Asana’s desktop app](https://help.asana.com/s/article/asana-desktop-app?language=en_US). To set up the integration via the mobile application management settings, follow these steps:

1.  Open the mobile app and tap **Other options**.
2.  In the bottom sheet, select **Enroll** **with Intune** and complete the enrollment process.
3.  Once enrollment is complete, Intune policies are applied and the app automatically restarts.
4.  Reopen the app and select **Sign in with Intune**.
5.  After signing in successfully, you can start using Asana.
6.  Follow the [Microsoft instructions here](https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policies#app-protection-policies-for-iosipados-and-android-apps) to create an app protection policy for Asana. In step 5 of the Microsoft instructions, choose **+ Select Public Apps**, and select **“Asana: Work in one place”** from the search results.

After you've added Asana in Intune, assign it to your users by following the instructions detailed [here](https://learn.microsoft.com/en-us/mem/intune/apps/apps-deploy).

## Configuring Intune for Asana

1.  From the iOS App Protection policy in the Intune portal, navigate to Manage \> Properties and click **Edit** for **Data Protection. **
2.  In **Send data to other apps** add the following exception based on the platform:
    1.  iOS: 
        1.  name: "Asana" and value: "asana"
    2.  Android: 
        1.  name: "Asana" and value: "com.asana.app"

This fix is necessary because Asana is not a managed app until after the user logs in, so we need to enable redirecting from a managed app (Edge) to an unmanaged app (Asana).

## Intune mobile login

1.  Open the mobile app and tap **Other options**.
2.  In the bottom sheet, select **Enroll** **with Intune** and complete the enrollment process.
3.  Once enrollment is complete, Intune policies are applied and the app automatically restarts.
4.  Reopen the app and select **Sign in with Intune**.
5.  After signing in successfully, you can start using Asana.

### Troubleshooting Intune Integration

**Symptom:** “Something went wrong. The Application couldn’t be opened” when clicking “Continue to app” during the login process.

**Fix:** Ensure the exemption configurations are set up correctly.

[ ](https://forum.asana.com/c/forum-en/tips/6)

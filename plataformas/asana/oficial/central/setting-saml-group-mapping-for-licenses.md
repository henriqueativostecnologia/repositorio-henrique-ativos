---
fonte: https://help.asana.com/s/article/setting-saml-group-mapping-for-licenses?language=en_US
baixado: 2026-11-10
---

# Setting SAML group mapping for licenses

SAML group mapping allows employees who do not have an Asana license to submit internal form responses without claiming a license. If your organization uses SAML to control sign-in and you want non-Asana users to be able to submit forms, such as IT requests or internal ticketing submissions, SAML group mapping is the solution. We recommend sharing this article with your IT department or identity provider (IdP) manager before beginning setup.

Super admins can use SAML Group Mapping to designate users who can consume a license based on the security group value passed via SAML. This allows you to have users consume a license during sign-in while other users will not, and their usage of Asana will be restricted to submitting internal form responses. Users who cannot consume a license will be routed to your internal ticketing system to request access to Asana.

This functionality allows non-licensed users to submit private form responses without claiming a license. If you plan on using Asana for Request Tracking or Ticketing, you should set up SAML Group Mapping accordingly.

## Requirements for configuring SAML group mapping for licenses

- Super admin privileges
- SAML SSO configured

## How to set up SAML Group Mapping

The SAML group attribute must be configured in your identity provider (IdP). The group claim must be named “group” or “groups” (e.g., [Azure documentation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-group-claims), [Okta documentation](https://help.okta.com/en-us/content/topics/apps/define-group-attribute-statements.htm)). Once you have configured your SAML configuration to include the group claim in your IdP, you can set up SAML group mapping in Asana.

1\. Sign in to the Asana admin console

2\. In the navigation menu, click on Security, then **SAML**

3\. Navigate to the **SAML group mapping** tab

4\. Click **Add Group Claim.**

5\. Enter the correct information for:

- **Eligible group name:** Group name (or group ID) of the IdP security group containing users eligible to consume an Asana license. If there are multiple groups, separate them with a comma.
- **URL for license requests from your organization:** This is where users who cannot consume a license will be redirected to.
- Status: 
  - **Off**: the mechanism is not active.
  - **Testing**: The mechanism is active for the designated testing users. Enter the email addresses of new users to test different scenarios. It’s crucial that these users are new, not existing. If you’d like to test with existing users, make sure to deprovision them first.
  - **Live**: the mechanism is active for all internal users

6\. Click **Save**

## Recommendations

For Azure customers: Limit the groups returned in the claim to only “Group assigned to the application.” Make sure to customize the group name to be “groups” ([documentation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-group-claims)).

## Limitations

1.  **Existing users:** Only new users are affected by the SAML Group Mapping mechanism when it comes to consuming licenses or not. New users are users that have never used Asana or have used Asana but have been deprovisioned.
2.  **Updating license type:** The current mechanism for SAML Group Mapping is limited to the consumption of licenses. It does not give granular control over what type of licenses.
3.  **Revoking licenses**: Licenses cannot be revoked via the SAML Group Mapping mechanism. Use SCIM or Asana admin console for license management.

## FAQ

### Are any modifications needed to the Asana application for your identity provider?

Yes. There are two modifications needed:

1.  Add group claims attribute to the SAML configuration
2.  Give access to Asana to the group of users that should be able to submit form responses without consuming a license

Here is a schematic of the configuration. Please note that if you have provisioning jobs enabled, we suggest a different configuration ([more details here](https://help.asana.com/s/article/saml-group-mapping-and-scim-interaction)). 

 

### Does SAML Group Mapping replace SCIM?

No. License consumption via SAML Group Mapping is only effective for new users during authentication. New users are users that have never used Asana or have used Asana but have been deprovisioned. SCIM is the right scalable option to automatically provision/deprovision. SAML Group Mapping should not be used to manage user and license lifecycle.

### How does SAML and SCIM interact with each other? 

Please read [this article](https://help.asana.com/s/article/saml-group-mapping-and-scim-interaction) for more information.

### Ineligible users are still able to consume a license?

Verify that the SAML payload you’ve pasted contains the group claim used to enforce SAML Group Mapping for license. The group claim should have the custom name: “group” or “groups.” SAML Group Mapping will not work if the group claim is not recognized by Asana.

### I’ve checked that the SAML payload contains the group claim named “group,” but ineligible users can still consume a license.

Verify that testing users are new users. New users are users who have never used Asana or who have used Asana but have been deprovisioned.

### Why does the URL for license requests show “Invalid URL”?

This URL must be a valid link to your internal intake form, which allows your users to request access to Asana. It can be an Asana org-only form.

### Can SAML Group Mapping be used to assign View Only Licenses?

No. Users who log in via SAML and are eligible to consume a license will consume a full license. Users with View Only Licenses should be set in the Asana admin console.

### Does SAML Group Mapping affect guests in the guest organization? 

No. License consumption only happens in the home organization of a given user. Guests do not consume licenses in the organizations where they are a guest. 

[](https://forum.asana.com/c/forum-en/tips/6)

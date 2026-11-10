---
fonte: https://help.asana.com/s/article/authentication-and-access-management-options-for-paid-plans?language=en_US
baixado: 2026-11-10
---

# Authentication and access management options for paid plans

By default, Asana's regular authentication steps apply, and your organization members have the choice to either use a traditional password or Google SSO to log into their respective accounts.

In paid organizations, super admins can select how their members log into Asana, set password complexity requirements and force reset all members' passwords. If you purchase a division plan on Enterprise, Enterprise+, then SAML can also be enabled. SAML can also be enabled for divisions on the Legacy Enterprise tier.

Paid authentication settings only apply to your organization members. Organization guests are not affected by your authentication settings.

Like what you see? Get started with a free Asana trial today. [Try for free.](https://asana.com/create-account "Try for free")

## Password strength and force password reset

[Check out this article to find out how to update password strength requirements and force a password reset for your organization.](https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US)

## Google Sign-In

If your company uses **Google Workspace** for business or education, and you are using a paid version of Asana, you have the option to require your members to authenticate via Google.

> You can't set up Google Sign-In if you are on a **Division Plan**.

To change your organization to Google Sign-In, navigate to the **Security** tab in the admin console. From here, go to the **Global authentication settings** and click **Google sign-in**. Select **Required for all members, except guests **and click **Save changes**.

Once this change has been saved, any passwords associated with your members' Asana accounts will no longer work and they will be required to use Google SSO.

If you are changing the email domain associated with your Google accounts, please [contact us](https://asana.com/support "contact us") so that we can add the new domain to your organization.

## SAML

If your company uses an identity provider like OneLogin, Okta, LastPass, Microsoft Entre, SecureAuth, or Active Directory, your IT department may want to configure SAML. To set up SAML, you must:

- Belong to an organization or division on Asana Enterprise, Enterprise+, or Legacy Enterprise.
- Be a super admin the organization

Once an organization has been set up with SAML, the organization members will no longer need a password to log into their accounts. From the login page, they can just enter their email and click Log in, leaving the password field empty. Alternatively, they can also use the IdP app dashboard to access Asana.

### Step One: Configure your IDP

If you meet those conditions, the first step is to configure Asana with your identity provider. The steps for OneLogin, Okta, LastPass, Bitium, SecureAuth, Active Directory and Entrust Identity are listed below, but you can also do this for other identity providers:

#### Active Directory

[Check out this document to find out how to set up SAML for Asana with Active Directory.](https://docs.google.com/document/d/1S7PkUHjv9KrihJ1r5aecmus5sLsiaoIuH1bXsd5qKCI/edit?usp=sharing "Check out this document to find out how to set up SAML for Asana with Active Directory.")

You could also try Okta Cloud Connect. Okta Cloud Connect is a free edition of Okta for one application. It allows you to set up Okta for AD integration and SSO for one core application. You can find more information [here](https://www.okta.com/asana/ "here").

#### Microsoft Entra

[Check out this article to find out how to set up SAML for Asana with Microsoft Entra.](https://docs.microsoft.com/azure/active-directory/saas-apps/asana-tutorial "Check out this article to find out how to set up SAML for Asana with Azure AD.")

> This set up is different from the Asana provided Microsoft SSO option. For more information on this, please see: [Asana for Microsoft](https://asana.com/microsoft)

#### Google Workspace

Learn how to set up SSO via SAML for Asana [here](https://support.google.com/a/answer/7376624?hl=en "here").

#### LastPass

- In LastPass Enterprise, first go to your Enterprise Console and select the SAML tab at the top of the console. You will then be taken to the main SAML page
- Click the Asana app icon
- Follow the instructions on the screen
- Copy the Log-in URL and the x.509 certificate for use in Step Two

#### Okta

- In Okta, click the **Applications** tab
- Search for Asana
- Copy the Log-in URL and the x.509 certificate for use in Step Two
- Learn more [here](http://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Asana.html "here").

#### OneLogin

- In OneLogin, go to **Apps \> Find apps**
- Search for Asana
- Click **add** next to Asana
- Click **Continue**
- Copy the the sign-in page URL and x.509 certificate somewhere for use in Step Two

#### SecureAuth

[Check out this article for step-by-step instructions on setting up SAML for Asana with SecureAuth.](https://asana.com/guide/help/premium/secureauth "Check out this article for step-by-step instructions on setting up SAML for Asana with SecureAuth.")

#### Entrust Identity

[Check out this article to find out how to set up SAML for Asana with Entrust Identity.](https://entrust.us.trustedauth.com/documentation/help/tigs/index.htm?_ga=2.130647435.584760475.1713911964-1508820560.1713911964#t=Integrate_Asana_Enterprise.htm "Check out this article to find out how to set up SAML for Asana with Entrust Identity.")

### Step Two: Configure Asana

After you've configured Asana with your identity provider, you now make the appropriate changes in Asana.

#### To change your organization to SAML

1.  Click your profile photo and select **Admin console** from the drop-down menu
2.  Navigate to the **Security** tab
3.  Navigate to the **Global authentication settings** section
4.  Click **SAML authentiction**
5.  Click **Required for all members, except guest accounts**
6.  Paste the sign-in page URL that you copied from Step One into its corresponding field
7.  Paste the X.509 Certificate that you copied from Step One into its corresponding field
8.  Set a session timeout for your members
9.  Add a mobile session timeout if needed
10. Click **Save changes**
11. All of your users will be logged out (you included) in order to guarantee that all of your full members authenticate via SAML from that moment on.

If you are using open-source or non native integrations, such as Shibboleth or PingFederate. You will need to share the Asana SSO metadata with the technical contact to be configured in their IdP of choice.

    <md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="https://app.asana.com/">
            <md:SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
                    <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
                    <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://app.asana.com/-/saml/consume" index="0"/>
            </md:SPSSODescriptor>
    </md:EntityDescriptor>

We recommend that a super admin for your organization first sets SAML to **optional** and tries to log in with their SAML credentials. Then after a successful login, the super admin can switch the configuration to **required**.

Once set up properly, anyone who belongs to your company's organization will be required to log in to their Asana account with your organization identity provider (regardless of other organizations or workspaces their account may have access to).

Super admins can control which internal users have access to Asana via their identity provider, by assigning SAML Sign-In to specific user groups only. If you are a super admin and are having trouble with setting up SAML for your organization, [contact us](https://asana.com/support "contact us"). If you’re looking to set some rules for different IdP user groups, please [contact us](https://form.asana.com/?k=csOe_OseUAdh8hWBZ90XvQ&d=15793206719).

## Audit log details for failed SAML logins

If your organization has access to the Audit Log API, failed SAML sign in attempts generate `user_login_failed` events in the [audit log](https://developers.asana.com/docs/audit-log-events).

When a member's SAML login fails, these `user_login_failed` events now include a sanitized version of the SAML response returned by your identity provider. This additional detail helps admins and IT teams understand why a login failed and quickly identify configuration issues between Asana and the identity provider, while keeping sensitive values redacted.

You can use the audit log to correlate failed sign in attempts with the user, the time of the attempt, and other event details from Asana and your identity provider. For the complete event schema and field definitions, see the [Audit log events developer documentation](https://developers.asana.com/docs/audit-log-events).

## SAML session timeout

Super admins can set SAML session timeout between 1 hour and 30 days in the admin console. Members will be automatically logged out and asked to log in again after the specified timeout set.

Mobile session timeouts are disabled by default. Manage this setting in the **Mobile session timeout** section at the bottom of the window.

## Public certificate

Asana supports the HTTP POST binding method for SAML, not HTTP REDIRECT. This means you must configure your IdP to use HTTP POST bindings, ensuring secure data transmission during the authentication process.

For enhanced security, Asana requires that either the SAML Assertions or the entire SAML Response is signed. This measure ensures the authenticity and integrity of the data exchanged. Ensure at least one of these elements is signed in your configuration.

Asana does not sign SAML requests. Consequently, when setting up SAML in your IdP, you should deactivate signing for authentication requests. This can be done by setting the Sign AuthnRequest preference to false (e.g., AuthnRequestsSigned="false").

Please include the IdP signing key information within the SAML assertion. This key is crucial for verifying the signature and maintaining the security of the SAML assertion.

## Two-factor authentication

For more information on two-factor authentication, see this [article](https://asana.com/guide/help/fundamentals/two-factor-authentication "here").

[](https://forum.asana.com/c/forum-en/tips/6)

---
fonte: https://help.asana.com/s/article/microsoft-single-sign-on?language=en_US
baixado: 2026-11-10
---

# Microsoft Single Sign-On

Asana supports Microsoft Single Sign-On (SSO), allowing your organization's members to log in to Asana using their Microsoft account credentials. To sign in with Microsoft, click **Continue with Microsoft** on the Asana login page and follow the prompts to authenticate with your Microsoft account.

How you use Microsoft SSO in Asana depends on your plan. Any member can sign in with their Microsoft account, but setting Microsoft SSO as required is available on paid plans only, and SAML with Microsoft Entra ID is available on Enterprise and Enterprise+ only.

## Setting Microsoft SSO as required

**Available on paid Asana plans. **

Organization admins can set Microsoft SSO as the required login and sign-up method for all members. When a required SSO is set, all members, except guests, must sign in using their Microsoft SSO option, and all other sign-in options will reroute the user.

To set Microsoft SSO as required, navigate to the **Admin console** and click the **Security** tab. Under the **Authentication settings**, click **Single Sign-On (SSO)**.

Note: You have to log in using the method you want to set as required. 

 

Locate the **Microsoft** row and check the **Required** checkbox. 

> You have to log in using the method you want to set as required. 

You will be prompted to log out and sign back in with your Microsoft account to confirm the change. Once confirmed, Microsoft SSO will be enforced as the only login method for your organization's members.

**Note**: If you have another method as required, you need to first uncheck it as required.

## Understanding different Microsoft authentication options

While the standard Microsoft SSO button allows quick access using Microsoft credentials, your organization might require more advanced, enterprise-grade identity management. Asana supports two distinct options for this: **Microsoft SSO** and SAML set up with **Microsoft Entra ID** as the IDP.

### 1. Microsoft SSO 

The Microsoft Single Sign-On (SSO) option is available to anyone with a Microsoft account. You do not require an enterprise security setup, nor do you need to use Microsoft Entra ID (formerly Azure Active Directory) as your identity provider (IDP). 

Please note that if you have a Microsoft Entra ID, you can configure admin consent workflows for applications that want to use Microsoft SSO. Sometimes Asana falls within this workflow. If so, when you try to use Microsoft SSO, you will be prompted to submit a request to your Microsoft admins for access to use SSO for Asana. For more information on how to set this up on the Microsoft side, please see: [Configure the admin consent workflow - Microsoft Entra ID \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)

### 2. SAML set up with Microsoft Entra ID (formerly Azure Active Directory)

**Available on Asana Enterprise and Enterprise+ plans.**

Asana offers SAML as an option for logging in to provide additional authentication and security controls. This is separate from the Microsoft SSO native option that Asana provides. 

Microsoft Entra ID is Microsoft’s full cloud identity and access management platform. This setup allows Microsoft Entra ID to act as your primary Identity Provider (IdP) using the [SAML](https://help.asana.com/s/article/authentication-and-access-management-options-for-paid-plans?language=en_US#gl-saml) protocol. This option is configured directly in Asana's general SAML console and is ideal for organizations that want additional security controls or centralized authentication management. Check [out this article to find out how to set up SAML for Asana with Microsoft Entra.](https://learn.microsoft.com/en-us/entra/identity/saas-apps/asana-tutorial)

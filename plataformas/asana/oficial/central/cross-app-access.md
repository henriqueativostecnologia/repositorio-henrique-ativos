---
fonte: https://help.asana.com/s/article/cross-app-access?language=en_US
baixado: 2026-11-10
---

# Cross-App Access

Cross-App Access (XAA) allows your identity provider (IdP) to issue tokens that can be used to access Asana on behalf of users. This is required for integrations such as MCP that authenticate using your organization's identity provider.

## **Prerequisites**

Before configuring Cross-App Access, ensure that:

- You are an **Asana Organization Admin**.
- Your identity provider (IdP) supports **OpenID Connect (OIDC)**.
- Your IdP application has been configured to issue OIDC tokens for Asana.

## Configure cross-app access

### Step 1: Open the Cross-App Access settings

- In the Asana Admin Console, navigate to → **Security** → **Cross-app access (XAA)**

### Step 2: Enable Cross-App Access

- Turn on the **Cross-app access** toggle. This enables the configuration fields below.

### Step 3: Configure your identity provider

- Provide the following values:

|                       |                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------|
| **Field**             | **Description**                                                                      |
| **Issuer URL**        | The issuer (iss) for your IdP. This identifies the identity provider issuing tokens. |
| **JWKS URI**          | The endpoint where Asana retrieves your IdP's public signing keys to verify tokens.  |
| **Expected Audience** | The audience (aud) claim that Asana expects to receive in issued tokens.             |

See the provider-specific setup guides below for instructions on locating these values in your identity provider.

#### Okta setup

When configuring Okta as your identity provider, use your org's base domain — not a custom authorization server path.

|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| **Field**      | **Correct value**                                                                    |
| **Issuer URL** | https://{yourOktaDomain} (e.g. [https://company.okta.com](https://company.okta.com)) |
| **JWKS URI**   | https://{yourOktaDomain}/oauth2/v1/keys                                              |

⚠️ **Do not use a custom authorization server URL** (formats like https://{yourOktaDomain}/oauth2/default or https://{yourOktaDomain}/oauth2/default/v1/keys). Cross-App Access issues tokens from Okta's **org-level** authorization server, not a custom authorization server. Using the /oauth2/{id} path will cause token exchange to fail with an invalid_grant error.

### Step 4: Save your configuration

Click **Save**.

After saving, Asana will accept tokens whose issuer (iss) and audience (aud) match the configured values.

## Updating your configuration

You can return to **Admin Console** → **Security** → **Cross-app access (XAA)** at any time to:

- Update your Issuer URL
- Update your JWKS URI
- Update your Expected Audience
- Disable Cross-App Access

---
fonte: https://support.google.com/appsheet/answer/10105083?hl=en
baixado: 2026-11-10
---

# Control user access using OpenID Connect

You can use any authentication provider that supports the standard OpenID Connect protocol to control authentication and user access control for your apps.

OpenId Connect is essentially the OAuth2 protocol with standardized definitions for the scopes and behaviors. Most modern authentication providers like Okta support this protocol.  You will have to go through some standard steps in the provider's admin console to define an *app* (this tells the provider that AppSheet is going to be accessing it) and get an app key and secret. These will need to be entered into your AppSheet account.

You can't use OpenID Connect domain groups as [custom roles in your application](https://support.google.com/appsheet/answer/10105082).

### Step 1 : Register an app with the OpenID Connect provider

The specifics of this vary by provider. Typically, the provider has an admin console where you would create a new app. 

- Give the app a name that is meaningful to you, like **AppSheet Access** or **Acme Corp Field Service.** 

- You'll be prompted for a callback URL. The callback URLs should be set to one of the following values based on region supported, and `http://localhost:53519/Account/ELC`, separated by a comma and a space:  
  To use a callback URL for a specific region, such as the European Union, you must enable that region in your AppSheet Enterprise account. See [Manage AppSheet data residency](https://support.google.com/appsheet/answer/13788479).

  - **Global region**: `https://www.appsheet.com/Account/ELC`
  - **European Union (EU) region**: `https://eu.appsheet.com/Account/ELC`
  - **Asia Pacific region**: `https://asia-southeast.appsheet.com/Account/ELC`

  **Note**: It is important that you enter the URLs as shown, matching the capitalization. Also, note that the second callback URL (`localhost`) is not strictly required; it would be necessary only if you want AppSheet to debug your application in the future.

- If there is a **scope** option, the value should be **openid**.

The provider should give you a key (or client id) and a secret for this app. Make sure to copy these as you will need them in the next step.

### Step 2: Configure your AppSheet account

Now that you have set up your provider, you need to register it in your AppSheet account.

1.  Sign in to [AppSheet](https://www.appsheet.com).
2.  Go to **My account \> Integrations \> Auth Domains.**
3.  Click **+ New Auth Domain**. 
    The Add a new authentication domain dialog displays.
4.  Enter a name for the auth source.
5.  Select **OpenID Connect**. You are prompted for the following inputs:
    - **App/client key/id**: Cliend ID value you copied in step 1.
    - **App/client secret**: Client secret value you copied in step 1.
    - **Auth endpoint**: Depends on the provider. For example, for Okta it is: **https://{yourOktaDomain}/oauth2/v1/authorize**
    - **Token endpoint**: Depends on the provider. For examle, for Okta it is: **https://{yourOktaDomain}/oauth2/v1/token**
    - **Scope**: Almost always this should be set to: **openid profile email** 

We recommend that you you refer to the OpenID Connector provider documentation to ensure that you configure this correctly, especially the auth and token endpoints. For example, for Okta, see: [https://developer.okta.com/docs/api/resources/oidc/#response-properties](https://developer.okta.com/docs/api/resources/oidc/#response-properties)

### Step 3: Use the new auth domain in your apps

You can now use this domain auth source in your apps. See [Set up domain authentication in your app](https://support.google.com/appsheet/answer/10105757#domain-auth-app).

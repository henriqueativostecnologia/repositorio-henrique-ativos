---
fonte: https://help.asana.com/s/article/secureauth-for-enterprise-organizations?language=en_US
baixado: 2026-11-10
---

# SecureAuth for Enterprise Organizations

**Available on Asana [Enterprise](https://asana.com/enterprise "https://asana.com/enterprise") and [Enterprise+](https://asana.com/enterprise "https://asana.com/enterprise") tiers, as well as [legacy tier](https://asana.com/pricing-legacy "https://asana.com/pricing-legacy") Legacy Enterprise.**

**Visit our [pricing page](https://asana.com/pricing "https://asana.com/pricing") for more information.**

Follow this Guide to setup SAML for your Enterprise Organization in Asana with SecureAuth.

[Learn more about SAML authentication in this article](https://asana.com/guide/help/premium/authentication#gl-saml "Learn more about SAML authentication in this article").

## Configuration steps

### Step 1

Create a new realm for Asana in SecureAuth and [configure the Overview tab](https://docs.secureauth.com/2404/en/configure-the-admin-realm--secureauth0-.html#overview-tab "configure the Overview tab") accordingly.

### Step 2

On the [Data tab](https://docs.secureauth.com/2404/en/saml-attribute-consumption-configuration.html#identity-platform-configuration-223 "Data tab") of the Asana realm, configure Membership Connection Settings to Active Directory.

Ensure that under the Profile Fields section, the Email 1 property field is set to "mail", which should be the Active Directory email attribute through the connector. Click **Save** after entry.

### Step 3

On the [Workflow tab](https://docs.secureauth.com/2404/en/saml-attribute-consumption-configuration.html#identity-platform-configuration-223 "Workflow tab") of the Asana realm, configure settings as appropriate.

Ensure that under the SAML 2.0 Service Provider section, SP Start URL is set to "[https://app.asana.com/"](https://app.asana.com/%22 "https://app.asana.com/"") (don’t include quotes). Click **Save** after entry.

Depending on desired authentication workflow, it may be necessary to setup a second realm for Asana’s mobile application. If this is desired, see Step 8.

### Step 4

Configure the [Registration Methods tab](https://docs.secureauth.com/2404/en/saml-attribute-consumption-configuration.html#identity-platform-configuration-223 "Registration Methods tab") accordingly. Click **Save** after entry.

### Step 5

Configure the [Post Authentication tab](https://docs.secureauth.com/2404/en/saml-attribute-consumption-configuration.html#identity-platform-configuration-223 "Post Authentication tab") as follows:

### Post Authentication Section

- **Authenticated User Redirect**: SAML 2.0 (SP Initiated) Assertion Page

### User ID Mapping Section

- **User ID Mapping**: Email 1
- **Name ID Format**: urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
- **Encode to Base64**: False

### SAML Assertion/WS Federation Section

- **WSFed/SAML Issuer**: "https://(insert url for SecureAuth IDP)
- **SAML Recipient**: [https://app.asana.com/-/saml/consume](https://app.asana.com/-/saml/consume "https://app.asana.com/-/saml/consume")
- **SAML Audience**: [https://app.asana.com/](https://app.asana.com/ "https://app.asana.com/")
- **SAML Offset Minutes**: 6
- **SAML Valid Hours**: 1
- **Append HTTPS to SAML Target URL**: True
- **Generate Unique Assertion ID**: True
- **Sign SAML Assertion**: False
- **Sign SAML Message**: True
- **Encrypt SAML Assertion**: False
- **Authentication Method (1.1)**: urn:oasis:names:tc:SAML:1.0:am:X509-PKI
- **Confirmation Method (1.1)**: urn:oasis:names:tc:SAML:1.0:cm:bearer
- **AuthnContextClass**: Unspecified
- **Include SAML Conditions**: True
- **SAML Response InResponseTO**: True
- **SubjectconviermationData Not Before**: False
- **Signing Cert Serial Number**: (use Select Certificate link to choose appropriate certificate)

### SAML Attributes/WS Federation Section

- **Attribute** 1
- **Name**: email
- **Namespace (1.1)**: (leave blank)
- **Format**: Basic
- **Value**: Email 1
- **Group Filter Expression**: \*

Click **Save** after entry.

### Step 6

At this point, SecureAuth should be configured and ready. Asana will need to be [configured](https://help.asana.com/s/article/authentication-and-access-management-options-for-paid-plans?language=en_US "configured") for SAML.

### Step 7

Once Asana has been configured, you should be ready to test the SecureAuth SAML interface. Go to [https://app.asana.com](https://app.asana.com/ "https://app.asana.com"), enter your email address into the email address field and click Log In.

You should be redirected to the SecureAuth Asana interface. Depending on what authentication methods you set, what information the interface requires will vary. Once you have entered the correct information, SecureAuth should pass a successful SAML assertion back to Asana, logging you in to your Asana account.

You can also find out more by taking a look at the[ SecureAuth Asana Integration Guide](https://docs.secureauth.com/0902/en/asana--sp-initiated--integration-guide.html)

### Step 8

If you need differing authentication methods for web page usage versus the Asana mobile app, you will need to do the following:

- Create a new realm for the mobile app and name it accordingly (i.e. Asana Mobile Interface).
- Copy all settings for this new realm from the primary Asana realm.
- Modify the Workflow tab according to your requirements and click Save.
- Install the IIS Rewrite module to the SecureAuth server (may require reboot). This can be found at: [http://www.iis.net/downloads/microsoft/url-rewrite](http://www.iis.net/downloads/microsoft/url-rewrite "http://www.iis.net/downloads/microsoft/url-rewrite")
- In the IIS 8.0 console, right click the sub-web site for the primary Asana realm and click URK Rewrite.
- Click Add Rule(s) and then select Blank Rule under Inbound rules.
- In the Name field, name the rule External IP Redirection.

### In the Match URL section:

- Requested URL: Matches the Pattern
- Using: Wildcards
- Pattern: \*

### In the Conditions section:

- Logical grouping: Match All

Add conditions (as often as necessary) using Add button with the following settings:

- Condition input: {REMOTE_ADDR}
- Check if input string: Does Not Match the Pattern
- Pattern: (insert internal IP address block, example 8.4.\*.\*)

### In the Action section:

- Action type: Redirect
- Action Properties -\> Rewrite URL: /(insert IIS subsite name, example /asanaext)
- Redirect type: Temporary (307)

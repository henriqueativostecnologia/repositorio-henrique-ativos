---
fonte: https://support.google.com/appsheet/answer/10104487?hl=en
baixado: 2026-11-10
---

# Control user access using Okta

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

Okta authentication allows for user authentication for your apps. It is similar to using an [OpenID provider](https://support.google.com/appsheet/answer/10105083) but allows for Okta-specific features such as group controls to be used. For example, you may want to limit access to certain apps to the Sales Team and others to the Support Team. Using Okta as an authentication source allows this.

To set up authentication there are three steps:

1.  [Create an Okta application](#create-okta-app)
2.  [Configure AppSheet to allow Okta](#configure-appsheet)
3.  [Sign in using Okta](#sign-in)

## Create an Okta application

First, create a single sign-on application for AppSheet inside the [Okta console](https://login.okta.com/).

1.  In the Application tab, click **Add Application**.

2.  Set the application type to **Web**.

3.  Set the callback URLs to be **https://www.appsheet.com/Account/ELC** and **http://localhost:53519/Account/ELC**. 
     
    **Note**: Be sure to copy the callback URLs exactly; capitalization is important. The second callback URL, with the localhost, is not strictly required; it would only be necessary if you want to request AppSheet to debug your application in the future.

4.  Optionally, add the user groups that you would like AppSheet to have access to.

5.  Click **Done**.

    The following provides an example of the settings.

    Okta Client Credentials page

    For more details on what each field means visit [Setting up an auth-code application](https://developer.okta.com/authentication-guide/implementing-authentication/auth-code/) in the Okta documentation.

6.  Configure Okta to allow for Group Claims. See Okta's article on how to [Customize tokens returned from Okta with custom claims](https://developer.okta.com/docs/how-to/creating-token-with-groups-claim/#create-a-groups-claim-for-okta-mastered-groups).

    Take note of the ID of the Okta group you create in this step. You'll need it when configuring AppSheet in the next step.

**Note**:  When you [add a groups claim for the org authorization server](https://developer.okta.com/docs/guides/customize-tokens-groups-claim/main/#add-a-groups-claim-for-the-org-authorization-server), you must set the **Group claim type** to **Filter**; the **Expression** type is not supported in this scenario. If the Group claims filter section is not configured correctly, then you might receive the following error: `Unable to fetch group membership. The most likely reason is that your Okta config has not enabled group claims filter as Regex *.`

## Configure AppSheet

Add Okta as an Auth Provider.

1.  Ensure your account has the Business plan so that you can use the Company Domain Authorization feature.

2.  Go to the **Integrations \> Auth Domain** pane and click **+ New Auth Domain**.

3.  Select **Okta** from the list

4.  Fill out the form which requires four fields:

    - **Client ID**, **Client Secret**: From the Okta application settings
    - **Domain**: From the Okta console. For example: `https://dev-12345.okta.com`

    Add Okta configuration

5.  Click **Authorize Access**.
    Okta is added to the list of authentication domains and you can now add it to your apps.

6.  Open your app in the editor.

7.  Go to the **Security \> Domain Authentication** pane. 

8.  Enable the **Require domain authentication** option. 

9.  Select the Okta domain source you created previously in the **Authentication domain source** drop-down.

10. In the **Restrict by domain** field, enter **Default**.

11. Click **Add** to add the name of the Okta group, app role, and app version to authorize access. Group names are case-senstive.

12. Click **Save**.

It is important to note that, due to caching, adding or removing a new member from an Okta group takes up to 15 minutes to take effect.

## Sign in using an Okta group

Share the app with your end users, as described in [Share: The Essentials](https://support.google.com/appsheet/answer/10104983). When the end user accesses the app, they will be prompted to sign in to the Okta group.

Sign in with Okta

That's it! You should be able to sign-in as a member of the specified group.

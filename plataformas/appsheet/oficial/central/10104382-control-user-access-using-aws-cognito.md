---
fonte: https://support.google.com/appsheet/answer/10104382?hl=en
baixado: 2026-11-10
---

# Control user access using AWS Cognito

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

AWS Cognito is a service provided by Amazon Web Services, and is available in [AppSheet Business Subscriptions](https://solutions.appsheet.com/enterprise). It allows you to set up your own authentication source. You can provision users with explicit passwords or using one of their existing social sign in accounts, and you utilize Cognito to control secure access to your AppSheet apps. There are three reasons to do this: 

- You would like to manage user access control at a scale that goes beyond simple allow lists.
- You want to be able to provision and manage the users, control password policy, and utilize other richer characteristics of an authentication source.
- You cannot use your corporate domain controller as an auth source, because your users come from outside your corporate domain.

Using AWS Cognito requires that you set up an AWS account. This is not part of the AppSheet service. This article explains the basics of setting up a Cognito service and configuring it to be accessible from your AppSheet account. See also [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).

To control user access using AWS Cognito, perform the following steps:

1.  [Configure a user pool in your Cognito service](#configure-user-pool)
2.  [Add an IAM user](#configure-aws)
3.  [Configure your AppSheet account](#configure-appsheet-account)
4.  [Configure your app](#configure-app)
5.  [Test sign in using AWS Cognito](#test)

You can create as many user pools as you need. Some app creators choose to make a user pool for each app. Others choose to apply a single user pool to multiple apps.

 

You can't use AWS Cognito domain groups as [custom roles in your application](https://support.google.com/appsheet/answer/10105082).

## Configure a user pool in your Cognito service 

To configure a user pool in your Cognito service:

1.  Go to [http://aws.amazon.com](https://aws.amazon.com/) and sign in to the console.
2.  Navigate to **Cognito**.
3.  Click **User Pools** in the left navigation
4.  Click **Create user pool**.

In the next steps, you create and configure a user pool. The users in the user pool will define the people who have access to your app. 

### Step 1: Configure sign-in experience

On the Configure sign-in experience page, you configure how you will allow users to sign in.

To configure the sign-in experience, under Authentication providers:

1.  Notice that **Cognito user pool** is already selected under Provider types.
2.  Under Cognito user pool sign-in options, elect **Email**.
    AppSheet recommends having users sign in using email. Since email addresses are unique, they work well as unique identifiers in apps. The email each user signs in with will be accessible in using the [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) function in your app.
3.  Click **Next**.

AWS Cognito configure sign-in experience

### Step 2: Configure security requirements

On the Configure security requirements screen you can choose what requirements to apply to passwords and whether to use multi-factor authentication (MFA). 

To configure security requirements:

1.  Under Password policy, select whether you want to use the Cognito defaults or Custom policy settings.
    If you choose Cognito defaults, be sure to review the password policy defaults.
2.  Under Multi-factor authentication (MFA), configure the preferred MFA enforcement. MFA is optional. 
3.  Under account recovery:
    1.  It is recommended that you select **Enable self-service account recovery** (it is selected by default).
    2.  Select your preferred method for user account recovery messages, such as **Email**.
4.  Click **Next**.

### Step 3: Configure sign-up experience

Determine how users sign up using AWS Cognito and the method to use to verify the user account.

1.  Under Self-service sign-up:
    - Select **Enable self-registration **to allow users to sign up themselves.
      In this case, new users will see a sign up link the first time they access the app. Clicking the link will take them to a sign up page where they can create a user profile. This would allow anyone with a link to the app to sign up.
    - Deselect **Enable self-registration** to only allow administrators to create users. In this case, the sign up link will be hidden. An admin with access to the AWS Cognito account will need to add the user to the User Pool. This will send an automatic email to the user with their temporary password. The user will be prompted to change their password on first sign in.
2.  Under Attribute verification and user account confirmation, you can use the default settings.
    AppSheet strongly recommends verifying the user information.
3.  Under Required attributes, attributes, such as **email**, will be selected by default based on previous selections. Optionally, you can require users to enter additional information in the Required attributes or Custom attributes sections. These attributes will be visible in the Cognito User Pool. However, the attributes won't not accessible from inside AppSheet apps.
4.  Click **Next**.

### Step 4: Configure message delivery

To configure message delivery:

1.  Under Email provider, select **Send email with Cognito**.
2.  You can customize the email address from which automated emails will be sent. This is optional, but recommended by AWS as a best practice.
3.  Click **Next**.

### Step 5: Integrate your app

Set up app integration for your user pool. When you define an app client in Cognito, you are telling Cognito to expect AppSheet to interact with it to prompt users to sign in. 

1.  Enter a name for the user pool in the **User pool name** field, such as **AppSheetUsers**.
2.  Under Hosted authentication pages, you can use the default settings. 
3.  Under initial app client:
    1.  For App type, select **Public client**.
    2.  For App client name, enter a name for the app client, such as **AppSheet**.
    3.  Select **Generate a client secret**. 
4.  Under the Advanced app client credentials and Attribute read and write permissions, you can use the default settings.
5.  Tags are optional and not used for basic setup. See [Tagging Amazon Cognito resources](https://docs.aws.amazon.com/cognito/latest/developerguide/tagging.html) in the AWS documentation.
6.  Click **Next**.

When you create your user pool, Cognito will create a Client Id and a Client Secret, which you can access after setup is complete. You will need this information when configuring your app in AppSheet.

### Step 6: Review and create the user pool

Review the settings and click **Create user pool**.

### Step 7: Define the domain for your Cognito user pool

To define the domain for your Cognito user pool:

1.  Click the user pool that you just created in the list.

2.  Select the **App integration** tab.

3.  Under Domain, select **Actions \> Create Cognito domain**.

4.  Enter a real or fake domain (for example, **appsheettest**) in the **Cognito domain** field. 

    You will need to specify the full domain, `https://{yourdomainname}/auth/{AWS region}/amazoncognito.com`, when configuring your app in AppSheet.

5.  Click **Create Cognito domain**.

6.  Scroll to the **App clients list**.

7.  Click the AppSheet app client that was automatically created for you. 

8.  In the Hosted UI section, click **Edit**.
    The Edit Hosted UI dialog displays.

9.  Click **Add callback URL** and enter: **`https://www.appsheet.com/Account/ELC`**
    This is where you will be directed after hosted UI authentication.

10. Click **Add another URL** and enter: **`http://localhost:53519/Account/ELC`**

    The second callback URL is not strictly required --- it is only necessary if you request AppSheet to debug your application at some point in the future.

11. In the **Identity Providers** drop-down, select **Cognito user pool**.

12. In the **OAuth 2.0 grant types** drop-down, select **Authorization code grant**. 

13. In the **OpenID Connect scopes** drop-down, select **OpenID**, **Email**, and **Profile**.

14. Click **Save changes**.

## ****Add an IAM user

Add an IAM user as described in the following steps:

1.  Add an IAM user, such as **AppSheetCongnitoUser**.

2.  Record the API **access key** and **access secret** for the user.

3.  Give your IAM user an **AmazonCognitoReadOnly** permissions policy, as shown in the following figure:

    AWS Cognito IAM user

    Alternatively, you can attach the permissions policy by using the following code:
     

    `{`
    `    "Version": "2012-10-17",`
    `    "Statement": [`
    `        {`
    `            "Effect": "Allow",`
    `            "Action": [`
    `                "cognito-identity:Describe*",`
    `                "cognito-identity:Get*",`
    `                "cognito-identity:List*",`
    `                "cognito-idp:Describe*",`
    `                "cognito-idp:AdminGet*",`
    `                "cognito-idp:AdminList*",`
    `                "cognito-idp:List*",`
    `                "cognito-idp:Get*",`
    `                "cognito-sync:Describe*",`
    `                "cognito-sync:Get*",`
    `                "cognito-sync:List*",`
    `                "iam:ListOpenIdConnectProviders",`
    `                "iam:ListRoles",`
    `                "sns:ListPlatformApplications"`
    `            ],`
    `            "Resource": "*"`
    `        }`
    `    ]`
    `}`

## Configure your AppSheet account

Now that you have set up your Cognito user pool, you need to register it in your AppSheet account.

To configure your AppSheet account:

1.  Follow the steps described in [Add an authentication domain to your AppSheet account](https://support.google.com/appsheet/answer/10105757#add) and select **AWS Cognito** in the list of authentication sources.

2.  Configure the fields using the information found in the AWS Cognito console.

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Field**                                                                     | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App Client ID                                                                 | App client ID created in [Step 5: Integrate your app](#integrate-your-app).   |
|                                                                               |                                                                               |
|                                                                               | To view the app client ID:                                                    |
|                                                                               |                                                                               |
|                                                                               | 1.  Go to [http://aws.amazon.com](https://aws.amazon.com/) and sign in to the |
|                                                                               |     console.                                                                  |
|                                                                               | 2.  Select **User Pools**.                                                    |
|                                                                               | 3.  Click your user pool.                                                     |
|                                                                               | 4.  Select the **App integration** tab.                                       |
|                                                                               | 5.  Scroll to the **App clients list** and click the app client in the list   |
|                                                                               |     to display its details.                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| App Client Secret                                                             | ID for the app client created in [Step 5: Integrate your                      |
|                                                                               | app](#integrate-your-app).                                                    |
|                                                                               |                                                                               |
|                                                                               | **Note**: If you edit the AWS Cognito configuration, you'll need to create a  |
|                                                                               | new App Client Secret in the AWS Console and then copy and paste it in this   |
|                                                                               | field.                                                                        |
|                                                                               |                                                                               |
|                                                                               | To view the app client secret:                                                |
|                                                                               |                                                                               |
|                                                                               | 1.  Go to [http://aws.amazon.com](https://aws.amazon.com/) and sign in to the |
|                                                                               |     console.                                                                  |
|                                                                               | 2.  Select **User Pools**.                                                    |
|                                                                               | 3.  Click your user pool.                                                     |
|                                                                               | 4.  Select the **App integration** tab.                                       |
|                                                                               | 5.  Scroll to the **App clients list** and click the app client in the list   |
|                                                                               |     to display its details.                                                   |
|                                                                               | 6.  Click **Show secret**.                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Domain Endpoint                                                               | The domain endpoint in the following format: \                                |
|                                                                               | `https://{yourdomainname}/auth/{AWS region}/amazoncognito.com`                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| User Pool ID                                                                  | Optional. You can leave this field blank unless you have an advanced use case |
|                                                                               | that requires it.                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AWS Key ID                                                                    | Enter the AWS Key ID copied when [adding an IAM user](#configure-aws).        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AWS Key Secret                                                                | Enter the AWS Secret copied when [adding an IAM user](#configure-aws).        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Configure your app

You can now use this domain auth source in any of your apps.

To configure your app: 

1.  Open your app in the editor.
2.  Go to the **Security \> Domain Authentication** pane. 
3.  Enable the **Require domain authentication** option. 
4.  Select the domain source you created previously in the **Authentication domain source** drop-down.
5.  In the **Restrict by domain** field, enter **Default**.
6.  For **Authentication groups**, click **Add** and add enter the following:
    - Group: **Any**
    - App role: **User**
    - App version: Set to **Default**, **Latest**, or **Stable**.

    Domain authentication configuraiion
7.  Save your app.

App users will need to update their app to the latest version or errors may occur.

## Test sign in

Open the Share dialog and copy the browser link. See [Send users a link to your app](https://support.google.com/appsheet/answer/10104983#send-link).

Open a new private session in your browser (incognito in Chrome), and paste the URL. You will see the option to authenticate with Cognito.

Option to sign in with AWS Cognito

## Additional UI customization

Cognito allows you to customize the look and feel of the sign in page. See [Customizing the built-in sign-in and sign-up web pages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-ui-customization.html) in the AWS documentation.

---
fonte: https://help.asana.com/s/article/api?language=en_US
baixado: 2026-11-10
---

# API

Collaboration across teams and tools works best when everyone stays in sync and processes flow easily, without friction. This is why we have Asana's API. It's a platform to ensure all of your information is up to date and that your teams stay efficient and in the loop.

Asana’s API provides a means for software and scripts to read information from inside Asana, input information from outside Asana, and automatically react when things change. This can include: consistently doing repetitive or tedious tasks, creating reports on the state of tasks and projects, or staying in sync with other software such as Slack or Salesforce used in your organization.

Asana’s platform is built to be flexible and powerful. It's built to be intuitive enough for all teams to adopt and maintain clarity on the work being done.

If you're looking for further information on how to use Asana's API check out our [Developer documentation](https://developers.asana.com/docs/overview). If you're interested in learning more about apps, check out our [Apps page](https://asana.com/apps?category=all-apps).

Explore Asana's paid features for free. Get started with a [free Asana trial](https://asana.com/create-account) today.

## Asana Connect

Asana Connect is an easy and secure way to grant API access to third-party applications without sharing your username and password.

Asana Connect uses OAuth 2.0, an industry standard for authentication. You have likely used OAuth to authenticate and log in to services using your Facebook, Twitter, or Google accounts.

Always use discretion when approving access to your account. Carefully read any access or permission requests from the services to which you are connecting. It is also recommended that you regularly review apps you have authorized and revoke access from integrations you no longer want or need to have access to your account; you can always grant access again later.

You can use [this link](https://app.asana.com/0/my-apps) to access your developer console or follow the steps below:

#### To review your account's authorized applications:

1.  Click your profile photo from the top bar and select **My Settings**
2.  Navigate to the [**Apps**](https://help.asana.com/s/article/apps-settings?language=en_US) tab
3.  Review the **Authorized** section

You can revoke an app's access at any time from this tab using the **Deauthorize** button next to that app's name.

## Manage PATs and developer apps

If you're a developer, use the Developer App Management page to create Personal Access Tokens.

You can use [this link](https://app.asana.com/0/my-apps) to access your developer console or follow the instructions laid out in the screenshots below:

#### To access the Developer App Management page:

1.  Click your profile photo from the top bar and select **My Settings**
2.  Navigate to the [**Apps**](https://help.asana.com/s/article/apps-settings?language=en_US) tab
3.  Click **Manage Developer Apps
    **

#### From the Developer App Management page, you can:

1.  Manage or register apps that you own
2.  Manage or create new Personal Access Tokens

### Personal Access Tokens

Personal Access Tokens provide individuals with a low friction means to access the Asana API when writing scripts, working with command line utilities, or prototyping applications. In most cases you should not provide personal access tokens to applications you do not know or fully trust the creator of.

You can use [this link](https://app.asana.com/0/my-apps) to access your developer console or follow the steps below:

#### Creating a Personal Access Token

1.   Click your profile photo and select **Settings**.
2.   Navigate to the **Apps** tab.
3.  Under the **Build new apps** section, click **View developer console**.
4.  Under the **Personal access tokens** section, click **Create new token**.
5.  Enter the token name, tick the **I agree to the Asana API Terms** checkbox, and click **Create token**.
6.  Copy your token for API authentication. 

 

#### Create a Personal Access token from the Developers App Management page:

1.  Type a description of what you'll use the Personal Access Token for
2.  Click **Create**
3.  Copy your token and use it to authorize requests

> Read more about working with authentication in the Asana API in our [developer documentation](https://developers.asana.com/docs/ "developer documentation").

Applications that support accessing Asana on behalf of many users should make use of [Asana Connect](https://asana.com/guide/help/api/api#gl-connect "Asana Connect") rather than Personal Access Tokens.

It's good practice to regularly review and deauthorize access tokens you no longer want or need.

## Frequently asked questions

### What is Asana's API used for?

Asana's API allows software and scripts to read information from Asana, input external data, and automatically react to changes. Common uses include automating repetitive tasks, creating reports, and syncing with tools like Slack or Salesforce.

### What is Asana Connect?

Asana Connect is a secure authentication method using OAuth 2.0 that grants third-party applications API access without sharing your username and password.

### What are Personal Access Tokens in Asana?

Personal Access Tokens provide individual access to the Asana API for writing scripts, working with command line utilities, or prototyping applications. You create and manage them through the Developer App Management page in your Asana Settings.

### When should I use Asana Connect instead of Personal Access Tokens?

Applications that access Asana on behalf of many users should use Asana Connect, while Personal Access Tokens are designed for individual use in scripts and prototypes.

> Like what you see? Get started with a free Asana trial today. [Try for free](https://asana.com/create-account "Try for free").

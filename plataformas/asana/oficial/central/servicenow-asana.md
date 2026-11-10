---
fonte: https://help.asana.com/s/article/servicenow-asana?language=en_US
baixado: 2026-11-10
---

# ServiceNow & Asana

**Available on Asana [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Business and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

**The native ServiceNow Spoke integration has been deprecated and is no longer actively supported by Asana. The legacy setup steps in this article are retained for historical reference only. Review the supported options below before deciding how to connect ServiceNow and Asana.**

The ServiceNow and Asana integration helps IT, operations, and service management teams coordinate work across both platforms. While the original ServiceNow Spoke is no longer supported, there are two ways to connect these tools.

> The ServiceNow and Asana integration is compatible with DC and Vancouver versions. [Learn more here](https://store.servicenow.com/sn_appstore_store.do#!/store/application/85d9f7961bd32410c50d2fc0604bcb68/1.2.29?referer=%2Fstore%2Fsearch%3Flistingtype%3Dallintegrations%25253Bancillary_app%25253Bcertified_apps%25253Bcontent%25253Bindustry_solution%25253Boem%25253Butility%25253Btemplate%25253Bgenerative_ai%25253Bsnow_solution%26q%3Dasana&sl=sh).

## Supported ways to connect ServiceNow and Asana

### Unito-powered integration

Asana recommends the Unito-powered ServiceNow integration for teams that want a maintained, supported connection between ServiceNow and Asana. This integration is built and supported by Unito and requires a paid Unito plan.

To learn more and begin setup, visit the [ServiceNow integration page](https://asana.com/apps/servicenow) on Asana's app directory.

### Custom API integration

Organizations that prefer to build their own connection can use the [Asana API](https://developers.asana.com/) to create a custom integration between ServiceNow and Asana. This approach requires technical resources, your own hosting infrastructure, and ongoing maintenance by your team.

A custom API integration is best suited for organizations with established internal integration practices and clear ownership for long-term support.

## Prerequisites for installing the ServiceNow integration

The ServiceNow integration requires an Asana [Advanced](https://asana.com/plan/advanced) account or [leg](https://asana.com/pricing-legacy)[acy](https://asana.com/pricing-legacy) [tier](https://asana.com/pricing-legacy) Business which provides access to all projects that are to be used in the Asana actions. All requests to Asana will be made in the context of this account.

## Steps to install the ServiceNow integration

1.  In ServiceNow, find and install the **Asana Spoke** from the [ServiceNow store](https://docs.servicenow.com/en-US/bundle/tokyo-application-development/page/administer/integrationhub-store-spokes/concept/asana-spoke.html).
2.  In Asana, create a new OAuth application by following the steps below. More detailed steps can be found here.

- Create a new OAuth application by clicking your profile picture, then navigating to **My Settings** \> **Apps** \> **Manage Developer Apps** \> b
- Provide an **App Name** (e.g., ServiceNow) and agree to the API terms and conditions.
- Click **Create App** and note the **Client ID**, **Client secret**, and **Redirect URLs** input.
- Add your ServiceNow instance redirect link to the **Redirect URLs** field in the following format: https://{**instance-name-here**}/oauth_redirect.do and click **Add**

3.  In ServiceNow, navigate to **System OAuth** \> **Application Registry**

- Find the **Asana OAuth Provider** record and open it.
- Replace **{instance-name-here}** in the **Authorization URL** field with your ServiceNow instance name.
- In the **Client ID** field, replace **{asana-application-client-id-here}** with your Asana app’s Client ID created in step 2.
- In the **Client Secret** field, replace **{asana-application-client-secret-here}** with your Asana app’s Client Secret, also created earlier in step 2.

4.  Within ServiceNow, go to **System Web Services** \> **Outbound** \> **Rest Message**

- Find the Asana record and open it
- Click on the **Get OAuth Token** link to receive tokens successfully

## [](https://github.com/Asana/asanadotcom/blob/master/_content/guide/07-help/13-api/33-servicenow.md#external-systems-connection)External systems connection

> Integration components required: Web services

## [](https://github.com/Asana/asanadotcom/blob/master/_content/guide/07-help/13-api/33-servicenow.md#steps-to-create-a-dedicated-integration-user-administrator-of-the-integration)Steps to create a dedicated integration user (administrator of the integration)

Assign the **x_asana_asana.asana_integration_admin** role to the user. Ensure that the user also has he following three system roles:

- **flow_designer**: User should be able to create and edit flows to use Asana actions
- **web_service_admin**: User should be able to open Outbound Integrations Asana REST Message to receive tokens
- **oauth_admin** : User should be able to add credentials and links to Asana OAuth provider and click on **Get OAuth token** button in Outbound Integrations Asana REST

## [](https://github.com/Asana/asanadotcom/blob/master/_content/guide/07-help/13-api/33-servicenow.md#steps-for-regular-users)Steps for regular users:

The Asana integration administrator needs to set **Run as: System User** in the properties of the flow/subflow if it should run for regular users without access to OAuth Credential Table.

If the flow/subflow should run in the context of the current regular user:

1.  A ServiceNow admin must navigate to **Tables** / **OAuth Credential** / **Controls** and enable Security Rules (ACLs).
2.  Create a role that provides read access to the OAuth Credential table.
3.  The Asana integration admin must then set **Run with role(s): Your created role with read access to OAuth Credential table** in **Flow Properties**.

## [](https://github.com/Asana/asanadotcom/blob/master/_content/guide/07-help/13-api/33-servicenow.md#testing-the-configuration)Testing the configuration

1.  To verify the connection and ensure a successful configuration, the Asana integration user can create a sub-flow in the Flow Designer.
2.  Add the **Get Task Data** action from the Asana application and enter a valid Asana task ID.
3.  Click **Finish** and **Test**.
4.  In the modal window, click on **Run test**.
5.  After the test execution, click **Your test has finished running. View the sub-flow execution details**.

Subflow execution details should contain the **Get task data** step. **Output Data** of the **Get task data** step must return the correct **Name** and **Description** of the task. **Status** should equal 200, and **Error Message** should be empty.

## Supported actions

Once installed, you can find supported actions by searching for Asana in the Flow Builder. You can then choose from a list of default actions.

The following Asana actions will be available for use in the FlowBuilder:

Tasks:

- Create task
- Update task
- Get task data
- Duplicate task

Projects:

- Duplicate project (based on project id)
- Get project data

> You cannot use a project_template_id to duplicate projects.

Approvals:

- Create approval
- Delete approval
- Update approval

Attachments:

- Add attachment to task or approval
- Get attachments from task or approval

## Use cases

Because of the flexibility of the ServiceNow platform, this is not a comprehensive list, but reflects some common use cases:

### Automatically assign work when an incident arises

IT service management teams using ServiceNow for automating incident management can create a flow that triggers a task in Asana for customer-facing teams whenever incidents of a certain severity level occur. So, if IT logs a serious performance issue in ServiceNow, it’ll automatically trigger an Asana task for marketing to monitor customer sentiment and prepare reactive comms.

### Escalate requests that require work outside of ServiceNow

Internal-facing service teams who use ServiceNow to track and manage employee tickets often receive requests that require actions outside ServiceNow, like fulfilling hardware requests, or managing a workplace request.

## Privacy

### What data is collected?

Please see Asana Privacy Statement for more information.

Asana processes information we receive directly from you, automatically collected when you use Asana or visit one of our websites, and collected by Asana from third parties. This includes information that is needed for Asana to create an account for you and manage your ability to log in and out of Asana, which may include but is not limited to:

- Identifiers
- Password
- billing information etc.

Information you provide to us through your use of Asana, which may include but is not limited to:

- information you submit in tasks, projects etc
- timestamps
- any other information you choose to provide while using Asana that identifies or can be reasonably associated with you.

Information automatically processed when you visit our websites or use our mobile or desktop app, which may include but is not limited to:

- Metadata and inference information related to your use of Asana, our websites, and third-party integrations to better understand the way you work in Asana. We may log the actions you take as you use Asana, including but not limited to, the number of Asana workspaces you work in, the number of tasks you are assigned, what tasks or other features you view, when you delete a task or comment, the features and embedded content you interact with, the types of files you transmit, and what, if any, third-party integrations you use
- Internet network activity, cookies, and similar tracking technologies
- Device information and activity when you use Asana via a mobile device, including the type of device you are using, device IDs, operating system version, and mobile network information to ensure that we are serving you the correct version of our application
- Derived device geolocation information, including approximate geographic location inferred from an IP address etc.

#### Information Asana receives from other sources

Sometimes Asana receives your information from third parties (other individuals, marketing services, third-party integrations), which may include but is not limited to:

- Information processed from third-party integrations you set up with Asana. For example, a third-party integration may give us access to information stored in that third party that Asana will process to facilitate the integration

#### ServiceNow integration

- The integration does not collect any ServiceNow User data from the instance, except the ServiceNow instance name that we use for logs in order to provide technical support & troubleshooting.
- The integration processes data that you enter as input parameters to actions ("Create Task", "Update task", etc.) and data retrieved from the Asana API, e.g. task, attachment and project data.
- For example, data processed for logs may contain “servicenow_instance_name”, type of Asana action, and IDs of created/updated Asana tasks, projects, attachments, etc. See [example use cases](https://help.asana.com/s/article/servicenow-asana?language=en_US#gl-UseCase).

Please see the [Asana Privacy Statement](https://asana.com/terms/privacy-statement#how-we-disclose-your-information) for more information.

### How is the data used?

Please see the [Asana Privacy Statement](https://asana.com/terms/privacy-statement#how-we-disclose-your-information) for more information.

Asana uses your information to operate our products and services, communicate with you, process transactions when you change Asana plans, for security and fraud prevention, and to comply with the law. Specifically, we may process your information to:
Provide services to you and operate our business, which may include but is not limited to:

- Maintain, provide, and improve our products and services including our AI features
- Suggest [Asana Help Center](https://help.asana.com/hc/en-us/categories/13974184441243-Help-Center-) articles that may be relevant to you
- Help us better understand user interests and needs, and customize Asana for you
- Analyze and research how you interact with our websites and applications
- Store data locally on your device to help our product operate more efficiently.

In addition, we use information about your use of Asana, account information (which may include your email address and name), and information related to third-party integrations to:

- Facilitate reporting and analyze performance of the Asana platform or features available in Asana
- Provide webinars or public presentations
- Demonstrate Asana or provide you access to a demo Asana instance
- Process your information at your direction
- Provide cross-device management of your account. If you wish to opt out of Google’s ability to locate you across devices in this way, you may install the Google Analytics Opt-out Browser Add-on by clicking [here](https://tools.google.com/dlpage/gaoptout).
- Provide you with support and get your feedback
- Respond to your requests for information
- Help identify and troubleshoot any issues with your account and answer your questions
- Resolve support requests
- Provide you with reports about usage
- Survey your opinions through surveys, research studies, and questionnaires

#### Combined information

Unless otherwise prohibited by law, we may combine the information that we collect through your use of our products and services with information that we receive from other sources, both online and offline, and use that combined information as set out above.

#### Aggregated and de-identified data

We may aggregate and/or de-identify information related to your use of Asana (for example, how many tasks or projects you created) so that such information can no longer be linked to you or your device. We may use such aggregated and de-identified data for any purpose, including but not limited to, research and marketing purposes and may also disclose such data to any third parties, including advertisers, promotional partners, sponsors, event promoters, and/or others.

#### Artificial intelligence and machine learning

Some features in Asana are powered by artificial intelligence (AI) and machine learning. Admins and super admins can adjust AI preferences for your domain at any time by visiting the admin console.

When features powered by Asana AI are enabled in your domain, we use metadata related to your domain’s use of Asana to train machine learning models. Depending on the model and the feature, these machine learning models power features, both in your domain and other Asana domains.

When features powered by AI Partners are enabled in your domain, we leverage [third-party LLM service providers](https://asana.com/terms/subprocessors). Our third-party LLM service providers do not use customer data to train their models.

For more information about AI in Asana, please review [Asana AI features and admin controls](https://help.asana.com/s/article/asana-ai-features-and-admin-controls).

Asana may use AI technologies, including bots on our websites and in our product, to communicate with you, respond to your comments and questions, and provide information about our products and services. Learn more by visiting [Asana’s Trust Center](https://security.asana.com/).

#### Legal bases for processing

For more information about the legal bases Asana relies on to process your information, please visit [Other Important Information](https://asana.com/terms/privacy-statement#other-important-information).

### How we disclose your information

Please see the [Asana Privacy Statement](https://asana.com/terms/privacy-statement#how-we-disclose-your-information) for more information.

We need to disclose the information we collect about you to make our products and services run smoothly and to operate our business, which may include but is not limited to:

- Because you ask us to disclose. We may disclose your information to third parties when you ask us to do so. This includes when you connect Asana with other tools via our available [integrations](https://asana.com/apps?category=all-apps).
- Service providers, subcontractors, and subprocessors. We may provide access or disclose your information to select third parties that use the information on our behalf to assist in providing Asana’s services, website, and features. These third parties provide a variety of services to us, including without limitation sales, marketing, provision of content and features, artificial intelligence enabled functionality, advertising, analytics, research, data storage, security, fraud prevention, and other services. You can find a list of our subprocessors [here](https://asana.com/terms/subprocessors).
- Compliance with legal obligations. To comply in good faith with a valid legal subpoena, request, or other lawful process that meets the requirements of our [Law Enforcement Guidelines](https://asana.com/terms/law-enforcement-guidelines). We will notify individuals or customers of that request unless: we are prohibited from doing so by law or court order; or there are exceptional circumstances, such as an emergency involving the risk of bodily injury or death to a person or group of people or potential harm to minors.

Please see the [Asana Privacy Statement](https://asana.com/terms/privacy-statement#how-we-disclose-your-information) for more information

### How is the data transferred, stored, and secured?

Please see the [Asana Privacy Statement](https://asana.com/terms/privacy-statement#how-we-disclose-your-information) for more information

#### Security

Asana takes technical and organizational measures to protect your information against accidental or unlawful destruction or accidental loss, alteration, unauthorized disclosure or access. However, no method of transmission over the Internet and no means of electronic or physical storage is absolutely secure, so we cannot ensure or warrant the security of that information. We are constantly updating and improving our safeguards and you can read up to date information about our security practices by visiting our [Trust](https://asana.com/trust) page.

#### Storage

When you use Asana, some information about you will be stored in the United States. For more information about our EU data storage options, please visit our [Trust](https://asana.com/trust) page.

#### Transfer of your information out of EEA, UK, Switzerland, and Japan

When you use our products and services, information about you will be transferred to the United States where the majority of Asana’s data processing occurs. We may also transfer information that we collect about you to third party processors across borders from your country or jurisdiction to other countries or jurisdictions around the world.

Asana complies with the EU-US Data Privacy Framework program (EU-US DPF), the UK Extension to the EU-US DPF, and the Swiss-US Data Privacy Framework program (Swiss-US DPF) as set forth by the US Department of Commerce. Asana has certified to the US Department of Commerce that it adheres to the EU-US Data Privacy Framework Principles (EU-US DPF Principles) with regard to the processing of personal data received from the European Union in reliance on the EU-US DPF and from the United Kingdom (and Gibraltar) in reliance on the UK Extension to the EU-US DPF. Asana has certified to the US Department of Commerce that it adheres to the Swiss-US Data Privacy Framework program Principles (Swiss-US DPF Principles) with regard to the processing of personal data received from Switzerland in reliance on the Swiss-US DPF.

#### Data retention

We will retain your information for the period necessary to fulfill the purposes outlined in this Privacy Statement, to make our products and services available to you, or as instructed by you, unless a longer retention period is required or permitted by law.

Please see the [Asana Privacy Statement](https://asana.com/terms/privacy-statement#how-we-disclose-your-information) for more information

> Looking for a better way to manage your work? Get started with a free Asana trial. [Try for free](https://asana.com/create-account "Try for free")

 

[ ](https://forum.asana.com/c/forum-en/tips/6)

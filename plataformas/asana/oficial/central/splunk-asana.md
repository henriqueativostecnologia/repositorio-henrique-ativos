---
fonte: https://help.asana.com/s/article/splunk-asana?language=en_US
baixado: 2026-11-10
---

# Splunk + Asana

The Asana for Splunk integration is available for Splunk Enterprise and Splunk Cloud and is compatible with Splunk’s Common Information Model (CIM). The integration enables **super admins** to leverage Asana’s Audit Log API with Splunk.

With Splunk for Asana, super admins can utilize Splunk’s leading Security Information and Event Management (SIEM) suite to investigate, monitor, and analyze suspicious activity. For example, if an employee in one region suddenly attempts multiple logins in a foreign location, admins can use timely customized alerts to take action.

> Asana for Splunk facilitates ingestion of all audit logs available through [Asana’s Audit Log API](https://help.asana.com/s/article/audit-suite-api-and-integration-support?language=en_US "Asana’s Audit Log API").

## Admissions

### Once in Splunk, super admins will have the ability to:

1.  Configure "alerting" to accommodate your organization’s risk posture
2.  Visualize aggregations of key security-and-compliance events in Asana using Asana’s pre-built dashboard
3.  Use Asana’s audit logs in tandem with Splunk solutions like Security Essentials

## Configuration

To enable Asana for Splunk, you will need to be a **super admin** of an Enterprise+ organization in Asana and an admin of your Splunk instance. Visit the [Splunkbase Website](https://splunkbase.splunk.com/app/5736 "Splunkbase Website") to begin installation.

### To set-up the Asana for Splunk application, follow these steps:

> You’ll need the generated key to grant Splunk access to Asana.

1.  Visit the “Asana for Splunk" app on Splunkbase to begin the installation process.
2.  Log in to your Asana admin console.
3.  After logging in, click the **Apps** tab from with your admin console.
4.  Click **Service accounts**.
5.  Click the **Add service account** button.
6.  Give the service account a name.
7.  Under **Permissions** scopes, choose **Scoped permissions**, and tick the **Audit logs** box.
8.  Click **Save changes** and copy the service account token from here for later use.
9.  Inspect the URL in your browser and parse the ID of your Asana workspace.

If you have questions, feedback, or need further support, please contact the [Asana Support team](https://asana.com/support "Asana Support team").

> Like what you see? Get started with a free Asana trial today. [Try for free](https://asana.com/create-account "Try for free").

[](https://forum.asana.com/c/forum-en/tips/6)

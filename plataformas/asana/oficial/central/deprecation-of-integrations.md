---
fonte: https://help.asana.com/s/article/deprecation-of-integrations?language=en_US
baixado: 2026-11-10
---

# Deprecation of integrations

At Asana, we are committed to building a robust, enterprise-grade work management platform that evolves with the way you work. To ensure we have the capacity to deliver the most impactful, secure, and scalable solutions—including the latest advancements in AI and work context connectors—we assess and refine our integration ecosystem on an ongoing basis.

This resource documents the integrations being deprecated.

## Overview of changes

**15 April 2026** integration deprecations:

**Five (5) widget-based integrations**

- Bynder
- DocuSign
- Freshdesk
- Intercom
- Vimeo

**Three (3) rule-based integrations**

- Jira Data Center (Server) bug fixes will no longer be supported; with technical sunset scheduled for 31 December 2026
- Mailchimp
- Twilio

**Two (2) third party integrations**

- Meta Workplace 
- Adobe Creative Cloud

## What to expect

**1. Data persistence **

Your historical context is safe. Any comments or campaign snapshots previously posted to your tasks (such as those from Mailchimp) will remain in Asana and will not be deleted.

**2. Task widgets **

Existing task widgets (e.g., DocuSign or Bynder windows) will transition into standard URL links. While the interactive preview will be retired, the direct links to your external files will remain active and accessible.

**3. Automated rules **

Existing rules that trigger actions in Jira Server, Twilio, or Mailchimp will stop functioning on **April 15**. We recommend your admins review and remove these rules prior to the sunset date to maintain clean workflows.

**4. Security and authentication **

As a standard security measure, Asana will automatically revoke all app authorizations for these integrations on **April 15**. No manual action is required from your IT or Admin teams.

## Transition and migration paths

We are committed to helping you find the right alternative to ensure your workflows continue to run smoothly.

- **For bidirectional sync:** We recommend our preferred partner, **Unito**. Unito offers deep, two-way synchronization that provides more advanced functionality than our legacy native widgets.
- **For workflow automation:** Tools like **Zapier** and **Workato** provide robust connectors for DocuSign, Twilio, and Freshdesk, allowing you to build highly customizable automations.
- **Custom integration:** For unique requirements, your team can leverage the **Asana API** to build tailored integrations. Asana’s Professional Services team is also available to assist with custom scoping.

## Frequently asked questions

What is the specific timeline for Jira Data Center (Server) users?

As the world shifts toward cloud-first environments, we are aligning our resources accordingly.

- **April 15, 2026:** Official End of Maintenance. No further bug fixes or version updates will be provided.
- **December 31, 2026:** Technical Sunset. The integration will remain accessible until this date to accommodate regulatory or complex migrations, but we strongly recommend migrating to Jira Cloud or Unito before then.

We have a few Asana \<\> Jira connectors. Will they all stop working?

Only the Asana-built connector will stop working. [This listing](https://marketplace.atlassian.com/apps/1223378/asana-for-jira-data-center) will be removed, and existing installs will cease to exist on 12/31/2026. Third-party integrations [like this one](https://marketplace.atlassian.com/apps/1216786/asana-issue-links-for-jira?hosting=cloud&tab=overview) will continue to work as they are not owned or maintained by Asana.

Do Asana customers enjoy any benefit if they choose Unito?

We have partnered with Unito to offer a streamlined way to maintain your syncs. You'll be able to add this to your existing Asana plan. More details will come in early April.

Will Asana PS charge to help build a custom integration?

Our PS team is available to help design a custom solution tailored to your specific needs. We can submit a request to scope this project and determine the commercials, if any.

What happens to the data already in my tasks?

Your historical data remains. All existing comments will remain in your tasks, and active widgets (e.g., DocuSign links) will transition to standard URL links.

For security best practices, we will delete user authentications with these apps. Mailchimp, Twilio, and Jira rules will no longer be functional and should be deleted.

Does my IT and/or Admin need to take any action?

As a security measure, Asana will automatically revoke all app authentications on the deprecation date. No manual action is required from your IT or admin teams beyond determining and executing a transition/migration path for a particular integration.

If we move to another recommended vendor, who is responsible for troubleshooting?

If another vendor is engaged, they will provide support accordingly for the integration(s).

---
fonte: https://support.google.com/appsheet/answer/11511009?hl=en
baixado: 2026-11-10
---

# Introduction to webhooks

You can use a webhook from an automation bot to post to any web service on the Internet. This is a powerful way to integrate your AppSheet app with a variety of popular services like Zapier, Slack, Twitter, Twilio, and IFTTT among others.

The web service must support a REST API. Your webhook can invoke any of the operations exposed via the web service's REST API.

To use a webhook you need to do the following:

- [Set up a developer account with the web service](#set-up-dev-account)
- [Call the webhook from a bot in AppSheet](#call-webhook)

By default, [webhook automation](https://support.google.com/appsheet/topic/11446299) API calls originate from a dynamic list of IP addresses. For AppSheet Enterprise accounts, if your webhook automation API calls depend on the stability of the IP addresses for access control security, you can request that they also use the [AppSheet static IP addresses](https://support.google.com/appsheet/answer/10104492) by contacting [AppSheet Support.](https://www.appsheet.com/Support/Contact)

## Set up a developer account with a remote web service

Set up a developer account with a remote web service, such as Twilio. The web service will normally provide three pieces of information:

- URL endpoint.
- Authentication information. This may be a token or username/password.
- REST API. This describes the JSON payload to be sent to the URL endpoint via an HTTP POST message to invoke a specific action.

## Call a webhook from a bot in AppSheet

Call a webhook from a bot in AppSheet, as described in [Call a webhook from a bot](https://support.google.com/appsheet/answer/11511244). When configuring the webhook, you provide the following information obtained when setting up your remote web service account:

- URL of the remote web service. You can use expressions to dynamically construct the URL.
- Authentication information, typically sent in the headers with the webhook.
- JSON payload data, typically sent in the Body of the webhook. You can use expressions when constructing the body based on the input to the automation.

---
fonte: https://support.google.com/appsheet/answer/11628886?hl=en
baixado: 2026-11-10
---

# API integration points in AppSheet

AppSheet provides several ways to integrate with external web services.

## AppSheet REST API \[Inbound\]

External web services can invoke the AppSheet REST API to access a table within an AppSheet app. The external web service can Add, Delete, Edit (update), Find (read), or Invoke a predefined Action in the app. See [Invoke the API](https://support.google.com/appsheet/answer/10105398).

## AppSheet webhooks \[Outbound\]

- Any automation which is triggered in any AppSheet app can optionally call a webhook. These are one-way communications to an external service. See [Introduction to webhooks](https://support.google.com/appsheet/answer/11511244) and [Call a webhook from a bot](https://support.google.com/appsheet/answer/11511244).
- The basic verbs are `Delete`, `Patch`, `Post` and `Put`. There is no return nor expectation of one by design. A variety of API body payloads and header configurations are supported.

**Note**: Currently there is no multipart file upload (such as, base64 image) MIME type support.

## Direct connect to OData protocol \[Inbound\]

AppSheet can directly connect to OData sources. If your REST API is represented as an OData feed this is a zero effort experience. See [Use data from an OData feed](https://support.google.com/appsheet/answer/10106380).

## Direct connect to external REST API (Apigee) \[Inbound\]

AppSheet can connect to REST API endpoints which meet certain requirements, that is, can be represented as an OpenAPI Spec (Swagger) or can be exposed in such a way that they are one or more rectangular or tabular data sources. See [Apigee data source](https://support.google.com/appsheet/answer/10106762).

## Zapier \[Outbound\]

You can use an AppSheet webhook to trigger a Zapier Zap. The Zapier Zap can, in turn, access hundreds of external services. See [Integrate with Zapier](https://support.google.com/appsheet/answer/11557001).

## Zapier \[Inbound\]

You can create a Zapier Zap that invokes the AppSheet REST API. You can use the REST API to Add, Update, Delete, and Find (read) records in an AppSheet table. You can also use the REST API to invoke a predefined AppSheet Action. See [Connect a Zapier "ZAP" to your app](https://support.google.com/appsheet/answer/10105001).

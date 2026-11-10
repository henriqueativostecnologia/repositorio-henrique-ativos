---
fonte: https://support.google.com/appsheet/answer/16418067?hl=en
baixado: 2026-11-10
---

# Access to resources restricted by external AppSheet accounts

Organizations that have [verified ownership of their domains](https://support.google.com/a/answer/60216) with Google Workspace can restrict access to their resources by external AppSheet accounts. So if you have apps that use resources, such as authentication domains, data sources, and connectors, that rely on credentials from an account owned by another organization, then your access may be restricted if your organization has [restricted access by external AppSheet accounts](https://support.google.com/appsheet/answer/15617758#restrict-external-account-credentials).

Organization ownership is based on Google Workspace verified domains, meaning that any AppSheet account with a domain that hasn't been verified by your organization administrator is considered to be an external account. Public email address providers (such as Gmail, Hotmail, onmicrosoft.com, iCloud, and so on) will always be considered external to your organization’s verified domains. That also means, however, that if your organization permits usage of AppSheet, you can access any of your resources from the AppSheet account owned by your organization as long as usage is compliant with your organization’s policies.

## Error message: Resource not available

If access to resources is restricted by external AppSheet accounts, you may see the following error:

**Resource not available**

You cannot access this data source, authentication domain or connector because the organization that owns it has restricted access from external accounts.

## How to resolve

If your apps encounter this error, there are two ways to resolve it:

1.  Remove the authentication domain, data source, or connector from the app
2.  Have your AppSheet account added to the allowed exception list by an organization administrator, as described in [Restrict access to resources by external AppSheet accounts](https://support.google.com/appsheet/answer/15617758#restrict-external-account-credentials)

## Frequently Asked Questions (FAQ)

## This data source used to be available to me before, why is my app being blocked now?

AppSheet has upgraded the security features available to organizations that verify ownership of their domains through Workspace. By default, all AppSheet organizations now restrict access to their resources from external accounts.

## I have the credentials required to access this resource, why am I being blocked?

The account that you are using to access this resource is not owned by the organization whose credentials you are using. If your organization permits you to use AppSheet, then you can access this resource by signing into the AppSheet account owned by your organization.

 

## My account is not external - it is owned by my organization, why am I being blocked?

It is likely because the domain of the account you are using hasn/t been officially verified by your Google Workspace organization. Your organization administrator must verify ownership with Workspace and then all accounts under that domain will no longer be considered external.

---
fonte: https://support.google.com/appsheet/answer/10104380?hl=en
baixado: 2026-11-10
---

# Control user access using Active Directory

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

If your organization uses Active Directory (as do most organizations that use Office 365 or Exchange for email), then you can utilize domain groups defined in Active Directory to control access to your apps.

This mechanism only works with Active Directory hosted in the cloud in Microsoft Azure. It does not work for Active Directory instances hosted on premise without federation to a cloud/Azure-based instance.

You may need to first configure your Active Directory enable API access. 

You will then need to add your Active Directory as a domain auth provider in your AppSheet account.

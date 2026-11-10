---
fonte: https://help.asana.com/s/article/saml-group-mapping-and-scim-interaction?language=en_US
baixado: 2026-11-10
---

# SAML group mapping and SCIM interaction

For customers who use an automatic provisioning job via SCIM and plan to use SAML Group Mapping for licenses, we **suggest having two different Asana applications in their IdP**. Deploying two separate applications for Asana — one for Single Sign-On (SSO) and another for System for Cross-domain Identity Management (SCIM) — can help manage access and user identities in a large organization. By doing so, authentication mechanisms are isolated from provisioning mechanisms.

## Benefits

- Users removed from the “eligible for a license” group get deprovisioned from Asana via SCIM instead of the configuration with a single application. 
- Provisioning jobs are much shorter, given the reduced number of users to provision.

> Changing the group assignment from claimable to unclaimable will **not** deprovision users. Users must be deprovisioned via the Asana admin console and then be removed from the IdP security group.

## Change management

When going from 1 application with both SSO and SCIM enabled to 2 applications, one for SSO and the other for SCIM, make sure to:

- Maintain the existing application for SSO to avoid disrupting the already authenticated sessions of your employees.
- Make sure to make ONLY the SSO application visible to your users in their Dashboard ([Okta documentation](https://help.okta.com/oag/en-us/content/topics/access-gateway/add-app-saml-pass-thru-hide.htm))
- Turn off the provisioning configuration from the SSO application.
- Enable the provisioning configuration on the SCIM application and assign the “SCIM-Asana-Application” to the group of users eligible to claim a license.
- Once you have enabled SGM, then proceed add all users to SSO application

[](https://forum.asana.com/c/forum-en/tips/6)

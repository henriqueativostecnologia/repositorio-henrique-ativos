---
fonte: https://help.asana.com/s/article/enterprise-key-management-ekm?language=en_US
baixado: 2026-11-10
---

# Enterprise Key Management (EKM)

**Available on the Asana [*Enterprise+*](https://asana.com/enterprise) tier. Visit our [*pricing page*](https://asana.com/pricing) for more information.**

Enterprise Key Management (EKM) is an Asana feature that allows you to encrypt your data with keys that you own. EKM affords you more control over your data by putting the keys in your hands, with visibility into how the keys are being used, all while you continue to get the most out of Asana.

Asana Enterprise Key Management integrates with your encryption keys which you create using [AWS KMS (Key Management Service)](https://aws.amazon.com/kms/ "AWS KMS (Key Management Service)"). Your keys will be used to encrypt your data across Asana’s data layer: data residing in [RDS (Relational Database Service)](https://aws.amazon.com/rds/ "RDS (Relational Database Service)"), Attachments residing in S3 and Search.

## EKM eligibility requirements

Enterprise Key Management can be provisioned for organizations where there is a minimum 100-seat Enterprise+ subscription in place.

## How EKM Works

EKM at Asana works by encrypting your data in all of our production datastores. At a high level, this is how EKM works:

- You set up AWS KMS keys specific to Asana EKM in your own AWS account. These keys should **only** be used for EKM at Asana, and not for any other purpose.
- You grant Asana access to these keys.
- For domain data in RDS, Asana uses these keys to encrypt your data and encrypt your database backups.
- For your attachments stored in S3, Asana will create a new AWS account for isolation. We’ll then create an S3 bucket set up with encryption using your keys.
- For your data residing in OpenSearch, Asana will create a new OpenSearch instance, set up with encryption using your keys.
- Your key is solely your responsibility; Asana is not liable if you lose, disable, or delete the key or any data under your encryption management process.

Note that some features and elements of the service are not compatible with EKM will remain unencrypted. Currently, these exceptions are:

- Email addresses
- Third Party Services and related metadata
- Videos created within the service

The following elements of the service are shared unencrypted with Asana subprocessors to enable provision of the services:

- End users’ names and email addresses
- Team names

> If you are interested in EKM please contact your sales representative.

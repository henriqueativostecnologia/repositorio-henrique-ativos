---
fonte: https://help.asana.com/s/article/asana-sandboxes?language=en_US
baixado: 2026-11-10
---

# Asana Sandboxes

**Available on the Asana [Enterprise+](https://asana.com/enterprise) tier.**

**Visit our [pricing page](https://asana.com/pricing) for more information.**

Sandboxes are a safe testing environment where super admins can set up new features and processes to try them out without putting your data at risk.

A sandbox provides a separate and empty space where you can experiment with different features and integrations before adopting them in your production environment at scale.

You can use sandboxes to trial new functionalities (such as testing AI), onboard and train new users, and evaluate new apps, all without affecting the production environment.

> The production environment and its sandbox exhibit identical performance, speed, and security levels.

## Sandboxes specifications

### Number of sandboxes

Every Asana Enterprise+ [organization](https://help.asana.com/s/article/managing-an-organization?language=en_US) can have one sandbox.

### Best practices

Clear guidelines for sandbox usage should be established to prevent users from unintentionally starting work in a test environment.

If your production environment is deleted, we will also delete your sandbox environment.

## How to request a sandbox

Super admins can create a sandbox for their domain via admin console. To create a sandbox, navigate to the admin console, click **Sandboxes** from the sidebar and click **Create sandbox**.

## How to access your sandbox

Once your domain's sandbox is enabled, super admins can navigate to their profile icon and click **Sandbox**. From there, they can invite other users.

> We copy your administrative settings to your sandbox.

### Granting access to a sandbox

There are a couple of ways super admins can grant access to users their sandbox:

1.  Admins can manage members in a sandbox similar to managing [members in an organization](https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US). Navigate to your sandbox’s admin console, go to the **Members** tab, and click **Invite members**.
2.  [Invite members](https://help.asana.com/s/article/how-to-invite-team-members-to-asana?language=en_US) to projects or tasks directly to start collaborating.

## Testing with data

If you are looking to test with data, the self-serve method involves exporting a project from your production instance and importing it using the [Asana CSV importer](https://asana.com/apps/csv-importer) to the sandbox.

## Deleting a sandbox

Super admins can delete the sandbox.

#### To delete a sandbox, navigate to the admin console and follow these steps:

1.  From the sidebar, click **Sandboxes**
2.  Click the three dot icon next
3.  Click **Delete**

Once the sandbox is deleted all data, including configurations, applications, and users associated with the sandbox, will be erased. Please note this action is irreversible.

> Deleting your sandbox does not affect your production instance.

## Clearing data from a sandbox

The only way to clear all data from a sandbox is to delete it and create a new sandbox.

## Sandboxes for EKM customers

When you create a sandbox and your production domain is on Enterprise Key Management, the sandbox will not be managed by your existing AWS EKM keys. Your Sandbox's data will be encrypted using Asana's AWS KMS. [What is EKM](https://help.asana.com/s/article/enterprise-key-management-ekm?language=en_US)?

**Ready to get started? Reach out to our [Customer Support team](https://help.asana.com/s/article/how-do-i-get-support-from-asana?language=en_US) today.**

 

[](https://forum.asana.com/c/forum-en/tips/6)

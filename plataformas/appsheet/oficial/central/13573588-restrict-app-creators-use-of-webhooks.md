---
fonte: https://support.google.com/appsheet/answer/13573588?hl=en
baixado: 2026-11-10
---

# Restrict app creators use of webhooks

Restrict app creators use of webhooks as described in the following sections:

- [Prevent app creators from using webhooks](#prevent-using-webhooks)
- [Restrict webhook URLs](#restrict-webhook-urls)

## Prevent app creators from using webhooks

Prevent app creators from using webhooks in their apps by using the "Disallow webhook" policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To prevent app creators from using webhooks:

1.  Select **My account \> Policies**.
2.  Click **+ Organization Policy** or **+ Team Policy** to add an account or team policy, respectively.
3.  Select **Disallow webhooks** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `NOT([Type] = Webhook)`
6.  Click **Save**.

## Restrict webhook URLs

Restrict app creators to use only a specific set of webhook URLs, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To prevent app creators from using webhooks:

1.  Select **My account \> Policies**.

2.  Click **+ Organization Policy** or **+ Team Policy** to add an account or team policy, respectively.

3.  Select **Restrict Webhook URLs** from the **Policy Template** drop-down.

4.  Click **Next**.

5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `OR(`
    `  STARTSWITH([Url], "https://api.appsheet.com/api"`
    `  STARTSWITH([Url], "https://script.googleapis.com"`
    `)`

6.  Click **Save**.

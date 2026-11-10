---
fonte: https://support.google.com/appsheet/answer/17498317?hl=en
baixado: 2026-11-10
---

# Using the Bring Your Own Email (BYOE) Feature

In **September 2026**, AppSheet launched the Public Preview of Bring Your Own Email (BYOE). This initial phase enables AppSheet creators to send automation emails from a custom Workspace email address instead of the default **noreply@appsheet.com** sender address.

This highly requested capability strengthens automation email security and helps prevent emails from being flagged as spam.

This Public Preview includes:

- Ability for Workspace customers to send automation emails directly from their Workspace/Gmail addresses instead of [*noreply@appsheet.com*](mailto:noreply@appsheet.com).
- Additional enhancements including support for Gmail Display Names and Gmail Aliases are expected to roll out during this Public Preview.

Important Note: Support for non-Workspace accounts is planned for a second phase release in 2027.

**How to use BYOE**

Follow these steps to configure a custom sender address:

1.  Create or open an existing AppSheet [*automation (bot)*](https://support.google.com/appsheet/answer/11432969).
2.  Configure the bot step to **Send an email**.
3.  Under the **From** setting, click **Select an account**.
    Note: Accounts available to select must match the domain you log in with, or one of your org's owned domains.
    This option is not available for users who log in with an account with a public domain (for example, @gmail.com).
    BYOE Select Account
    If prompted, select **Authorize** to authenticate with your Workspace/Gmail account.
4.  Select the desired sender account from the dropdown list.
    Address Dropdown

    Note: While *noreply@appsheet.com* remains the default, using a custom email address is highly recommended.

&nbsp;

6.  Fill in the **To**, **Subject**, and **Body** fields.
    Email To Subject and Body
7.  Click **Save**.
8.  Trigger the automation by performing the configured app change [*event*](https://support.google.com/appsheet/answer/11445188#configure-app-event) or using the [*bot testing*](https://support.google.com/appsheet/answer/11432969?hl=en#test-bot&zippy=%2Cif-you-are-using-the-legacy-editor) feature.
9.  Once triggered, the automated email will be sent using the selected custom address.

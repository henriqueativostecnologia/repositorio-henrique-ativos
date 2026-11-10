---
fonte: https://support.google.com/appsheet/answer/15015105?hl=en
baixado: 2026-11-10
---

# Purchase AppSheet Enterprise Plus without a Google Workspace account

If you want to purchase an AppSheet Enterprise Plus subscription individually or on behalf of your AppSheet organization but don't have a Google Workspace account, you can sign up for [Cloud Identity Free](https://workspace.google.com/gcpidentity/signup?sku=identitybasic) and then complete the purchase in the Google Admin console. 

To purchase AppSheet Enterprise Plus without a Google Workspace account, do the following steps:

1.  Create an admin account using Cloud Identity Free:
    1.  Go to the [Cloud Identify Free sign-up page](https://workspace.google.com/gcpidentity/signup?sku=identitybasic).

        Cloud Identity Free wizard
    2.  Step through the instructions to [create your Cloud Identity account and first time admin user](https://support.google.com/cloudidentity/answer/7390066).
    3.  [Verify ownership](https://support.google.com/a/answer/60216) of the specified domain.
2.  Sign in to the Google Admin Console using the admin user account and [purchase AppSheet Enterprise Plus](https://support.google.com/a/answer/10447197).
3.  [Assign one license](https://support.google.com/a/answer/1727173) to your account (as the Super Admin).
4.  [Sign in to AppSheet](https://appsheet.com) and create an AppSheet account using the same account you just created.
    You should see **AppSheet Enterprise Plus** when you select **My Account**.
5.  To provision your users with AppSheet Enterprise, you have the following two options:
    - [Create Cloud Identity accounts](https://support.google.com/cloudidentity/answer/7332836) for your users and then [assign them an AppSheet Enterprise Plus license](https://support.google.com/a/answer/10569787) using the Google Admin console
    - Use [pooled licensing](https://support.google.com/appsheet/answer/14101111#pooled-licensing) to grant AppSheet Enterprise Plus licenses to any user from your Google Workspace [verified domains](https://support.google.com/a/answer/60216) when they sign in to AppSheet using any identity provider.
      **Note**: After this process is complete, all users from your domain that sign in to AppSheet consume an AppSheet Enterprise Plus license. See [How many licenses do I need to purchase for my subscription?](https://support.google.com/appsheet/answer/10105400#how-many-licenses)

**Known limitations of using AppSheet Enterprise Plus with Cloud Identity**

 

Cloud Identity Free doesn't come with access to Google Drive, Google Sheets, or other non-Google Admin services. As a result, certain features might not work as expected. For example, copying template apps will result in an error because Cloud Identity doesn't come with file storage. You can learn more about [defining alternative object stores](https://support.google.com/appsheet/answer/10106769?hl=en). You will still have access to apps created natively using AppSheet databases or any other data source you specify.

After purchasing AppSheet Enterprise Plus with Cloud Identity, it's possible to authenticate using non-Google identity providers (for example, Active Directory, AWS Cognito, Okta, etc.), however the enterprise license won't be automatically granted in AppSheet unless the user assigned the license authenticates through Google. Automatically granting enterprise licenses to users with non-Google identity providers requires the [team licensing model](https://support.google.com/appsheet/answer/14101111). Contact your [AppSheet Sales](https://workspace.google.com/contact/) representative for more information.

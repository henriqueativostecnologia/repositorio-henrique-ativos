---
fonte: https://support.google.com/appsheet/answer/10106382?hl=en
baixado: 2026-11-10
---

# Configure Google Cloud Storage as a cloud object store

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

The following steps involve downloading a [*service account key*](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) to the local file system. A service account key is like a password that grants the bearer full access to the service account. These steps should only be performed on a trusted device, and the downloaded file must be handled carefully to avoid accidentally exposing your GCP resources. The file should be deleted after setup is complete (or if setup is abandoned before completion), and you should take care not to leave it in a “recycle bin”. Please also ensure that your service account has only been granted the [*minimum roles and data access*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) required to use this feature. If you are hesitant to accept the risks of an exported key, consider using an [*alternative object store*](https://support.google.com/appsheet/answer/10106769).

Configure Google Cloud Storage as a cloud object store as described in the following sections:

1.  [Configure Google Cloud Storage as a cloud object store](#configure)
2.  [Create a service account in Google Cloud Console](#create-sa)
3.  [Add the cloud object store to your AppSheet account](#add-store-AppSheet)
4.  [Configure a table in an app to use the cloud object store](#configure-table)

### Configure Google Cloud Storage as a cloud object store

1.  Create a Google Cloud Storage (GCS) bucket and give it a name, such as **mytestbucket**.

    Create a GCS bucket named mytestbucket
2.  Choose a storage class, such as **Standard.**

    Choose Standard method to store your data
3.  Choose how to control access to objects.
    We recommend **Uniform** access, since your entire app will be accessing this storage bucket using the API credentials provided:

    Choose uniform access control to objects
4.  Choose the encryption method.
    We recommend using a **Google-managed-key**:

    Choose Google-managed key as the encryption method

## ****Create a service account in Google Cloud Console

Create a service account in Google Cloud Console. For more information, see [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts).

Create a service account

To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and creating a new dedicated service account for this connection even if you have existing service accounts.

Give your service account a meaningful name (the information is blurred out below):

Enter service account details.

Give your service account **Storage Admin** role:

Assign Storage Admin role to service account

To minimize unnecessary exposure of your Google Cloud Platform resources, we recommend following the [*principle of least privilege*](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) and not granting any other roles than the minimum required to use this feature.

**Important**: Create a key and store this safely somewhere (you will need it later):

Create a key for service account

The key should be of type **JSON.**

Download private key as JSON file

When you click **Create**, a JSON key file will be saved to your Downloads folder. Open the file with a text editor you trust so you can copy and paste the contents in the [*next step*](#add-store-AppSheet)

## ****Add the cloud object store to your AppSheet account

After you have your Google Cloud Storage configured, you are ready to add it to your AppSheet account:

1.  Sign in to [AppSheet](https://www.appsheet.com).
2.   Select your account from the account profile drop-down to go to the **My account** page.

    Access the My account page
3.  Click the **Integrations** tab.
4.  Click **Stores** in the left navigation.
5.  Perform one of the following steps:
    - To add an object store for use by your own account, click **New Cloud Store** under **Object Stores**, then click **Google Cloud Storage**.
    - To add an object store for your team member accounts, click **New Cloud Store** under **Team** **Object Stores**, then click **Google Cloud Storage**.
      **Note**: You must be a **Team Admin** to create a team object store.
6.  Complete the Add Google Cloud Storage integration dialog to create the new object store.
    - Provide a user-friendly name for this storage connection.
    - Copy the entire JSON file from above into the **Private Key JSON String** field.
    - Enter the exact bucket name.
7.  Click **Test Connection** to test the connection.
8.  Click **Save**.

At this point you no longer need the downloaded JSON file, and we recommend [*deleting it from the filesystem*](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#file-system) (and be careful not to leave it in a “recycle bin”). If for some reason you want to retain it, be sure to [*move it out of the Downloads folder*](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#temp-locations) to a secure location

## ****Configure a table in an app to use the cloud object store

After you have added a cloud object store to your account, you can configure a table in an app to use it.

1.  Sign in to [AppSheet](https://appsheet.com).
2.  Open the app in the app editor.
3.  Go to **Data**  and select the table you want to configure.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **Data \> Columns** and expand the table you want to configure.
4.  Click **Table settings** Table settings icon .
5.  In the **Store for image and file** drop-down, select the name of the object store that you set up for your account (such as, **GCSStore**).
6.  Save the change.

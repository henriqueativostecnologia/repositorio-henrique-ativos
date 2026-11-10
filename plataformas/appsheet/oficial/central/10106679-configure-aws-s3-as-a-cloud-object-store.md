---
fonte: https://support.google.com/appsheet/answer/10106679?hl=en
baixado: 2026-11-10
---

# Configure AWS S3 as a cloud object store

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

Configure AWS S3 as a cloud object store as described in the following sections:

1.  [Configure AWS S3 as a cloud object store](#configure)
2.  [Add the cloud object store to your AppSheet account](#add-store-appsheet)
3.  [Configure a table in an app to use the cloud object store](#configure-table)

Apps that use cloud object stores work without any difference in behavior. If your app is used to capture images, you will find that the images are saved to the AWS S3 bucket. The object names in AWS S3 are similar to file path names and use the same protocol. For clarity, they are always prefixed with the source name of the table that they belong to.

## ****Configure AWS S3 as a cloud object store

1.  Create an AWS bucket and give it a name, such as **mytestbucket**.
2.  Add an IAM user, such as **AppSheetS3User**.
3.  Record the API **access key** and **access secret** for the user.
4.  Give your S3 bucket a permissions policy similar to the following (change the **Id** and **Sid** properties to unique values):

&nbsp;

    {
    "Version": "2012-10-17",
    "Id": "Policy1490153669091",
    "Statement": [
     {
     "Sid": "Stmt1490216152721",
     "Effect": "Allow",
     "Principal": {
      "AWS": "arn:aws:iam:::user/AppSheetS3User"
      },
     "Action": "s3:*",
     "Resource": "arn:aws:s3:::mytestbucket/*"
     }
     ]
    }

## ****Add the cloud object store to your AppSheet account

After you have your AWS S3 bucket configured, you are ready to add it to your AppSheet account

1.   Sign in to [AppSheet](https://www.appsheet.com).
2.   Select your account from the account profile drop-down to go to the **My account** page.

    Access the My account page
3.  Go to **Integrations \> Stores**. 
4.  Perform one of the following steps:
    - To add an object store for use by your own account, click **New Cloud Store** under **Object Stores**, then click **AWS-S3**.
    - To add an object store for your team member accounts, click **New Cloud Store** under **Team** **Object Stores**, then click **AWS-S3**.
      **Note**: You must be a **Team Admin** to create a team object store.
5.  Complete the Add AWS-S3 integration dialog to create the new object store.
6.  Enter a name, such as **S3Store**. Choose the AWS Region, and provide the BucketName, such as **mytestbucket**, Access Key, and Access Secret.
7.  Click **Save**.

This page shows that your account has one configured cloud object store.

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
5.  In the **Store for image and file** drop-down, select the name of the object store that you set up for your account (such as, **S3Store**).
6.  Save the change.

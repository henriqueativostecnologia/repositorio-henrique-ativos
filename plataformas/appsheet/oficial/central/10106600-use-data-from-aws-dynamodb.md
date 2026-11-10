---
fonte: https://support.google.com/appsheet/answer/10106600?hl=en
baixado: 2026-11-10
---

# Use data from AWS DynamoDB

You can create apps in AppSheet with data from AWS DynamoDB. To do this, you need to first add a DynamoDB data source to your AppSheet account.

Table names that contain dashes (-) in an AWS DynamoDB are not supported for use with AppSheet.

## Add an AWS DynamoDB data source

To add an AWS DynamoDB data source to your AppSheet account:

1.  Go to the **My Account \> Sources** tab.
2.  Click **+ New Data Source**.
3.  Enter a name for the data source and click **Cloud Database** or **On-premises Database**.
    The Add database connection information dialog displays.
4.  Configure the database connection information. 
    - **Type**: Select **DynamoDB**.
    - **AWS region**: AWS region to use.
    - **S3 bucket**: S3 bucket that will be used for any images captured by apps using data from DynamoDB.
    - **Access key id**: Access key id to access the DynamoDB. Make sure to correctly paste in this information from your AWS account.
    - **Secret key**: Secret key to access the DynamoDB. Make sure to correctly paste in this information from your AWS account.

In order for AppSheet servers to access your data, both your network and DynamoDB must accept inbound connections to the database from AppSheet servers. See [Manage IP address and firewall information](https://support.google.com/appsheet/answer/10104492) for further information.

Once a DynamoDB data source has been added to your account, you can add its tables or views to any app. When you click **+ New Table** in your app, you can select the specific data source, and a table or view from that data source.

Once added to the app, AppSheet treats all data sources similarly. In fact, it's common and natural to combine data from a DynamoDB data source with data from other sources in the same app.

## Deal with loosely structured tables

Tables in DynamoDB can be loosely structured. Each "row" is a combination of property-value pairs and different rows can have different properties. However, an AppSheet app requires regularly structured data.

Do not try to build AppSheet apps with DynamoDB tables that have no regular structure. This won't work well. Likewise, do not build apps with tables that have serialized JSON objects or other such non-tabular data.

On the other hand, it's common to use DynamoDB to store regular structured tables with each row having some optional extra properties. AppSheet tries to deduce the extra properties by reading the first hundred rows of data. It also automatically includes five additional hidden columns when it extracts the column structure. This allows the app creator to change the column names to explicitly include properties that the system didn't automatically deduce.

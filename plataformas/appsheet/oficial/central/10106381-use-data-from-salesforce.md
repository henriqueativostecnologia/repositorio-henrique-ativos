---
fonte: https://support.google.com/appsheet/answer/10106381?hl=en
baixado: 2026-11-10
---

# Use data from Salesforce

You can use AppSheet to make mobile apps from Salesforce data. Typical apps combine data from Salesforce with data from other data sources.

## Before you start

The Salesforce account administrator must first install the AppSheet "package" for users on that Salesforce instance. To explain this simply, it informs your Salesforce instance that AppSheet is allowed to connect to your SalesForce data.

- if deploying into a Salesforce sandbox environment, use [this link](https://test.salesforce.com/packaging/installPackage.apexp?p0=04to0000000PxZ4)
- if deploying into a Salesforce production environment, use [this link](https://login.salesforce.com/packaging/installPackage.apexp?p0=04to0000000PxZ4)

**Note**: AppSheet communicates with your Salesforce instance using the Salesforce API. According to [Salesforce documentation](https://help.salesforce.com/apex/htviewsolution?id=000005705&language=en_US), this API is enabled automatically for the Enterprise, Unlimited, and Developer editions of Salesforce. Users of the Professional edition may need to purchase API access separately from Salesforce separately.

## Use Salesforce in AppSheet

**Notes**: 

- When using data from Salesforce, setting the initial value of the Row ID column to `UNIQUEID()` isn't required and has no impact. Salesforce sets the Row ID column using its own unique ID.
- [Polymorphic relationship](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_and_polymorph_keys.htm) columns aren't supported in AppSheet.
- If a Salesforce column is missing in the AppSheet column settings, this normally means that it's using a Salesforce data type that's not supported in AppSheet.

When creating an AppSheet account, you can use Salesforce as the authentication provider. In other words, your primary sign-in can be based on your Salesforce account.

If you have installed AppSheet in a sandbox instance of Salesforce, you will have to modify the URL used for sign-in. Use a URL that includes `sandboxInstance=true` in the query string. and make sure that it persists when adding the data source. For example: 

`https://www.appsheet.com/account/login`**`?sandboxInstance=true`**

`https://www.appsheet.com/Account/AddSource`**`?sandboxInstance=true`**`?returnUrl=%2FAccount%2FAccount%23_tab_acctSources`

Note that you can do this when you sign in from the browser and it will work in the emulator or full-screen browser environment. However, the mobile app will only work against a production or developer instance of Salesforce.

To add your Salesforce account as a data source to your AppSheet account:

1.  Go to the **My Account \> Sources** tab.
2.  Click **+ New Data Source**.
3.  Enter a name for the data source and click **Salesforce**.

You'll be prompted to sign in to your Salesforce instance via the  OAuth process supported by Salesforce.

Once a Salesforce data source has been added to your account, you can add existing tables to any app. When you choose **+ New Table** in your app, you can select the specific data source, and a table from that data source.

Once added to the app, AppSheet treats all data sources similarly. In fact, it's common and natural to combine data from a Salesforce data source with data from other sources in the same app.

**Note:** Salesforce does not allow storing just time data with no date component; only the `DateTime` type is supported. If you are using the Salesforce connector for your application, be sure to use the `DateTime` datatype instead of `Time`, or you will receive a JSON parser error.

## Copy template apps to Salesforce

AppSheet provides a gallery of standard template apps that are meant to work uniformly across data sources and authentication providers. It's common for app creators to make a copy of a sample app and modify the copy to suit their needs. While the template app data can be copied to a Salesforce data source, there are some limitations. Each of the tables in the template app is created as a custom table in Salesforce. However, because of the naming conventions enforced by the Salesforce platform, all custom object and field names will be prefixed by `appsheet_` and suffixed by `__c`. This can potentially cause errors in the template apps when there are formulas that use the names of tables and columns. These errors will need to be manually corrected.

## Save images to Salesforce

AppSheet treats image and file columns in a special way. When your AppSheet app captures and saves an image or file, AppSheet creates a new file on the provider's file system for each image or file, and writes the image or file data to that file. It then places the name of this file into the image or file column in your Salesforce table. The files will be saved in a subfolder of your account's default folder path (usually `/appsheet/data/appName`). You can view and change the default folder path in your account page under the **Settings** tab.

## Use images and files from Salesforce

Some Salesforce data (such as Leads) include a `PhotoUrl` column. If you want these photos shown within the app, they need to be accessible publicly. To do so, you must enable* ***External Sharing Model** in your Salesforce account. Do so via the **Sharing Settings** control pane in Salesforce, as shown below.

Sharing Settings pane in Salesforce

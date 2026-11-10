---
fonte: https://support.google.com/appsheet/answer/10106380?hl=en
baixado: 2026-11-10
---

# Use data from an OData feed

**Note: **This is a preview release of OData connector. See [Track and manage feature releases](https://support.google.com/a/topic/1227580). Preview offerings are intended for use in test environments only. This feature is not recommended for use in production apps. For questions or assistance with this feature, contact  [AppSheet Support](https://www.appsheet.com/Support/Contact).

Compared to on-premises software, cloud computing offers several advantages, including regular updates and releases, reduced and flexible costs, and streamlined IT management. However, as more business applications migrate to the cloud, integrating with an ever growing number of third-party SaaS applications becomes increasingly time-consuming. In many cases, you and your company must spend a lot of time and effort to free your business data from the physical silos of on-premises servers, only for it to be locked up again in virtual silos in the cloud that are fenced by esoteric APIs.

The Open Data Protocol (OData) aims to solve this problem. OData is an open protocol that allows the creation and consumption of queryable and interoperable REST APIs in a simple and standard way. Simply put, by setting up an OData feed, you will enable not just AppSheet, but any other third-party application that has an OData connector to access and work with your data. As a result, you only need to put in the work to set up a single data feed that would work with multiple cloud vendors, thereby saving time and money.

Currently, AppSheet supports [OData v3](https://www.odata.org/documentation/odata-version-3-0/) and [OData v4](https://www.odata.org/documentation/), although V4 is preferred. If your data resides in SAP, you can find detailed instructions on how to set up an OData v4 Gateway for your SAP data [here](https://help.sap.com/viewer/68bf513362174d54b58cddec28794093/7.5.9/en-US/1bbc4ecf0da94f358b1355fcbffa3363.html). Once your OData feed has been set up, you can add it as a data source to allow your AppSheet apps to use data from the feed.

## Add a new OData feed

To add an OData feed to your AppSheet account:

1.  Go to the **My Account \> Sources** tab.
2.  Click **+ New Data Source**.
3.  Enter a name for the data source and click **OData**.
    The Add database connection information dialog displays.
4.  Configure the database connection information. 
    - **OData Version**: Select the OData version from the drop-down.
    - **OData Service Root URL**: Enter the URL for the root of the OData feed service.
    - **Username**: Enter the username of the database user.
    - **Password**:Enter the password for the database user.
    - **SAP Gateway**: Select whether the OData data source is an SAP Gateway.
    - **Require Cross-Site Request Forgery (CSRF) Token**: Select whether CSRF is required.
5.  Click **Test** to test the connection details.
6.  After a successful test, click **Authorize Access** to save the data source in your AppSheet account.

Add OData connection information dialog

## Common issues

As you add your OData source to your AppSheet account, there are a number of common issues that you should take note of:

**Incorrect service root URL:** As the name suggests, the service root URL identifies the root of your OData feed. If the root service URL is incorrect, AppSheet will not be able to connect to the feed. Here's a rule of thumb that will help you quickly identify the root URL of your data feed: every single URL endpoint in your OData feed must start with the root URL. As such, if the URL that you provide in the connection information contains components that do not exist in other URLs in your OData feed, it is most likely an incorrect root URL.

**Missing or incorrectly implemented metadata endpoint:** Your OData feed must contain a metadata endpoint that is implemented according to the OData v3 or v4 specifications. AppSheet relies on the metadata endpoint in order to explore and identify tables (or "entity sets" in OData parlance) in your feed. If the metadata endpoint is missing, or is not correctly implemented according to the OData specifications, AppSheet will not be able to connect to your OData feed.

**Pagination:** If the tables in your OData feed contain more than a few hundred rows each, we highly recommend that you implement pagination in your feed to ensure that AppSheet can retrieve all of the rows. The pagination must be implemented according to the OData specifications in order to work correctly with AppSheet. Also, you should experiment with different page sizes to find a page size that is optimal for performance. For instance, if one of your OData tables contains 10,000 rows, but the page size is only 100 rows, AppSheet will need to send 100 requests in order to fetch all of the data in the table. By increasing the page size to 1000, you can reduce the number of requests by an order of magnitude, thereby reducing the app's sync time, .

**Authentication:** Different OData feeds might implement different authentication mechanisms. As recommended by the OData [specifications](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html#_Toc406398367), AppSheet currently only supports Basic Access Authentication, or Basic Auth, in order to achieve "the highest level of interoperability with generic clients". Because the authentication credentials are included in every request header in Basic Auth, AppSheet requires that the connection be established over secure HTTPS. If your OData feed is not secured with HTTPS, AppSheet will not be able to connect to it.

## Save files created in the app

OData feeds differ from the rest of our cloud-storage providers in that they do not have a file system. This leads to a change in AppSheet behavior when saving files (like images and documents). If the app has to capture photographs, they are normally stored in a folder next to the source of data in cloud storage. In the case of an OData table, image and document files are stored in the main cloud file system associated with the app creator's primary AppSheet account (typically Google Drive/Dropbox/Office 365/Box). The files will be saved in a subfolder of your account's default folder path (usually `/appsheet/data`). You can view and change the default folder path in your account page under the **Settings** tab.

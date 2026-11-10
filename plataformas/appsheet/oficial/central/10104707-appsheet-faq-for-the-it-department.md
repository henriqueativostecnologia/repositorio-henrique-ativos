---
fonte: https://support.google.com/appsheet/answer/10104707?hl=en
baixado: 2026-11-10
---

# AppSheet FAQ for the IT department

AppSheet frequently asked questions (FAQ) for the IT department.

## Architecture FAQ

## How are AppSheet apps created?

Apps are created on the AppSheet website. Each app is based on one or more "tables". It’s often the case that each table tied to a spreadsheet, but other forms of structured data can be used instead. The rest of the app is defined via configuration options. There is no code involved, so apps can be created in minutes.

## How are AppSheet apps distributed?

Apps are distributed by sending an [install email to desired users with an install link](https://support.google.com/appsheet/answer/10104983). Users open the install email on a mobile device, click on the install link, and can install the apps instantly.

## What is the high-level architecture of AppSheet?

Each mobile app is based on structured backend data, typically a spreadsheet hosted on a cloud storage system like Google Drive, Dropbox, or Office 365. On the mobile device, a copy of the data is cached locally in order to permit offline operation. Whenever changes are made in the app, or when the users explicitly choose to sync the app, the [changes from the app are moved to the backend spreadsheet and vice versa](https://support.google.com/appsheet/answer/10108301). All communication between the app and the backend data happens through the cloud-hosted AppSheet web service. 

## Where is AppSheet hosted?

AppSheet's web service is hosted on Google Cloud's web hosting infrastructure.

## Can AppSheet be hosted on-premise within the company?

AppSheet apps can run from on-premise data, but the AppSheet platform is hosted in the cloud. It is not an on-premises service.

## Is AppSheet reliable?

The AppSheet web service is highly reliable with 99.99% monthly uptime. The reliability derives from both the redundant cloud architecture as well as the reliability of the underlying Google Cloud infrastructure services. The greatest source of reliability concerns for a mobile app stem from [connectivity issues](https://support.google.com/appsheet/answer/10105762). AppSheet is explicitly designed for environments with bad or intermittent connectivity, and the data synchronization technology handles various kinds of failures seamlessly without data loss.

## Is each app separately deployed via the iOS or Android app store?

No. Mobile apps run on the device within a common "host" app called AppSheet. This host app is already available in the iOS and Android app stores. This allows any new app to be [instantly deployable](https://support.google.com/appsheet/answer/10104495).

## Data Architecture FAQ

## What sources of data can AppSheet access?

AppSheet apps can access spreadsheet data from Google Drive, Office 365, Dropbox, Box, and Smartsheet. More data sources are being added actively. AppSheet also supports connectors to Salesforce and SQL databases for Enterprise subscription plans.

## Do we have to use data in a spreadsheet?

AppSheet is meant for non-developers to easily build apps, which is why we have emphasized access to spreadsheets. We also support more traditional enterprise data sources for Enterprise subscription plan app creators.

## Can you connect to our corporate database or resources behind a firewall?

Yes. [Google Cloud Integration Connectors](https://cloud.google.com/integration-connectors/docs/overview) let you expose your enterprise data in different applications and integrations, including AppSheet. The connections you create in Google Cloud can be used as data sources in AppSheet. See [Overview of Integration Connectors with AppSheet](https://support.google.com/appsheet/answer/16178487).

This is a **preview release** of Integration Connectors with AppSheet.

## Mobile Platform FAQ

## What mobile platforms do you support?

AppSheet apps run on iOS and Android devices. Check [Apple App Store](https://apps.apple.com/us/app/appsheet/id732548900) and [Google Play](https://play.google.com/store/apps/details?id=x1Trackmaster.x1Trackmaster) for recommended versions. Using a lower version than what is recommended can cause subtle bugs or performance problems in certain scenarios.

## Can the apps run in a browser?

Yes. While we primarily focus on mobile devices, many AppSheet customers also run their apps in a web browser, usually within an iframe. In fact, on unsupported mobile platforms like Windows Phone, we recommend running within a browser. Most of the app functionality is supported in a browser (except offline image caching and barcode scanning). We recommend a modern browser, and the apps work best on Chrome. AppSheet does not work on IE versions lower than V10.0.

## Functionality FAQ

## Do you support feature X?

We add features to AppSheet at a rapid rate; it isn't uncommon for us to unblock a customer by adding a new feature in a couple of weeks. There is an active [AppSheet community](http://community.appsheet.com/) that drives and prioritizes our feature investments. All features are initially announced on the community for trial and added to the Appsheet documentation.

## Security FAQ

## Where can I learn about the security model?

We have written a short article describing different aspects of the [AppSheet security model](https://support.google.com/appsheet/answer/10105078). We're happy to share further details with IT experts.

## What data does AppSheet store on its servers?

The AppSheet service records user signup information and access tokens in order to be able to access backend spreadsheet data. The definition of each app is also stored. [The actual data used by each app is not copied to the AppSheet service](https://support.google.com/appsheet/answer/10108551). Instead, it passes through the AppSheet service as it flows between the mobile device and the backend cloud storage system chosen by the customer.

AppSheet does record usage events and also logs data updates in order to support diagnostics, debugging, analytics, and billing. We're introducing an option for customers to limit the duration for which this information stays in the system logs.

## Is AppSheet SOC compliant?

Yes. AppSheet is SOC 2 Type 2 audited. Our SOC Report is available to customers under NDA and upon request. See [SOC 2](https://cloud.google.com/security/compliance/soc-2).

## Support and Services FAQ

## What is the response time for product support questions?

Contact [AppSheet Support](https://support.google.com/appsheet/gethelp) with your support questions. Most issues are responded to within hours. We also offer prioritized support for customers in higher subscription plans.

The [AppSheet Community](https://www.googlecloudcommunity.com/gc/AppSheet/ct-p/appsheet) is also available to find answers, ask questions, suggest features, and connect with other app creators.

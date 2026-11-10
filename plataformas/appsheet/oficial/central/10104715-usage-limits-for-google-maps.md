---
fonte: https://support.google.com/appsheet/answer/10104715?hl=en
baixado: 2026-11-10
---

# Usage limits for Google Maps

AppSheet uses the Google Maps API to geocode address values --- for example, to convert a street address into a high-precision lat-long location that can be shown on a map.

Each AppSheet account has a monthly usage limit on the number of addresses that receive high-precision geocoding. This limit is **1000 addresses geocoded per month**. The vast majority of our customers fall within this usage limit.

If an account exceeds this limit, the account owner will be alerted using email. If you receive an alert, you can increase your limit by setting up your own Google Maps account at [https://cloud.google.com/maps-platform/pricing/](https://cloud.google.com/maps-platform/pricing/). Google gives each Google Maps account \$200/month of free credit, which is equivalent to 40,000 addresses geocoded per month.

To use your Google Maps account with AppSheet, copy the **Browser access key** in the **Credentials** section and add it to your AppSheet account in the **Account \> Integrations \> App Services** pane. Apps in your AppSheet account will now use your Google Maps account and will not have usage limits applied.

**Note**: You can turn on or off maps and geocoding in your app using the **Allow maps and geocoding** setting when [configuring external services](https://support.google.com/appsheet/answer/10104999#external-services).

---
fonte: https://support.google.com/appsheet/answer/10104788?hl=en
baixado: 2026-11-10
---

# Errors and retry

Mobile apps must account for failure to send updates to the backend. There are multiple reasons for failure:

- Your mobile device may have connectivity issues.
- We hate to say this, but AppSheet's servers could have occasional connectivity or downtime issues.
- Your cloud file system (eg: Google Drive) can have occasional connectivity or downtime issues.

These are the realities of working in a mobile-to-cloud environment where changes from the app have to be recorded at the backend cloud service. Yet any data captured by the app should never be lost.

AppSheet accomplishes this using three basic mechanisms (none of which you need to do anything to configure-- it just happens automatically):

1.  All changes are recorded locally on the device. Even if the device shuts down and restarts, the changes are still available. Of course, if the device is lost or destroyed before you sync, those changes are gone forever.

2.  When data is synced from the app, it travels to the AppSheet backend, and then on to the backend spreadsheet. At this point, the acknowledgment of success has to flow all the way back to the mobile app. If this does not happen in a timely fashion, the user sees an error message. Importantly, the change is queued up for a subsequent retry. If the user syncs again, the change gets sent again.

3.  Of course, now we could have the situation where the same change is attempted multiple times (because the success acknowledgment may have failed to reach the app even if the update was successfully applied). All AppSheet updates are designed to be *idempotent*--that is, you can apply them repeatedly without a change in behavior.

There is one other situation where errors occur: when the app creator changes the app definition by adding or removing columns, but some user of the app still has the old version of the app and has un-synced updates on that app. Unfortunately, when there is a structure mismatch between the updates and the app definition, the updates fail. Retries will continue to fail. More details on handling this situation are provided in [Errors and warnings during sync](https://support.google.com/appsheet/answer/10105777).

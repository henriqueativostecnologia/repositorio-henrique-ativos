---
fonte: https://support.google.com/appsheet/answer/10105762?hl=en
baixado: 2026-11-10
---

# What if I lose connectivity?

If you expect your app to be offline for any non-trivial period of time, we strongly recommend configuring the app to indicate that it should work offline. AppSheet has platform features that explicitly handle this scenario.

However, even for apps that have not enabled this feature, AppSheet is designed to work through transient connectivity failures. Mobile apps work in occasionally connected environments, and network failures do occur.

- All changes are made locally and are queued up to send over the network when you choose to Sync.
- During Sync, if any changes fail to be propagated, they are retried. Our system is designed so that the changes are *idempotent* - this means that even if we mistakenly try to apply the same change repeatedly, the result is still sensible.
- You can keep using the app until you get to a location with reliable connectivity and successfully Sync your changes.

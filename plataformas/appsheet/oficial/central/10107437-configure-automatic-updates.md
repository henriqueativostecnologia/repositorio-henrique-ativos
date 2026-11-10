---
fonte: https://support.google.com/appsheet/answer/10107437?hl=en
baixado: 2026-11-10
---

# Configure automatic updates

When [configuring offline mode](https://support.google.com/appsheet/answer/10107724#configure-offline-mode), if you enable **Automatic updates** in the **Sync: App to Cloud** section, there are two things that happen: 

1.  When a user makes a change locally, the change starts being pushed back to the server. If the device is connected, sending will be attempted; if updates fail it will take longer. When working normally, this happens immediately. 
2.  It takes about 30 minutes to read back the latest data from other users' changes. Changes are applied to a particular user's app when they navigate away from the place where the change was made. The 30-minute timeframe exists so as to mitigate the amount of work for the server. 

**Automatic updates **is enabled by default. 

Sync: App to Cloud configuration properties

If you disable **Automatic updates**, you have to sync changes manually. If the updates aren't happening, that's a sign you may have an error and need to sync manually as well to figure out what's causing the issue.

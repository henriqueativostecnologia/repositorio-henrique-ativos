---
fonte: https://support.google.com/appsheet/answer/10105097?hl=en
baixado: 2026-11-10
---

# About API performance

AppSheet API performance is entirely dependent on the time required to do the following:

- Read the updated table. 
- Enforce the security filter for the updated table.
- Compute expressions for the virtual columns of the updated table. 
  If the virtual column expressions of the updated table refer to other tables, you must include the time to read those tables, enforce their security filters, and compute the expressions for their virtual columns.
- Perform automation rules that are triggered for the updated table.
- Re-write the updated table.

As a result, API performance is almost entirely application dependent. 

The best way to understand API performance is to use the [Performance Profiler](https://support.google.com/appsheet/answer/10104997). You can open the Performance Profiler by going to **Manage \> Monitor \> Performance Profile** in the editor. Then look at the REST API Invoke results in the Performance Profile.

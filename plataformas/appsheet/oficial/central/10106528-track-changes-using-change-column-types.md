---
fonte: https://support.google.com/appsheet/answer/10106528?hl=en
baixado: 2026-11-10
---

# Track changes using Change column types

In some apps, it is important to track when and where some data was changed. For example, in a field service app, it may be important to record when a certain field was changed.

AppSheet has a simple mechanism to track changes -- the Change column types. There are three Change column types: `ChangeTimestamp`**,** `ChangeCounter`**,** and `ChangeLocation`. These column types all have a set of shared characteristics:

1.  What triggers a change: Any change to any other column, any change to some specific fields or a single field, or changes to a specific field that result in one of a known set of values

2.  What should happen when such a change is detected: Increment a counter (`ChangeCounter`), set a timestamp to the current time (`ChangeTimestamp`), or record the current location (`ChangeLocation`) 

## Get started 

Check out the [Change Columns](https://www.appsheet.com/templates/Keep-track-of-when-columns-change?appGuidString=8a1572da-c548-418c-8767-a04482f2f7ed) sample app that demonstrates how to keep track of changes to columns using the Change column types.

## ChangeCounter Update Mode setting

The `ChangeCounter` **Update Mode** setting controls how the counter increments when data changes occur.

- **Accumulate** (default): In this mode, the counter increments by 1 per row update when at least one qualifying change occurs. In other words, it counts how many times a row has changed in a way that triggered the counter. An individual row update might occur through a single save of a form, a single [Quick Edit](https://support.google.com/appsheet/answer/10106609) in a detail view, or a single [action](https://support.google.com/appsheet/answer/10107706).
- **Reset**: In this mode, the counter resets to its initial value at the beginning of each update and counts the total number of changed columns that triggered the counter within that update. This mode makes it easy to detect that a particular change occurred during a given update, which is useful for setting up automations that only fire when a specific change occurs.

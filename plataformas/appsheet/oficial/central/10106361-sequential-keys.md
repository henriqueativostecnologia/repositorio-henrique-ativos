---
fonte: https://support.google.com/appsheet/answer/10106361?hl=en
baixado: 2026-11-10
---

# Sequential keys

Is it possible to create sequential keys for each record?

The brief answer is **No**. 

Some customers ask for the ability to create sequentially increasing keys. They ask that these keys accurately reflect the order in which the records were created. As described in [What is a key?](https://support.google.com/appsheet/answer/10106672) AppSheet does not support sequentially increasing key values. The same is true for sequentially increasing values in a column that is not a key.

This article explains the technical rationale for this limitation. It's technically impossible in a system that combines multiple distributed users who are allowed to concurrently add records and who can add records while offline.

It's only possible (but may not be fast) if the system is willing to relax (that is, give up on) one or more of these requirements. AppSheet does not implement any of the following design alternatives. They are described here primarily to explain what other design choices could have been made instead.

1.  Monotonically increasing keys, such as 1, 2, 3 ... or 1000, 1001, 1002, ...
2.  Keys that accurately reflect the order in which the records were first created by the user.
3.  The ability for two or more users to add records concurrently.
4.  The ability for users to add records while offline.

For example, the system can achieve a monotonically increasing key through a central locking scheme if it gives up the ability to add records while offline.

If the system gives up having the record number increase strictly monotonically and reflecting the exact order in which the records were created, then it can give each app user a block of numbers that only that specific user uses for newly added record key values. The block of numbers reserved for each app user must be large enough so nobody runs out of preassigned numbers while working offline. The record number keys are no longer strictly monotonically increasing and they don't strictly reflect the order of creation, but they roughly reflect the order in which the records were added.

The system can assign monotonically increasing number keys to newly added records by having the backend assign the record number keys after the app synchronizes. The resulting record number keys reflect the order in which the newly added record first reached the backend, rather than the absolute time they were created by each app. This can lead to some complications because the app only knows the record's "real key" after it synchronizes with the backend. If the app adds a set of records that are related by key value, the app must assign the actual key values to each of the newly created records, and ensure he references between these records reflect the actual key values. The app can only do this after the actual key values are returned by the backend.

There are other design alternatives, but all of them involve trade-offs regarding which requirements are relaxed and how much cost/inefficiency is absorbed in order to achieve nearly monotonically increasing record number keys.

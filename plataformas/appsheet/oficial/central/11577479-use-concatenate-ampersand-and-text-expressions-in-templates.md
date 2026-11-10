---
fonte: https://support.google.com/appsheet/answer/11577479?hl=en
baixado: 2026-11-10
---

# Use CONCATENATE(), Ampersand, and text expressions in templates

This section describes how to use `CONCATENATE()` function and Ampersand (`&`) operator expressions in your email templates. For information about using text expressions in templates, see [Text expressions](https://support.google.com/appsheet/answer/10108184).

You can include `CONCATENATE()` functions or Ampersand (`&`) operators in your template to combine two or more values to yield a single text value.

An Ampersand operator is just a synonym for the `CONCATENATE() `function. When you specify an Ampersand operator in an expression, AppSheet converts that portion of the expression into a `CONCATENATE()` function. Using an Ampersand operator is simply a compact way of specifying the `CONCATENATE()` function.

For example, the following two expressions are equivalent:

    <<CONCATENATE("Time: ",[MeetingTime], " (Uses CONCATENATE)")>>
    <<"Time: "&[MeetingTime]&" (Uses &)">>

 

If you refer to a field in a `CONCATENATE()` expression, the value of that field is not formatted. Because AppSheet uses the `CONCATENATE()` function when combining two or more record key field values to yield the compound key value for the record, the resulting key value must contain the entire unformatted value of each key field.

For example, if the `CONCATENATE()` expression contains a `MeetingTime` time field that specifies `Ignore seconds "On"`, the time value is displayed in full; the **`Ignore seconds`** setting is not honored.

For example, the following:

    <<CONCATENATE("Time: ",[MeetingTime], " (Uses CONCATENATE)")>>
    <<"Time: "&[MeetingTime]&" (Uses &)">>

Results in :

    Time: 3:30:45 PM (Uses CONCATENATE)
    Time: 3:30:45 PM (Uses &)

 

You can force a field value to be formatted by enclosing the field value in a `TEXT() `function.

For example:

    <<CONCATENATE("Time: ",TEXT([MeetingTime]), " (Uses CONCATENATE)")>>
    <<"Time: "&TEXT([MeetingTime])&" (Uses &)">>

Results in:

    Time: 3:30 PM (Uses CONCATENATE)
    Time: 3:30 PM (Uses &)

---
fonte: https://support.google.com/appsheet/answer/10107395?hl=en
baixado: 2026-11-10
---

# Conditional expressions

Behavior depends on a set of conditions

When using expressions, some values depend on other values conditionally. Here are some examples of conditional statements:

1.  If you oversleep, then you're late to work.
2.  If you drink a lot of water, then you're hydrated, but if you don't, you're dehydrated.

In expressions, you can approach these conditional situations in a few ways:

- `IF(condition, then-expression, else-expression)`to choose one of the results based on whether the condition evaluates to `TRUE` or `FALSE`.
- `IFS(condition1, then-expression1, condition2, then-expression2, ...)` to provide a sequence of condition-value pairs that are evaluated left-to-right until one of the conditions is true.
- `SWITCH(expression, value1, result1, value2, result2, ..., default_result)` to choose one of the results based on the value of the expression.

Expressions may be used in various AppSheet features--[app formulas](https://support.google.com/appsheet/answer/10106437), [initial values,](https://support.google.com/appsheet/answer/10106437) [virtual columns](https://support.google.com/appsheet/answer/10106758) and [column constraints](https://support.google.com/appsheet/answer/10107948) ([`Editable_If`](https://support.google.com/appsheet/answer/10107954),  [`Required_If`](https://support.google.com/appsheet/answer/10106535), [`Show_If`](https://support.google.com/appsheet/answer/10106628), or [`Valid_If`](https://support.google.com/appsheet/answer/10107949))--to customize app behavior and provide your users with advanced functionality.

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

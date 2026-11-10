---
fonte: https://support.google.com/appsheet/answer/10104977?hl=en
baixado: 2026-11-10
---

# Limit users to their own data using security filters

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

A security filter is an optional [Yes/No](https://support.google.com/appsheet/answer/10107946) expression that is evaluated for each row in a table. For steps to configure security filters, see [Security filters: The Essentials](https://support.google.com/appsheet/answer/10104488).

When you use security filters, you typically use the user's email address, and possibly other data values, to limit the data shown to the app user, as follows:

1.  [Require user sign-in](https://support.google.com/appsheet/answer/10104975). After a user signs in, AppSheet knows the user's email address. You can then use the user's email address to filter the data shown to that user.
2.  Include a field in each record that identifies the owner of the record. Typically this field contains the owner's email address. When adding a new record to a table, you can use the [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) function in that field's Initial Value property to initialize it with the user's email address. See [Define app formulas and initial values](https://support.google.com/appsheet/answer/10106437).

To limit access by user email:

`[EmailColumn] = USEREMAIL()`

To limit access by user email domain:

`CONTAINS(USEREMAIL(), [EmailDomainColumn])`

To limit access by user email but allow any manager to have access, create a `Managers` table that contains the email addresses of all managers. Then specify a security filter like:

`OR(IN(USEREMAIL(), Managers[Email]), USEREMAIL() = [EmailColumn])`

To filter based on the `Department` name contained in the `Employees` table. The security filter would be:

`IN(LOOKUP(USEREMAIL(), Employees, Email, Department), LIST("Payroll","Personnel"))`

To filter the `Customers` table so that each sales representative sees only their own customers. If you have a separate `CustomersToReps` lookup table having columns `CustomerId` and `SalesRepEmail`, the security filter for the `Customers` table would be:

`IN([CustomerId], SELECT(CustomersToReps[CustomerId], [SalesRepEmail] = USEREMAIL()))`

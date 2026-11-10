---
fonte: https://support.google.com/appsheet/answer/10100703?hl=en
baixado: 2026-11-10
---

# Manage identical apps

To make an application that has different data for each user, you have two options. You can either create a separate app for each user, or you can make one app with only the information pertinent to each user.

## Option 1: Use multiple spreadsheets

Make app copies using multiple spreadsheets: copy the app repeatedly and switch it to a different spreadsheet for each user. This is simple and gives you a lot of control. You can make changes to each app if you want. Of course, it can be tedious if you have many apps to create and maintain.

## Option 2A: Use row filters with a single app

Use [row filters](https://support.google.com/appsheet/answer/10106308) for **a single app** using a single spreadsheet -- row filters can achieve a similar effect with a single app. Different users of the app can see different subsets of the data. In particular, consider adding slices in the Editor using the 'Matches the user name' or 'Matches the user email' condition to filter the right data to the right user. Then send the same link to each user.

## Option 2B: Use row filters with multiple apps

Use row filters for multiple apps using a single spreadsheet -- row filters can achieve a similar effect with multiple apps. You can slice the data as in the above example, but instead of using multiple slices, just use one slice per app per user. Then send each user their unique app's link.

## Build apps with different update permissions for different classes of users

You can also build multiple apps with the same data, but different update permissions for different classes of users, through [limiting them to particular tables, views, and actions](https://support.google.com/appsheet/answer/10104696).

---
fonte: https://support.google.com/appsheet/answer/10106580?hl=en
baixado: 2026-11-10
---

# Data: The Essentials

AppSheet enables you to create apps from your data as described in the following sections.

- [Get started: Prepare your Google Sheet](#quick-intro)
- [Prepare your data](#get-started-with-data)
- [Manage your data in AppSheet](#manage)

## Get started: Prepare your Google Sheets for use with AppSheet

Watch how to prepare your Google Sheets for use with AppSheet.
See also: [Best practices with Sheets and AppSheet](https://www.youtube.com/watch?v=tnH3hPQ644I)

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=Xu6WDdulLs0

## Prepare your data

To get the most out of AppSheet, it helps to organize your data in an app-friendly way. Once you understand the basic concepts described in this topic, your data will be easier to manage and your apps will be more powerful.

- [Basic concepts](#basic-concepts)
- [How data changes](#how-data-changes)
- [What tables do you need?](#what-tables)
- [Be smart: Don't repeat](#do-not-repeat)
- [Give each row a unique identity](#give-row-unique-identity)
- [Avoid lists](#avoid-lists)
- [Relationships between records](#relationships-between-records)
- [One-to-many relationships](#one-to-many)
- [Many-to-many relationships](#many-to-many)
- [Put data in your spreadsheet](#put-data-in-spreadsheet)

### Basic concepts

First, let's review the most basic concepts about data:

- [Data is made up of records](#data-is-records)
- [Tables are collections of records](#tables-are-collection-records)
- [Columns are the attributes of tables](#columns-attributes-records)

#### Data is made up of records

A record is stored as a single row in your spreadsheet. It is an individual piece of data in your app, and might describe an individual customer, specific job site, or single product.

What we’ll want to do is keep each type of record separate from the others. To do that, each type of record should have its own [table](https://support.google.com/appsheet/answer/10105821).

Customers, Job Sites, and Products tables

#### Tables are collections of records

A [table](https://support.google.com/appsheet/answer/10105821) is a collection of records of the same type. You might have a Customers table (like below), a Job Sites table, or a Products table. Think of tables as simulating things in the real world: people, objects, locations, events, etc.

Customers table with First Name, Last Name, and Phone \# columns

#### Columns are the attributes of records

The rows in each table share the same set of [columns](https://support.google.com/appsheet/answer/10106674). These columns are the attributes that describe the records: fields like **Name**, **Address**, **Date**, **ID**, and so on.

Each row is going to have its own values for each column, but the overall column structure determines the parameters and requirements of the table as a whole.

Think of a table like a form. A form asks the same set of questions of everyone who fills it out, but everyone has different answers. If you were making a table out of this form, each question would be a column, and each person’s answers would be in their own row.

Customers table with edits

### How data changes

The row data within the table is what changes. As you use your app, you might add a new Customer, change the address of an existing Customer, or remove an old Customer. In fact, almost everything an app does is done by adding, updating, and deleting rows. But the [column structure](https://support.google.com/appsheet/answer/10106674) remains the same.

### What tables do you need?

The first thing to do is figure out **what tables you need**. You'll probably have several tables, since you'll have different questions of different types of data.

A good way to create tables is to create a single spreadsheet for the app, then add a sheet (tab) for each table. Name the sheet after the kind of records the table contains, such as `Customers` or `Project Locations`.

For instance, a library app that keeps track of books would probably need a table of `Books` and a table of `Checkouts`.

Books and Check-Out tables

Next, figure out the **columns for each table**. What information is needed for each record? What questions need to be asked?

In this library app, the `Book` table will have columns for `Title`, `Author`, `Publisher`, and `Copyright` date. The `Checkouts` table will have columns for `Checkout` date, `Return` date, `Title`, `Patron` name, and patron `Email`.

Books and Check Out tables showing columns

### Be smart: Don’t repeat!

If you have a set of columns whose values will be repeated across many rows, you might want to take those columns and put them in their own table.

These column sets usually describe a person or place related to the current row. But imagine you had to update that information. You’d have to change it in every single related row, possibly making mistakes along the way.

It would be much easier to keep that information in one place. Fortunately, AppSheet lets you [reference rows from other rows](https://support.google.com/appsheet/answer/10106510), which we’ll get to in the next section.

Let's create a new table, `Patrons`, that will have the columns `Name` and `Email`. This way, you can update a patron’s information in one place instead of changing it in every `Check Out` row to which they're attached.

Patrons table has Name and Email defined and is referenced by the Check Out table

### Give each row a unique identity

It’s important that each row can be uniquely identified. One of the columns should be a unique identifier, or primary [key](https://support.google.com/appsheet/answer/10106672), that has a different value for each row.

Names and addresses stick out as obvious choices, but they aren’t always the best choice. Multiple people can have the same name, and addresses can change--that’s the reason you see seemingly random customer IDs and order numbers.

It’s not a bad idea to follow suit and give every table an ID column.

The `Patrons` table has a `ID` column as its primary key. That way, if I have two patrons named Alex Green, they won’t accidentally check out books on each other’s accounts. `Books` and `Check Out `will each get an ID column as their primary keys, too.

Patrons, Books, and Check Out tables all with ID column as key

### Avoid lists

Tables, like [spreadsheets](https://support.google.com/appsheet/answer/10099416), can only have one value per cell. You can’t pack in a whole list of records. For example, you might want to have a `Cats` column, but since you can’t list multiple cats in a single spreadsheet cell, you’ll need a workaround.

At first, you might think a good solution is to use multiple columns: `Cat 1`, `Cat 2`, `Cat 3`, and so on. But then you have a fixed number of cats, and it can be hard to add new columns later.

A better solution is to create a new [table](https://support.google.com/appsheet/answer/10105821). It may seem silly to create an entire table if all you want is a single piece of information in each row, but this option is much more flexible. You can connect rows in this new table to rows in other tables using reference columns.

New Cats table that can be referenced from the Friends table using referenced columns

### Relationships between records

If you have multiple tables, you probably want to connect them in some way. A row in one table will have a [reference](https://support.google.com/appsheet/answer/10106510) to a row in another table, or you might want to have a list of related rows. These relationships are created using a special type of column called a reference, or `Ref` for short.

A `Ref` column takes a row’s primary key as its value. If you name the column something like `Book`, AppSheet will automatically figure out it should contain a key to some row in the `Books` table. Then in the app, you’ll be able to link directly from a row to its related row and back again.

The `Check Out` table should have a `Title` column so that when you look at a `Check Out` row, it will have a link to the book from the `Books` table. Similarly, you can give it a `Patron` column so it can reference rows in the `Patrons` table.

Title and Patron columns in Check Out table reference Books and Patrons table, respectively

### One-to-many relationships

If you want to create a list of related rows, you’re in luck! AppSheet will automatically create a list of related rows.

If you want a record in my `Books` table to have a list of reviews, you need to reference the book from each `Review` record. Then when you look at a book in your app, you’ll see a list of related reviews.

Next, add a `Reviews` table. It’s going to have columns for `ID`, `Book`, `Reviewer`, `Star Rating`, and `Comments`. You don't need to add anything to the `Books` table: you'll see links to related `Reviewer` rows when you look at a book in the app.

Reviews table showing Book and Reviewer columns referencing Books and Patrons tables, respectively

### Many-to-many relationships

If you want two tables whose records each contains a list of records in the other table, you have hit upon a slightly more advanced topic. You can learn how to do this, and many other things besides, from a more general guide to data modeling or database design. The following aren't AppSheet-specific, but the same principles apply:

- [A Quick-Start Tutorial on Relational Database Design](https://personal.ntu.edu.sg/ehchua/programming/sql/Relational_Database_Design.html)
- [Introduction to Database Design](http://www.datanamic.com/support/lt-dez005-introduction-db-modeling.html)

### Put data in your spreadsheet

Now that you know how to organize your data, we have a few tips for how to set up your spreadsheet. See [5 Tips for Building Better Spreadsheets for your AppSheet Mobile Apps](https://appsheet.wordpress.com/2014/12/03/5-tips-for-building-better-spreadsheets-for-your-appsheet-mobile-apps/).

When you have data in your spreadsheet, make sure your column headers are **bold** so AppSheet will recognize them as headers.

Spreadsheet showing bold headers

Notice how those columns also have clear and specific names. This is much more helpful for you than naming your columns `Column`, `Column1`, and `Column2`. 

Make sure that the data type format is consistent through each cell in the column. New data should be added as new rows. AppSheet can only interpret new data as a row; if you add it as a column, it won't work.

Bottom line: make sure that AppSheet reads a single table as your main source of information. Avoid using unstructured data, multi-format columns, or data outside of a table.

##  Manage your data in AppSheet

Manage your data in AppSheet, as follows:

- Add and edit data in your app, as described in: 
  - [Tables: The Essentials](https://support.google.com/appsheet/answer/10105821)
  - [Columns: The Essentials](https://support.google.com/appsheet/answer/10106674)
  - [Manage data sources](https://support.google.com/appsheet/answer/10106309)
- Add and edit data slices, as described in [Slices: The Essentials](https://support.google.com/appsheet/answer/10106592)
- [Configure user settings](https://support.google.com/appsheet/answer/10106760)

Watch the following video for a high-level overview of the AppSheet data model. 

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=pk5nH8U16bo

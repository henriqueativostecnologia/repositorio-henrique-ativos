---
fonte: https://support.google.com/appsheet/answer/10104385?hl=en
baixado: 2026-11-10
---

# Advanced techniques: Horizontal scaling

Effective scaling for apps with large datasets can reduce sync times while maintaining a convenient user interface. When an app syncs, the data is copied from the database to the device, allowing the user to easily interact with the data inside the app. By default all data associated with the app will be synced when the app is initially loaded. The default setting is effective for apps with small to medium datasets, but will result in long sync times for very large datasets.

Horizontal scaling is a technique by which the app creator can structure how and when data is synced into the app. This is accomplished by breaking the data up into buckets. Bucket \#1 contains data the user needs to begin using the app. Bucket \#2 contains additional data based on what the user selects in Bucket \#1. This model can be scaled indefinitely with each bucket drilling down further based on the selection made in the preceding bucket.

To give an example, let’s consider an app that allows users to see a menu of desserts. To make things interesting, let’s assume our company offers a vast array of desserts totaling over 60,000 unique delicious choices. Loading the entire dataset will take some time. However, by thoughtfully breaking the data up into buckets, we can significantly reduce the sync time and improve performance.

#### Table Structure

## Workflow

I broke the tables up into three buckets based on the user experience I will create in my app. 

**Bucket 1**
When the user opens the app, they are taken to a home page where they can select the type of dessert. At this point, AppSheet has only synced the `Type` table. The user makes their selection and clicks **Go** to proceed.

Bucket 1 in the app enables users to to select type of dessert from Type table

 

**Bucket 2**
AppSheet loads all rows from the `Dessert` table where `Type` matches the user’s selection from Bucket 1. By using the initial filter, we have significantly reduced the sync requirements from the full 60,000.

Bucket 2 in the app showing only pies from the Dessert table

**Bucket 3**
AppSheet loads only the `Reviews` and `Recipes` associated with the subset of `Desserts` loaded in Bucket 2. This offers another significant reduction to the number of records loaded during the sync.

Bucket 3 including items from the Reviews and Recipes tables based on previous selections

## Implementation

[User Settings](https://support.google.com/appsheet/answer/10106760) and [security filters](https://support.google.com/appsheet/answer/10104488) are the tools in AppSheet that enable horizontal scaling.

User Settings are displayed as a Form view and allow users to make a selection and save the form. These values can then be accessed by formulas throughout the app.

Security filters are formulas that limit the data loaded during the sync. By creating a security filter based on the User Settings selected by the user, we are able to filter the data to only the `Type`(s) selected. The data that does not meet the filter criteria will not be included in the sync. 

Although security filters limit data access, they aren't a complete security solution. Users should protect sensitive data operations at the data source level. For more information about securing your data, see [Security: The Essentials](https://support.google.com/appsheet/answer/10105078).

**Example: Security filter used on Dessert table**

`= [Type ID]=USERSETTINGS("Type")`

**Example: Security filter used on Review table**

`= IN([Dessert ID], Dessert[Dessert ID])`

## Variant approach using slices

The implementation described above has a limitation where the user is not able to see any desserts until they select a `Type`. In some cases, you may want to allow your users to make their initial selection by searching on the full list of desserts. 

**Example: Updated User Settings to allow display of desserts**

Allow users to click Full Dessert List to view and select a dessert

Searching the entire dessert list presents a challenge because we want to have the full dessert list available, but we don’t want to load all the `Reviews` and `Recipes` associated with *every* dessert. We can solve this with [slices](https://support.google.com/appsheet/answer/10106592).

Slices are subsets of data. The subset can then be used throughout AppSheet in the same way as a data table. We can create a slice of the dessert table and apply a Row filter condition based on the Search Method chosen by the user. If the user filters by type, the slice will contain all desserts that match that type. If the user chooses to select a single dessert from the full list, the slice will contain only that single dessert. 

**Example: Filter expression for Dessert Slice**

`SWITCH(USERSETTINGS("Search Method"), "Type", [Type ID]=USERSETTINGS("Type"), "Full Dessert List", [Dessert ID]=USERSETTINGS("Dessert"), FALSE)`

The security filter for `Reviews` and `Recipes` will select only those rows where the `Dessert ID` matches what is in the slice.

**Example: Security filter used on Review and Recipe tables**

`= IN([Dessert ID], Dessert Slice[Dessert ID])`

**Example: Updated table structure**

## Auto-select based on user’s email

Another variant on this concept is to auto-select a subset of the data when the application loads. A common use case is to filter based on the signed-in user’s email. This is effective in situations where the user only needs to see records with which they are associated. 

**Example: Security filter for user’s email**

`= [mailColumn]=USEREMAIL()`

An additional performance improvement can be achieved by filtering child tables to only load data associated with the rows of the parent table that passed the `USEREMAIL()` filter. This can be done by checking if the Primary Key in the reference column of the child table matches a Primary Key of the filtered parent table. This can be done using an `IN() `statement such as the one below.

**Example: IN() statement to filter child table**

`= IN([Parent ID], Parent Table[Parent ID])`

For more information about applying security filters based on user’s email, see [Limit users to their own data](https://support.google.com/appsheet/answer/10104977).

## Partitioning

As mentioned in the [Approaches to data scalability](https://support.google.com/appsheet/answer/10104705) article, an app based on spreadsheets will receive limited performance improvement from security filters. This is because the entire spreadsheet must be read before the security filter is applied. When working with spreadsheets, [partitioning](https://support.google.com/appsheet/answer/10105383) is a powerful tool for both improving performance and avoiding maximum data size restrictions.

## Limitations

The limitation for horizontal scaling is the interface for updating User Settings. The user must access these settings from the menu. It is possible to set the User Settings view as the home page to prompt the user for an initial selection before entering the app. However, once the initial selection has been made, the user must return to User Settings from the menu to update their selection.

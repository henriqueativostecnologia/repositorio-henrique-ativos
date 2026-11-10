---
fonte: https://www.notion.com/help/boards
baixado: 2026-11-10
---

# Board view

Vídeo: https://www.youtube.com/watch?v=_efKZce3eDY

In this help doc

## Boards are helpful for showing items in a database as they move through stages of a process, or grouped by property.

[Jump to FAQs](https://www.notion.com/help/boards#faq)

------------------------------------------------------------------------

Board view groups your database pages by a specific property. Whereas kanban boards typically group to-do items by their status, board views in Notion can be grouped by status, assignee, priority, and more depending on what you need. They can also show you exactly what you want to see via filters, sorts, and custom database properties.

## [Create a board](https://www.notion.com/help/boards#create-a-board)

To add a board to your workspace:

1.  Create a new page in your workspace.

2.  Under `Get started with`, click the `•••` and then `Board`.

If you want to create an inline board view, type `/Board view` on any page and press `enter`.

## [Add board view to a database](https://www.notion.com/help/boards#add-board-view-to-a-database)

You can add a board to an existing database to view its data in that format. To do this:

1.  Click `+` next to the name of your database or the name of your current database view.

2.  Select `Board` from the dropdown menu.

By default, your board will be grouped by a status property if your database has one. Otherwise, your database items will be grouped by a select, person, multi-select, or relation property that’s in your database. If none of these properties exist, a new status property will be created in your database for you.

## [Edit your board's groups](https://www.notion.com/help/boards#edit-your-board's-groups)

### [Group by a different property](https://www.notion.com/help/boards#group-by-a-different-property)

If you want to group your board by assignee, for example, instead of status, you can change the property that your board is grouping by. To do this:

1.  Open the settings menu at the top right of your database → `Group`.

2.  Find and select the property you’d like to group by.

Let’s say you want to group by a property that doesn’t already exist in your database. For example, maybe you want to start assigning a priority to your tasks and organizing them by priority. You’ll need to add a new priority property. To do this:

1.  Open the settings menu at the top right of your database → `Edit properties`.

2.  Select `New property`.

3.  Find the type of property you want, like `Select`, and set your property up with a name and, if needed, options (like `P0`, `P1`, and `P2`).

### [Add a new group](https://www.notion.com/help/boards#add-a-new-group)

You might want to change the labels for each of the groups in your board view. For example, maybe you want to turn `In progress` into `Ongoing`, or you need a new `In review` status. You’ll need to edit the property itself to accomplish this. To edit a property:

1.  Open the settings menu at the top right of your database → `Edit properties`.

2.  Select the property you’re currently grouping by. Let’s say you're grouping by `Status` and want to add a new status option.

3.  Click into each status option that your database currently has and give your options a new name or color, or `Delete` them entirely. You can also select `+` next to your existing options to create a new one.

### [Add or change sub-groups](https://www.notion.com/help/boards#add-or-change-sub-groups)

In board view, you can add a second layer of groups, called sub-groups. This lets you further organize your database items within a group.

1.  Open the settings menu at the top right of your database → `Sub-groups`.

2.  Find and select the property you’d like to sub-group by.

## [Reorder columns and cards](https://www.notion.com/help/boards#reorder-columns-and-cards)

Switch up how your board is ordered with drag-and-drop.

- To rearrange columns, click and hold on a heading, then drag left or right.

- To move cards up and down or between columns, click, hold, and drag.

**Tip:** Board view columns are colored by default, but you can turn this off by clicking Group at the top right, and then toggling "Color columns".

## [Change card size](https://www.notion.com/help/boards#change-card-size)

Depending on how you want your board to look, you can choose large, medium, or small card sizes. Your choice is applied to all cards.

1.  Open the settings menu at the top right of your database → `Layout`.

2.  Click `Card size` and select an option from the dropdown.

## [Display images on cards](https://www.notion.com/help/boards#display-images-on-cards)

Dress up your board by adding an image or preview of your card's content.

1.  Open the settings menu at the top right of your database → `Layout`.

2.  Click `Card preview` and select from one of the following options.

    - `Page cover`: Will show the image you chose as your page's cover on your card.

    - `Page content`: Will show a preview of the page's content. If you have images on your page, the card will display whichever image comes first.

    - If you have a `Files & media` property in your database, you'll see the name of those properties in this menu. Your card will display whatever image files you’ve uploaded to these properties.

3.  You can also toggle `Fit image` on or off.

    - When turned on, the entirety of the image will fit within the frame of the card. You can hover over an image in a card and select `Reposition` to drag the image into the position you want.

    - When turned off, the image will be cropped to fill the entire card frame.

## [Display properties on cards](https://www.notion.com/help/boards#display-properties-on-cards)

You can choose which properties you want displayed on the front of your cards in your board. To do this:

1.  Open the settings menu at the top right of your database → `Property visibility`.

2.  Select `👁️` next to properties to show or hide them.

3.  Use **`⋮⋮`** to drag your properties in the order in which you want them to be displayed in your cards.

## [Hide columns](https://www.notion.com/help/boards#hide-columns)

1.  For the column you want to hide, click `•••` to the right of the heading.

2.  Click `Hide group`.

3.  Reveal hidden columns by opening the settings menu at the top of your database → `Group`. You'll see a list of visible and hidden columns.

## [Calculations](https://www.notion.com/help/boards#calculations)

To the immediate right of each column heading, you'll see a gray number. The default is for this to show the number of cards in each column, but you can change it to give you other information. 

Depending on the type of properties you have in your database, you’ll see some or all of the following calculation options:

- `Count all`: Gives you the total number of rows in the column.

- `Count values`: Counts the number of property values contained in the column. 

- `Count unique values`: Counts the number of unique property values contained in the column, omitting duplicates. 

- `Count empty`: Counts the number of rows that do not have a value in the column. 

- `Count not empty`: Counts the number of rows where the column is filled. 

- `Percent empty`: Gives you the percentage of rows that do not have the chosen property filled in. 

- `Percent not empty`: Gives you the percentage of cards that do have the property filled in. 

- `Earliest date`: If you have time-related properties in your table like `Last edited` or `Created time`, you can choose to show when the oldest row was edited or created.

- `Latest date`: Shows when the newest row was last edited or created.

- `Date range`: Shows you the time gap between the oldest and newest edit or creation time.

- If you have a `Number` property in your table, you unlock several other calculation options:

  - `Sum`: Shows the sum of the numbers in the column.

  - `Average`: Shows the average of the numbers in the column.

  - `Median`: Shows the median of the numbers in the column.

  - `Min`: Shows the lowest number in the column.

  - `Max`: Shows the highest number in the column.

  - `Range`: Subtracts the lowest number from the highest.

**Templates:** Here are some use cases for boards from our team and the Notion community:

- [Work Portfolio](https://www.notion.so/3ac78550a0ab43da8c649d18f5a57725)

- [Employee Onboarding](https://www.notion.so/a011205609eb4be59418edee4fa398f9)

- [Recruiting Pipeline](https://www.notion.so/458b529bfc09494ab69914e86e192e3f)

- [Roadmap](https://www.notion.so/6c53b191c9924fa89468f92fb3d430bf)

------------------------------------------------------------------------

## FAQs

How can I turn a full-page database into an inline database, or vice versa?

To change a full-page database into an inline database:

1.  Drag the full-page database from your sidebar into another page. It will become a sub-page of that page.

2.  Open the parent page, click the **`⋮⋮`** button next to the database sub-page, and select `Turn into inline`.

To change an inline database to a full-page database, drag an inline database block into your sidebar as a top-level page.

I don’t want my database pages to open on the side or in the center of my page. Is there anyway to open a database page in full-screen by default?

Yes! To do this:

1.  Open the settings menu at the top of your database.

2.  Select `Layout` → `Open pages in` → `Full page`.

Is there a way to add background colors to board cards?

Yes! Learn more about conditional color [here →](https://www.notion.com/help/database-properties#conditional-color)

Any way to group by a relation or formula property?

Not currently 😓 It’s a legit use case though, and definitely something we want to support in the future.

I have a "Done" column in my board that's getting a bit crowded. Can I archive these automatically?

We'd recommend hiding this column. You can do this by clicking the `•••` icon next to the column heading and selecting `Hide`. You can drag any completed tasks into this hidden archive by clicking and dragging your cards into that tag under `Hidden Columns`.

Still have more questions? Message support

## Contents

- [Create a board](#create-a-board)
- [Add board view to a database](#add-board-view-to-a-database)
- [Edit your board's groups](#edit-your-board's-groups)
- [Group by a different property](#group-by-a-different-property)
- [Add a new group](#add-a-new-group)
- [Add or change sub-groups](#add-or-change-sub-groups)
- [Reorder columns and cards](#reorder-columns-and-cards)
- [Change card size](#change-card-size)
- [Display images on cards](#display-images-on-cards)
- [Display properties on cards](#display-properties-on-cards)
- [Hide columns](#hide-columns)
- [Calculations](#calculations)

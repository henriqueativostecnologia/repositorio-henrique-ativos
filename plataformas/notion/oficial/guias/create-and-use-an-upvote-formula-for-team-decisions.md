---
fonte: https://www.notion.com/help/guides/create-and-use-an-upvote-formula-for-team-decisions
baixado: 2026-11-10
---

# Create and use an upvote formula for team decisions

## Using an upvote formula in a shared database gives teammates a voice and fosters company-wide transparency.

- Company-wide use
- Managers
- Organization

5 min read

A company Q&A with questions, who asked them, and who wants them answered.

------------------------------------------------------------------------

It’s important for teams of all sizes (remote teams in particular!) to ensure their employees’ voices are heard. That can be hard on a shared Zoom call with triple-digit attendees.

Whether it’s selecting the most urgent questions to discuss at the next all-hands meeting or an engineering team voting on which product feature should be next in line for development, an upvote formula in your database lets everyone play a role in decision-making.

This provides managers with transparency into what matters most to their team, so they can take their views into account when making big decisions. Creating a database for team-wide voting and decision-making helps individuals feel valued and included in the most important aspects of your product or your business.

The questions with the most upvotes get answered first.

## [How your team can use an upvoting system](https://www.notion.com/help/guides/create-and-use-an-upvote-formula-for-team-decisions#how-your-team-can-use-an-upvoting-system)

Think about all the times you’ve had teammates raise their hands to vote on something, or tried picking through feedback from a chat window or Slack thread. This upvote database comes in handy whenever you want people to suggest new ideas or share their opinions — and it might help you prioritize based on what your team’s voting on most.

Here are a few situations where teams will find upvotes useful.

- **Vote for questions to tackle at all-hands meetings** — All-hands meetings can get chaotic, especially as your organization grows. It can be tough to stay focused and cover what matters to your team. To prepare for the meeting, attendees can enter questions into a database, the entire team can vote on the questions, and those with the highest votes will get answered. You can even take notes directly inside the question pages, so that those answers can be referred back to later.

Everyone can ask questions to be answered at the next all-hands.

- **Decide which product feature to build next** — Your product team likely has tons of ideas for new features, and it’s important to have a database to record all these suggestions. Before deciding which features your team will build next, have everyone vote. This way, distributed teammates are accounted for, and it helps frame your discussion (instead of a free-for-all where you’ve got to go through every idea). You can even broaden the upvoting, allowing other teams across the organization to vote, leveraging their experience with users or potential customers.

Give your team a voice in which features you’ll build next.

- **Log user feedback** — Listening to what your users say can help you find ways to improve and solve problems. Create a database so your customer support team has a place to log feedback they receive from users. When another teammate encounters the same feedback, they can tag themselves, thus addressing the most frequent user issues.

Customer support teams can tag themselves in feedback from users to surface the most relevant problems.

- **Vote on branding decisions** — designers who’ve been immersed in a rebranding project for a while will appreciate some external input when it comes to making final decisions on which designs make the cut. When you’ve narrowed it down to a few options, you can create a [gallery database](https://www.notion.so/Galleries-91ff852bc42b4d26bd1e8d7b568844d2) showcasing all your designs, build in an upvote feature, and invite the rest of your organization to choose their favorites.

Designers can vote on their favorite typeface.

You can use an upvote to collect team sentiment and quickly organize or prioritize your work based on the votes. It helps foster communication and ensure that team members get the chance to have a say in what happens in your organization.

## [**How to create a database with an upvoting system**](https://www.notion.com/help/guides/create-and-use-an-upvote-formula-for-team-decisions#how-to-create-a-database-with-an-upvoting-system)

Here’s how to create your own upvote database for All-hands questions database, where team members submit and vote on questions to cover in upcoming meetings.

1.  Create a table database where you’ll add all the items you want people to vote on.

2.  Next, add a `Created by` property. This will automatically populate with the person who creates the database entry. You’ll see we’ve renamed this `Asked by` to show that this is who's suggesting the question.

3.  Add a `Person` property, and call it `Upvoted by`. People will tag themselves in this column to vote on ideas.

4.  Now add a `Formula` property, click on the property and select `Edit formula`. In the formula editor, you can paste the following:

`length(prop("Upvoted by")) /* or you can write this as: */`  
`prop("Upvoted by").length()`

This formula will add up the number of people tagged in the `Upvoted by` column and display that as a number.

Add an upvote formula property using this flow.

Tag yourself in the upvote column to vote for questions and bring those with the most votes to the top.

Learn more about formulas

When you use this formula, the default number of upvotes will appear as one, which assumes that whoever created the suggestion also votes in favor of it. Every time someone else tags themselves in the “Upvoted By” column, it will add one to the total count of upvotes.

Tag yourself in the upvote column to vote for questions and bring those with the most votes to the top.

## [Organize and customize your team’s database](https://www.notion.com/help/guides/create-and-use-an-upvote-formula-for-team-decisions#organize-and-customize-your-team%E2%80%99s-database)

It makes sense to sort your database so that the pages with the most votes are at the top. To do this, click `Sort` in the top right of the database and `+ Add a sort`. From the dropdown, choose `Upvotes` and select `Descending`.

Plus — you wouldn’t want already-answered questions to appear in your database. To help you focus on questions that need attention, add a `Select` property to assign tags such as “Answered” and “Unanswered.” Same goes for features you’ve built. You could assign `Select` properties for “Built” or “Next up” or “Being considered.”

Then, you could filter your database to only show questions that need answering. Click `Filter` in the database menu. From the dropdown, choose your `Status` property, select `is` and `Unanswered`. Now, answered questions won’t show up in this view, but they’ll still be safely stored in the database. Just be sure to assign “Answered” to questions you...answer.

Hide all answered questions and bring questions with the most upvotes to the top of your database.

Resources to create and use your upvote formula

- Find out more about Notion [databases](https://www.notion.so/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e) and [properties](https://www.notion.so/notion/Intro-to-databases-fd8cd2d212f74c50954c11086d85997e#6b755095caf3419fb544f2cc996fe926).

- An article to help you nail [formulas](https://www.notion.so/notion/Formulas-28f3f5c3ae644c59b4d862046ea6a541).

- Go through our [advanced Notion training](https://www.notion.so/guides/notion-training-advanced).

Templates where you can use an upvote formula

- [Company home](https://www.notion.so/templates/company-home)

- [Meeting notes](https://www.notion.so/templates/1-1-notes)

- [User research database](https://www.notion.so/templates/user-research-database)

Share this guide

------------------------------------------------------------------------

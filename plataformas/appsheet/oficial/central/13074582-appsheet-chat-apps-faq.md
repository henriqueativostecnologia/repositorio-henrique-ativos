---
fonte: https://support.google.com/appsheet/answer/13074582?hl=en
baixado: 2026-11-10
---

# AppSheet Chat apps FAQ

Find answers to your questions about AppSheet Chat apps.

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/13074582)

#### What can I do with this feature?

**AppSheet app creators** *can:*

- Deploy a Chat app in AppSheet using the Chat app builder UI with automatic or manual configuration
- Start from scratch, a template, or an existing app
- Share a Chat app with a limited group or their whole domain
- Trigger events based on Chat app interactions, like typing a slash command, adding a Chat app to a space, or removing it from one
- Send messages and app views to Chat spaces based on data change or schedule-based triggers

*In-domain Google* **Chat users** *can:*

- Install an AppSheet Chat app in Google Chat
- Navigate through an AppSheet app via Chat
- View your data in deck views, take actions on rows in detail views or create new rows using form views— all from Chat
- Control Chat App behavior using custom slash command and space event listeners— trigger an automation to run, shortcut to an app view, and more

#### What’s NOT in this release but is coming soon?

Here’s a few of the things we have planned for the (relatively) near future:

- Support for additional app views
- Additional column type support

#### Is this feature available to all AppSheet creators?

You must be a **Google Workspace user** to create Chat apps with AppSheet. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197). Be sure to sign in to AppSheet using your Google Workspace account.

#### What app views and column types are supported? What do they look like on Chat?

We currently support deck, form, and detail views, and most column types. You can find full information on what’s currently available [Summary of features supported for Chat apps with AppSheet](https://support.google.com/appsheet/answer/12917178). To request support for additional column types or other features, contact [AppSheet Support](https://www.appsheet.com/Support/Contact).

#### Do my AppSheet policies apply to my Chat apps?

Generally yes, but with some caveats: 

- Policies whose stage is set to “check on deployment” will apply when **deploying** the app, **not publishing the Chat app**. If changes that break policy are made post-deployment, pre-publication, they will not be blocked. 
- "Check when your user is using an app" policies will apply whenever a user interacts with a Chat app (@-mentioned, view menu card is clicked, a slash command is invoked, app data is being viewed or edited).

#### How do AppSheet permissions, data sources, access rules, etc. work for Chat apps?

Because a Chat app is, at root, just another deployment surface of an AppSheet app, all the rules about who can access apps, how permissions are handled, what data sources you can connect to, and so on also apply to your Chat apps. 

#### I have an existing AppSheet app. Who can enable it as a Chat app?

Only app creators will be able to enable an AppSheet app a Chat app.

#### Can I use a template to make a Chat app?

Yes! Any AppSheet app – template, existing, or new – can be enabled as a Chat app. While we’re at this early be aware that some templates use views not yet supported in Chat, but we’re working towards full view support and a set of purpose-built Chat app templates. For an example, see [Quick start: Create your first Chat app with AppSheet](https://support.google.com/appsheet/answer/12923581).

#### Do I have to set up slash commands? Why are they optional? What happens if I don’t configure any?

Slash commands are just another way to control your Chat app. You can set them up to give users “shortcuts” to invoke your different app views or trigger automations, but they’re not required. Even if you don’t set up slash commands, users will still be able to get to your app’s views by @-mentioning your app name and clicking on the appropriate link in the menu card.

#### Do I have to create a Google Cloud project to use a Chat app?

Yes, Google Cloud projects are the “containers” from which Chat apps are run and are part of the required technical implementation. See [About the Google Cloud projects used by Chat apps](https://support.google.com/appsheet/answer/13536336). AppSheet creates a project for you when you use [automatic configuration](https://support.google.com/appsheet/answer/12849362#automatic-configuration). If you want to create and configure the project yourself use [manual configuration](https://support.google.com/appsheet/answer/12849362#manual-configuration).

## Who can access and manage the Google Cloud project that is associated with a Chat app

Only a Google Cloud admin can directly locate, view, or edit Google Cloud projects in the Google Cloud console.

#### Does creating a Chat app, running it from Google Cloud Platform, or configuring any of those APIs cost me or my company anything?

No. AppSheet Chat apps use only free features of Google Cloud Platform.

#### Can I add my Chat app to a one-on-one conversation? A group? A space?

You can have a one-on-one conversation directly with your Chat app by searching in Google Chat and clicking "Chat," which will open a 1:1 “chat” with your new bot.

Additionally, you can add a Chat app to any other type of Google Chat space. This includes one-on-one conversations with another person and conversations with groups.

## Do users need AppSheet access (licenses) to use my Chat app?

Yes. AppSheet Chat app users are billed the same way as AppSheet users using the mobile/desktop apps.

#### What if someone who sees or tries to interact with my Chat app doesn’t have an AppSheet license?

They will have the same experience as when an unlicensed user accesses a web-based AppSheet application: depending on why they don’t have a license, [*they’ll either be able to proceed as normal for a limited time*](https://support.google.com/appsheet/answer/10104499?hl=en#about-enforcement) or, if the licensing issue isn't resolved, they’ll ultimately see a “cannot access application” message after some time.

#### Do Chat apps work on mobile versions of Chat?

Yes, but not all features may be supported in the mobile version of Google Chat.

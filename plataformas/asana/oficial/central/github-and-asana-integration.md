---
fonte: https://help.asana.com/s/article/github-and-asana-integration?language=en_US
baixado: 2026-11-10
---

# GitHub and Asana integration

**The Asana for GitHub integration is available on Asana [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

With the Asana for GitHub integration, you can automatically sync GitHub pull request status updates to Asana tasks to improve cross-functional collaboration.

This integration helps raise visibility and transparency around engineering work between technical and non-technical teams. With this new integration, developers can communicate effortlessly through Asana to keep teams and cross-functional stakeholders in the know and prevent work from falling through the cracks.

**This integration does not support GitHub Enterprise Server.**

## Installation for Asana and GitHub Actions

Connect Asana and GitHub to sync your pull request statuses. To utilize the integration, configuration is set up in Asana and for additional features, within GitHub as well.

#### How to configure in Asana:

1.  Navigate to an Asana project where you would like to install the Asana for GitHub integration. Click the **Customize** button in the top right-hand corner.
2.  Scroll down to **Apps** and select **+ Add app**

- Select **GitHub**
- Follow the instructions to authorize your GitHub account.
- The Asana for GitHub integration will be installed at the project level.

Congratulations, you can now connect GitHub pull requests to Asana tasks. If you would like to enable additional functionalities with the integration, please review the next section. Otherwise please skip to [Key functionality](https://asana.com/guide/help/api/github#gl-key "Key functionality") below.

### How to configure GitHub Actions:

This section assumes basic familiarity with [git](https://git-scm.com/ "git") and GitHub repository secrets. If you do not have access to set up repository secrets, please contact the repository owner.

We support two types of GitHub Actions:

1.  **Automate GitHub pull request notifications in Asana:** This action comments the status of the pull request on the Asana task. It includes the pull request title with a link to the associated Asana task. To set this up, visit the [GitHub Action page](https://github.com/Asana/comment-on-task-github-action "GitHub Action page").
2.  **Connect pull request attachments from GitHub pull request descriptions to Asana:** This action automatically connects a GitHub pull request to Asana task(s), by adding the Asana task url(s) to the pull request description. To set this up, visit the [GitHub Action page](https://github.com/Asana/create-app-attachment-github-action "GitHub Action page").

Similar to other GitHub Actions, they will only run when an event occurs in the repository you have set up the actions for. For example, you can set up an action to run every time someone merges or comments on a pull request.

Each of these GitHub Actions must be set up individually, unless there are multiple, identical actions in the same repository. For example, you can set up an action to comment on the task in the pull request description when a test is complete and another action to add a different comment to the task when the pull request is merged.

GitHub Actions can also be added as part of an existing workflow. Reference the [GitHub Actions resource guide](https://docs.github.com/en/actions "GitHub Actions resource guide") to learn more.

#### Revoking secret tokens

If you set up Github Actions in the previous section, you can revoke secret tokens. Visit [this set-up page](https://github.integrations.asana.plus/auth?domainId=manage_tokens "this set-up page"), and select **Revoke all**.

This will revoke all existing GitHub Actions secret tokens.

> You will still be able to see pull request information in the existing Asana projects where you have added this integration.

## Key functionality

### How to attach a pull request to an Asana task (in Asana):

After installing the GitHub integration in Asana, you will be able to see a GitHub field on every task in the associated project.

To attach a pull request to an Asana task, retrieve the pull request URL and paste it in the empty GitHub field. A widget with the following details should now appear on the Asana task: Review status, Build state, PR status, Line changes, and conversation count within GitHub.

### How to attach a pull request to an Asana task (in GitHub):

After installing the GitHub integration in Asana and setting up GitHub Actions, you can now automatically attach a pull request to an Asana task from a GitHub pull request description.

In your GitHub pull request description, retrieve the Asana task URL and paste it into the description. A widget with the following details should now appear when viewing the task in Asana: Review status, Build state, PR status, and Line changes.

> Any errors should be reflected in the GitHub Actions tab within GitHub.

### How to receive pull request merge and close updates:

Pull requests can be closed in GitHub after the appropriate teams review and merge the changes. The status in the Asana widget will automatically update.

If you would like to attach a new GitHub pull request, you can add the Asana task URL to the new GitHub pull request description and the widget will automatically be replaced or you can remove the closed pull request within Asana by clicking the menu in the top right. Once removed, you can enter in a new GitHub pull request url.

After installing the GitHub integration in Asana and setting up GitHub Actions, you will now receive comments on Asana tasks with an open pull request attached. This will include updates on whether or not the pull request has been merged or closed.

## FAQ

#### Can the same generated secret be used in multiple repositories?

Yes

#### Can my teammates see information about the pull requests I attach on an Asana task, even if they do not have access to the pull request?

Yes. When you attach a pull request to a task, everyone who can view the task can see the information in the widget.

#### Does generating a new token disable my old secret token?

No, your old secret tokens will still work. If you want to disable your existing secret tokens, you can do so [here](https://github.integrations.asana.plus/auth?domainId=manage_tokens "here").

#### Can the same generated secret be used in multiple repositories?

Yes

#### When trying to push the workflow file, `git` says that my token does not have access to create workflows. What should I do?

If you are using two-factor authentication and interacting with GitHub on the command line, GitHub requires that [you use your personal access token as the password](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/accessing-github-using-two-factor-authentication#using-two-factor-authentication-with-the-command-line "you use your personal access token as the password"). Please create a new GitHub personal access token with the workflow scope.

#### Why do we request these GitHub permissions?

We only read and write from pull requests in this integration. The permission on the authentication page is the most restrictive permission GitHub allows us to request in order to access pull requests.

#### What happens if the GitHub Action attaches a pull request to a task in a project that does not have the integration activated?

An attachment that links to the pull request will be visible in the task comment section, but the widget that syncs the pull request status will not appear.

> Like what you see? Get started with a free Asana trial today. [Try for free](https://asana.com/create-account "Try for free").

[](https://forum.asana.com/c/forum-en/tips/6)

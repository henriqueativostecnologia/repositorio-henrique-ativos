---
fonte: https://support.google.com/appsheet/answer/10104795?hl=en
baixado: 2026-11-10
---

# Share resources with your team

**Note**: Teams are supported for Enterprise Plus plans only.

Share the following resources with your team:

- [Share authoring of apps](#share-authoring-apps)
- [Share authoring of databases](#share-authoring-database)
- [Share sample apps with your team](#share-sample-apps)
- [Share data sources with your team](#share-data-sources)
- [Restrict access to team data sources](#restrict-access-team-data-sources)
- [Share integrations with your team](#share-integrations)

See also:

- [Share sample apps in your public portfolio](https://support.google.com/appsheet/answer/11938113)
- [Work with a shared drive](https://support.google.com/appsheet/answer/16701354)

## Share authoring of apps

Team root and admin accounts can access all team apps regardless of whether or not they are shared.

AppSheet app creators can share app authoring with individual team members. For details, see [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

## Share authoring of databases

AppSheet database creators can share database authoring with individual team members. For details, see [S](https://support.google.com/appsheet/answer/10104983)[hare databases](https://support.google.com/appsheet/answer/12637319).

## Share sample apps with your team

You can share sample apps with your team configuring your [team](#share-config-team) or your [app](#share-config-app). Your team sample apps can be viewed or copied (but not modified) on the My Team page by anyone on the team.

**Note**: Apps must be deployed before you can share them with your team.

### Share sample apps when configuring your team

To share a sample app with your team when configuring your team:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Select **My team** in the account profile drop-down.
3.  Click **Shared Apps**.
4.  Click **Add a team sample**.

    Add a team sample app
5.  Click the sample that you want to share with your team.

### Share sample apps when configuring your app

To share a sample app with your team when configuring your app:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Open the app in the app editor.
3.  Select **Manage \> Author**.
4.  Expand the **Team Work** section.
5.  Turn on **Make this a team sample?**
6.  To hide the app definition details from team members in the team portfolio, turn on **Hide app definition**. In this case, team members won't have the option to view the app details.
7.  Click **Change visibility**.

## Share data sources with your team

To share a data source with your team:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Select **My team** in the account profile drop-down.
3.  Click **Shared data**.
4.  Click **+ New Data Source** and follow the prompts to add a new data source.
5.  After the data source is added, select  More menu options  More **\> Share with my team** in the **More** menu.
    **Note**: To hide a shared data source from your team, select **Hide from Team** in the More menu.

    Share with team option in More menu

    A copy of the data source appears under Team Sources. For example:

    Shared data source under Team Sources

Team members can view all shared data sources by selecting **My team \> Shared Data**.

 

Shared data including 3 team data sources and 1 team domain

## Restrict access to team data sources

Restrict access to team data sources to only specific team members by defining a governance policy. When naming team data sources, AppSheet includes the string: `:Team:` 

For example: `google_cloud_identity-1:Team:1234567`

Using the `:Team:` string in a policy condition, you can restrict the team members that can access any of the team data source. 

To restrict access to team data sources, do the following

1.  [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy).

2.  In the Policy template drop-down, select **Restrict data sources**.

3.  Update the **Condition** as follows, modifying the list of approved team member email addresses in the `LIST()` function:

    `OR(NOT(CONTAINS(DataSourceName], ":Team:")), IN(USEREMAIL(), LIST("`*`emailaddress1`*`", "`*`emailaddress2`*`", ...)))`

    Modify the other fields, as required. See [Configure the policy](https://support.google.com/appsheet/answer/11948767#configure-policy). 

    For example:

    Policy for restricting access to team data sources

4.  [Review policy compliance](https://support.google.com/appsheet/answer/11948767#policy-compliance).

5.  Click **Save**.

## Share integrations with your team

When adding integration points on the **My account \> Integrations** tab, such as auth domains, object stores, inbound and outbound channels, or app services, you can share those integrations with your team by selecting    More menu options  More **\> Share with team** after you add the integration.

In addition, you can set an auth domain as the team default by selecting   More menu options  More **\> Make team default** after you share the auth domain with your team.

Make team default

See also:

- [*Domain integration: The Essentials*](https://support.google.com/appsheet/answer/10105757)
- [*Understand Cloud Object Stores*](https://support.google.com/appsheet/answer/10106769)
- [*API integration points in AppSheet*](https://support.google.com/appsheet/answer/11628886)

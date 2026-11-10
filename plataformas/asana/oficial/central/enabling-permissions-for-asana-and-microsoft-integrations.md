---
fonte: https://help.asana.com/s/article/enabling-permissions-for-asana-and-microsoft-integrations?language=en_US
baixado: 2026-11-10
---

# Enabling permissions for Asana-built and Microsoft 365 integrations

If you want to use Asana-built Microsoft 365 integrations, you may need to work with your Microsoft admins with access to Microsoft Entra (fka Azure Active Directory) to consent to the required permissions. Consenting to these permissions authorize Asana to read and/or write data in the corresponding Microsoft 365 applications so the Asana-built integrations can “talk to” these applications.

In this article, we summarize the required permissions for the Asana-built Microsoft 365 integrations and walk through several options for your Microsoft admins to turn on these permissions for you. 

## Required permissions by integration

 

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| **Integration**                                                 | **Required permissions**                                                                   |
+=================================================================+============================================================================================+
| [Outlook Calendar + Asana Rules & Sync +                        | Calendars.ReadWrite                                                                        |
| Meetings](https://asana.com/apps/outlook-calendar)              |                                                                                            |
|                                                                 | Permissions to use AI Meetings:                                                            |
|                                                                 |                                                                                            |
|                                                                 | -   User.Read                                                                              |
|                                                                 | -   offline_access                                                                         |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| [Microsoft Teams + Asana](https://asana.com/apps/microsoft)     | [Permissions to use Asana Bot in MS                                                        |
|                                                                 | Team                                                                                       |
|                                                                 | s:](https://help.asana.com/s/article/microsoft-teams-and-asana-integration?language=en_US) |
|                                                                 |                                                                                            |
|                                                                 | -   ChatMember.Read                                                                        |
|                                                                 | -   User.Read                                                                              |
|                                                                 | -   offline_access                                                                         |
|                                                                 | -   Channel.ReadBasic.All                                                                  |
|                                                                 | -   Team.ReadBasic.All                                                                     |
|                                                                 |                                                                                            |
|                                                                 | Permissions to use MS Teams app within Asana to create Asana App rules:                    |
|                                                                 |                                                                                            |
|                                                                 | -   offline_access                                                                         |
|                                                                 | -   User.Read                                                                              |
|                                                                 | -   Channel.ReadBasic.All                                                                  |
|                                                                 | -   Team.ReadBasic.All                                                                     |
|                                                                 | -   TeamsAppInstallation.ReadWriteForTeam                                                  |
|                                                                 | -   Chat.ReadWrite                                                                         |
|                                                                 | -   AppCatalog.Read.All                                                                    |
|                                                                 | -   TeamsAppInstallation.ReadWriteSelfForChat                                              |
|                                                                 | -   TeamsAppInstallation.ReadForUser                                                       |
|                                                                 |                                                                                            |
|                                                                 | Permissions for Asana Tab in MS Teams:                                                     |
|                                                                 |                                                                                            |
|                                                                 | -   TeamsTab.Create                                                                        |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| [Outlook Email + Asana](https://asana.com/apps/outlook)         | Outlook Email + Asana:                                                                     |
|                                                                 |                                                                                            |
|                                                                 | -   User.Read                                                                              |
|                                                                 | -   Mail.Send                                                                              |
|                                                                 | -   Mail.ReadWrite                                                                         |
|                                                                 | -   Files.Read                                                                             |
|                                                                 | -   Mail.read                                                                              |
|                                                                 | -   openid                                                                                 |
|                                                                 | -   profile                                                                                |
|                                                                 | -   offline_access                                                                         |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| [OneDrive + Asana                                               | Files.Read.All                                                                             |
| Rules](https://asana.com/apps/microsoft-one-drive)              |                                                                                            |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------+

##

## How Microsoft admins can enable these permissions

Depending on the organizational culture, there are several ways to enable these permissions. We summarize 3 ways below, and you can find one that works best for your organization. 

> After a user attempts to connect to the Asana app, the app appears in **Enterprise Applications**.

### Assign users or groups to an integration

If your organization wants to have strict control over which users or groups have access to a particular Asana-built integration, your Microsoft admins can assign the integration to specific users or groups. Most organizations would prefer this approach.

1.  Log into Microsoft Entra \> Enterprise applications
2.  Search and open an Asana-built integration, e.g. Asana for Outlook Email
3.  Click “Assign users and groups” and then “Add user/group”
4.  Added user(s) and group(s) are authorized the permissions to this application

### Enable “Allow user consent for apps”

If your organization encourages employees to experiment and adopt integrations that work best for their workflows, Microsoft admins can allow “user consent for apps” to give employees’ autonomy to consent to relevant permissions. 

In Microsoft Entra, navigate to **Enterprise applications \| Consent and permissions** to enable user consent. This gives your employees the flexibility to accept or decline requested permissions when they attempt to use Asana-built Microsoft integrations. 

### Enable “Grant admin consent”

Your Microsoft admins can also choose to grant “admin” consent to the permissions required of an Asana-built integration (e.g., Asana for Outlook Email). This grants consent to the Asana integration on behalf of everyone in your organization, so users won't be asked to consent individually.

If this is the preferred approach, you can:

1.  Go to Microsoft Entra \> Enterprise applications 
2.  Search and open an Asana-built integration. For example, Asana for Outlook Email
3.  Click **Permissions** under the left nav bar
4.  Click **Grant admin consent for {Your organization's domain name}**

 

[](https://forum.asana.com/c/forum-en/tips/6)

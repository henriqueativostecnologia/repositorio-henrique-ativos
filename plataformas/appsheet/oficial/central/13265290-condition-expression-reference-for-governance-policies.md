---
fonte: https://support.google.com/appsheet/answer/13265290?hl=en
baixado: 2026-11-10
---

# Condition expression reference for governance policies

The following lists the column names and types, and the valid values that you can include in the [Condition](https://support.google.com/appsheet/answer/11948767#condition) expression when [defining governance policies](https://support.google.com/appsheet/answer/11948767). The column names are organized by AppSheet component, such as actions, settings, tables, and so on.

The following AppSheet functions are **not** supported for use in the [Condition](https://support.google.com/appsheet/answer/11948767#condition) expression: 

`EXTRACT()`, `EXTRACTCHOICE()`, `EXTRACTDATES()`, `EXTRACTDATETIMES()`, `EXTRACTDOMAINS()`, `EXTRACTDURATIONS()`, `EXTRACTEMAILS()`, `EXTRACTHASHTAGS()`,` EXTRACTMENTIONS()`, `EXTRACTNUMBERS()`, `EXTRACTPHONENUMBERS()`, `EXTRACTPRICES()`, `EXTRACTTIMES()`, `HERE()`, `HYPERLINK()`, `INPUT()`, `LAT()`, `LATLONG()`, `LATLONGDISTANCE()`, `LINKTEXT()`, `LINKTOAPP()`, `LINKTOFILTEREDVIEW()`, `LINKTOFORM()`, `LINKTOPARENTVIEW()`, `LINKTOROW()`, `LINKTOVIEW()`, `LINKURL()`, `LONG()`, `NOW()`, `OCRTEXT()`, `RANDBETWEEN()`, `SNAPSHOT()`, `TEXTICON()`, `TIMENOW()`, `TODAY()`, `UNIQUEID()`, `UTCNOW()`, and `XY()`

Also, the [`CONTEXT()`](https://support.google.com/appsheet/answer/10107885) function is only supported using the following keywords: `AppName` or `OwnerEmail`

The following AppSheet functions are not supported for use in the policy [Condition](#condition) setting when [Stage](#stage) is set to **Enforce Always**: 

`USEREMAIL()`, `USERLOCALE()`, `USERNAME()`, `USERROLE()`, `USERSETTINGS()`, and `USERTIMEZONE()`. 

 

+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| **AppSheet component**                | **Column name**                       | **Column type**                       | **Description**                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Actions                               | `ActionType`                          | `Enum`                                | Type of action. See [Action           |
|                                       |                                       |                                       | types](https://support.google.com/ap  |
|                                       |                                       |                                       | psheet/answer/10107706#action-types). |
|                                       |                                       |                                       | Valid values include:                 |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | -   `ADD_RECORD`                      |
|                                       |                                       |                                       | -   `ADD_RECORD_TO`                   |
|                                       |                                       |                                       | -   `CALL`                            |
|                                       |                                       |                                       | -   `COMPOSITE`                       |
|                                       |                                       |                                       | -   `COPY_EDIT_ROW`                   |
|                                       |                                       |                                       | -   `DELETE_RECORD`                   |
|                                       |                                       |                                       | -   `EDIT_RECORD`                     |
|                                       |                                       |                                       | -   `EMAIL`                           |
|                                       |                                       |                                       | -   `EXPORT_VIEW`                     |
|                                       |                                       |                                       | -   `IMPORT_FILE`                     |
|                                       |                                       |                                       | -   `NAVIGATE_APP`                    |
|                                       |                                       |                                       | -   `NAVIGATE_BACK`                   |
|                                       |                                       |                                       | -   `NAVIGATE_DIFFERENT_APP`          |
|                                       |                                       |                                       | -   `NAVIGATE_URL`                    |
|                                       |                                       |                                       | -   `OPEN_FILE`                       |
|                                       |                                       |                                       | -   `REF_ACTION`                      |
|                                       |                                       |                                       | -   `SET_COLUMN_VALUE`                |
|                                       |                                       |                                       | -   `SMS`                             |
|                                       |                                       |                                       | -   `TRIGGER_PROCESS`                 |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| API settings                          | `EnableAPI`                           | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | API is enabled. See [Enable the API   |
|                                       |                                       |                                       | for cloud-based service               |
|                                       |                                       |                                       | communication](https://support.       |
|                                       |                                       |                                       | google.com/appsheet/answer/10105769). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `Description`                         | `Text`                                | Description of the app. See [App      |
|                                       |                                       |                                       | proper                                |
|                                       |                                       |                                       | ties](https://support.google.com/apps |
|                                       |                                       |                                       | heet/answer/10106613#app-properties). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `DisableAutoUpdate`                   | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Automatic updates** is turned off.  |
|                                       |                                       |                                       | See [Can I have my app update         |
|                                       |                                       |                                       | automatically?](https://support       |
|                                       |                                       |                                       | .google.com/appsheet/answer/10108001) |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `Id`                                  | `Text`                                | App ID. View the App ID when enabling |
|                                       |                                       |                                       | the API as described in [Enable the   |
|                                       |                                       |                                       | API for cloud-based service           |
|                                       |                                       |                                       | communication](https://support.       |
|                                       |                                       |                                       | google.com/appsheet/answer/10105769). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `IsPublic`                            | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | app is public. See [Share your app    |
|                                       |                                       |                                       | with anyone (public                   |
|                                       |                                       |                                       | a                                     |
|                                       |                                       |                                       | ccess)](https://support.google.com/ap |
|                                       |                                       |                                       | psheet/answer/10104983#share-anyone). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `IsTeamPublic`                        | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | app is a team sample. See [Share      |
|                                       |                                       |                                       | resources with your                   |
|                                       |                                       |                                       | team](https://support.                |
|                                       |                                       |                                       | google.com/appsheet/answer/10104795). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `Name`                                | `Yes/No`                              | Name of the app. See [App             |
|                                       |                                       |                                       | proper                                |
|                                       |                                       |                                       | ties](https://support.google.com/apps |
|                                       |                                       |                                       | heet/answer/10106613#app-properties). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `OwnerId`                             | `Number`                              | ID of the app owner.                  |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `Title`                               | `Text`                                | Short description of the app. See     |
|                                       |                                       |                                       | [App                                  |
|                                       |                                       |                                       | proper                                |
|                                       |                                       |                                       | ties](https://support.google.com/apps |
|                                       |                                       |                                       | heet/answer/10106613#app-properties). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App settings                          | `UsePublicOwner`                      | `Yes/No`                              | Setting that specifies whether **Use  |
|                                       |                                       |                                       | public app owner** is turned on to    |
|                                       |                                       |                                       | display the public app owner to users |
|                                       |                                       |                                       | of the app. See [Set the public app   |
|                                       |                                       |                                       | own                                   |
|                                       |                                       |                                       | er](https://support.google.com/appshe |
|                                       |                                       |                                       | et/answer/11918568#public-app-owner). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `DelayedSync`                         | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Delayed sync** is turned on to      |
|                                       |                                       |                                       | queue up changes until you explicitly |
|                                       |                                       |                                       | choose to sync. See [Delayed          |
|                                       |                                       |                                       | sync](https://support.goog            |
|                                       |                                       |                                       | le.com/answer/10107724#delayed-sync). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `DeltaSync`                           | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Delta sync** is turned on to        |
|                                       |                                       |                                       | maintain timestamps for the last time |
|                                       |                                       |                                       | each table was fetched. See           |
|                                       |                                       |                                       | [C](https://support.google.c          |
|                                       |                                       |                                       | om/appsheet/answer/10107724)[onfigure |
|                                       |                                       |                                       | the data caçhe                        |
|                                       |                                       |                                       | settings                              |
|                                       |                                       |                                       | ](https://support.google.com/appsheet |
|                                       |                                       |                                       | /answer/10104985#configure-settings). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `EnableCaching`                       | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Server caching** is turned on to    |
|                                       |                                       |                                       | maintain cached copies of read-only   |
|                                       |                                       |                                       | tables for up to five minutes. See    |
|                                       |                                       |                                       | [C](https://support.google.c          |
|                                       |                                       |                                       | om/appsheet/answer/10107724)[onfigure |
|                                       |                                       |                                       | the data cache                        |
|                                       |                                       |                                       | settings                              |
|                                       |                                       |                                       | ](https://support.google.com/appsheet |
|                                       |                                       |                                       | /answer/10104985#configure-settings). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `FiveButtonFooter`                    | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Allow five views in the bottom      |
|                                       |                                       |                                       | navigation bar** is turned on. See    |
|                                       |                                       |                                       | [System                               |
|                                       |                                       |                                       | But                                   |
|                                       |                                       |                                       | tons](https://support.google.com/apps |
|                                       |                                       |                                       | heet/answer/10107387#system-buttons). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `FullOfflineCaching`                  | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Store content for offline use** is  |
|                                       |                                       |                                       | turned on so that AppSheet caches     |
|                                       |                                       |                                       | images and documents for offline use. |
|                                       |                                       |                                       | See [Cache images and                 |
|                                       |                                       |                                       | documents](https://support.google     |
|                                       |                                       |                                       | .com/appsheet/answer/10108551#cache). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `HideDefinition`                      | `Yes/No`                              | Setting that specifies whether **Hide |
|                                       |                                       |                                       | app definition** is turned on when    |
|                                       |                                       |                                       | sharing samples apps with your team.  |
|                                       |                                       |                                       | See [Share resources with your        |
|                                       |                                       |                                       | team](https://support.g               |
|                                       |                                       |                                       | oogle.com/appsheet/answer/10104795).  |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `HighPrecisionGeocoding`              | `Yes/No`                              | Setting that specifies whether **Use  |
|                                       |                                       |                                       | my Google Maps integration** is       |
|                                       |                                       |                                       | turned on. See [Map                   |
|                                       |                                       |                                       | view](https://support.google.c        |
|                                       |                                       |                                       | om/appsheet/answer/10107387#map-view) |
|                                       |                                       |                                       | configuration settings.               |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `LaunchOffline`                       | `Yes/No`                              | Setting that specifies whether The    |
|                                       |                                       |                                       | **app can start when offline** is     |
|                                       |                                       |                                       | turned on to allow the app to start   |
|                                       |                                       |                                       | when there is no internet connection. |
|                                       |                                       |                                       | See [Enable app to start when         |
|                                       |                                       |                                       | offline                               |
|                                       |                                       |                                       | ](https://support.google.com/appsheet |
|                                       |                                       |                                       | /answer/10108551#start-when-offline). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `PullToSync`                          | `Yes/No`                              | Setting that specifies whether **Pull |
|                                       |                                       |                                       | to refresh** is turned on. See        |
|                                       |                                       |                                       | [General](https://support.google.     |
|                                       |                                       |                                       | com/appsheet/answer/10107387#general) |
|                                       |                                       |                                       | configuration settings.               |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Behavior settings                     | `SyncOnStart`                         | `Yes/No`                              | Setting that specifies whether **Sync |
|                                       |                                       |                                       | on start** is turned on to sync data  |
|                                       |                                       |                                       | every time the app starts to make     |
|                                       |                                       |                                       | sure the user has the latest          |
|                                       |                                       |                                       | data. See [Sync: App to               |
|                                       |                                       |                                       | Clou                                  |
|                                       |                                       |                                       | d](https://support.google.com/appshee |
|                                       |                                       |                                       | t/answer/10107724#sync-app-to-cloud). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Bots                                  | `Disabled`                            | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | bot automation is disabled. See       |
|                                       |                                       |                                       | [Enable or disable a                  |
|                                       |                                       |                                       | bot](https://support.google.com/a     |
|                                       |                                       |                                       | ppsheet/answer/11432969#disable-bot). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Chatbot settings                      | `EnableChatbot`                       | `Yes/No`                              | Setting that specifies whether Chat   |
|                                       |                                       |                                       | bots are enabled. See [Chat apps: The |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/12860535). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Columns                               | `Name`                                | `Text`                                | Name of the column. See [Columns: The |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10106674). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Columns                               | `Type`                                | `Text`                                | Type of column. See [Column data      |
|                                       |                                       |                                       | types](https://support.               |
|                                       |                                       |                                       | google.com/appsheet/answer/10106435). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Description                           | `DesignDetails`                       | `Text`                                | Design details of the app. See [App   |
|                                       |                                       |                                       | documentatio                          |
|                                       |                                       |                                       | n](https://support.google.com/appshee |
|                                       |                                       |                                       | t/answer/10106613#app-documentation). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Description                           | `IsWhitelabel`                        | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | app is branded. See [Branded apps:    |
|                                       |                                       |                                       | Establish your own                    |
|                                       |                                       |                                       | branding](https://support.            |
|                                       |                                       |                                       | google.com/appsheet/answer/10105389). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Description                           | `Purpose`                             | `Text`                                | Purpose of the app. See [App          |
|                                       |                                       |                                       | documentatio                          |
|                                       |                                       |                                       | n](https://support.google.com/appshee |
|                                       |                                       |                                       | t/answer/10106613#app-documentation). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AllowAllSignedInUsers`               | `Yes/No`                              | Setting that specifies whether all    |
|                                       |                                       |                                       | signed-in users have access. See      |
|                                       |                                       |                                       | [Share you apps with all signed-in    |
|                                       |                                       |                                       | users](https://support.google.        |
|                                       |                                       |                                       | com/answer/10104983#share-signed-in). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AuthDomain`                          | `Text`                                | Display name of the authentication    |
|                                       |                                       |                                       | domain. See [Domain integration: The  |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10105757). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AuthDomainSource`                    | `Text`                                | Name of authentication domain         |
|                                       |                                       |                                       | source. See [Domain integration: The  |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10105757). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AuthGroup`                           | `Text`                                | Name of authentication group.         |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AuthGroupId`                         | `Text`                                | ID of authentication group.           |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AuthProvider`                        | `Text`                                | Authentication provider. See [Require |
|                                       |                                       |                                       | sign-in: The                          |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10104975). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AuthRequired`                        | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | authentication is required. See       |
|                                       |                                       |                                       | [Require sign-in: The                 |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10104975). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `AutoBackgroundUpdate`                | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Automatic updates** is turned on.   |
|                                       |                                       |                                       | See [Can I have my app update         |
|                                       |                                       |                                       | automatically?](https://support       |
|                                       |                                       |                                       | .google.com/appsheet/answer/10108001) |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `CanMakePublic`                       | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | **Yes, I am authorized to set up an   |
|                                       |                                       |                                       | insecure app** is turned on. See      |
|                                       |                                       |                                       | [Share app with anyone (public        |
|                                       |                                       |                                       | a                                     |
|                                       |                                       |                                       | ccess)](https://support.google.com/ap |
|                                       |                                       |                                       | psheet/answer/10104983#share-anyone). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `ConsentAuthorizedPublicApp`          | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | **Yes, I am authorized to set up a    |
|                                       |                                       |                                       | public app** is turned on. See [Share |
|                                       |                                       |                                       | you apps with all signed-in           |
|                                       |                                       |                                       | users](https://support.google.        |
|                                       |                                       |                                       | com/answer/10104983#share-signed-in). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `ConsentPublicApp`                    | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | **Yes, this is a public app** is      |
|                                       |                                       |                                       | turned on. See [Share app with anyone |
|                                       |                                       |                                       | (public                               |
|                                       |                                       |                                       | access)](ht                           |
|                                       |                                       |                                       | tps://support.google.com/appsheet/ans |
|                                       |                                       |                                       | wer/10104983#share-anyone) and [Share |
|                                       |                                       |                                       | you apps with all signed-in           |
|                                       |                                       |                                       | users](https://support.google.        |
|                                       |                                       |                                       | com/answer/10104983#share-signed-in). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `DisableAppSharing`                   | `Yes/No`                              | Setting that specifies whether the    |
|                                       |                                       |                                       | Disable Share button is turned on.    |
|                                       |                                       |                                       | See [System                           |
|                                       |                                       |                                       | But                                   |
|                                       |                                       |                                       | tons](https://support.google.com/apps |
|                                       |                                       |                                       | heet/answer/10107387#system-buttons). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `DomainAuthRequired`                  | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Require domain authentication** is  |
|                                       |                                       |                                       | turned on. See [Domain integration:   |
|                                       |                                       |                                       | The                                   |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10105757). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `EncryptLocalData`                    | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Encrypt device data** is turned on. |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `HasExternalAuth`                     | `Yes/No`                              | Setting that specifies whether app    |
|                                       |                                       |                                       | creators can use external data        |
|                                       |                                       |                                       | sources and external authentication   |
|                                       |                                       |                                       | domains. See:                         |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | -   [Manage data                      |
|                                       |                                       |                                       |     sources](https://support          |
|                                       |                                       |                                       | .google.com/appsheet/answer/10106309) |
|                                       |                                       |                                       | -   [Prevent app creators from using  |
|                                       |                                       |                                       |     external data                     |
|                                       |                                       |                                       |     sources](https://support          |
|                                       |                                       |                                       | .google.com/appsheet/answer/13579362) |
|                                       |                                       |                                       | -   [Prevent app creators from using  |
|                                       |                                       |                                       |     external authentication           |
|                                       |                                       |                                       |     domains]                          |
|                                       |                                       |                                       | (https://support.google.com/appsheet/ |
|                                       |                                       |                                       | answer/10105757#prevent-auth-domains) |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `RequireImageAndFileUrlSigning`       | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Require Image and File URL          |
|                                       |                                       |                                       | signing** is turned on. See [External |
|                                       |                                       |                                       | URL for image                         |
|                                       |                                       |                                       | files]                                |
|                                       |                                       |                                       | (https://support.google.com/appsheet/ |
|                                       |                                       |                                       | answer/10107317#external-url-images). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `RequireUserConsent`                  | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Require user content** is turned on |
|                                       |                                       |                                       | to require users to consent before    |
|                                       |                                       |                                       | using the app. See [Security: The     |
|                                       |                                       |                                       | Essentials.](https://support          |
|                                       |                                       |                                       | .google.com/appsheet/answer/10105078) |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `SecureImageAccess`                   | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Secure Image access** is turned on  |
|                                       |                                       |                                       | to not cache an image in Cloud CDN.   |
|                                       |                                       |                                       | See [Document and image               |
|                                       |                                       |                                       | cach                                  |
|                                       |                                       |                                       | ing](https://support.google.com/appsh |
|                                       |                                       |                                       | eet/answer/10107317#caching#caching). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `SecurePDFAccess`                     | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Secure PDF** is turned on to not    |
|                                       |                                       |                                       | cache a PDF file in Cloud CDN. See    |
|                                       |                                       |                                       | [Document and image                   |
|                                       |                                       |                                       | cach                                  |
|                                       |                                       |                                       | ing](https://support.google.com/appsh |
|                                       |                                       |                                       | eet/answer/10107317#caching#caching). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Security                              | `TreatAllDataAsPII`                   | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Treat all data columns as           |
|                                       |                                       |                                       | Sensitive** is turned on. See         |
|                                       |                                       |                                       | [Sensitive Personally Identifiable    |
|                                       |                                       |                                       | Information (PII) data                |
|                                       |                                       |                                       | policy](https://support.              |
|                                       |                                       |                                       | google.com/appsheet/answer/10104377). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tables                                | `CloudObjectStore`                    | `Text`                                | Name of the cloud object store.       |
|                                       |                                       |                                       | [Configure a relational database as a |
|                                       |                                       |                                       | cloud object                          |
|                                       |                                       |                                       | store](https://support.               |
|                                       |                                       |                                       | google.com/appsheet/answer/10106513). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tables                                | `DataAccessMode`                      | `Text`                                | Access mode. See [Access mode: as app |
|                                       |                                       |                                       | creator or app                        |
|                                       |                                       |                                       | user](https://support.                |
|                                       |                                       |                                       | google.com/appsheet/answer/10105756). |
|                                       |                                       |                                       | Valid values include:                 |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | -   `as app creator` (default if      |
|                                       |                                       |                                       |     invalid or no value provided)     |
|                                       |                                       |                                       | -   `as app user`                     |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tables                                | `DataSourceName`                      | `Text`                                | Name of data source. See [Summary of  |
|                                       |                                       |                                       | data source                           |
|                                       |                                       |                                       | types](https://support.google.c       |
|                                       |                                       |                                       | om/appsheet/answer/10106309#summary). |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | To restrict access to team data       |
|                                       |                                       |                                       | sources to only specific team         |
|                                       |                                       |                                       | members, use the `:Team:` string in a |
|                                       |                                       |                                       | governance policy condition. See      |
|                                       |                                       |                                       | [Restrict access to team data         |
|                                       |                                       |                                       | sources](https://suppo                |
|                                       |                                       |                                       | rt.google.com/appsheet/answer/1565456 |
|                                       |                                       |                                       | 7#restrict-access-team-data-sources). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tables                                | `DisableAutoUpdate`                   | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | automatic updates is turned off. See  |
|                                       |                                       |                                       | [Can I have my app update             |
|                                       |                                       |                                       | automatically?](https://support       |
|                                       |                                       |                                       | .google.com/appsheet/answer/10108001) |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tables                                | `Name`                                | `Text`                                | Name of the table. See [Table: The    |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10105821). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tables                                | `ProviderName`                        | `Text`                                | Name of the provider. Valid values    |
|                                       |                                       |                                       | include:                              |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | -   `airtable`                        |
|                                       |                                       |                                       | -   `apigee_api`                      |
|                                       |                                       |                                       | -   `apple`                           |
|                                       |                                       |                                       | -   `aws_cognito_domain`              |
|                                       |                                       |                                       | -   `big_query`                       |
|                                       |                                       |                                       | -   `box`                             |
|                                       |                                       |                                       | -   `data_studio` ([Looker            |
|                                       |                                       |                                       |     Studio](https://c                 |
|                                       |                                       |                                       | loud.google.com/looker/docs/studio/)) |
|                                       |                                       |                                       | -   `database` (all cloud and         |
|                                       |                                       |                                       |     on-premises databases)            |
|                                       |                                       |                                       | -   `dropbox`                         |
|                                       |                                       |                                       | -   `dynamodb`                        |
|                                       |                                       |                                       | -   `google`                          |
|                                       |                                       |                                       | -   `google_calendar`                 |
|                                       |                                       |                                       | -   `google_tables` (see also         |
|                                       |                                       |                                       |     [Disable AppSheet                 |
|                                       |                                       |                                       |     databases](https://support.       |
|                                       |                                       |                                       | google.com/appsheet/answer/12629371)) |
|                                       |                                       |                                       | -   `integration_connector`           |
|                                       |                                       |                                       | -   `mariadb`                         |
|                                       |                                       |                                       | -   `microsoft`                       |
|                                       |                                       |                                       | -   `mysql`                           |
|                                       |                                       |                                       | -   `odata`                           |
|                                       |                                       |                                       | -   `okta_domain`                     |
|                                       |                                       |                                       | -   `openid_connect`                  |
|                                       |                                       |                                       | -   `oracle`                          |
|                                       |                                       |                                       | -   `postgres`                        |
|                                       |                                       |                                       | -   `redshift`                        |
|                                       |                                       |                                       | -   `salesforce`                      |
|                                       |                                       |                                       | -   `sqlserver`                       |
|                                       |                                       |                                       | -   `sketch` (to [create an view apps |
|                                       |                                       |                                       |     using                             |
|                                       |                                       |                                       |     Spec](https://support.            |
|                                       |                                       |                                       | google.com/appsheet/answer/12007354)) |
|                                       |                                       |                                       | -   `smartsheet`                      |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | See [Summary of data source           |
|                                       |                                       |                                       | types](https://support.google.c       |
|                                       |                                       |                                       | om/appsheet/answer/10106309#summary). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tables                                | `UpdateMode`                          | `Enum`                                | Type of updates allowed in a table.   |
|                                       |                                       |                                       | See [Control add, update, and delete  |
|                                       |                                       |                                       | operations](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10106345). |
|                                       |                                       |                                       | Valid values include:                 |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | -   `ADDS_AND_DELETES`                |
|                                       |                                       |                                       | -   `ADDS_AND_UPDATES`                |
|                                       |                                       |                                       | -   `ADDS_ONLY`                       |
|                                       |                                       |                                       | -   `ALL_CHANGES`                     |
|                                       |                                       |                                       | -   `DELETES_ONLY`                    |
|                                       |                                       |                                       | -   `READ_ONLY`                       |
|                                       |                                       |                                       | -   `UNASSIGNED`                      |
|                                       |                                       |                                       | -   `UPDATES_AND_DELETES`             |
|                                       |                                       |                                       | -   `UPDATES_ONLY`                    |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Tasks                                 | `Type`                                | `Enum`                                | Type of automation task. See          |
|                                       |                                       |                                       | [Supported task                       |
|                                       |                                       |                                       | types](                               |
|                                       |                                       |                                       | https://support.google.com/appsheet/a |
|                                       |                                       |                                       | nswer/11445301#supported-task-types). |
|                                       |                                       |                                       | Valid values include:                 |
|                                       |                                       |                                       |                                       |
|                                       |                                       |                                       | -   `AiCategorize`                    |
|                                       |                                       |                                       | -   `AiExtract`                       |
|                                       |                                       |                                       | -   `AiExtractTable `(Extract rows)   |
|                                       |                                       |                                       | -   `AiSummarize`                     |
|                                       |                                       |                                       | -   `AppsScript`                      |
|                                       |                                       |                                       | -   `Chat`                            |
|                                       |                                       |                                       | -   `Email`                           |
|                                       |                                       |                                       | -   `IsAITask`                        |
|                                       |                                       |                                       | -   `MakeDoc`                         |
|                                       |                                       |                                       | -   `Notification`                    |
|                                       |                                       |                                       | -   `SMS`                             |
|                                       |                                       |                                       | -   `Webhook`                         |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UserDomains                           | `Domain`                              | `Text`                                | Name of the user domain. See [Domain  |
|                                       |                                       |                                       | integration: The                      |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10105757). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UserWhiteList                         | `Email`                               | `Text`                                | User email allowlist. See [Share: The |
|                                       |                                       |                                       | Essentials](https://support.          |
|                                       |                                       |                                       | google.com/appsheet/answer/10104983). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UXSettings                            | `BackgroundImageUrl`                  | `Text`                                | URL of the background image. See      |
|                                       |                                       |                                       | [Display images, documents, and audio |
|                                       |                                       |                                       | files](https://support.               |
|                                       |                                       |                                       | google.com/appsheet/answer/10107317). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UXSettings                            | `HideSystemButtons`                   | `Yes/No`                              | Setting that specifies whether system |
|                                       |                                       |                                       | actions are hidden. See [Use system   |
|                                       |                                       |                                       | actions](https://support.             |
|                                       |                                       |                                       | google.com/appsheet/answer/10108131). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UXSettings                            | `LogoUrl`                             | `Text`                                | URL of the logo image. See [Display   |
|                                       |                                       |                                       | images, documents, and audio          |
|                                       |                                       |                                       | files](https://support.               |
|                                       |                                       |                                       | google.com/appsheet/answer/10107317). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UXSettings                            | `PhotoResolution`                     | `Text`                                | Resolution used for images. See       |
|                                       |                                       |                                       | [Capture                              |
|                                       |                                       |                                       | images](https://support.              |
|                                       |                                       |                                       | google.com/appsheet/answer/10106529). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UXSettings                            | `RespectShowIfEverywhere`             | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | **Apply show-if constraints           |
|                                       |                                       |                                       | universally** is turned on. See       |
|                                       |                                       |                                       | [Scope of                             |
|                                       |                                       |                                       | Show_If](https://support.             |
|                                       |                                       |                                       | google.com/appsheet/answer/10106628). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| UXSettings                            | `ShowPreviewRollouts`                 | `Yes/No`                              | Setting that specifies whether        |
|                                       |                                       |                                       | the **Preview new features** setting  |
|                                       |                                       |                                       | is turned on to gain access to app    |
|                                       |                                       |                                       | features that are in the [AppSheet    |
|                                       |                                       |                                       | preview                               |
|                                       |                                       |                                       | program](https://support.             |
|                                       |                                       |                                       | google.com/appsheet/answer/13270531). |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+

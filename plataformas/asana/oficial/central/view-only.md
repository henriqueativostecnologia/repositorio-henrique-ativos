---
fonte: https://help.asana.com/s/article/view-only?language=en_US
baixado: 2026-11-10
---

# View only

**Available on Asana** [**Enterprise**](https://asana.com/enterprise) **and** [**Enterprise+**](https://asana.com/enterprise) **tiers. View only licenses are not available in divisions.**

****Visit our [pricing page](https://asana.com/pricing) for more information.****

With view only licenses, billing owners will have the ability to streamline their license management while ensuring that teams across the organization have visibility into work happening in Asana, even if they rely on different tools. With view only, people across the organization will have visibility across goals, reporting, portfolios and projects, helping teams stay aligned.

View only users can see any Asana object they are given access to but cannot collaborate or take any actions, such as commenting on or editing objects.

## View only functionality access

|                                                       |                             |                       |
|-------------------------------------------------------|-----------------------------|-----------------------|
| **Action**                                            | **Full Enterprise license** | **View only license** |
| View projects, tasks, and inbox                       | ✅                          | ✅                    |
| Be assigned a task                                    | ✅                          | ✅                    |
| Search for tasks and projects                         | ✅                          | ✅                    |
| Share tasks and messages                              | ✅                          | ✅                    |
| Invite new users to domain                            | ✅                          | ✅                    |
| Like tasks and messages                               | ✅                          | ✅                    |
| View goals, portfolios, and reporting views           | ✅                          | ✅                    |
| API access                                            | ✅                          | ✅ (Read-only)        |
| View teams and user profiles                          | ✅                          | ✅                    |
| Create or edit goals, portfolios, and reporting views | ✅                          | ❌                    |
| Create or edit tasks and projects                     | ✅                          | ❌                    |
| Complete tasks                                        | ✅                          | ❌                    |
| View Home and My tasks                                | ✅                          | ❌                    |
| Add comments                                          | ✅                          | ❌                    |
| Use Asana's mobile app                                | ✅                          | ❌                    |
| Integrations access                                   | ✅                          | ❌                    |
| Use Smart Chat                                        | ✅                          | ❌                    |

## Viewing a license type from the admin console

Admins and super admins can navigate to the **Members** tab and filter users by their license.

### To filter users:

1.  Navigate to the **Members** tab in the admin console
2.  Click the **License** drop-down
3.  Use the **Type** filter to view who is an admin, super admin, billing owner, or member.
4.  You can see how many members there are depending on the license

From the **Members** tab, you can also view who invited the user to Asana in the **Invited by** column.

## Inviting new members

When admins and super admins invite new members to Asana, they can choose from a **View only** or an **Enterprise** license.

### To invite a new user:

1.  Navigate to the **Members** tab in the admin console
2.  Click **Invite** in the top-right corner
3.  Fill out the details
4.  Choose from an **Enterprise** or a **View only** license
5.  Click **Send**

## Scale provisioning of view only users

Admins and super admins can quickly add new view only license users through the [CSV user import](https://help.asana.com/s/article/csv-user-import?language=en_US). Super admins can add new view-only users via automated provisioning using SCIM 2.0 with identity providers like Microsoft Azure Entra ID and Okta.

### SCIM provisioning for view-only licenses

**Prerequisites:**

- Enterprise or Enterprise+ plan with view only licenses enabled
- Service Account configured in your Asana domain ([learn more](https://help.asana.com/s/article/service-accounts))
- SCIM connector set up in your identity provider

Asana supports SCIM 2.0 provisioning to automatically assign view only licenses to users based on their attributes in your identity provider. This is accomplished using the **userType** attribute in SCIM requests.

**Supported userType values:**

- "**enterprise**" - Assigns a full Enterprise license
- "**view only**" - Assigns a view only license

### Microsoft Azure Entra ID Configuration

To configure view only license provisioning in Azure Entra ID:

1.  **Set up the Asana connector** following [Microsoft's tutorial](https://learn.microsoft.com/en-us/entra/identity/saas-apps/asana-provisioning-tutorial)

2.  **Configure attribute mapping:**

- Navigate to **Provisioning** \> **Mappings** in your Asana application

- Add a new attribute mapping for **userType** as a String field

- Map this attribute to app role assignments

3.  **Create app roles:**

- "Asana Enterprise" - for users who should receive Enterprise licenses

- "Asana View Only" - for users who should receive view only licenses

4.  **Assign users to app roles** based on your organizational needs

5.  **Test the provisioning** with a small group before full deployment

For detailed step-by-step instructions including expression mapping, contact your account executive or [support team](https://help.asana.com/s/#chat).

### Okta Configuration

To configure view only license provisioning in Okta:

 

1.  **Configure the Asana SCIM connector** in your Okta admin console

2.  **Set up attribute mapping** to map user attributes to the **userType** field

3.  **Configure group assignments** to automatically assign the appropriate license type based on group membership

4.  **Test provisioning** before enabling for all users

For implementation guidance, contact your account executive or [support team](https://help.asana.com/s/#chat).

### Additional provisioning resources

- [SCIM API documentation](https://developers.asana.com/docs/scim) - Technical reference for developers

- [Provisioning and deprovisioning members with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) - General SCIM setup guide

**Note:** Changes to user license types through SCIM may take a few minutes to take effect in Asana.

## License settings

Admins and super admins can take action over a member’s license.

1.  From the **Members** tab in the admin console, click the three dot icon to the right of a member’s name.
2.  Under **License settings,** you’ll see two options: **View only** and **Pause license**.

### What’s the difference between pausing a license and view only?

When pausing a license, you reduce the number of paid seats by one without permanently removing users. The users' data will be kept, and once they log back in, they will be unpaused automatically and once again take up a paid seat.

A view only license grants users limited access to specific elements in Asana, and users with view only licenses won’t be able to collaborate. If they’d like to collaborate in Asana, they will need to request a license to take up a paid seat.

> You can’t pause view only licenses.

## Requesting an Enterprise license

If you have a view only license and want to request an Enterprise license to collaborate with team members in Asana, click the **Request upgrade** button next to your profile picture.

You’ll be prompted to fill out a request reason, and your admin will be notified to approve your request.

You'll receive an email once your request has been approved or rejected.

Admins and super admins can view the pending user requests from the **Members** tab in the admin console. Click **Review** to view the requests.

### Setting a location for members to request license upgrade

Admins and super admins can set a location for users to request a license upgrade. This also applies to other types of requests like access. 

#### To set a location:

1.  Open the admin console
2.  Navigate to the **Security** tab
3.  Under **Membership & invites** click **Request management**

The **request management** setting in the a**dmin console** controls where license upgrade requests are submitted and reviewed. This setting is specifically scoped to license-related requests, such as when a user needs to upgrade from a view-only license to a full member license. It does not function as a general access control gate or determine who is permitted to enter your Asana organization.

From here, you can choose from two options:

- **In Asana**: Members will submit requests in Asana
- **External URL**: Members will be directed to a specific URL to submit requests

If you choose **External URL** you need to paste the URL in the text box. Then, you can test it.

 

> Once you save the changes for requests, the destination for requests will be immediately updated. This will make no changes to existing pending requests.

## Frequently asked questions

### What can view only license holders do in Asana?

View only users can view projects, tasks, goals, portfolios, and reporting views they're given access to, search for work, and be assigned tasks, but they cannot create or edit content, add comments, or use Asana's mobile app.

### What's the difference between pausing a license and assigning a view only license?

Pausing a license temporarily removes a paid seat and automatically unpauses when the member logs back in, while a view only license grants permanent limited access without collaboration capabilities, and view only licenses cannot be paused.

### Can view only users use Asana's mobile app?

No, view only license holders cannot use Asana's mobile app and must access Asana through the web browser.

### How can a view only user request an Enterprise license?

View only users can click the "Request upgrade" button next to their profile picture, fill out a request reason, and wait for their admin to approve or reject the request via email notification.

 

*View only licenses are available in* [*Enterprise*](https://asana.com/enterprise) *and* [*Enterprise+*](https://asana.com/enterprise) *plans. View only licenses are not available in divisions.*

[](https://forum.asana.com/c/forum-en/tips/6)

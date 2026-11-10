---
fonte: https://help.asana.com/s/article/setting-up-asana-roles-in-okta-with-scim?language=en_US
baixado: 2026-11-10
---

# Setting up Asana roles in Okta with SCIM

**Available to organizations on an [Enterprise+](https://asana.com/enterprise) plan.**

## Before you begin

- Make sure that [Asana’s Okta integration has already been added to your Okta account and is set up](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim?language=en_US#gl-provisioning). 
- Make sure you’re an Okta administrator who has the scope to Add/Update Groups and Applications, and create custom attributes.

If you set up Asana roles in Okta, any changes you make in the admin console to user roles will be overridden when an update to that user’s information in Asana triggers. We recommend that you choose to manage roles solely in Asana or solely in Okta.

## Setting up ‘roles’ attribute

Go into the Asana Application, navigate to the **Provisioning** tab, then go to **Profile Editor**, and click **+ Add Attribute**.

You should create an exact copy of this attribute. Make sure the following fields are as follows:

- Data type: string array
- Display name: role
- Variable name: asana_role
- ​​External name: roles.^\[primary==true\].value
- External namespace: urn:ietf:params:scim:schemas:core:2.0:User

Check the **Define enumerated list of values checkbox**. 

In **Attribute members**, add the names of the roles that represent all the Asana roles you have. This will include, at a minimum, the standard roles (Admin, Member) and any additional custom roles you might have.

> ‘Guest’ is not a supported role in Okta. Because guests are users who have an external email domain, they cannot be assigned through SCIM through Okta for Asana. 

Switch over to the Asana Admin console and go to the **Manage roles** tab. Click on the **three dot icon** and click on **‘Copy ID**’.

Go back to Okta and copy and paste the ID into the **Value field** in each of the respective roles under **Attribute members**. Make sure each role ID you’re copying from maps to the correct role you just added to Okta.

1.  Set the **Attribute Type** to ‘**Group’**
2.  Set the **Group Priority** to ‘**Combine values across groups’**
3.  Click **Save**

> Leaving the **Attribute Type** as **Group** would allow you to configure roles on a group basis. Choose **Personal** if you want to manage roles on a user basis only.

## Setting up Okta assignment groups and mapping them to your custom attribute

Go to the **Groups** tab and click on **+ Add Group**. 

Add a group for each role: Admin, and Member (and other custom roles you may have).

Then, assign the Asana application to the group.

1.  Click into the group
2.  Go to the **Applications** tab
3.  Select **Assign applications**

While assigning, set the value of the newly created **Role** attribute to match the role group. 

Click **Save and Go Back.** Repeat this process for all the groups you’ve created.

> Only select one role per group.

## Assigning role groups to people

In each role group, go to the **People** tab and click **Assign people**.

Click on **Advanced search** and use filters to bulk assign the right users to the group or search for users individually.

Click the **+** icon to the right of the user's name to assign them to the corresponding group. Click **Done**. 

Repeat this process to assign all the users to the correct group.

# Changing roles individually

Go to the **People** tab and either filter or search for the user you want to change.

Go to the **Groups** tab of the user, search for the role group you want to put them in, and click on the group. Then, click on the **‘x’** icon to remove the user from the old role group.

The user is now assigned to a different role group, and their role in Asana will be changed to the role that group is mapped to.

# Ranking role priorities

Asana currently supports one role per user. When users are assigned to multiple roles (i.e., Admin and Member) in Okta, the role they get will default to the role group that is highest in priority. We suggest ranking roles with elevated permissions higher in the priority list, so that if a user is both a Member and Admin, their role will default to Admin. If you have custom roles set up, place the custom role with more permissions higher in the priority list. Under the Asana application in **Applications**, go to **Assignments,** then **Groups.** Reorder the groups by priority by using the handle on the side of the card.

> If you have Okta groups set up for Asana licenses (Enterprise or View-only), we require you to order the groups by placing license groups on top of the list (i.e., Enterprise above View Only), followed by the Roles-related groups in the priority order described above (e.g, Admin above Member).

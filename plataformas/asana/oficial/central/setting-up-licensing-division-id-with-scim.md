---
fonte: https://help.asana.com/s/article/setting-up-licensing-division-id-with-scim?language=en_US
baixado: 2026-11-10
---

# Setting up Licensing Division ID with SCIM

The Licensing Division ID feature allows Enterprise and Enterprise+ organizations to use SCIM provisioning to automatically assign users to divisions in Asana. When configured, your identity provider maps each user to a specific division using the **licensingDivisionId** attribute, which corresponds to the unique numeric ID of a division in your Asana organization. 

For more information about creating and managing divisions, see [Divisions in paid organizations](https://help.asana.com/s/article/divisions-in-paid-orgs).

#### Related articles

- [Divisions in paid organizations](https://help.asana.com/s/article/divisions-in-paid-orgs)
- [License assignment in divisions](https://help.asana.com/s/article/license-assignment-in-divisions)
- [A guide to divisions in Asana](https://help.asana.com/s/article/a-guide-to-divisions-in-asana)
- [Provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim)
- [Setting up Asana roles in Okta with SCIM](https://help.asana.com/s/article/setting-up-asana-roles-in-okta-with-scim)

## Before you begin

To use this feature, your organization must be on the Enterprise or Enterprise+ tier and have SCIM provisioning already configured with your identity provider. You will need the division IDs for each division in your Asana organization. These IDs are numeric strings visible in the Asana admin console and are used as the mapped values in your identity provider.

## Find your division IDs

Before configuring your identity provider, collect the division IDs from the Asana admin console. Open the **Admin console** and select **Divisions** from the left navigation. For each division, note the numeric ID associated with it. These IDs are the values you will map to users in your identity provider to ensure correct division assignment upon provisioning.

## Set up licensingDivisionId in Okta

### Add the attribute to your Okta profile

- Open your Asana app in Okta and go to **Profile Editor**.
- Click **Add Attribute**.

&nbsp;

- Set **Data type** to string.
- Set **Display name** and **External name** to licensingDivisionId.
- Set **External namespace** to urn:ietf:params:scim:schemas:core:2.0:User.
- Turn on **Enum** and add one value for your organization and one value for each division ID.
- Set **Attribute required** to **Yes**, **Attribute type** to **Group**, and **Mutability** to **READ_WRITE**.
- Click **Save Attribute**.

### Map the attribute to groups

- In **Profile Editor**, open **Mappings**.
- Find the **licensingDivisionId** row and map each Okta group to the correct division value.
- On the app page, click **Assign to Groups**.
- Select each group, click **Assign**, and then click **Done**.

## Set up licensingDivisionId in Microsoft Entra ID

### Configure the attribute mapping

1.  Open your Asana app in the Azure portal and go to **Provisioning**.
2.  Open **Attribute Mapping (Preview)**.
3.  Find the **licensingDivisionId** target attribute and add or edit the mapping.
4.  Set **Mapping type** to **Expression**.
5.  Enter a Switch() expression that maps your source attribute, such as department, to the correct Asana division IDs. For example: Switch(\[department\], "OrgID", "Division 1 name", "Division1ID", "Division 2 name", "Division2ID"). 
6.  Set **Default value** if null to your organization-level ID so that users without a matching value are assigned to the organization by default.
7.  Set **Target attribute** to **licensingDivisionId**.
8.  Set **Match objects using this attribute** to **No** and **Apply this mapping** to **Always**.
9.  Click **Ok** to save.

## Verify the configuration

After completing the setup in your identity provider, trigger a SCIM sync or provision a test user to confirm that the **licensingDivisionId** value is being sent correctly. In the Asana admin console, open the **Users** section and check that provisioned users appear under the correct division in the **Division** column. If a user appears without a division assignment, review the attribute mapping in your identity provider to ensure the correct division ID is being passed.

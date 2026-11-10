---
fonte: https://help.asana.com/s/article/ip-allowlisting-in-asana?language=en_US
baixado: 2026-11-10
---

# IP allowlisting in Asana

**Available on Asana [Enterprise+](https://asana.com/enterprise). Visit our [pricing page](https://asana.com/pricing) for more information.**

IP Allowlisting enhances your organization's security by restricting access to your Asana organization from only specified IP addresses or ranges. This ensures that only users connecting from approved networks can access your Asana organization.

## Key features

- **Super admin configuration**: Only super admins can enable or modify IP allowlisting settings. To activate this feature, the super admin must include their own IP address in the allowlist.
- **Customizable IP ranges**: Define specific IP addresses in IPv4 or IPv6 format, or include any ranges in CIDR notation.
- **User-level restrictions**: Apply IP restrictions to all users, only organization members, or only guests.
- **API** **Restrictions:** Choose to apply IP restrictions to API traffic

## Configuring IP allowlist

To  enhance your organization's security by restricting access to approved IP addresses, follow these steps:

1.  Navigate to the admin console

2.  Under the **Security** section, locate the **IP Allowlisting** settings

3.  Next, define your IP allowlist settings.
    1.  Set to apply settings to all users, only members, or only guests
    2.  Name and IP address or range/s

4.  Save settings
    1.  Ensure your current IP address is included in the allowlist.
    2.  Click Save to apply the changes.

5.  Ensure you have checked the box **Enable allowlist** which will start enforcing access based on the entered IP addresses or ranges.

When a user tries to access your organization on a non-approved IP they will be asked to join on an approved network.

 

## Managing API Access

By default, IP allowlisting applies to browser-based access only. To also restrict API traffic, you must separately enable the “**Apply to API traffic”** option. This setting is off by default and independent of your main allowlist toggle — enabling IP allowlisting alone does not restrict API access.

When enabled, API traffic filtering applies to all programmatic access to your domain, including:

- Personal Access Tokens (PAT)
- OAuth apps (third-party and custom integrations)
- Service accounts
- SCIM and other identity provider provisioning endpoints

**When to use this setting**

API traffic filtering works best when your organization controls the network that API requests originate from. Good fits include:

- Organizations that route all app integrations through a corporate network or proxy, keeping IP addresses stable and predictable
- Organizations that have disabled third-party app access and only use internally managed integrations
- High-security environments where all programmatic access must be network-restricted for compliance purposes

**When to avoid this setting**

We do not recommend enabling API traffic filtering if your organization uses cloud-hosted apps or public integrations. These services use dynamic IP addresses that change frequently and are not under your control. Enabling this setting in those environments will likely cause integrations to stop working.

If you want to restrict which apps and integrations can access your domain without relying on IP addresses, we recommend using Asana's [**App Management and Integrations** controls. This feature p](https://help.asana.com/s/article/app-management-and-integrations?language=en_US)rovides administrators with robust tools to control and monitor third-party applications connected to their organization's Asana environment. This includes capabilities such as viewing connected apps, setting global app permissions, blocking or approving specific apps, and managing personal access tokens.

## Frequently Asked Questions

### Can I use IP Allowlisting without being a super admin?

No. Only Super Admins can configure or modify IP Allowlisting settings.

### What happens if two super admins are editing the IP Allowlist at the same time? 

Each Super Admin’s update will be reflected simultaneously. To avoid conflicts, it’s best to only have one super admin editing the settings at a time.

### What happens if a user's IP isn't on the allowlist?

They will be denied access to Asana until their IP is added to the allowlist.

### Can I specify IP ranges instead of individual IP addresses?

Yes. Asana supports both individual IP addresses and CIDR-formatted IP ranges (e.g., 192.168.1.0/24).

### Can I apply IP restrictions only to guests or members?

Yes. You can scope restrictions to all users, only members, or only guests.

### What if I forget to include my own IP when setting up the allowlist?

The system requires the Super Admin's current IP to be included to save or enable the settings.

### Does IP Allowlisting affect API or SCIM access?

Not by default, only if you choose to opt-in API traffic. If so, API and SCIM requests will be subject to IP restrictions. You may also choose to manage API access through Asana's App Controls and Permissions features.

[](https://forum.asana.com/c/forum-en/tips/6)

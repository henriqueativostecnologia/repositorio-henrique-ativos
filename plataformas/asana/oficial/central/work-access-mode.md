---
fonte: https://help.asana.com/s/article/work-access-mode?language=en_US
baixado: 2026-11-10
---

# Work access mode

**Available on Asana **[Enterprise](https://asana.com/enterprise)** and **[Enterprise+](https://asana.com/enterprise)** tiers. Visit our **[pricing page](https://asana.com/pricing)** for more information.**

**Work access mode is not available to divisions.**

Work access mode allows super admins to access both public and private work content within Asana. With this feature, super admins can use advanced search to locate tasks, projects, and portfolios across the organization, even if they're private. Previously, super admins could only view private tasks or projects if they had been added to them directly. Work access mode removes this limitation, giving super admins full visibility when needed.

## Benefits of work access mode

Work access mode is especially useful in situations like employee onboarding, offboarding, or team and role transitions, where access to current or past work is critical for ensuring business continuity and maintaining organizational security. It also allows super admins to assist other team members by granting access to relevant tasks or projects when needed.

Super admins can also search for content created by removed users using advanced search in work access mode.

## Important considerations

- Before making changes to private content accessed through Work Access Mode, you must first join the object (project, team, or task). Attempting to create status updates, edit projects, or make other changes without joining will cause Asana to crash with error messages. See [working with private content](https://help.asana.com/s/article/work-access-mode#working-with-private-content) below for more detail.
- We recommend that super admins use work access mode only for essential business needs. For personal professional use of Asana, super admins should disable work access mode to maintain appropriate access levels.
- Currently, work access mode applies to tasks within projects, projects themselves, as well as portfolios.
- Editing or creating rules on portfolios is not currently supported inside work access mode.

## Enabling work access mode

To enable work access mode:

1.  Navigate to the admin console

2.  Click **Launch Asana** in the left pane

3.  Select **Work access mode**

## Session length

Super admins can use work access mode for up to 30 minutes, but can extend their session if needed. 5 minutes before the session ends, a message will appear which asks you to either end the session or extend it. Clicking **Extend session** will extend work access mode by 30 minutes.

## Working with private content

While Work Access Mode allows super admins to view private tasks, projects, and portfolios across the organization, **making changes** to private content requires additional steps to ensure proper permissions.

### Joining Requirements

Before making any changes to private content accessed through Work Access Mode, you must first join the object (project, team, or task). Attempting to create status updates, edit project details, or make other changes without joining will result in the application crashing or displaying error messages.

Actions which require joining the object:

- Creating or editing status updates on private projects
- Editing project descriptions, names, or settings
- Adding or modifying tasks within private projects
- Changing project members or permissions
- Creating rules or custom fields on private projects

Actions which do not require joining the object:

- Viewing private content (tasks, projects, portfolios)
- Searching through private content using advanced search
- Reading project descriptions and status updates
- Viewing task details and comments

### How to join objects

To join a private object while using Work Access Mode:

1.  Navigate to the private project, portfolio, or task you need to edit
2.  Click the **Share** button or **Members** section
3.  Add yourself as a member with appropriate permissions (**Editor** or **Admin** access)
4.  Once you've joined, you can safely make the required changes

Remember: Work Access Mode is designed for viewing and accessing content. Making changes still requires following standard Asana permission protocols.

## Exiting work access mode

** **

After super admins have finished accessing the necessary content, they should exit work access mode by selecting **Turn off** in the top bar. This will successfully disable work access mode and return the admin to normal viewing permissions.

[ ](https://forum.asana.com/c/forum-en/tips/6)

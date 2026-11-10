---
fonte: https://support.google.com/appsheet/answer/12193489?hl=en
baixado: 2026-11-10
---

# Reuse automation components

AppSheet Automation enables *reusability*, allowing you to build components once and reuse them in various automations to save time and accelerate development. You can create events, processes, tasks, and actions that can be reused in other components. For example, you can reuse actions and tasks within new processes, reuse events and processes within new bots, and so on.

Manage component reuse as described in the following sections:

- [Enable or disable automation component reuse](#enable)
- [Reuse an automation component](#reuse)
- [View the linked components](#view-number)
- [View all reusable components](#view-all-reusable-components)
- [Edit or delete a reusable component](#eidt-linked-component)
- [Disable reusability for an automation component](#disable)

## Enable or disable automation component reuse

Automation component reuse is:

- Disabled by default when you create a component within a bot.
- Enabled by default when you create a component as a stand-alone component (for example, Automation \> Events).

When configuring a component within a bot, you can enable reuse by expanding the **Linking** panel and enabling the **Linking** setting. For events and tasks, the Linking panel appears in the Settings panel, as shown:

For processes, the Linking panel appears in the center edit pane.

You can also enable or disable linking when [viewing all reusable components](#view-all-reusable-components)

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

When configuring an automation component from the relevant tab (for example, Automation \> Tasks), you can enable reuse by expanding the **Linking** panel and enabling the **Linking** setting, as shown:

**Note for processes**: You can enable or disable reusability for a process only by using the **Automation \> Processes** tab. To [view all reusable and non-reusable processes](#all-reusable), click **Show unlinked.** (Non-reusable processes are hidden, by default.)

Similarly, when configuring an automation component within a bot, you can enable reuse by expanding the **Linking** panel and enabling the **Linking** setting in the Settings panel, as shown:

**Note for actions**: You can enable or disable reusability for an action only by using the Settings panel when configuring the action. 

To disable automation component reuse, disable the toggle.

## Reuse an automation component

When you [*enable automation component reuse*](#enable), that component will be included as a suggestion when adding components to your bots.

For example, when adding a new task to a process, the relevant reusable automation components are listed as suggestions:

Weekly Inspection: Send Email shown under Reuse an Existing Task

To reuse a process, when editing a bot, select **Swap** in the **Then run...** drop-down and select a linkable process in **Select a linkable process** dialog. 

## View the linked components

 View the linked components that are currently using the component in the Linking panel. 

For example, in the component **Settings** panel, you can:

- View the number of linked components in the linking lozenge
- Expand the Linking panel to view the full list of linked components
- Click a linked component to navigate to it in the relevant component tab

Settings pane with 1 linked component identified in the lozenge and in the list

## View all reusable components

After you enable at least one reusable (or linkable) component for a type (event, process, or task), you can view all reusable components of a given type by selecting the type in the fly-out menu. For example, select **Automation \> Tasks** to view all reusable tasks.

View all reusable components

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

## If you are using the legacy editor

 View all reusable and non-reusable components on the relevant tabs (such as, **Automation \> Processes**).

Reusable components display the number of linked components in the linking lozenge. Non-reusable components do not display the lozenge. To show only reusable components, click **Hide unlinked**. Then, to show all components, including non-reusable components, click **Show unlinked**.

View all reusable components from the automation tabs and toggle display of not linked components

## Edit or delete a reusable component

When editing or deleting a reusable component, your changes affect all linked components. Ensure that your changes do not negatively impact the operation of the linked components.

Before you delete a reusable automation component, consider removing the component from other bots or processes that use it.

## If you are using the legacy editor

 If you try to delete a reusable component that is used by one or more bots, AppSheet will prompt you to confirm the operation. For example:

Warning displayed for reusable component when attempting to delete

## Disable reusability for an automation component

Before you disable reusability for an automation component, consider removing the component from other bots or processes that use it. See [*View the linked components*](#view-number).

 When configuring an automation component, disable reusability by selecting **More**   **\>** **Disable linking** in the **Settings** panel.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy editor

 To disable reusability:

- When editing a component on its relevant tab (such as, Automation \> Tasks), expand the component, expand the **Linking** panel, and disable the **Linking** toggle.

   
- When editing a component within a bot, expand the **Linking** panel in the **Settings** panel, and disable the **Linking** toggle.

  Linking OFF in Settings pane

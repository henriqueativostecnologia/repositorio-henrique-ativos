---
fonte: https://support.google.com/appsheet/answer/12407883?hl=en
baixado: 2026-11-10
---

# Explore the desktop design

AppSheet's desktop design is optimized for desktop browsers, presenting a more complete view of information with a consistent organization and structure. The desktop design lets users navigate their apps more easily and access information in context, and provides an efficient way to edit existing records without losing context.

The desktop design isn't used for apps viewed on mobile devices. In this case, the app is optimized for the mobile device.

The following provides an example of the desktop design:

 

As highlighted in the previous figure, with the desktop design:

- The left navigation bar contains links to both [primary and menu views](https://support.google.com/appsheet/answer/10106688#view-location-position). Users can expand or collapse the navigation bar. When collapsed (as shown), icons and tooltips enable users to easily identify the views.
- The collection (card, deck, gallery, or table) and detail views display in separate panels on the same page. To adjust focus, users can expand to a tabbed view or resize the view panels. The desktop layout is customizable for detail views when [configuring the detail view options](https://support.google.com/appsheet/answer/10106385#configure-view-options). When you configure a detail view to [include Show type columns](https://support.google.com/appsheet/answer/10107387#detail-view), [Page headers](https://support.google.com/appsheet/answer/10107388#configure-page-headers) appear as the title of each card in a detail. (On mobile devices, page headers don't appear, only secondary headers.)
- Users can filter a collection view by its grouped items (configured using the **Group by** setting).
- Primary actions for a view appear in the top navigation bar in the panel.
- When editing row content, you can customize the editing experience to allow users to edit the content in place or edit content in a separate form. For more information, see the [**Desktop behavior **option](https://support.google.com/appsheet/answer/10107706#app-edit-this-row).
- Users can view detailed information as card blocks within a detailed view (configured using [Show type](https://support.google.com/appsheet/answer/10106435#show) columns in a table). See [Configure card blocks in detail views to optimize the desktop design](https://support.google.com/appsheet/answer/10106385#configure-card-blocks).
- You can customize the color of individual icons using [format rules.](https://support.google.com/appsheet/answer/10106703)

The following sections provide more information about the optimized desktop design:

- [Limitations and known issues](#limitations-known-issues)
- [Optimize existing apps for the desktop design](#best-pratices-configure-app)
- [Use the legacy desktop design](#legacy-desktop)

## Limitations and differences

The following features are not currently supported in the desktop design:

- [Smart Assistant](https://support.google.com/appsheet/answer/10104391)
- The Share button is not available. To share a view, copy and paste its URL. Recipients must have access to the app.

The following lists the differences with the new desktop design from the mobile experience:

- The [Text size](https://support.google.com/appsheet/answer/10106612#settings) style setting isn't supported at this time.
- For [grouped actions](https://support.google.com/appsheet/answer/10107706#composite&zippy=%2Cgrouped-execute-a-sequence-of-actions):
  - Only one [navigation action](https://support.google.com/appsheet/answer/10107706#navigate) or [external action](https://support.google.com/appsheet/answer/10107706#external-communication) is executed, even if you specify more than one. It also ends the execution of the grouped action.
  - [Validations rules](https://support.google.com/appsheet/answer/10107949) are enforced in each step of the grouped action.
- When [grouping by header](https://support.google.com/appsheet/answer/10106698) in a view, the last group by header doesn't include inline or `REF` view actions.
- When navigating from an app that uses new desktop design or [mobile framework](https://support.google.com/appsheet/answer/15831909) to one that doesn't, or vice-versa, the option to return to the previous app will no longer appear in the app menu. If your app links to other apps we suggest using consistent settings for the new desktop design and mobile framework across all of them.
- [Background images](https://support.google.com/appsheet/answer/10106612) are currently not supported

## Optimize existing apps for the desktop design 

Consider the following to optimize existing apps for the desktop design:

- **Reconsider your use of dashboard views**
  For example, you may have used the [dashboard view](https://support.google.com/appsheet/answer/10106384) to present more information on a single page. With the optimized desktop design, this level of information is provided by default, without the use of a dashboard view.
- **Revisit design elements implemented to improve the legacy desktop experience**
  You may have configured design elements to improve the layout in the legacy desktop. These elements may no longer be needed.
- **Test the app interactions thoroughly**
  You may discover areas in the app where you want to make minor changes.

## Use the legacy desktop design

The legacy desktop design provides an experience similar to the mobile and tablet device.  The following provides an example of the legacy desktop design for a detail view:
 

As highlighted in the previous figure:

- Detail views display on a page separate from the collection view. Users need to navigate back to see the collection view.
- The navigation bar for [primary views](https://support.google.com/appsheet/answer/10106688#view-location-position) appears at the bottom of the screen. Navigation for [menu views](https://support.google.com/appsheet/answer/10106688#view-location-position) appears in a drop-down (accessible only from the collection view). 
- Primary actions appear as overlay (floating) icons. 

 When you create a new app, you are opted in to the optimized desktop design. You can continue to use the legacy desktop design in your app by disabling the optimized desktop design. When [configuring general settings for views](https://support.google.com/appsheet/answer/10107387#general-settings), **turn off** the **Desktop mode** setting in the **General** section.

On the UX Options pane, the Desktop mode (Preview) toggle is highlighted

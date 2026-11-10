---
fonte: https://support.google.com/appsheet/answer/10108214?hl=en
baixado: 2026-11-10
---

# Run actions based on view events

View events allow you to specify [actions](https://support.google.com/appsheet/answer/10107706) to run when certain events occur, such as selecting a row in a table view or saving a form. These actions can replace default navigation behaviors, enabling you to create streamlined custom navigation within your apps.  

The following sections describe how to run actions based on view events:

- [Supported view event types](#event-type)
- [Configure an event action](#configure-event-action)

**Notes**:

- Multiple actions for one event can be combined by providing a [grouped action](https://support.google.com/appsheet/answer/10107706#composite).
- Not all view types currently support event actions.
- To configure Form Saved events, you may need to create a new form [reference view](https://support.google.com/appsheet/answer/10106516) first.
- Actions based on different tables than the view will not appear in the drop-down. If you don't see an action in the list, make sure the data sources match.

## Supported view event types

The following view event types are supported:

- [Row selected (table, deck, and gallery views)](#row-selected)
- [Form saved (form views)](#form-saved)

### Row Selected (deck, gallery, and table views)

The **Row Selected** event is triggered when a user taps on an individual record in a deck, gallery, or table view. If you specify an action, it will replace the default behavior of viewing the record details in a detail view (even if the action does not cause its own navigation). Example use cases include the following:

- Navigating directly to the edit form when selecting a row
- Quickly changing the value of a status column without the need to open the details view 

### Form Saved (form views)

The **Form Saved** event is triggered when a user saves an add or edit form. If an action is provided that causes navigation, it will replace the default navigation behavior (including auto-reopen and finish view settings). Unlike the row selected event, if a form saved event action is provided that doesn't cause navigation (such as an update row action or a navigation action whose condition is not met), the default navigation behavior will still occur.

## Configure an event action

You can configure event actions within the Behavior view settings for the supported view types.

To configure an event action:

1.  Create the event action, as described in [Actions: The Essentials](https://support.google.com/appsheet/answer/10107706).
2.  [Configure a view](https://support.google.com/appsheet/answer/10106688#configure-view). 
3.  Expand the **Behavior** section and select the action in the  **Event Actions** drop-down for the event type.

**Note**: **Only actions based on the same source table as the view are eligible to be selected as Event Actions**. System-generated actions such as View Map associated with `Address` columns or View Related associated with `Ref` columns can also be selected. The default **Auto assign** option corresponds to the built-in behaviors normally associated with each event.

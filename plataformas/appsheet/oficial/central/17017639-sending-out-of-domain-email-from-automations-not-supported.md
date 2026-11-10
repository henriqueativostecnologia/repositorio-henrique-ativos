---
fonte: https://support.google.com/appsheet/answer/17017639?hl=en
baixado: 2026-11-10
---

# Sending out of domain email from automations not supported

As of **May 4th, 2026**, AppSheet creators who use automations to send emails are only able to send emails to recipients matching the domain that they use to log into AppSheet. 

The specifics of this update are:

- Users who login with a "non-public" email domain (for example, "@customdomain.com"), are now only able to send automation emails to other email addresses within the same domain (“@[customdomain.com](http://customdomain.com)”)
- Users who are part of a Workspace organization are still able to send automation emails to any domains owned by their Workspace organization. 
- Users who login with a "public" email domain (for example, "@gmail.com") are now only able to send emails via automations to their own email address.

We understand there are many current users who may rely on automation email capabilities. For this reason, all users who have created an AppSheet account before **May 4th, 2026**, or that belong to a Workspace organization created before **May 4th, 2026**, have been automatically exempted from this change, meaning that their new and existing automations will not be subject to this restriction.

Users who have created an AppSheet account after **May 4th, 2026**, and do not belong to a Workspace organization created before that date, are subject to this restriction.

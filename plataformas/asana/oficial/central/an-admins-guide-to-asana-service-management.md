---
fonte: https://help.asana.com/s/article/an-admins-guide-to-asana-service-management?language=en_US
baixado: 2026-11-10
---

# An admin’s guide to Asana Service Management

To get Asana Service ready for your team, start by assigning access in the admin console, creating your queues, choosing how requests should come in, and connecting the resources that will support your team. Following that setup order will support your launch with the essentials in place.

Before you start, make sure you have [admin access](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US) in Asana. You will need it to manage licenses, create queues, and configure intake channels.

## AI prerequisites

AI resolutions require Asana AI to be enabled for your domain and for the people submitting requests. Before testing AI resolutions, check domain settings, role permissions, individual user access and AI provide availability.

To enable Asana AI:

1.  Navigate to the **admin console**
2.  Click the **Settings** tab
3.  Select the checkbox to **Enable Asana AI**.

AI resolutions will not function if Asana AI is not enabled at the domain level.

## Assign licences

Before your team can manage requests in Asana Service, assign licenses to the people who will work in your queues.  

Assign licenses from your admin settings before you create your first queue. Starting here helps make sure the right people are ready to access the queue as soon as it is set up.

If you want more control over who can create queues and knowledge bases, [role-based access control](https://help.asana.com/s/article/control-queue-and-knowledge-base-creation-with-rbac) (RBAC) lets you manage this at the organization level. You can create a custom role with the relevant permissions and assign it to the right people. 

### To assign a licence:

1.  Navigate to your admin console and click **Manage users**
2.  Open the user’s settings and click **Licences**
3.  Select the appropriate option next to **Asana Service Management**

## Create a queue

A queue is where your team receives, organizes, and works on tickets. You might create separate queues for teams such as IT, HR, or Finance.

### To create a queue:

1.  In **Service mode**, navigate to **Admin**
2.  Click **Create Queue**
3.  Enter the queue name in **Name your queue** and click **Next** 
4.  Enter a **Category group name** and select or add relevant categories
5.  Click **Create Queue**

From there, you will arrive at the queue settings where you can take further actions like add members to the queue, add custom fields, and set service level agreements.

To add team members to a queue, click **Members** in the queue settings and invite them by name or email. 

To remove team members, find them in the user list and click **Remove from queue**.

> Removing a team member does not delete their past work or auto-reassign their open tickets. You will need to review any open tickets they own and reassign them as needed.

## Configure queue settings

Configure the queue settings that shape how work moves through the queue. This includes [applying categories and custom fields](https://help.asana.com/s/article/how-to-configure-queue-categories-and-custom-fields), [defining ticket statuses](https://help.asana.com/s/article/how-to-configure-ticket-statuses?language=en_US), and [setting service level agreements and team schedules](https://help.asana.com/s/article/configuring-slas-and-work-schedules?language=en_US).

## Set up intake channels

Intake channels decide how people submit requests to your queue. Asana Service Management includes a chat-based portal and a form where users can submit requests directly in Asana. Additionally, you can turn on the channels that best match how your team works.

- Use [email-to-ticket](https://help.asana.com/s/article/using-email-intake-to-create-tickets-in-asana-service-management) when you want messages sent to a dedicated address to become tickets automatically. 
- Use [Slack](https://help.asana.com/s/article/how-to-connect-asana-service-to-slack) when you want employees to submit requests from a channel and receive confirmation there. 

## Connect a knowledge base

A connected knowledge base gives [Service AI](https://help.asana.com/s/article/service-AI-and-your-knowledge-base) the information it needs to handle requests autonomously. Any request that Service AI cannot resolve becomes a ticket and is routed to a queue for a human team member to pick up. 

Learn how to [set up a knowledge base in Asana Service Management](https://help.asana.com/s/article/set-up-a-knowledge-base-in-asana-service-management). 

## View and export AI resolutions ticket data

To view and export AI resolutions data for your tickets, navigate to your admin console and click **AI resolutions** under **Asana AI**. 

From here, you can view your AI resolution usage across all queues, with the ability to filter by queue and time period. You can also toggle the view to see your daily usage.

Export this data to CSV by clicking the **Export** icon at the top of your screen.

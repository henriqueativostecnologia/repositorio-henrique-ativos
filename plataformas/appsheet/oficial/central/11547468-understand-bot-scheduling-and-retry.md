---
fonte: https://support.google.com/appsheet/answer/11547468?hl=en
baixado: 2026-11-10
---

# Understand bot scheduling and retry

The following sections provide details about how AppSheet stores, triggers, executes and retries bots with scheduled events.

- [Store bots with scheduled events](#store)
- [Trigger bots with scheduled events](#trigger)
- [Execute bots with scheduled events](#execute)
- [Retry bots with scheduled events](#retry)

### Store bots with scheduled events

Each bot with a scheduled event is stored as a record in a SQL database. Each record contains the following information:

- Name of the application containing the bot with a scheduled event
- Name of the bot with a scheduled event
- Date and time at which the scheduled event should be triggered

### Trigger bots with scheduled events

The Schedule Service triggers the bot with a scheduled event at the appropriate time. It does this by reading the records from the SQL database and looking for bots with scheduled events that are due to be triggered.

When the Schedule Service finds a bot with a scheduled event that is due to be triggered, it issues a request to the AppSheet service to invoke the scheduled event. The request contains the names of the application and bot with a scheduled event. This allows the AppSheet Service to find and execute the scheduled event.

The Schedule Service then waits for a timeout period of up to five minutes for the scheduled event to complete.

### Execute bots with scheduled events

The AppSheet service is responsible for executing the bot with a scheduled event. When it receives the request from the Schedule Service it uses the names of the application and bot with a scheduled event contained in the request o retrieve the scheduled event and begin executing it.

The AppSheet service records the time the scheduled event begins executing. Periodically, the AppSheet service checks to see if the scheduled event is taking too long to execute. If the total execution time exceeds five minutes, the AppSheet service aborts its execution.

When the bot with a scheduled event completes, the AppSheet service responds to the request and indicates whether the scheduled event completed successfully.

### Retry bots with scheduled events

While the AppSheet service is executing the bot with a scheduled event, the Schedule Service is waiting for the AppSheet service to complete the scheduled event and respond to the request.

If the bot with a scheduled event does not complete within five minutes, the Schedule Service assumes that the scheduled event failed for some reason. A bot with a scheduled event can fail for several reasons including:

- The bot with a scheduled event may be complicated and take a long time to execute. As a result, the bot may exceed the AppSheet service's five-minute timeout period.
- The bot with a scheduled event may be delayed because it is competing with other bots that are scheduled to run at the same time. It is common to schedule bots with scheduled events to run exactly on the hour. This can cause a flood of bots to fire on exactly the hour and result in one bot waiting for other competing bots to complete. This can result in a timeout because the bot is not initiated immediately and does not complete within the Schedule Service's five-minute timeout period. You can mitigate this by scheduling your bot to run at least a few minutes before or after the hour.
- The bot with a scheduled event may be executing on an AppSheet server that is restarted for some reason. This can also cause a timeout.

When the Schedule Service detects that the bot with a scheduled event has not completed within the five-minute timeout period, it will retry its execution up to three additional times. If the Audit History indicates that the bot with a scheduled event is being invoked at five-minute intervals, it is likely that the Schedule Service is retrying its execution.

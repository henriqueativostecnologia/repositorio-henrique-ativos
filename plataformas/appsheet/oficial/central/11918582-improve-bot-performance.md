---
fonte: https://support.google.com/appsheet/answer/11918582?hl=en
baixado: 2026-11-10
---

# Improve bot performance

When you have a performance problem with an automation bot, go to **Manage \> Monitor \> Performance Profile**, click **Launch performance analyzer**, and take a close look at the Performance Profile information and recommendations. See also [Monitor app performance using Performance Profile](https://support.google.com/appsheet/answer/10104997).

For bots with data change events, AppSheet captures the time required to perform each step of the add, update, or delete operation. AppSheet also captures the time required to perform each step of the tasks triggered by the add, update, or delete.

For bots with scheduled events, AppSheet captures the time required to perform each step in the bot.

AppSheet captures the elapsed time down to a resolution of one to two milliseconds. Admittedly the detail can be overwhelming, but the benefit of these very fine-grained measurements is that they provide clear insights into the length of time to complete specific steps in the process.

Often time is being consumed computing virtual columns or expressions. This is especially true if AppSheet needs to read other tables to compute the virtual column or expression. Based on this information, you can implement changes to improve your expressions to make them more efficient.

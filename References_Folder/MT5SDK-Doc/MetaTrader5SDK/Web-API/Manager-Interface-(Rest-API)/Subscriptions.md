[🏠 Document Start](../../README.md) / [Web API](../README.md) / [Manager Interface (Rest API)](../Manager-Interface-(Rest-API).md) / Subscriptions

[Previous](Settings-Files/Delete.md) | [Next](Subscriptions/Data-Structure.md)

# Subscriptions

With the "Subscriptions" service, you can offer additional paid services to traders directly through the client terminals. For example, you can sell subscriptions for high-quality market data from well-known providers, offer personal manager services to assist traders in understanding the basics of trading, deliver one-time services such as position transferring or currency conversion, and much more. For more details, please read the [MetaTrader 5 Administrator Help](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions).

The requests described in this section enable the management of subscriptions on traders' accounts:

Request | Purpose  
---|---  
[/api/subscription/join](Subscriptions/Subscribe.md) | Add a subscription for a user.  
[/api/subscription/cancel](Subscriptions/Unsubscribe.md) | Cancel a user subscription user.  
[/api/subscription/add](Subscriptions/Add-to-Database.md) | Add a user subscription directly to the server database.  
[/api/subscription/update](Subscriptions/Update-in-Database.md) | Edit a user subscription directly in the server database.  
[/api/subscription/delete](Subscriptions/Delete-from-Database.md) | Delete a user subscription directly from the server database.  
[/api/subscription/get](Subscriptions/Get.md) | Get a user subscription user.  
[/api/subscription/exist](Subscriptions/Check-Existence.md) | Check if the user has a subscription to the specified service.  
[/api/subscription/history/add](Subscriptions/Add-to-History.md) | Add a user subscription action directly to the server database.  
[/api/subscription/history/update](Subscriptions/Update-in-History.md) | Edit a user subscription action directly in the server database.  
[/api/subscription/history/delete](Subscriptions/Delete-from-History.md) | Delete a user subscription action directly from the server database.  
[/api/subscription/history/get](Subscriptions/Get-from-History.md) | Get a history of user's subscription actions.  
  
The format, in which the subscription data is passed, is described in the "[Data Structure](Subscriptions/Data-Structure.md)" section.

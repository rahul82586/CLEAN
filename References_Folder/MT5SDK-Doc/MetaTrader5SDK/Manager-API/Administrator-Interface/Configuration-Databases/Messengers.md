[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Messengers

[Previous](Mail-Servers/EmailSend.md) | [Next](Messengers/MessengerCreate.md)

# Integration with instant messengers

The MetaTrader 5 platform features the built-in service for sending messages via different service: SMS, messengers, push servers. This service can be used to verify phone numbers which traders specify when opening accounts via client terminals. For more details, please read the [MetaTrader 5 Administrator Help](https://support.metaquotes.net/en/docs/mt5/platform/administration/integration).

The functions described in this section enable users to manage messenger configurations, as well as to subscribe and to unsubscribe from events related to configuration changes.

Function | Purpose  
---|---  
[MessengerCreate](Messengers/MessengerCreate.md) | Create a messenger configuration object.  
[MessengerCountryCreate](Messengers/MessengerCountryCreate.md) | Create an object of a country for which the messenger will be used.  
[MessengerGroupCreate](Messengers/MessengerGroupCreate.md) | Create an object of an account group for which the messenger will be used.  
[MessengerTemplateCreate](Messengers/MessengerTemplateCreate.md) | Create a message template object that will be used in the messenger.  
[MessengerUnsubscribe](Messengers/MessengerUnsubscribe.md) | Subscribe to events and hooks associated with messenger configurations.  
[MessengerUnsubscribe](Messengers/MessengerUnsubscribe.md) | Unsubscribe from events and hooks associated with messenger configurations.  
[MessengerUpdate](Messengers/MessengerUpdate.md) | Add or update a messenger configuration.  
[MessengerUpdateBatch](Messengers/MessengerUpdateBatch.md) | Add or edit multiple messenger configurations.  
[MessengerDelete](Messengers/MessengerDelete.md) | Delete a messenger configuration by name or index.  
[MessengerDeleteBatch](Messengers/MessengerDeleteBatch.md) | Delete multiple messenger configurations.  
[MessengerShift](Messengers/MessengerShift.md) | Change the position of a messenger configuration in the list.  
[MessengerTotal](Messengers/MessengerTotal.md) | Get the total number of messenger configurations available in the platform.  
[MessengerNext](Messengers/MessengerNext.md) | Get a messenger configuration by index.  
[MessengerGet](Messengers/MessengerGet.md) | Get a messenger configuration by name.  
[MessengerVerifyPhone](Messengers/MessengerVerifyPhone.md) | Verify the validity of a passed phone number based on local phone number formation rules.  
[MessengerSend](Messengers/MessengerSend.md) | Send an SMS message.

[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../Configuration-Databases.md) / Subscriptions

[Previous](Plugins/Get-Module-by-Name.md) | [Next](Subscriptions/Data-Structure.md)

# Subscriptions

With the "Subscriptions" service, you can offer additional paid services to traders directly through the client terminals. For example, you can sell subscriptions for high-quality market data from well-known providers, offer personal manager services to assist traders in understanding the basics of trading, deliver one-time services such as position transferring or currency conversion, and much more. For more details, please read the [MetaTrader 5 Administrator Help](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions).

The following requests are provided for operations with subscription settings in the trading platform:

Function | Purpose  
---|---  
[/api/subscription/config/add](Subscriptions/Add.md) | Add and update a subscription configuration in the trading platform.  
[/api/subscription/config/delete](Subscriptions/Delete.md) | Delete a subscription configuration from the trading platform.  
[/api/subscription/config/shift](Subscriptions/Shift.md) | Change the position of a subscription configuration in the list.  
[/api/subscription/config/total](Subscriptions/Get-Total.md) | Get the number of subscription configurations available in the platform.  
[/api/subscription/config/next](Subscriptions/Get-by-Index.md) | Get one or more subscription configurations by index in the list.  
[/api/subscription/config/get](Subscriptions/Get-by-NameID.md) | Get subscription configurations by a list of IDs or indexes, as well as by name.  
  
The format, in which the subscription configuration data is passed, is described in the "[Data Structure](Subscriptions/Data-Structure.md)" section.

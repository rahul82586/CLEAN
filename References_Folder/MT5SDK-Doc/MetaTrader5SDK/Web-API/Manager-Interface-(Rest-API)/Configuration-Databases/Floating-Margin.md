[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../Configuration-Databases.md) / Floating Margin

[Previous](Symbols/Get-Subgroup-List.md) | [Next](Floating-Margin/Data-Structure.md)

# Floating Margin

In this section, you can configure a list of rules for quick adjustments of client leverages/margin. You can create several profiles and quickly switch between them in the group settings. Thus, the platform enables the implementation of a dynamic leverage, often referred to as a floating leverage, which adjusts based on different conditions. For example, leverage and margin values may vary depending on the volume of positions on the client account, on the day of the week or other conditions. For further details, please see [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/en/docs/mt5/platform/administration/leverages).

The following requests are provided for managing floating margin settings:

Request | Description  
---|---  
[Add](Floating-Margin/Add.md) | Create or update the floating margin configuration on the server.  
[Delete](Floating-Margin/Delete.md) | Delete a floating margin configuration with the specified name.  
[Shift](Floating-Margin/Shift.md) | Change the position of the floating margin configuration in the list.  
[Get total](Floating-Margin/Get-Total.md) | Getting the number of floating margin configurations existing on the trading server.  
[Get by Index](Floating-Margin/Get-by-Index.md) | Get one or more floating margin configurations by index in the list.  
[Get by Name](Floating-Margin/Get-by-Name.md) | Get one or more floating margin configurations by name.  
  
The format in which the symbol configuration data is provided is described in the [Data Structure](Floating-Margin/Data-Structure.md) section.

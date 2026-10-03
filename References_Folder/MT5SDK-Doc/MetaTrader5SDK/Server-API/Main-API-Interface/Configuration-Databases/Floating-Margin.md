[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Floating Margin

[Previous](Subscriptions/SubscriptionCfgGetByID.md) | [Next](Floating-Margin/LeverageCreate.md)

# Floating Margin

In this section, you can configure a list of rules for quick adjustments of client leverages/margin. You can create several profiles and quickly switch between them in the group settings. Thus, the platform enables the implementation of a dynamic leverage, often referred to as a floating leverage, which adjusts based on different conditions. For example, leverage and margin values may vary depending on the volume of positions on the client account, on the day of the week or other conditions. For further details, please see [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/ru/docs/mt5/platform/administration/leverages).

The functions described in this section enable the management of floating margin configurations:

Function | Purpose  
---|---  
[LeverageCreate](Floating-Margin/LeverageCreate.md) | Create a floating margin configuration object.  
[LeverageRuleCreate](Floating-Margin/LeverageRuleCreate.md) | Create an object for a floating margin configuration rule.  
[LeverageTierCreate](Floating-Margin/LeverageTierCreate.md) | Create an object for a floating margin rule rule.  
[LeverageSubscribe](Floating-Margin/LeverageSubscribe.md) | Subscribe to events and hooks related to a floating margin configuration.  
[LeverageUnsubscribe](Floating-Margin/LeverageUnsubscribe.md) | Unsubscribe from events and hooks related to a floating margin configuration.  
[LeverageAdd](Floating-Margin/LeverageAdd.md) | Add or update a floating margin configuration.  
[LeverageDelete](Floating-Margin/LeverageDelete.md) | Delete a floating margin configuration by name and by index.  
[LeverageShift](Floating-Margin/LeverageShift.md) | Change the position of a floating margin configuration in the list.  
[LeverageTotal](Floating-Margin/LeverageTotal.md) | Get the total number of floating margin configurations present in the platform.  
[LeverageNext](Floating-Margin/LeverageNext.md) | Get a floating margin configuration by index.  
[LeverageGet](Floating-Margin/LeverageGet.md) | Get a floating margin configuration by name.  
  
To apply a floating margin configuration to a group, use the [IMTConGroup::MarginFloatingLeverage](../../../Configuration-Interfaces/Groups/IMTConGroup/MarginFloatingLeverage.md) method.

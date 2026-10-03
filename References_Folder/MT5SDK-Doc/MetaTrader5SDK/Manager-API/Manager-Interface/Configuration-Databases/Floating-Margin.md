[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Floating Margin

[Previous](Symbols/SymbolExist.md) | [Next](Floating-Margin/LeverageCreate.md)

# Floating Margin

In this section, you can configure a list of rules for quick adjustments of client leverages/margin. You can create several profiles and quickly switch between them in the group settings. Thus, the platform enables the implementation of a dynamic leverage, often referred to as a floating leverage, which adjusts based on different conditions. For example, leverage and margin values may vary depending on the volume of positions on the client account, on the day of the week or other conditions. For further details, please see [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/ru/docs/mt5/platform/administration/leverages).

The functions described in this section enable the management of floating margin configurations:

Function | Purpose  
---|---  
[LeverageCreate](Floating-Margin/LeverageCreate.md) | Create a floating margin configuration object.  
[LeverageCreateArray](Floating-Margin/LeverageCreateArray.md) | Create an object for a floating margin configuration array.  
[LeverageRuleCreate](Floating-Margin/LeverageRuleCreate.md) | Create an object for a floating margin configuration rule.  
[LeverageTierCreate](Floating-Margin/LeverageTierCreate.md) | Create an object for a floating margin rule rule.  
[LeverageSubscribe](Floating-Margin/LeverageSubscribe.md) | Subscribe to events and hooks related to a floating margin configuration.  
[LeverageUnsubscribe](Floating-Margin/LeverageUnsubscribe.md) | Unsubscribe from events and hooks related to a floating margin configuration.  
[LeverageTotal](Floating-Margin/LeverageTotal.md) | Get the total number of floating margin configurations present in the platform.  
[LeverageNext](Floating-Margin/LeverageNext.md) | Get a floating margin configuration by index.  
[LeverageGet](Floating-Margin/LeverageGet.md) | Get a subscription configuration by name.  
[LeverageRequest](Floating-Margin/LeverageRequest.md) | Request a floating margin configuration from the server by name.  
[LeverageRequestArray](Floating-Margin/LeverageRequestArray.md) | Request an array of floating margin configurations from the server by groups.  
  
To apply a floating margin configuration to a group, use the [IMTConGroup::MarginFloatingLeverage](../../../Configuration-Interfaces/Groups/IMTConGroup/MarginFloatingLeverage.md) method.

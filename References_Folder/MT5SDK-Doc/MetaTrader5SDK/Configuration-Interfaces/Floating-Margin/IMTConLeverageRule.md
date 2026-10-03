[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Floating Margin](../Floating-Margin.md) / IMTConLeverageRule

[Previous](IMTConLeverageArray/SearchRight.md) | [Next](IMTConLeverageRule/Enumerations.md)

# IMTConLeverageRule

The IMTConLeverageRule class contains methods for retrieving and updating rules in [floating margin](https://support.metaquotes.net/en/docs/mt5/platform/administration/leverages) configurations:

Method | Purpose  
---|---  
[Release](IMTConLeverage/Release.md) | Delete the current object.  
[Assign](IMTConLeverage/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConLeverage/Clear.md) | Clear an object.  
[Name](IMTConLeverageRule/Name.md) | Get the name of a rule in a floating margin configuration.  
[Description](IMTConLeverageRule/Description.md) | Get the description of a rule in a floating margin configuration.  
[Path](IMTConLeverageRule/Path.md) | Get the path to a symbol or group of symbols for which the floating margin rule is applied.  
[RangeMode](IMTConLeverageRule/RangeMode.md) | Get the level type for a rule in a floating margin configuration.  
[RangeValueCurrency](IMTConLeverageRule/RangeValueCurrency.md) | Get the currency to which the notional value of positions in [IMTConLeverageRule::RANGE_VALUE* (#enrangemode)](IMTConLeverageRule/Enumerations.md#enrangemode) modes is converted.  
[TierAdd](IMTConLeverageRule/TierAdd.md) | Add a level to a floating margin rule.  
[TierUpdate](IMTConLeverageRule/TierUpdate.md) | Update a level in a floating margin rule.  
[TierDelete](IMTConLeverageRule/TierDelete.md) | Delete a level from a floating margin rule.  
[TierClear](IMTConLeverageRule/TierClear.md) | Clear the list of levels in a floating margin rule.  
[TierShift](IMTConLeverageRule/TierShift.md) | Move a level in a floating margin rule.  
[TierTotal](IMTConLeverageRule/TierTotal.md) | Get the total number of levels in a floating margin rule.  
[TierNext](IMTConLeverageRule/TierNext.md) | Get a level from floating margin rules by index.  
  
The IMTConLeverageRule class contains the following enumerations:

Enumeration | Description  
---|---  
[EnRangeMode (#enrangemode)](IMTConLeverageRule/Enumerations.md#enrangemode) | Level types for the rule.

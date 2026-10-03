[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageTierCreate

[Previous](LeverageRuleCreate.md) | [Next](LeverageSubscribe.md)

# IMTServerAPI::LeverageTierCreate

Create an object for a floating margin rule rule.
    
    
    IMTConLeverageTier*  IMTServerAPI::LeverageTierCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConLeverageTier](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageTier.md) interface. In case of failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConLeverageTier::Release](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageTier/Release.md) method of this object.

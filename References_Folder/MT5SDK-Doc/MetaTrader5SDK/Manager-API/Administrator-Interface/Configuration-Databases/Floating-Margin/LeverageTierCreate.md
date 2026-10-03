[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageTierCreate

[Previous](LeverageRuleCreate.md) | [Next](LeverageSubscribe.md)

# IMTAdminAPI::LeverageTierCreate

Create an object for a floating margin rule rule.

C++
    
    
    IMTConLeverageTier*  IMTAdminAPI::LeverageTierCreate()

.NET
    
    
    CIMTConLeverageTier  CIMTAdminAPI.LeverageTierCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConLeverageTier](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageTier.md) interface. In case of failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConLeverageTier::Release](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageTier/Release.md) method of this object.

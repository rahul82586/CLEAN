[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageCreate

[Previous](../Floating-Margin.md) | [Next](LeverageRuleCreate.md)

# IMTAdminAPI::LeverageCreate

Create a floating margin configuration object.

C++
    
    
    IMTConLeverage*  IMTAdminAPI::LeverageCreate()

.NET
    
    
    CIMTConLeverage  CIMTAdminAPI.LeverageCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConLeverage](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverage.md) interface. In case of failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConLeverage::Release](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverage/Release.md) method of this object.

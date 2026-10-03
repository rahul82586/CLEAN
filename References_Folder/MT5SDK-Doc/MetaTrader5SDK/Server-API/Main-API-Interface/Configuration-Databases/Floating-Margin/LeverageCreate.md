[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageCreate

[Previous](../Floating-Margin.md) | [Next](LeverageRuleCreate.md)

# IMTServerAPI::LeverageCreate

Create a floating margin configuration object.
    
    
    IMTConLeverage*  IMTServerAPI::LeverageCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConLeverage](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverage.md) interface. In case of failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConLeverage::Release](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverage/Release.md) method of this object.

[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageCreateArray

[Previous](LeverageCreate.md) | [Next](LeverageRuleCreate.md)

# IMTManagerAPI::LeverageCreateArray

Create an object for a floating margin configuration array.

C++
    
    
    IMTConLeverageArray*  IMTManagerAPI::LeverageCreateArray()

.NET
    
    
    CIMTConLeverageArray  CIMTManagerAPI.LeverageCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTConLeverageArray](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageArray.md) interface. In case of failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConLeverageArray::Release](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageArray/Release.md) method of this object.

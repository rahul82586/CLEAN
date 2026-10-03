[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageRuleCreate

[Previous](LeverageCreateArray.md) | [Next](LeverageTierCreate.md)

# IMTManagerAPI::LeverageRuleCreate

Create an object for a floating margin configuration rule.

C++
    
    
    IMTConLeverageRule*  IMTManagerAPI::LeverageRuleCreate()

.NET
    
    
    CIMTConLeverageRule  CIMTManagerAPI.LeverageRuleCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConLeverageRule](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageRule.md) interface. In case of failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConLeverageRule::Release](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageRule/Release.md) method of this object.

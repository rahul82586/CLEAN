[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadLegCreate

[Previous](SpreadCreate.md) | [Next](SpreadSubscribe.md)

# IMTGatewayAPI::SpreadLegCreate

Create an object of the configuration of a spread leg.

C++
    
    
    IMTConSpreadLeg*  IMTGatewayAPI::SpreadLegCreate()

.NET
    
    
    CIMTConSpreadLeg  CIMTGatewayAPI.SpreadLegCreate()

### Return Value

It returns a pointer to the created object that implements [IMTConSpreadLeg](../../../../Configuration-Interfaces/Spreads/IMTConSpreadLeg.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTConSpreadLeg::Release](../../../../Configuration-Interfaces/Spreads/IMTConSpreadLeg/Release.md) method of this object.

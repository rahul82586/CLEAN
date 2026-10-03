[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadLegCreate

[Previous](SpreadCreate.md) | [Next](SpreadSubscribe.md)

# IMTServerAPI::SpreadLegCreate

Create an object of the configuration of a spread leg.
    
    
    IMTConSpreadLeg*  IMTServerAPI::SpreadLegCreate()

### Return Value

It returns a pointer to the created object that implements [IMTConSpreadLeg](../../../../Configuration-Interfaces/Spreads/IMTConSpreadLeg.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTConSpreadLeg::Release](../../../../Configuration-Interfaces/Spreads/IMTConSpreadLeg/Release.md) method of this object.

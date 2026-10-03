[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadCreate

[Previous](../Spreads.md) | [Next](SpreadLegCreate.md)

# IMTAdminAPI::SpreadCreate

Create an object of the configuration of a spread.

C++
    
    
    IMTConSpread*  IMTAdminAPI::SpreadCreate()

.NET
    
    
    CIMTConSpread  CIMTAdminAPI.SpreadCreate()

### Return Value

It returns a pointer to the created object that implements [IMTConSpread](../../../../Configuration-Interfaces/Spreads/IMTConSpread.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTConSpread::Release](../../../../Configuration-Interfaces/Spreads/IMTConSpread/Release.md) method of this object.

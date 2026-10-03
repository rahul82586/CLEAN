[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionCreateArray

[Previous](PositionCreate.md) | [Next](PositionRequest.md)

# IMTAdminAPI::PositionCreateArray

Create an object of the array of trade positions.

C++
    
    
    IMTPositionArray*  IMTAdminAPI::PositionCreateArray()

.NET
    
    
    CIMTPositionArray  CIMTAdminAPI.PositionCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTPositionArray](../../../../Database-Interfaces/Trade/Positions/IMTPositionArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTAdminAPI::Release](../../../../Database-Interfaces/Trade/Positions/IMTPositionArray/Release.md) method of this object.

[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionCreateArray

[Previous](PositionCreate.md) | [Next](PositionSubscribe.md)

# IMTServerAPI::PositionCreateArray

Create an object of the array of trade positions.
    
    
    IMTPositionArray*  IMTServerAPI::PositionCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTPositionArray](../../../../Database-Interfaces/Trade/Positions/IMTPositionArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTPositionArray::Release](../../../../Database-Interfaces/Trade/Positions/IMTPositionArray/Release.md) method of this object.

[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionCreate

[Previous](../Positions.md) | [Next](PositionCreateArray.md)

# IMTServerAPI::PositionCreate

Create an object of a trade position.
    
    
    IMTPosition*  IMTServerAPI::PositionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTPosition](../../../../Database-Interfaces/Trade/Positions/IMTPosition.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTPosition::Release](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Release.md) method of this object.

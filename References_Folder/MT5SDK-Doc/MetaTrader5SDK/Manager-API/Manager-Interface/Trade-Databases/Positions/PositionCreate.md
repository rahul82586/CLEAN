[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionCreate

[Previous](../Positions.md) | [Next](PositionCreateArray.md)

# IMTManagerAPI::PositionCreate

Create an object of a trade position.

C++
    
    
    IMTPosition*  IMTManagerAPI::PositionCreate()

.NET
    
    
    CIMTPosition  CIMTManagerAPI.PositionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTPosition](../../../../Database-Interfaces/Trade/Positions/IMTPosition.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTPosition::Release](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Release.md) method of this object.

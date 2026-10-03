[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionCreateArray

[Previous](PositionCreate.md) | [Next](PositionSubscribe.md)

# IMTManagerAPI::PositionCreateArray

Create an object of the array of trade positions.

C++
    
    
    IMTPositionArray*  IMTManagerAPI::PositionCreateArray()

.NET
    
    
    CIMTPositionArray  CIMTManagerAPI.PositionCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTPositionArray](../../../../Database-Interfaces/Trade/Positions/IMTPositionArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTPositionArray::Release](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Release.md) method of this object.

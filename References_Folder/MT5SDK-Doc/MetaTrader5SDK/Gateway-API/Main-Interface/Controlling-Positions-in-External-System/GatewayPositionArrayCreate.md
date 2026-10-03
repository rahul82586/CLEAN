[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Controlling Positions in External System](../Controlling-Positions-in-External-System.md) / GatewayPositionArrayCreate

[Previous](GatewayParamArrayCreate.md) | [Next](GatewayPositionsAnswer.md)

# IMTGatewayAPI::GatewayPositionArrayCreate

Create an object of the array of positions.

C++
    
    
    IMTPositionArray*  IMTGatewayAPI::GatewayPositionArrayCreate()

.NET
    
    
    CIMTPositionArray  CIMTGatewayAPI.GatewayPositionArrayCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTPositionArray](../../../Database-Interfaces/Trade/Positions/IMTPositionArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTPositionArray::Release](../../../Database-Interfaces/Trade/Positions/IMTPositionArray.md) method of this object.

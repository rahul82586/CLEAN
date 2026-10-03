[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Databases](../Trade-Databases.md) / PositionCreate

[Previous](OrderCreate.md) | [Next](../Trade-Requests.md)

# IMTGatewayAPI::PositionCreate

Create an object of a trade position.

C++
    
    
    IMTPosition*  IMTGatewayAPI::PositionCreate()

.NET
    
    
    CIMTPosition  CIMTGatewayAPI.PositionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTPosition](../../../Database-Interfaces/Trade/Positions/IMTPosition.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTPosition::Release](../../../Database-Interfaces/Trade/Positions/IMTPosition/Release.md) method of this object.

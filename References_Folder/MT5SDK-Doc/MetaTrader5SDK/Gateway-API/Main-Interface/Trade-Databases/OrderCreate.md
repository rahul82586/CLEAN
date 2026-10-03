[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Databases](../Trade-Databases.md) / OrderCreate

[Previous](../Trade-Databases.md) | [Next](PositionCreate.md)

# IMTGatewayAPI::OrderCreate

Create an object of a trade order.

C++
    
    
    IMTOrder*  IMTGatewayAPI::OrderCreate()

.NET
    
    
    CIMTOrder  CIMTGatewayAPI.OrderCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTOrder](../../../Database-Interfaces/Trade/Orders/IMTOrder.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTOrder::Release](../../../Database-Interfaces/Trade/Orders/IMTOrder/Release.md) method of this object.

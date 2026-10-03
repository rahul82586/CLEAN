[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Controlling Orders in External System](../Controlling-Orders-in-External-System.md) / GatewayOrderArrayCreate

[Previous](../Controlling-Orders-in-External-System.md) | [Next](GatewayOrdersAnswer.md)

# IMTGatewayAPI::GatewayOrderArrayCreate

Create an object of the array of positions.

C++
    
    
    IMTOrderArray*  IMTGatewayAPI::GatewayOrderArrayCreate()

.NET
    
    
    CIMTOrderArray  CIMTGatewayAPI.GatewayOrderArrayCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTOrderArray](../../../Database-Interfaces/Trade/Orders/IMTOrderArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOrderArray::Release](../../../Database-Interfaces/Trade/Orders/IMTOrderArray/Release.md) method of this object.

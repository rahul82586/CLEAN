[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderCreate

[Previous](../Orders.md) | [Next](OrderCreateArray.md)

# IMTServerAPI::OrderCreate

Create an object of a trade order.
    
    
    IMTOrder*  IMTServerAPI::OrderCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTOrder:Release](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Release.md) method of this object.

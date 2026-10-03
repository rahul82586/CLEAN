[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderCreateArray

[Previous](OrderCreate.md) | [Next](OrderSubscribe.md)

# IMTServerAPI::OrderCreateArray

Create an object of the array of orders.
    
    
    IMTOrderArray*  IMTServerAPI::OrderCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTOrderArray](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOrderArray::Release](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray/Release.md) method of this object.

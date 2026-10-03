[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderCreateArray

[Previous](OrderCreate.md) | [Next](OrderSubscribe.md)

# IMTManagerAPI::OrderCreateArray

Create an object of the array of orders.

C++
    
    
    IMTOrderArray*  IMTManagerAPI::OrderCreateArray()

.NET
    
    
    CIMTOrderArray  CIMTManagerAPI.OrderCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTOrderArray](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOrderArray::Release](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray/Release.md) method of this object.

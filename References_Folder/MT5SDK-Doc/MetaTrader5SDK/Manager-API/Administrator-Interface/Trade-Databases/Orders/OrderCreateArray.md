[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderCreateArray

[Previous](OrderCreate.md) | [Next](OrderRequest.md)

# IMTAdminAPI::OrderCreateArray

Create an object of the array of orders.

C++
    
    
    IMTOrderArray*  IMTAdminAPI::OrderCreateArray()

.NET
    
    
    CIMTOrderArray  CIMTAdminAPI.OrderCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTOrderArray](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOrderArray::Release](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray/Release.md) method of this object.

[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderCreateArray

[Previous](OrderCreate.md) | [Next](OrderGet.md)

# IMTReportAPI::OrderCreateArray

Create an object of the array of orders.
    
    
    IMTOrderArray*  IMTReportAPI::OrderCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTOrderArray](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOrderArray::Release](../../../../Database-Interfaces/Trade/Orders/IMTOrderArray/Release.md) method of this object.

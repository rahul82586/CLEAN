[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderCreate

[Previous](../Orders.md) | [Next](OrderCreateArray.md)

# IMTReportAPI::OrderCreate

Create an object of a trade order.
    
    
    IMTOrder*  IMTReportAPI::OrderCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTOrder::Release](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Release.md) method of this object.

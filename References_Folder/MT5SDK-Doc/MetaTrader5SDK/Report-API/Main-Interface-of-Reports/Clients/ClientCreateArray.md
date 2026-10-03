[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Clients](../Clients.md) / ClientCreateArray

[Previous](ClientCreate.md) | [Next](ClientGet.md)

# IMTReportAPI::ClientCreateArray

Create an object of the client array.
    
    
    IMTClientArray*  IMTReportAPI::ClientCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTClientArray](../../../Database-Interfaces/Clients/IMTClientArray.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTClientArray::Release](../../../Database-Interfaces/Clients/IMTClientArray/Release.md) method of this object.

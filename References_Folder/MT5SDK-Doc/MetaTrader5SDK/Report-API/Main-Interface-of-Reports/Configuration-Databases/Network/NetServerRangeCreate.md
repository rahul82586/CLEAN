[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerRangeCreate

[Previous](NetServerCreate.md) | [Next](NetServerTotal.md)

# IMTReportAPI::NetServerRangeCreate

Create an object of the range of orders, deals or accounts.
    
    
    IMTConServerRange*  IMTReportAPI::NetServerRangeCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServerRange](../../../../Configuration-Interfaces/Network/IMTConServerRange.md) interface. In case of failure, it returns Null.

### Note

The created object must be deleted by calling the [IMTConServerRange::Release](../../../../Configuration-Interfaces/Network/IMTConServerRange/Release.md) method of this object.

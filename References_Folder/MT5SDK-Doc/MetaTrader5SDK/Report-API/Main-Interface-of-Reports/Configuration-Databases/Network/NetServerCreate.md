[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerCreate

[Previous](../Network.md) | [Next](NetServerRangeCreate.md)

# IMTReportAPI::NetServerCreate

Create an object of configuration of the platform components.
    
    
    IMTConServer*  IMTReportAPI::NetServerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServer](../../../../Configuration-Interfaces/Network/IMTConServer.md) interface. In case of failure, it returns Null.

### Note

The created object must be deleted by calling the [IMTConServer::Release](../../../../Configuration-Interfaces/Network/IMTConServer/Release.md) method of this object.

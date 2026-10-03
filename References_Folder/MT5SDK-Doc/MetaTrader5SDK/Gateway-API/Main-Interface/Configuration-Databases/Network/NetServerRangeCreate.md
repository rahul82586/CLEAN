[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerRangeCreate

[Previous](NetServerCreate.md) | [Next](NetServerSubscribe.md)

# IMTGatewayAPI::NetServerRangeCreate

Create an object of the range of orders, deals or accounts.

C++
    
    
    IMTConServerRange*  IMTGatewayAPI::NetServerRangeCreate()

.NET
    
    
    CIMTConServerRange  CIMTGatewayAPI.NetServerRangeCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServerRange](../../../../Configuration-Interfaces/Network/IMTConServerRange.md) interface. In case of failure, it returns Null.

### Note

The created object must be deleted by calling the [IMTConServerRange::Release](../../../../Configuration-Interfaces/Network/IMTConServerRange/Release.md) method of this object.

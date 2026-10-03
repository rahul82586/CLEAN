[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerAddressRangeCreate

[Previous](NetServerRangeCreate.md) | [Next](NetServerClusterStateCreate.md)

# IMTAdminAPI::NetServerAddressRangeCreate

Create an object of the range of IP addresses. These objects are used for configuring the Anti-DDoS Proxy Server component which enables the use of [external Anti-DDoS service providers](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_anti_ddos).

C++
    
    
    IMTConServerAddressRange*  IMTAdminAPI::NetServerAddressRangeCreate()

.NET
    
    
    CIMTConServerAddressRange  CIMTAdminAPI.NetServerAddressRangeCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServerAddressRange](../../../../Configuration-Interfaces/Network/IMTConServerAddressRange.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConServerAddressRange::Release](../../../../Configuration-Interfaces/Network/IMTConServerAddressRange/Release.md) method of this object.

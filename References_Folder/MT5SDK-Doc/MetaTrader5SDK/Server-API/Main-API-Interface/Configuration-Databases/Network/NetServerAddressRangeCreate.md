[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerAddressRangeCreate

[Previous](NetServerRangeCreate.md) | [Next](NetServerBackupFolderCreate.md)

# IMTServerAPI::NetServerAddressRangeCreate

Create an object of the range of IP addresses. These objects are used for configuring the Anti-DDoS Proxy Server component which enables the use of [external Anti-DDoS service providers](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_anti_ddos).
    
    
    IMTConServerAddressRange*  IMTServerAPI::NetServerAddressRangeCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConServerAddressRange](../../../../Configuration-Interfaces/Network/IMTConServerAddressRange.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConServerAddressRange::Release](../../../../Configuration-Interfaces/Network/IMTConServerAddressRange/Release.md) method of this object.

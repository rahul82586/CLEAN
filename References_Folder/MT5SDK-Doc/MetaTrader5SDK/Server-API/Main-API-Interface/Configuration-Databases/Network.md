[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Network

[Previous](Common/Set.md) | [Next](Network/NetServerCreate.md)

# Network Configuration

Network configuration means the management of settings of the the server components of the platform: main and ordinary trade servers, history and access servers, backup servers.

Functions described in this section allow managing the configuration of the platform components, as well subscribe and unsubscribe from events associated with its change.

Function | Purpose  
---|---  
[NetServerCreate](Network/NetServerCreate.md) | Create an object of the network configuration.  
[NetServerClusterStateCreate](Network/NetServerClusterStateCreate.md) | Create the network connection status object.  
[NetServerRangeCreate](Network/NetServerRangeCreate.md) | Create an object of the range of orders, deals or accounts.  
[NetServerAddressRangeCreate](Network/NetServerAddressRangeCreate.md) | Create an object of the range of IP addresses.  
[NetServerBackupFolderCreate](Network/NetServerBackupFolderCreate.md) | Create an object describing the user directory to back up.  
[NetServerSubscribe](Network/NetServerSubscribe.md) | Subscribe to events and hooks associated with the network configuration.  
[NetServerUnsubscribe](Network/NetServerUnsubscribe.md) | Unsubscribe from events and hooks associated with the network configuration.  
[NetServerAdd](Network/NetServerAdd.md) | Add or update a server configuration.  
[NetServerDelete](Network/NetServerDelete.md) | Delete a server configuration by the index.  
[NetServerShift](Network/NetServerShift.md) | Change the position of a server configuration in the list.  
[NetServerTotal](Network/NetServerTotal.md) | The total number of server configurations available in the platform.  
[NetServerNext](Network/NetServerNext.md) | Get a server configuration by the index.  
[NetServerGet](Network/NetServerGet.md) | Get a server configuration by the ID.  
[TLSCertificateUpdate](Network/TLSCertificateUpdate.md) | Add or update an SSL certificate on access servers.  
[TLSCertificateDelete](Network/TLSCertificateDelete.md) | Delete an SSL certificate from access servers by position.  
[TLSCertificateShift](Network/TLSCertificateShift.md) | Change the position of an SSL certificate in the list.  
[TLSCertificateTotal](Network/TLSCertificateTotal.md) | The total number of certificates installed for access servers.  
[TLSCertificateNext](Network/TLSCertificateNext.md) | Get the data of a certificate installed for access servers, by index.  
[TLSCertificatePfx](Network/TLSCertificatePfx.md) | Get the file of a certificate installed for access servers, by index.

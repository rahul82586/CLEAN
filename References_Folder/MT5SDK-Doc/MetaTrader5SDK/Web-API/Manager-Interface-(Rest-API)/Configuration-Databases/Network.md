[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../Configuration-Databases.md) / Network

[Previous](Common/Set.md) | [Next](Network/Data-Structure.md)

# Network

Network configuration features settings of the platform's server components, which include the main and ordinary trade servers, as well as history, access and backup servers. The following requests are provided for relevant operations:

Request | Description  
---|---  
[/api/server/add](Network/Add-Server.md) | Add and update a server configuration in the trading platform.  
[/api/server/delete](Network/Delete-Server.md) | Delete a server configuration from the trading platform.  
[/api/server/shift](Network/Shift-Server.md) | Change the position of a server configuration in the list.  
[/api/server/total](Network/Get-Number-of-Servers.md) | Get the total number of server configurations existing in the platform.  
[/api/server/next](Network/Get-Server-by-Index.md) | Get the configuration of one or more servers by index in the list.  
[/api/server/get](Network/Get-Server-by-Identifier.md) | Get server configurations by a list of IDs or indexes in a list.  
[/api/server/restart](Network/Restart-Server.md) | Restart the server to which the Web client is connected.  
[/api/tls_certificate/add](Network/Add-Certificate.md) | Add or update an SSL certificate on access servers.  
[/api/tls_certificate/delete](Network/Delete-Certificate.md) | Delete an SSL certificate from access servers by position.  
[/api/tls_certificate/shift](Network/Shift-Certificate.md) | Change the position of an SSL certificate in the list.  
[/api/tls_certificate/total](Network/Get-Total-Certificates.md) | The total number of certificates installed for access servers.  
[/api/tls_certificate/next](Network/Get-Certificate-by-Index.md) | Get the data of a certificate installed for access servers, by index.  
  
The network configuration data format is described in the "[Data Structure](Network/Data-Structure.md)" section.

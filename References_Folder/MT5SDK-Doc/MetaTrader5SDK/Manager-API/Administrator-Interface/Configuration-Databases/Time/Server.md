[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Server

[Previous](Set.md) | [Next](ServerRequest.md)

# IMTAdminAPI::TimeServer

Get the calculated current time of the trading server.

C++
    
    
    INT64  IMTAdminAPI::TimeServer()

.NET
    
    
    long   CIMTAdminAPI.TimeServer()

Python
    
    
    AdminAPI.TimeServer()

### Return Value

The current trading time of the platform in the number of seconds elapsed since 01.01.1970.

### Note

Unlike the [TimeServerRequest](ServerRequest.md) function, the trading time is calculated on the Manager API application side: the current local computer time is adjusted in accordance with the server time zone.

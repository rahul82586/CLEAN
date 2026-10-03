[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Server Management](../Server-Management.md) / ServerActivate

[Previous](../Server-Management.md) | [Next](ServerLiveUpdate.md)

# IMTAdminAPI::ServerActivate

Request activation of a trading platform license.

C++
    
    
    MTAPIRES  IMTAdminAPI::ServerActivate()

.NET
    
    
    MTRetCode  CIMTAdminAPI.ServerActivate()

Python
    
    
    AdminAPI.ServerActivate()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A non-activated license for the platform has a number of limitations (number of users, groups, trade operations, etc.).

  * A request is sent to the update server of the developer company;
  * In case of successful license check, a new activated license is generated, which is bound to the configuration of the server on which the platform is installed;
  * An activated license is sent back to a trade server.



[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupUpdate

[Previous](GroupUnsubscribe.md) | [Next](GroupUpdateBatch.md)

# IMTAdminAPI::GroupUpdate

Adds or updates a group configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::GroupUpdate(
       IMTConGroup*  group      // Group configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GroupUpdate(
       CIMTConGroup  group      // Group configuration object
       )

Python
    
    
    AdminAPI.GroupUpdate(
       group         # Group configuration object
       )

### Parameters

**group**  
[in] An object of group configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.

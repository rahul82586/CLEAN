[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteUnsubscribe

[Previous](RouteSubscribe.md) | [Next](RouteUpdate.md)

# IMTAdminAPI::RouteUnsubscribe

Unsubscribe from events associated with the configuration of request routing.

C++
    
    
    MTAPIRES  IMTAdminAPI::RouteUnsubscribe(
       IMTConRouteSink*  sink      // A pointer to the IMTConRouteSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.RouteUnsubscribe(
       CIMTConRouteSink  sink      // CIMTConRouteSink object
       )

Python
    
    
    AdminAPI.RouteUnsubscribe(
       sink              # IMTConRouteSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConRouteSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a pair method to [IMTAdminAPI::RouteSubscribe](RouteSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.

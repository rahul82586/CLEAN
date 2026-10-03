[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteSubscribe

[Previous](RouteDealerCreate.md) | [Next](RouteUnsubscribe.md)

# IMTAdminAPI::RouteSubscribe

Subscribe to events associated with the configuration of request routing.

C++
    
    
    MTAPIRES  IMTAdminAPI::RouteSubscribe(
       IMTConRouteSink*  sink      // A pointer to the IMTConRouteSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.RouteSubscribe(
       CIMTConRouteSink  sink      // CIMTConRouteSink object
       )

Python
    
    
    AdminAPI.RouteSubscribe(
       sink              # IMTConRouteSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConRouteSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConRouteSink](../../../../Configuration-Interfaces/Routing/IMTConRouteSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.

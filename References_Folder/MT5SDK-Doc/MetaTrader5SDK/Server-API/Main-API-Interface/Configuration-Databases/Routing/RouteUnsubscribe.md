[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteUnsubscribe

[Previous](RouteSubscribe.md) | [Next](RouteAdd.md)

# IMTServerAPI::RouteUnsubscribe

Unsubscribe from events and hooks associated with the configuration of request routing.
    
    
    MTAPIRES  IMTServerAPI::RouteUnsubscribe(
       IMTConRouteSink*  sink      // A pointer to the IMTConRouteSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConRouteSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a pair method to [IMTServerAPI::RouteSubscribe](RouteSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.

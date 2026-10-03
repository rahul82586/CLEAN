[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageSubscribe

[Previous](LeverageTierCreate.md) | [Next](LeverageUnsubscribe.md)

# IMTAdminAPI::LeverageSubscribe

Subscribe to events and hooks related to a floating margin configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageSubscribe(
       IMTConLeverageSink*  sink   // Pointer to the IMTConLeverageSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageSubscribe(
       CIMTConLeverageSink  sink   // The CIMTConLeverageSink object
       )

Python
    
    
    AdminAPI.LeverageSubscribe(
       sink                 # The IMTConLeverageSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implements theIMTConLeverageSinkinterface.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is implemented in a thread-safe manner. The same [IMTConLeverageSink](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverageSink.md) interface cannot be subscribed to an event twice; in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.

[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageUnsubscribe

[Previous](LeverageSubscribe.md) | [Next](LeverageUpdate.md)

# IMTAdminAPI::LeverageUnsubscribe

Unsubscribe from events and hooks related to a floating margin configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageUnsubscribe(
       IMTConLeverageSink*  sink   // Pointer to the IMTConLeverageSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageUnsubscribe(
       CIMTConLeverageSink  sink   // The CIMTConLeverageSink object
       )

Python
    
    
    AdminAPI.LeverageUnsubscribe(
       sink                 # The IMTConLeverageSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implements theIMTConLeverageSinkinterface.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method is a counterpart to the [IMTAdminAPI::LeverageSubscribe](LeverageSubscribe.md) method. When attempting to unsubscribe from an interface that was not previously subscribed, the error [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

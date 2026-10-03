[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Get.md)

# IMTAdminAPI::VPSUnsubscribe

Unsubscribe from events and hooks associated with changes in the VPS sponsorship settings.

C++
    
    
    MTAPIRES  IMTAdminAPI::VPSUnsubscribe(
       IMTConVPSSink*  sink   // the pointer to the IMTConVPSSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.VPSUnsubscribe(
       CIMTConVPSSink  sink   // CIMTConVPSSink object
       )

Python
    
    
    AdminAPI.VPSUnsubscribe(
       sink            // IMTConVPSSink object
       )

### Parameters

**sink**  
[in] The pointer to the object that implements theIMTConVPSSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::VPSSubscribe](../../../../Server-API/Main-API-Interface/Configuration-Databases/VPS/Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.

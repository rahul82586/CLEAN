[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Connection to the Server](../Connection-to-the-Server.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](ProxySet.md)

# IMTAdminAPI::Unsubscribe

Unsubscribe from common events of the [IMTAdminAPI](../../Administrator-Interface.md).

C++
    
    
    MTAPIRES  IMTAdminAPI::Unsubscribe(
       IMTManagerSink*  sink      // A pointer to the IMTManagerSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.Unsubscribe(
       CIMTManagerSink  sink      // CIMTManagerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTManagerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::Subscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.

[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Connection to the Server](../Connection-to-the-Server.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](ProxySet.md)

# IMTManagerAPI::Unsubscribe

Unsubscribe from common events of the [IMTManagerAPI](../../Manager-Interface.md) interface.

C++
    
    
    virtual MTAPIRES  IMTManagerAPI::Unsubscribe(
       IMTManagerSink*  sink      // A pointer to the IMTManagerSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.Unsubscribe(
       CIMTManagerSink  sink      // CIMTManagerSink object
       )

Python
    
    
    ManagerAPI.Unsubscribe(
       sink             # IMTManagerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTManagerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is pared to [IMTManagerAPI::Subscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.

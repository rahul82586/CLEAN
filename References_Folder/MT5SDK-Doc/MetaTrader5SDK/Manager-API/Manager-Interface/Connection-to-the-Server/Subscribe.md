[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Connection to the Server](../Connection-to-the-Server.md) / Subscribe

[Previous](Disconnect.md) | [Next](Unsubscribe.md)

# IMTManagerAPI::Subscribe

Subscribe to common events of the [IMTManagerAPI](../../Manager-Interface.md) interface.

C++
    
    
    virtual MTAPIRES  IMTManagerAPI::Subscribe(
       IMTManagerSink*  sink      // A pointer to the IMTManagerSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.Subscribe(
       CIMTManagerSink  sink      // CIMTManagerSink object
       )

Python
    
    
    ManagerAPI.Subscribe(
       sink             # IMTManagerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTManagerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTManagerSink](../../Interface-of-Events.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.

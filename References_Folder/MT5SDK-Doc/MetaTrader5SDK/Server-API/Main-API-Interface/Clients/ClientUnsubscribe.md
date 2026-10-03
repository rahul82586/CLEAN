[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientUnsubscribe

[Previous](ClientSubscribe.md) | [Next](ClientAdd.md)

# IMTServerAPI::ClientUnsubscribe

Unsubscribe from the events and hooks associated with changes in the client base.
    
    
    MTAPIRES  IMTServerAPI::ClientUnsubscribe(
       IMTClientSink*  sink      // A pointer to the IMTClientSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTClientSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTServerAPI::ClientSubscribe](ClientSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.

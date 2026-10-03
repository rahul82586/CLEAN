[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / DocumentUnsubscribe

[Previous](DocumentSubscribe.md) | [Next](DocumentAdd.md)

# IMTServerAPI::DocumentUnsubscribe

Unsubscribe from the events and hooks associated with changes in the document database.
    
    
    MTAPIRES  IMTServerAPI::DocumentUnsubscribe(
       IMTDocumentSink*  sink      // A pointer to the IMTDocumentSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDocumentSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is paired with [IMTServerAPI::DocumentSubscribe](DocumentSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.

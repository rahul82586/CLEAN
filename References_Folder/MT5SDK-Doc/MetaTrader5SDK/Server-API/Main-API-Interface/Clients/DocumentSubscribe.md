[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / DocumentSubscribe

[Previous](DocumentCreateArray.md) | [Next](DocumentUnsubscribe.md)

# IMTServerAPI::DocumentSubscribe

Subscribe to events and hooks associated with changes in the document database.
    
    
    MTAPIRES  IMTServerAPI::DocumentSubscribe(
       IMTDocumentSink*  sink      // A pointer to the IMTDocumentSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDocumentSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. The same [IMTDocumentSink](../../../Database-Interfaces/Clients/IMTDocumentSink.md) interface cannot subscribe to an event twice: in this case the [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) response code is returned.

[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentSubscribe

[Previous](CommentCreateArray.md) | [Next](CommentUnsubscribe.md)

# IMTServerAPI::CommentSubscribe

Subscribe to events and hooks associated with changes in the comment database.
    
    
    MTAPIRES  IMTServerAPI::CommentSubscribe(
       IMTCommentSink*  sink      // A pointer to the IMTCommentSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTCommentSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. The same [IMTCommentSink](../../../Database-Interfaces/Clients/IMTCommentSink.md) interface cannot subscribe to an event twice: in this case the [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) response code is returned.

[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentUnsubscribe

[Previous](CommentSubscribe.md) | [Next](CommentAdd.md)

# IMTServerAPI::CommentUnsubscribe

Unsubscribe from the events and hooks associated with changes in the comment database.
    
    
    MTAPIRES  IMTServerAPI::CommentUnsubscribe(
       IMTCommentSink*  sink      // A pointer to the IMTCommentSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTCommentSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is paired with [IMTServerAPI::CommentSubscribe](CommentSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.

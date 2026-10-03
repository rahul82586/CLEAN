[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentSink](../IMTCommentSink.md) / OnCommentUpdate

[Previous](OnCommentAdd.md) | [Next](OnCommentDelete.md)

# IMTCommentSink::OnOrderUpdate

Comment update event handler.

C++
    
    
    virtual void  IMTCommentSink::OnOrderUpdate(
       const IMTComment*  comment  // A pointer to a comment
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTCommentSink.OnOrderUpdate(
       CIMTComment        comment  // Comment object
       )

### Parameters

**comment**  
[in] A pointer to the comment object.

### Note

This method is called by the API to notify of a comment update.

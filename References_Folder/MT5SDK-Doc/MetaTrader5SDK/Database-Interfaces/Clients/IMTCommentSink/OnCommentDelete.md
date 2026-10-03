[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentSink](../IMTCommentSink.md) / OnCommentDelete

[Previous](OnCommentUpdate.md) | [Next](../IMTDocument.md)

# IMTCommentSink::OnOrderDelete

Comment deletion event handler.

C++
    
    
    virtual void  IMTCommentSink::OnOrderDelete(
       const IMTComment*  comment  // A pointer to the comment object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTCommentSink.OnOrderDelete(
       CIMTComment        comment  // Comment object
       )

### Parameters

**comment**  
[in] A pointer to the deleted comment object.

### Note

This method is called by the API to notify of a comment deletion.

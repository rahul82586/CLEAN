[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentSink](../IMTDocumentSink.md) / OnDocumentDelete

[Previous](OnDocumentUpdate.md) | [Next](../IMTAttachment.md)

# IMTDocumentSink::OnDocumentDelete

Document deletion event handler.

C++
    
    
    virtual void  IMTDocumentSink::OnDocumentDelete(
       const IMTDocument*  document  // A pointer to the document object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDocumentSink.OnDocumentDelete(
       CIMTDocument        document  // Document object
       )

### Parameters

**document**  
[in] A pointer to the deleted document object.

### Note

This method is called by the API to notify of a document deletion.

[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentSink](../IMTDocumentSink.md) / OnDocumentUpdate

[Previous](OnDocumentAdd.md) | [Next](OnDocumentDelete.md)

# IMTDocumentSink::OnDocumentUpdate

Document update event handler.

C++
    
    
    virtual void  IMTDocumentSink::OnDocumentUpdate(
       const IMTDocument*  document  // A pointer to the document
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDocumentSink.OnDocumentUpdate(
       CIMTDocument        document  // Document object
       )

### Parameters

**document**  
[in] A pointer to the document object.

### Note

This method is called by the API to notify of a document update.

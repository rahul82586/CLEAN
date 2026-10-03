[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentSink](../IMTDocumentSink.md) / OnDocumentAdd

[Previous](../IMTDocumentSink.md) | [Next](OnDocumentUpdate.md)

# IMTDocumentSink::OnDocumentAdd

New document adding event handler.

C++
    
    
    virtual void  IMTDocumentSink::OnDocumentAdd(
       const IMTDocument*  document  // A pointer to the document object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDocumentSink.OnDocumentAdd(
       CIMTDocument        document  // Document object
       )

### Parameters

**document**  
[in] A pointer to the document object.

### Note

This method is called by the API to notify that a new document has been added.

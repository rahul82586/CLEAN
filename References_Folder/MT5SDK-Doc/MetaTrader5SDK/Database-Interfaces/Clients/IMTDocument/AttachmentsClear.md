[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / AttachmentsClear

[Previous](AttachmentsAdd.md) | [Next](AttachmentsTotal.md)

# IMTDocument::AttachmentsClear

Clear the list of document files.

C++
    
    
    MTAPIRES  IMTDocument::AttachmentsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.AttachmentsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears the entire list of files in a document.

[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / DocumentUpdate

[Previous](DocumentAddBatchArray.md) | [Next](DocumentUpdateBatch.md)

# IMTAdminAPI::DocumentUpdate

Change a document in the client record.

C++
    
    
    MTAPIRES  IMTAdminAPI::DocumentUpdate(
       IMTDocument*  document   // document object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DocumentUpdate(
       CIMTDocument  document   // document object
       )

### Parameters

**document**  
[in]Document object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A document can only be changed from the applications connected to the trading server, on which the client has been created ([IMTDocument::RelatedClient](../../../Database-Interfaces/Clients/IMTDocument/RelatedClient.md)). The [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) response code will be returned for all other applications. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

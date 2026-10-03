[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / DocumentAdd

[Previous](DocumentUnsubscribe.md) | [Next](DocumentUpdate.md)

# IMTServerAPI::DocumentAdd

Add a document to a client record.
    
    
    MTAPIRES  IMTServerAPI::DocumentAdd(
       IMTDocument*  document,  // Document object
       const UINT64  author     // Author
       )

### Parameters

**document**  
[in]Document object.

**author**  
[in] The login of the manager account, on whose behalf the document is being added. The login is equal to theIMTConManager::Loginvalue. This information is used to keep the history of client changes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A comment can only be added from plugins running on the same trade server where the client was created ([IMTDocument::RelatedClient](../../../Database-Interfaces/Clients/IMTDocument/RelatedClient.md)). For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

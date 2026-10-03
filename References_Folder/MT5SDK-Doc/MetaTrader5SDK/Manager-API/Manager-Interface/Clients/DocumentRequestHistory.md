[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / DocumentRequestHistory

[Previous](DocumentRequestByClient.md) | [Next](CommentCreate.md)

# IMTManagerAPI::DocumentRequestHistory

Get the history of client document changes.

C++
    
    
    MTAPIRES  IMTManagerAPI::DocumentRequestHistory(
       const UINT64     document_id,  // identifier
       const UINT64     author,      // author
       const INT64      from,        // period beginning
       const UINT64     to,          // period end
       IMTClientArray*  history      // object of the array of clients
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DocumentRequestHistory(
       ulong            document_id,  // identifier
       ulong            author,      // author
       long             from,        // period beginning
       long             to,          // period end
       CIMTClientArray  history      // object of the array of clients
       )

### Parameters

**document_id**  
[in] Document ID (IMTDocument::RecordID).

**author**  
[in] The login of the manager account by whom the document was changed. The login is equal to theIMTConManager::Loginvalue.

**from**  
[in] The beginning of the period for which you wish to get the history of document changes. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you wish to get the history of document changes. The date is specified in seconds that have elapsed since 01.01.1970.

**history**  
[out] An object of an array of documents. The 'history' object must be previously created using theIMTServerAPI::DocumentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method returns an array of document descriptions: all the document states after being changed by the specified author, in the specified time period.

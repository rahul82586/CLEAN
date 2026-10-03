[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientRequestHistory

[Previous](ClientRequestByGroup.md) | [Next](ClientUserAdd.md)

# IMTManagerAPI::ClientRequestHistory

Get the history of client changes.

C++
    
    
    MTAPIRES  IMTManagerAPI::ClientRequestHistory(
       const UINT64     client_id,  // identifier
       const UINT64     author,     // author
       const INT64      from,       // period beginning
       const UINT64     to,         // period end
       IMTClientArray*  history     // object of client array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ClientRequestHistory(
       ulong            client_id,  // identifier
       ulong            author,     // author
       long             from,       // period beginning
       long             to,         // period end
       CIMTClientArray  history     // object of client array
       )

Python
    
    
    ManagerAPI.ClientRequestHistory(
       int              client_id,  # identifier
       int              author,     # author
                        from,       # period beginning
                        to          # period end
       )

### Parameters

**client_id**  
[in] Client identifier (IMTClient::RecordID).

**author**  
[in] The login of the manager account by whom the client was changed. The login is equal to theIMTConManager::Loginvalue.

**from**  
[in] The beginning of the period for which you wish to get the history of client changes. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you wish to get the history of client changes. The date is specified in seconds that have elapsed since 01.01.1970.

**history**  
[out] An object of an array of clients. The 'history' object must be previously created using theIMTManagerAPI::ClientCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method returns an array of client descriptions: all the client states after changes by the specified author, in the specified time period.

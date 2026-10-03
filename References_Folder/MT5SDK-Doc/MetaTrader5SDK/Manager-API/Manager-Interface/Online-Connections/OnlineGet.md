[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineGet

[Previous](OnlineNext.md) | [Next](OnlineDisconnect.md)

# IMTManagerAPI::OnlineGet

Get connection record by login.

C++
    
    
    MTAPIRES  IMTManagerAPI::OnlineGet(
       const UINT64     login,     // Client login
       IMTOnlineArray*  online     // Connection record array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OnlineGet(
       ulong            login,     // Client login
       CIMTOnlineArray  online     // Connection record array object
       )

Python
    
    
    ManagerAPI.OnlineGet(
       login            # Client login
       )
    
    
    ManagerAPI.OnlineGetArray()

### Parameters

**login**  
[in] The login of a client.

**online**  
[out] Connection record array object. The online object should be first created usingIMTManagerAPI::OnlineCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a connection with the specified login to the online object.

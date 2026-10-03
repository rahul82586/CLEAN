[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineNext

[Previous](OnlineTotal.md) | [Next](OnlineGet.md)

# IMTManagerAPI::OnlineNext

Get connection record by index.

C++
    
    
    MTAPIRES  IMTManagerAPI::OnlineNext(
       const UINT     pos,        // Connection record position
       IMTOnline*     online      // Connection record object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OnlineNext(
       uint           pos,        // Connection record position
       CIMTOnline     online      // Connection record object
       )

Python
    
    
    ManagerAPI.OnlineNext(
       pos            # Connection record position
       )

### Parameters

**pos**  
[in] Position of the record, starting with 0.

**online**  
[out] Connection record object. The online object should be first created usingIMTManagerAPI::OnlineCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a connection records with the specified index to the online object.

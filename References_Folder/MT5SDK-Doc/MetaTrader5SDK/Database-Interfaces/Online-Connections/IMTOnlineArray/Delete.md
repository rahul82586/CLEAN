[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTOnlineArray::Delete

Delete connection record object by its position.

C++
    
    
    MTAPIRES  IMTOnlineArray::Delete(
       const UINT  pos      // Connection record position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.Delete(
       uint        pos      // Connection record position
       )

### Parameters

**pos**  
[in] Position of a connection record in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTOnline::Release](../IMTOnline/Release.md) method.

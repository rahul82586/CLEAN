[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTOnlineArray::UpdateCopy

Change a connection record at the specified position of an array by copying the parameters of a passed object of a connection record.

C++
    
    
    MTAPIRES  IMTOnlineArray::UpdateCopy(
       const UINT        pos,       // Position
       const IMTOnline*  online     // Connection record object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOnlineArray.UpdateCopy(
       uint              pos,       // Position
       CIMTOnline        online     // Connection record object
       )

### Parameters

**pos**  
[in] Position of a client record in an array, starting with 0.

**online**  
[in] Connection record object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the online object into a connection record object at the specified position of an array.

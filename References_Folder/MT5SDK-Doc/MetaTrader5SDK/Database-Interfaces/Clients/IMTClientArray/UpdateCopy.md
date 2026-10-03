[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTClientArray::UpdateCopy

Change a client at the specified position of an array by copying the parameters of a passed client object.

C++
    
    
    MTAPIRES  IMTClientArray::UpdateCopy(
       const UINT        pos,       // Position
       const IMTClient*  client     // Client object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.UpdateCopy(
       uint              pos,       // Position
       CIMTClient        client     // Client object
       )

### Parameters

**pos**  
[in] Position of a client in the array, starting with 0.

**client**  
[in]Client object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method copies the 'client' object parameters to the client object at the specified position in the array.

[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTClientArray::Delete

Delete a client object by its position.

C++
    
    
    MTAPIRES  IMTClientArray::Delete(
       const UINT  pos      // Client position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClientArray.Delete(
       uint        pos      // Client position
       )

### Parameters

**pos**  
[in] Position of a client in the array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by calling the [IMTClient::Release](../IMTClient/Release.md) method.

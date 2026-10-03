[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Delete

[Previous](Requests-AddCopy.md) | [Next](Requests-Detach.md)

# IMTRequestArray::Delete

Delete a trade request by its index.

C++
    
    
    MTAPIRES  IMTRequestArray::Delete(
       const UINT  pos      // Request position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.Delete(
       uint        pos      // Request position
       )

### Parameters

**pos**  
[in] Position of a trade request in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by calling the [IMTRequest::Release](../IMTRequest/Requests-Release.md) method.

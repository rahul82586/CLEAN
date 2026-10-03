[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Detach

[Previous](Requests-Delete.md) | [Next](Requests-Update.md)

# IMTRequestArray::Detach

Detach an object of a trade request from an array.

C++
    
    
    IMTRequest*  IMTRequestArray::Detach(
       const UINT  pos      // Request position
       )

.NET (Gateway/Manager API)
    
    
    CIMTRequest  CIMTRequestArray.Detach(
       uint        pos      // Request position
       )

### Parameters

**pos**  
[in] Position of a trade request in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of the trade request.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.

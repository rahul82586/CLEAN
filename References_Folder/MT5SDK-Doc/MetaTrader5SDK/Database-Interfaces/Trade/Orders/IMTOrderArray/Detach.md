[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTOrderArray::Detach

Detach an object of a trade order from an array.

C++
    
    
    IMTOrder*  IMTOrderArray::Detach(
       const UINT  pos      // Position of an order
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTOrder  CIMTOrderArray.Detach(
       uint        pos      // Position of an order
       )

### Parameters

**pos**  
[in] Position of an order in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of an order.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.

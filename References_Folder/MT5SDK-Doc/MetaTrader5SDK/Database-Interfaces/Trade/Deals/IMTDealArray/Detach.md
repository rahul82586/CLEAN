[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTDealArray::Detach

Detach an object of a deal from an array.

C++
    
    
    IMTDeal*  IMTDealArray::Detach(
       const UINT  pos      // Position of a deal
       )

.NET (Gateway/Manager API)
    
    
    CIMTDeal  CIMTDealArray.Detach(
       uint        pos      // Position of a deal
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of a deal.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.

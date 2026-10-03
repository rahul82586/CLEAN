[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Detach

[Previous](IMTHistoryDealArray-Delete.md) | [Next](IMTHistoryDealArray-Update.md)

# IMTECNHistoryDealArray::Detach

Detach a deal object from an array.

C++
    
    
    IMTECNHistoryDeal*  IMTECNHistoryDealArray::Detach(
       const UINT  pos      // deal position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTECNHistoryDeal  CIMTECNHistoryDealArray.Detach(
       uint        pos      // deal position
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of a deal.

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.

[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Next

[Previous](IMTHistoryDealArray-Total.md) | [Next](IMTHistoryDealArray-Sort.md)

# IMTECNHistoryDealArray::Next

Get a deal object by its position.

C++
    
    
    IMTECNHistoryDeal*  IMTECNHistoryDealArray::Next(
       const UINT  pos      // deal position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTECNHistoryDeal  CIMTECNHistoryDealArray.Next(
       uint        pos      // deal position
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

### Return Value

If successful, the method returns a pointer to the deal object at the specified position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, if you delete an array object, the returned pointer will become invalid.

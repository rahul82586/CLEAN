[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray Delete

[Previous](IMTHistoryMatchingArray-AddCopy.md) | [Next](IMTHistoryMatchingArray-Detach.md)

# IMTECNHistoryMatchingArray::Delete

Delete a matching order object by its position.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::Delete(
       const UINT  pos      // order position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.Delete(
       uint        pos      // order position
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The deleted object will be automatically released by the [IMTECNHistoryMatching::Release](../IMTHistoryMatching.md) method call.

[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray UpdateCopy

[Previous](IMTHistoryMatchingArray-Update.md) | [Next](IMTHistoryMatchingArray-Shift.md)

# IMTECNHistoryMatchingArray::UpdateCopy

Update a matching order at the specified array position by copying the parameters of a passed order object.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::UpdateCopy(
       const UINT                    pos,    // position
       const IMTECNHistoryMatching*  order   // order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.UpdateCopy(
       uint                          pos,    // position
       CIMTECNHistoryMatching        order   // order object
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

**order**  
[in]Matching order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method copies the parameters of the order object into an object of an order at the specified position of an array.

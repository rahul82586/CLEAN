[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray Assign

[Previous](IMTHistoryMatchingArray-Release.md) | [Next](IMTHistoryMatchingArray-Clear.md)

# IMTECNHistoryMatchingArray

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNMatchingArray::Assign(
       const IMTECNHistoryMatchingArray*  array    // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.Assign(
       CIMTECNHistoryMatchingArray        array    // source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

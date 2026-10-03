[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray Assign

[Previous](IMTMatchingArray-Release.md) | [Next](IMTMatchingArray-Clear.md)

# IMTECNMatchingArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNMatchingArray::Assign(
       const IMTECNMatchingArray*  array    // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatchingArray.Assign(
       CIMTECNMatchingArray        array    // source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFillingArray](../IMTHistoryFillingArray.md) / IMTHistoryFillingArray Assign

[Previous](IMTHistoryFillingArray-Release.md) | [Next](IMTHistoryFillingArray-Clear.md)

# IMTECNFillingArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNHistoryFillingArray::Assign(
       const IMTECNHistoryFillingArray*  array     // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFillingArray.Assign(
       CIMTECNHistoryFillingArray        array     // source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

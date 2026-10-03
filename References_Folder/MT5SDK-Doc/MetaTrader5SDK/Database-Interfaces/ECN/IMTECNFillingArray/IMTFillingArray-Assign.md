[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray Assign

[Previous](IMTFillingArray-Release.md) | [Next](IMTFillingArray-Clear.md)

# IMTECNFillingArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNFillingArray::Assign(
       const IMTECNFillingArray*  array     // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFillingArray.Assign(
       CIMTECNFillingArray        array     // source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

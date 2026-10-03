[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Assign

[Previous](IMTHistoryFilling-Release.md) | [Next](IMTHistoryFilling-Clear.md)

# IMTECNHistoryFilling::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Assign(
       const IMTECNHistoryFilling*  order // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Assign(
       CIMTECNHistoryFilling        order // source object
       )

### Parameters

**order**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Assign

[Previous](IMTHistoryMatching-Release.md) | [Next](IMTHistoryMatching-Clear.md)

# IMTECNHistoryMatching::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Assign(
       const IMTECNHistoryMatching*  order // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Assign(
       CIMTECNHistoryMatching        order // source object
       )

### Parameters

**order**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

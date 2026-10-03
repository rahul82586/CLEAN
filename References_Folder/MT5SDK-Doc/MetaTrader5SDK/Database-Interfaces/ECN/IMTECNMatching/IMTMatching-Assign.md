[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Assign

[Previous](IMTMatching-Release.md) | [Next](IMTMatching-Clear.md)

# IMTECNMatching::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNMatching::Assign(
       const IMTECNMatching*  order // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Assign(
       CIMTECNMatching        order // source object
       )

### Parameters

**order**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

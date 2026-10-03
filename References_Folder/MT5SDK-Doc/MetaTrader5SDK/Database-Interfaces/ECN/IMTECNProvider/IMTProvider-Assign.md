[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProvider](../IMTProvider.md) / IMTProvider Assign

[Previous](IMTProvider-Release.md) | [Next](IMTProvider-Clear.md)

# IMTECNProvider::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNProvider::Assign(
       const IMTECNProvider*  provider // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNProvider.Assign(
       CIMTECNProvider        provider // source object
       )

### Parameters

**provider**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

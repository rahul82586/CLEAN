[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Assign

[Previous](IMTFilling-Release.md) | [Next](IMTFilling-Clear.md)

# IMTECNFilling::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNFilling::Assign(
       const IMTECNFilling*  order // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Assign(
       CIMTECNFilling        order // source object
       )

### Parameters

**order**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

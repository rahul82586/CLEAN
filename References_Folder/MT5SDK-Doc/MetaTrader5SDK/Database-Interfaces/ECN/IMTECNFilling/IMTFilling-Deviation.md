[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Deviation

[Previous](IMTFilling-Digits.md) | [Next](IMTFilling-Provider.md)

# IMTECNFilling::Deviation

Get the allowable deviation for the filling order.

C++
    
    
    UINT  IMTECNFilling::Deviation()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNFilling.Deviation()

### Return Value

Allowable deviation for the filling order. The value is specified in points.

# IMTECNFilling::Deviation

Set the allowable deviation for the filling order.

C++
    
    
    MTAPIRES  IMTECNFilling::Deviation(
       const UINT    deviation   // deviation
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Deviation(
       uint          deviation   // deviation
       )

### Parameters

**deviation**  
[in] Allowable deviation for the filling order. The value is specified in points.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

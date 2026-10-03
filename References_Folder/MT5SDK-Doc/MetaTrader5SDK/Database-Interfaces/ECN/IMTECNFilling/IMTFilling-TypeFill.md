[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling TypeFill

[Previous](IMTFilling-Type.md) | [Next](IMTFilling-TypeTime.md)

# IMTECNFilling::TypeFill

Get the fill policy used for the filling order.

C++
    
    
    UINT  IMTECNFilling::TypeFill()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNFilling.TypeFill()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](../../Trade/Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.

# IMTECNFilling::TypeFill

Set the fill policy used for the filling order.

C++
    
    
    MTAPIRES  IMTECNFilling::Type(
       const UINT  type      // fill policy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Type(
       uint        type      // fill policy
       )

### Parameters

**type**  
[in] Fill policy. The fill policy is passed using theIMTOrder::EnOrderFillingenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

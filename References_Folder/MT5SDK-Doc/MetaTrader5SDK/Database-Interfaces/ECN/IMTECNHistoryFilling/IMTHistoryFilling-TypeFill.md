[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling TypeFill

[Previous](IMTHistoryFilling-Type.md) | [Next](IMTHistoryFilling-TypeTime.md)

# IMTECNHistoryFilling::TypeFill

Get the fill policy used for the filling order.

C++
    
    
    UINT  IMTECNHistoryFilling::TypeFill()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryFilling.TypeFill()

### Return Value

A value of the [IMTOrder::EnOrderFilling (#enorderfilling)](../../Trade/Orders/IMTOrder/Enumerations.md#enorderfilling) enumeration.

# IMTECNHistoryFilling::TypeFill

Set the fill policy used for the filling order.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Type(
       const UINT  type      // fill policy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Type(
       uint        type      // fill policy
       )

### Parameters

**type**  
[in] Fill policy. The fill policy is passed using theIMTOrder::EnOrderFillingenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

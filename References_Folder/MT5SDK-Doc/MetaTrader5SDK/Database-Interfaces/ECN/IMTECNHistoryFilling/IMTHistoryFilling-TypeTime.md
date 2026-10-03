[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling TypeTime

[Previous](IMTHistoryFilling-TypeFill.md) | [Next](IMTHistoryFilling-VolumeInitialExt.md)

# IMTECNHistoryFilling::TypeTime

Get the expiration type of the filling order.

C++
    
    
    UINT  IMTECNHistoryFilling::TypeTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryFilling.TypeTime()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertime) enumeration.

# IMTECNHistoryFilling::TypeTime

Set the expiration type of the filling order.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::TypeTime(
       const UINT  type      // expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.TypeTime(
       uint        type      // expiration type
       )

### Parameters

**type**  
[in] Filling order expiration type. The type is passed using theIMTOrder::EnOrderTimeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

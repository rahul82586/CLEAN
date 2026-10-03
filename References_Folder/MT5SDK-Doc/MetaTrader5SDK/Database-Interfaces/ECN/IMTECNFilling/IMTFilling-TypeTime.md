[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling TypeTime

[Previous](IMTFilling-TypeFill.md) | [Next](IMTFilling-VolumeInitialExt.md)

# IMTECNFilling::TypeTime

Get the expiration type of the filling order.

C++
    
    
    UINT  IMTECNFilling::TypeTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNFilling.TypeTime()

### Return Value

A value of the [IMTOrder::EnOrderTime (#enordertime)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertime) enumeration.

# IMTECNFilling::TypeTime

Set the expiration type of the filling order.

C++
    
    
    MTAPIRES  IMTECNFilling::TypeTime(
       const UINT  type      // expiration type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.TypeTime(
       uint        type      // expiration type
       )

### Parameters

**type**  
[in] Filling order expiration type. The type is passed using theIMTOrder::EnOrderTimeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

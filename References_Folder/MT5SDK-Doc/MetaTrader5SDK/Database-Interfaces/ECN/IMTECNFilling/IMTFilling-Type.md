[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Type

[Previous](IMTFilling-Symbol.md) | [Next](IMTFilling-TypeFill.md)

# IMTECNFilling::Type

Get the type of the order created for sending to the external system.

C++
    
    
    UINT  IMTECNFilling::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNFilling.Type()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertype) enumeration.

# IMTECNFilling::Type

Set the type of the order created for sending to the external system.

C++
    
    
    MTAPIRES  IMTECNFilling::Type(
       const UINT  type      // order type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Type(
       uint        type      // order type
       )

### Parameters

**type**  
[in] Order type. The type is passed using theEnOrderTypeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

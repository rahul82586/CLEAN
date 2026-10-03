[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Type

[Previous](IMTHistoryFilling-Symbol.md) | [Next](IMTHistoryFilling-TypeFill.md)

# IMTECNHistoryFilling::Type

Get the type of the order created for sending to the external system.

C++
    
    
    UINT  IMTECNHistoryFilling::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryFilling.Type()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](../../Trade/Orders/IMTOrder/Enumerations.md#enordertype) enumeration.

# IMTECNHistoryFilling::Type

Set the type of the order created for sending to the external system.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Type(
       const UINT  type      // order type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Type(
       uint        type      // order type
       )

### Parameters

**type**  
[in] Order type. The type is passed using theEnOrderTypeenumeration.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

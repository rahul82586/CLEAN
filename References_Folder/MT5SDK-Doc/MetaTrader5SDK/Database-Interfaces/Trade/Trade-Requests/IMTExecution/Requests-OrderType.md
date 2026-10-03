[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests OrderType

[Previous](Requests-OrderExternalID.md) | [Next](Requests-OrderVolume.md)

# IMTExecution::OrderType

Get the order type.

C++
    
    
    UINT  IMTExecution::OrderType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.OrderType()

### Return Value

A value of the [IMTOrder::EnOrderType (#enordertype)](../../Orders/IMTOrder/Enumerations.md#enordertype) enumeration.

# IMTExecution::OrderType

Set the order type.

C++
    
    
    MTAPIRES  IMTExecution::OrderType(
       const UINT  type      // Order type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.OrderType(
       uint        type      // Order type
       )

### Parameters

**type**  
[in] Order type. To pass the type, theEnOrderTypeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

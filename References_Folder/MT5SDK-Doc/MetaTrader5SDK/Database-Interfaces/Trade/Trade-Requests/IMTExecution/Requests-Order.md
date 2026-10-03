[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Order

[Previous](Requests-Comment.md) | [Next](Requests-OrderExternalID.md)

# IMTExecution::Order

Gets the number of an order in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTExecution::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.Order()

### Return Value

The number of an order in the MetaTrader 5 platform.

### Note

This is a required trade execution field.

# IMTExecution::Order

Sets the number of an order in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTExecution::Order(
       const UINT64  order      // Order number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Order(
       ulong         order      // Order number
       )

### Parameters

**order**  
[in] The number of an order in the MetaTrader 5 platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a required trade execution field.

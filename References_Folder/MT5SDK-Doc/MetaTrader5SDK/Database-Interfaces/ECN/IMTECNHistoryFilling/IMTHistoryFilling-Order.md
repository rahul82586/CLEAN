[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Order

[Previous](IMTHistoryFilling-Clear.md) | [Next](IMTHistoryFilling-OrderMatching.md)

# IMTECNHistoryFilling::Order

Get the order ticket in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTECNHistoryFilling::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryFilling.Order()

### Return Value

Order ticket in the MetaTrader 5 platform.

# IMTECNHistoryFilling::Order

Set the order ticket in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Order(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Order(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The ticket of the filling order in the MetaTrader 5 platform.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

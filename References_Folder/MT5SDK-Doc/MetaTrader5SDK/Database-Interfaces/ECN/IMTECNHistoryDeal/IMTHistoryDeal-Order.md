[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Order

[Previous](IMTHistoryDeal-Clear.md) | [Next](IMTHistoryDeal-OrderGateway.md)

# IMTECNHistoryDeal::Order

Get the ticket of the original client order in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTECNHistoryDeal::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryDeal.Order()

### Return Value

The ticket of the original client order in the MetaTrader 5 platform.

# IMTECNHistoryDeal::Order

Set the ticket of the original client order in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Order(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Order(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The ticket of original client order in the MetaTrader 5 platform.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

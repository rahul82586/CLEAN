[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal DealGateway

[Previous](IMTHistoryDeal-OrderGateway.md) | [Next](IMTHistoryDeal-Login.md)

# IMTECNHistoryDeal::DealGateway

Get the internal ticket of the deal (used within the ECN for internal purposes).

C++
    
    
    UINT64  IMTECNHistoryDeal::DealGateway()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryDeal.DealGateway()

### Return Value

The internal ticket of the deal.

# IMTECNHistoryDeal::DealGateway

Set the internal ticket of the deal (used within the ECN for internal purposes).

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::DealGateway(
       const UINT64  deal       // deal ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.DealGateway(
       ulong         deal       // deal ticket
       )

### Parameters

**deal**  
[in] The internal ticket of the deal.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

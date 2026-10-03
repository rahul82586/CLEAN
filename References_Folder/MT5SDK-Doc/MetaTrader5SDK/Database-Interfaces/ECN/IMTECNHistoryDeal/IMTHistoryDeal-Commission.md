[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Commission

[Previous](IMTHistoryDeal-DigitsGateway.md) | [Next](IMTHistoryDeal-Provider.md)

# IMTECNHistoryDeal::Commission

Get the commission charged by an external system for the deal.

C++
    
    
    UINT  IMTECNHistoryDeal::Commission()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryDeal.Commission()

### Return Value

Commission charged by the external system for the deal.

### Note

The commission is charged by the gateway through which the deal is executed.

# IMTECNHistoryDeal::Commission

Set the commission charged by an external system for the deal.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Commission(
       const UINT    commission  // commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Commission(
       uint          commission  // commission
       )

### Parameters

**commission**  
[in] Commission charged by the external system for the deal.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

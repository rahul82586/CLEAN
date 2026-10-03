[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Action

[Previous](IMTHistoryDeal-Symbol.md) | [Next](IMTHistoryDeal-VolumeExt.md)

# IMTECNHistoryDeal::Action

Get deal type.

C++
    
    
    UINT  IMTECNHistoryDeal::Action()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryDeal.Action()

### Return Value

[IMTDeal::EnDealAction (#endealaction)](../../Trade/Deals/IMTDeal/Enumerations.md#endealaction) enumeration value. DEAL_BUY and DEAL_SELL values are used.

# IMTECNHistoryDeal

Set the deal type.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Action(
       const UINT  action    // deal type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Action(
       uint        action    // deal type
       )

### Parameters

**action**  
[in] Deal type. The deal type is passed using theIMTDeal::EnDealActionenumeration. DEAL_BUY and DEAL_SELL values are used.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

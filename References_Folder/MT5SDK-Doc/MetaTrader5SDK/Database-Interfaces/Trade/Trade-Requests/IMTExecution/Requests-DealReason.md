[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealReason

[Previous](Requests-DealPrice.md) | [Next](Requests-DealStorage.md)

# IMTExecution::DealReason

Get the reason for a deal.

C++
    
    
    UINT  IMTExecution::Reason()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.Reason()

### Return Value

A value of the [IMTDeal::EnDealReason (#endealreason)](../../Deals/IMTDeal/Enumerations.md#endealreason) enumeration.

# IMTExecution::DealReason

Set the reason for a deal.

C++
    
    
    MTAPIRES  IMTExecution::DealReason(
       const UINT  reason      // Deal reason
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealReason(
       uint        reason      // Deal reason
       )

### Parameters

**reason**  
[in] The reason for deal execution. To pass it, theIMTDeal::EnDealReasonenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The deal reason can be additionally specified when using the [TE_DEAL_EXTERNAL](Requests-Enumerations.md) trade execution.

## 

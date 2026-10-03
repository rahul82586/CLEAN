[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / ExpertID

[Previous](RateMargin.md) | [Next](PositionID.md)

# IMTDeal::ExpertID

Get the ID of the Expert Advisor that has executed a deal.

C++
    
    
    UINT64  IMTDeal::ExpertID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.ExpertID()

### Return Value

The ID of the Expert Advisor that has executed a deal. If a deals has been set manually, 0 is returned.

### Note

This identifier is set by the Expert Advisor.

# IMTDeal::ExpertID

Set the ID of the Expert Advisor that has executed a deal.

C++
    
    
    MTAPIRES  IMTDeal::ExpertID(
       const UINT64  id      // Expert Advisor ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.ExpertID(
       ulong         id      // Expert Advisor ID
       )

### Parameters

**id**  
[in] The ID of the Expert Advisor that has executed a deal. The 0 value means that the deal was executed manually.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

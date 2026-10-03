[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Entry

[Previous](Action.md) | [Next](Digits.md)

# IMTDeal::Entry

Get the direction of a deal.

C++
    
    
    UINT  IMTDeal::Entry()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDeal.Entry()

### Return Value

A value of the [IMTDeal::EnDealEntry (#endealentry)](Enumerations.md#endealentry) enumeration.

# IMTDeal::Entry

Set the direction of a deal.

C++
    
    
    MTAPIRES  IMTDeal::Entry(
       const UINT  entry      // Direction of a deal
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Entry(
       uint        entry      // Direction of a deal
       )

### Parameters

**entry**  
[in] The direction of a deal. TheIMTDeal::EnDealEntryenumeration is used to pass the direction..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

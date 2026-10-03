[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Action

[Previous](Order.md) | [Next](Entry.md)

# IMTDeal::Action

Get the type of action performed with a deal.

C++
    
    
    UINT  IMTDeal::Action()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTDeal.Action()

### Return Value

A value of the [IMTDeal::EnDealAction (#endealaction)](Enumerations.md#endealaction) enumeration.

# IMTDeal::Action

Set the type of action performed with a deal.

C++
    
    
    MTAPIRES  IMTDeal::Action(
       const UINT  action      // Type of action
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Action(
       uint        action      // Type of action
       )

### Parameters

**action**  
[in] Tupe of action performed with a deal. TheIMTDeal::EnDealActionenumeration is used to pass the action..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

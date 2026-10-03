[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealSink](../IMTDealSink.md) / OnDealPerformCloseBy

[Previous](OnDealPerform.md) | [Next](../../Positions.md)

# IMTDealSink::OnDealPerformCloseBy

A handler of the event related to the execution of a Close By deal, created using the [IMTServerAPI:DealPerformCloseBy](../../../../Server-API/Main-API-Interface/Trade/Deals/DealPerformCloseBy.md) function.

C++
    
    
    virtual void  IMTDealSink::OnDealPerformCloseBy(
       const IMTDeal*  deal      // Pointer to the deal object
       const IMTDeal*  deal_by   // Pointer to the deal object
       IMTAccount*     account   // Pointer to the account trade state
       IMTPosition*    position  // Pointer to the resulting position
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDealSink.OnDealPerformCloseBy(
       CIMTDeal        deal      // Pointer to the deal object
       CIMTDeal        deal_by   // Pointer to the deal object
       CIMTAccount     account   // Pointer to the account trade state
       CIMTPosition    position  // Pointer to the resulting position
       )

### Parameters

**deal**  
[in] A pointer to the object of thedealwhich has been executed to close the source position.

**deal_by**  
[in] A pointer to the object of thedealwhich has been executed to close the opposite position.

**account**  
[in] A pointer to the object of theaccount trading stateafter deal execution.

**position**  
[in] A pointer to the object of the resultingpositionafter deal execution.

### Note

The handler is only called for [IMTDeal::ENTRY_OUT_BY (#endealentry)](../IMTDeal/Enumerations.md#endealentry) type deals, in addition to [IMTDealSink::OnDealPerform](OnDealPerform.md).

[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealSink](../IMTDealSink.md) / OnDealPerform

[Previous](OnDealSync.md) | [Next](OnDealPerformCloseBy.md)

# IMTDealSink::OnDealPerform

A handler of the event of execution of a deal, created using [IMTServerAPI:DealPerform*](../../../../Server-API/Main-API-Interface/Trade/Deals/DealPerform.md), [IMTAdminAPI:DealPerform*](../../../../Manager-API/Administrator-Interface/Trade-Databases/Deals/DealPerform.md) or [IMTManagerAPI::DealPerform*](../../../../Manager-API/Manager-Interface/Trade-Databases/Deals/DealPerform.md) function.

C++
    
    
    virtual void  IMTDealSink::OnDealPerform(
       const IMTDeal*  deal      // A pointer to the deal object
       IMTAccount*     account   // A pointer to the trading state of an accounts
       IMTPosition*    position  // A pointer to the final position
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDealSink.OnDealPerform(
       CIMTDeal        deal      // A pointer to the deal object
       CIMTAccount     account   // A pointer to the trading state of an accounts
       CIMTPosition    position  // A pointer to the final position
       )

### Parameters

**deal**  
[in] A pointer to the object of the executeddeal.

**account**  
[in] A pointer to the object of theaccount trading stateafter the execution of the deal.

**position**  
[in] A pointer to the object of the resultingpositionafter the execution of the deal. Due to architecture specifics, the position is transmitted with zero values in PriceOpen, TimeCreate and TimeCreateMsc fields.

### Note

The call of the handler means that the deal has been executed and the result of its execution is already reflected on the trading account balance and the position state.

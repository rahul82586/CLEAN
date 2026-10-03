[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / DealSet

[Previous](Deal.md) | [Next](ExternalID.md)

# IMTDeal::DealSet

Sets the ticket of a deal.

C++
    
    
    UINT64  IMTDeal::DealSet(
       const UINT64  deal      // The ticket of a deal
       )

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.DealSet(
       ulong         deal      // The ticket of a deal
       )

### Parameters

**deal**  
[in] Deal ticket.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method should only be used for recovering databases of deals using the [IMTAdminAPI::DealBackupRestore](../../../../Manager-API/Administrator-Interface/Trade-Databases/Deals/DealBackupRestore.md) method.

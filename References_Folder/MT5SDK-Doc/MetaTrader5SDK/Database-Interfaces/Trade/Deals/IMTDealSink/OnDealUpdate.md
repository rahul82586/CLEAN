[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealSink](../IMTDealSink.md) / OnDealUpdate

[Previous](OnDealAdd.md) | [Next](OnDealDelete.md)

# IMTDealSink::OnDealUpdate

A handler of the event of updating a deal.

C++
    
    
    virtual void  IMTDealSink::OnDealUpdate(
       const IMTDeal*  deal      // A pointer to the deal object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDealSink.OnDealUpdate(
       CIMTDeal        deal      // Deal object
       )

### Parameters

**deal**  
[in] A pointer to the object of the updated deal.

### Note

This method is called by the API to notify that a deal has been modified.

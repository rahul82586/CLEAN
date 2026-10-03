[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealSink](../IMTDealSink.md) / OnDealDelete

[Previous](OnDealUpdate.md) | [Next](OnDealClean.md)

# IMTDealSink::OnDealDelete

A handler of the event of deal removal.

C++
    
    
    virtual void  IMTDealSink::OnDealDelete(
       const IMTDeal*  deal      // A pointer to the deal object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDealSink.OnDealDelete(
       CIMTDeal        deal      // Deal object
       )

### Parameters

**deal**  
[in] A pointer to the object of the deleted deal.

### Note

This method is called by the API to notify that a deal has been deleted.

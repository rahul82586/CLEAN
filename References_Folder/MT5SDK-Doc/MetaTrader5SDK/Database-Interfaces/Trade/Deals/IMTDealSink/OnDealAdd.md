[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealSink](../IMTDealSink.md) / OnDealAdd

[Previous](../IMTDealSink.md) | [Next](OnDealUpdate.md)

# IMTDealSink::OnDealAdd

A handler of the event of adding a deal.

C++
    
    
    virtual void  IMTDealSink::OnDealAdd(
       const IMTDeal*  deal      // A pointer to the deal object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDealSink.OnDealAdd(
       CIMTDeal        deal      // Deal object
       )

### Parameters

**deal**  
[in] A pointer to the object of the added deal.

### Note

This method is called by the API to notify that a new deal has been added.

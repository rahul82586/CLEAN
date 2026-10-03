[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealSink](../IMTDealSink.md) / OnDealSync

[Previous](OnDealClean.md) | [Next](OnDealPerform.md)

# IMTDealSink::OnDealSync

A handler of the event of a deal database synchronization.

C++
    
    
    virtual void  IMTDealSink::OnDealSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDealSink.OnDealSync()

### Note

This method is called only on the trade server in the Server API. It notifies of the completion of deal database synchronization between the trade server and its backup server.

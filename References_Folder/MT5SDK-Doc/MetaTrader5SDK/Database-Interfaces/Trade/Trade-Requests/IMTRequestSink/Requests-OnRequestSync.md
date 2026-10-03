[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestSink](../Requests-IMTRequestSink.md) / Requests OnRequestSync

[Previous](Requests-OnRequestDelete.md) | [Next](../Requests-IMTConfirm.md)

# IMTRequestSink::OnRequestSync

A handler of the event of synchronization of a queue of trade requests.

C++
    
    
    virtual void  IMTRequestSink::OnRequestSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTRequestSink.OnRequestSync()

### Note

This handler is required to notify dealers of the events in the queue of trade requests.

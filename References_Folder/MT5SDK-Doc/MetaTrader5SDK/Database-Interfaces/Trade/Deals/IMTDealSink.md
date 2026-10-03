[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / IMTDealSink

[Previous](IMTDealArray/SearchRight.md) | [Next](IMTDealSink/OnDealAdd.md)

# IMTDealSink

The IMTDealSink class contains the following methods:

Method | Purpose  
---|---  
[OnDealAdd](IMTDealSink/OnDealAdd.md) | A handler of the event of adding a deal.  
[OnDealUpdate](IMTDealSink/OnDealUpdate.md) | A handler of the event of updating a deal.  
[OnDealDelete](IMTDealSink/OnDealDelete.md) | A handler of the event of deal removal.  
[OnDealClean](IMTDealSink/OnDealClean.md) | A handler of the event of clearing of a client's deals.  
[OnDealSync](IMTDealSink/OnDealSync.md) | A handler of the event of a deal database synchronization (only in MetaTrader 5 Server API). The method is obsolete and is no longer used.  
[OnDealPerform](IMTDealSink/OnDealPerform.md) | A handler of the event of deal execution (only in MetaTrader 5 Server API).  
[OnDealPerformCloseBy](IMTDealSink/OnDealPerformCloseBy.md) | A handler of the event related to the execution of a Close By deal (only in MetaTrader 5 Server API).  
  
> In events, it is only allowed to use synchronous calls of methods changing, creating and deleting only those deals which are in the same groups as the deal for which the event was received. In all other cases, you should use asynchronous calls — API methods should be called in a separate thread, and not in the thread that triggers the events of the deal database. Failure to comply with this rule can cause server deadlocks.

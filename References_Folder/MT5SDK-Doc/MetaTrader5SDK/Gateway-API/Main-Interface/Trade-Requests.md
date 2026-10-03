[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Main Interface](../Main-Interface.md) / Trade Requests

[Previous](Trade-Databases/PositionCreate.md) | [Next](Trade-Requests/RequestCreate.md)

# Trade Requests

Functions described in this section allow working with the server trade requests queue. They allow to get existing trade requests and subscribe to events associated with changes in the queue of requests.

The following functions are available for working with trade requests:

Function | Purpose  
---|---  
[RequestCreate](Trade-Requests/RequestCreate.md) | Create an object of a trade request.  
[RequestArrayCreate](Trade-Requests/RequestArrayCreate.md) | Create an object of the array of trade requests.  
[RequestSubscribe](Trade-Requests/RequestSubscribe.md) | Subscribe to events associated with trade requests queue changes.  
[RequestUnsubscribe](Trade-Requests/RequestUnsubscribe.md) | Unsubscribe from events associated with requests queue changes.  
[RequestTotal](Trade-Requests/RequestTotal.md) | Get the total amount of trade requests in a requests queue.  
[RequestNext](Trade-Requests/RequestNext.md) | Get a trade request by a queue position.  
[RequestGet](Trade-Requests/RequestGet.md) | Get a trade request by ID.  
[RequestGetAll](Trade-Requests/RequestGetAll.md) | Get all the trade requests in a queue.

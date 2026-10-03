[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests Request

[Previous](Requests-Unsubscribe.md) | [Next](Requests-Profit.md)

# IMTServerAPI::TradeRequest

Add a trade request to the queue of requests.
    
    
    MTAPIRES  IMTServerAPI::TradeRequest(
       IMTRequest*  request      // An object of a trade request
       )

### Parameters

**request**  
[in] An object of a trade request that is being added. The request object must first be created using theIMTServerAPI::TradeRequestCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

To track the execution result, use trade events handlers in [IMTTradeSink](../../../Interface-of-Trade-Events.md). To identify the request, use the [IMTRequest::ID](../../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ID.md) property which is filled by the trade server in the request object when placing it to the queue. 

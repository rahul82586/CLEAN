[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerLock

[Previous](DealerGet.md) | [Next](DealerAnswer.md)

# IMTServerAPI::DealerLock

Gets a request with the specified ID for processing.
    
    
    MTAPIRES  IMTServerAPI::DealerLock(
       const UINT64  dealer,     // Dealer's login
       const UINT    id,         // Trade request ID
       IMTRequest*   request     // An object of a trade request
       )

### Parameters

**dealer**  
[in] The login of the manager account, which will be used to process the request. Corresponds toIMTConManager::Login.

**id**  
[in] Trade request ID. TheIMTRequest::Idvalue is used as the identifier. A request with the specified identifier must exist in the queue.

**request**  
[out] The object of a trade request. The object must first be created using theIMTServerAPI::TradeRequestCreatemethod.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code. Code MT_RET_OK_NONE means that the request is no longer available on the trade server. For example, it could have been captured by another dealer or application.

### Note

The method can only be used after a call of [IMTServerAPI::DealerStart](DealerStart.md) for the appropriate manager account.

[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerGet

[Previous](DealerStop.md) | [Next](DealerLock.md)

# IMTServerAPI::DealerGet

Gets the next request for processing. The method captures requests from the queue in the same order they are received from clients.
    
    
    MTAPIRES  IMTServerAPI::DealerGet(
       const UINT64  dealer,     // Dealer's login
       IMTRequest*   request     // An object of a trade request
       )

### Parameters

**dealer**  
[in] The login of the manager account, which will be used to process the request. Corresponds toIMTConManager::Login.

**request**  
[out] The object of a trade request. The object must first be created using theIMTServerAPI::TradeRequestCreatemethod.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method can only be used after a call of [IMTServerAPI::DealerStart](DealerStart.md) for the appropriate manager account.

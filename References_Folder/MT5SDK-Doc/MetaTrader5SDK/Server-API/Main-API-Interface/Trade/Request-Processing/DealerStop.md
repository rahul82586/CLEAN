[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerStop

[Previous](DealerStart.md) | [Next](DealerGet.md)

# IMTServerAPI::DealerStop

Stops processing requests via the specified manager account.
    
    
    MTAPIRES  IMTServerAPI::DealerStop(
       const UINT64     dealer,  // Dealer's login
       IMTRequestSink*  request  // A pointer to the IMTRequestSink object
       )

### Parameters

**dealer**  
[in] The login of the manager account, dealing through which should be stopped. Corresponds toIMTConManager::Login.

**request**  
[in] A pointer to theIMTRequestSinkobject, which was previously passed toIMTServerAPI::DealerStart.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The queue of requests is available to the plugin until the call of IMTServerAPI::DealerStop for each of the dealers, who were previously connected via [IMTServerAPI::DealerStart](DealerStart.md). For example, if the plugin starts processing requests on behalf of four different dealers, and then completes the operation of three of them, the plugin will continue to receive events.

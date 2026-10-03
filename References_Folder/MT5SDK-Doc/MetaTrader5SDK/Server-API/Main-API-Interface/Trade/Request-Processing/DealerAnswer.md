[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerAnswer

[Previous](DealerLock.md) | [Next](DealerExecution.md)

# IMTServerAPI::DealerAnswer

A response to a trade request, which [IMTServerAPI::DealerGet](DealerGet.md) or [IMTServerAPI::DealerLock](DealerLock.md) has received for processing.
    
    
    MTAPIRES  IMTServerAPI::DealerAnswer(
       const UINT64  dealer,     // Dealer's login
       IMTConfirm*   confirm     // Trade request confirmation object
       )

### Parameters

**dealer**  
[in] The login of the manager account, on whose behalf the request is processed. Corresponds toIMTConManager::Login.

**confirm**  
[in] The filledtrade request confirmation object.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method can only be used after a call of [IMTServerAPI::DealerStart](DealerStart.md) for the appropriate manager account.

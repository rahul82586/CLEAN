[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerRequestGetAll

[Previous](DealerRequestGet.md) | [Next](../../History-Data.md)

# IMTServerAPI::DealerRequestGetAll

Gets all trade requests from the trade queue available to the specified manager account.
    
    
    MTAPIRES  IMTServerAPI::DealerRequestGetAll(
       const UINT64  dealer,     // Dealer's login
       IMTRequest*   requests    // An object of the array of trade requests
       )

### Parameters

**dealer**  
[in] The login of the manager account. Corresponds toIMTConManager::Login.

**requests**  
[out] An object of the array of trade requests. The object must first be created using theIMTServerAPI::TradeRequestCreateArraymethod.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method can only be used after a call of [IMTServerAPI::DealerStart](DealerStart.md) for the appropriate manager account.

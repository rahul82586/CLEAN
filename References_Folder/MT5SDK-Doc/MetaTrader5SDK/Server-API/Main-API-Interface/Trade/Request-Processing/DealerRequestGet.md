[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerRequestGet

[Previous](DealerRequestNext.md) | [Next](DealerRequestGetAll.md)

# IMTServerAPI::DealerRequestGet

Gets a trade request with the specified identifier.
    
    
    MTAPIRES  IMTServerAPI::DealerRequestGet(
       const UINT64  dealer,     // Dealer's login
       const UINT    id,         // Trade request ID
       IMTRequest*   request     // An object of a trade request
       )

### Parameters

**dealer**  
[in] The login of the manager account. Corresponds toIMTConManager::Login.

**id**  
[in] Trade request ID.IMTRequest::Idis used as an identifier.

**request**  
[out] The object of a trade request. The object must first be created using theIMTManagerAPI::RequestCreatemethod.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method can only be used after a call of [IMTServerAPI::DealerStart](DealerStart.md) for the appropriate manager account.

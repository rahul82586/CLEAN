[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerStart

[Previous](../Request-Processing.md) | [Next](DealerStop.md)

# IMTServerAPI::DealerStart

Starts processing requests on behalf of the specified manager account.
    
    
    MTAPIRES  IMTServerAPI::DealerStart(
       const UINT64     dealer,  // Dealer's login
       IMTRequestSink*  request  // A pointer to the IMTRequestSink object
       )

### Parameters

**dealer**  
[in] The login of the manager account, on whose behalf requests will be processed. Corresponds toIMTConManager::Login.

**request**  
[in] A pointer to the object that implements theIMTRequestSinkinterface.

### Return value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The manger account needs to have the dealing permission: [IMTConManager::RIGHT_TRADES_DEALER (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights).

[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerRequestTotal

[Previous](DealerExecution.md) | [Next](DealerRequestNext.md)

# IMTServerAPI::DealerRequestTotal

Gets the total number of requests in the trade queue available to the specified manager account.
    
    
    UINT  IMTServerAPI::DealerRequestTotal(
       const UINT64  dealer      // Dealer's login
       )

### Return value

The number of trade requests in the queue.

### Note

The method can only be used after a call of [IMTServerAPI::DealerStart](DealerStart.md) for the appropriate manager account.

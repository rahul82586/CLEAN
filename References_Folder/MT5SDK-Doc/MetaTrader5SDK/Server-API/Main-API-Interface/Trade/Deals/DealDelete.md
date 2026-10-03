[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealDelete

[Previous](DealUpdateBatchArray.md) | [Next](DealDeleteBatch.md)

# IMTServerAPI::DealDelete

Deletes a deal from the server data base.
    
    
    MTAPIRES  IMTServerAPI::DealDelete(
       const UINT64  ticket      // The ticket of a deal
       )

### Parameters

**ticket**  
[in] The number (ticket) of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A deal can be deleted only from the plugins that run on the same trade server where the deal was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

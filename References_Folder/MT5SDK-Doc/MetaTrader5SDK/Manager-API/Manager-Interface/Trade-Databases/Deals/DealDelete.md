[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealDelete

[Previous](DealUpdateBatchArray.md) | [Next](DealDeleteBatch.md)

# IMTManagerAPI::DealDelete

Deletes a deal.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealDelete(
       const UINT64  ticket      // The ticket of a deal
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealDelete(
       ulong         ticket      // The ticket of a deal
       )

Python
    
    
    ManagerAPI.DealDelete(
       ticket        # The ticket of a deal
       )

### Parameters

**ticket**  
[in] The number (ticket) of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A deal can only be deleted from the applications connected to the trade server, on which the deal has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

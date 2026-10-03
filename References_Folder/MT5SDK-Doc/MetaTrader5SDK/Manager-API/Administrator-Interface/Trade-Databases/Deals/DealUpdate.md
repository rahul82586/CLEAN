[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealUpdate

[Previous](DealAddBatchArray.md) | [Next](DealUpdateBatch.md)

# IMTAdminAPI::DealUpdate

Updates a deal.

C++
    
    
    MTAPIRES  IMTAdminAPI::DealUpdate(
       IMTDeal*  deal      // Deal object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.DealUpdate(
       CIMTDeal  deal      // Deal object
       )

Python
    
    
    AdminAPI.DealUpdate(
       deal      # Deal object
       )

### Parameters

**deal**  
[in] An object of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A deal can be updated only from the applications that are connected to the same trade server where the deal was created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

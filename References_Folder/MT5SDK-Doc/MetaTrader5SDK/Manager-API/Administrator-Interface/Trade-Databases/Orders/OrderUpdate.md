[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderUpdate

[Previous](OrderAddBatchArray.md) | [Next](OrderUpdateBatch.md)

# IMTAdminAPI::OrderUpdate

Updates a trade order.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderUpdate(
       IMTOrder*  order      // An order object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderUpdate(
       CIMTOrder  order      // An order object
       )

Python
    
    
    AdminAPI.OrderUpdate(
       order      # An order object
       )

### Parameters

***order**  
[in] Order object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

An order can only be updated from the applications connected to the trade server, on which the order has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

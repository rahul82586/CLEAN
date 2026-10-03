[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderDelete

[Previous](OrderUpdateBatchArray.md) | [Next](OrderDeleteBatch.md)

# IMTManagerAPI::OrderDelete

Deletes a trade order.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderDelete(
       const UINT64  ticket      // Order number
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderDelete(
       ulong         ticket      // Order number
       )

Python
    
    
    ManagerAPI.OrderDelete(
       ticket        # Order number
       )

### Parameters

**ticket**  
[in] Order number.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

An order can only be deleted from the applications connected to the trade server, on which the order has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderRequestOpen

[Previous](OrderRequest.md) | [Next](OrderRequestByGroup.md)

# IMTAdminAPI::OrderRequestOpen

Request open orders of a client from a server.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderRequestOpen(
       const UINT64    login,      // Client login
       IMTOrderArray*  orders      // An object of the array of orders
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderRequestOpen(
       ulong           login,      // Client login
       CIMTOrderArray  orders      // An object of the array of orders
       )

Python
    
    
    AdminAPI.OrderRequestOpen(
       login           # Client login
       )

### Parameters

**login**  
[in] The login of the client, whose open orders you need to get.

**orders**  
[out] An object of the array of orders. The orders object must be first created using theIMTAdminAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method cannot be called from event handlers (any methods of IMT*Sink classes).

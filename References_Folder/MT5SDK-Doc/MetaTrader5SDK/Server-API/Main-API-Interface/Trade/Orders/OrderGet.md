[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderGet

[Previous](OrderCancelBatch.md) | [Next](OrderGetByGroup.md)

# IMTServerAPI::OrderGet

Get an open trade order by a ticket.
    
    
    MTAPIRES  IMTServerAPI::OrderGet(
       const UINT64  ticket,     // Ticket
       IMTOrder*     order       // An order object
       )

### Parameters

**ticket**  
[in] The number (ticket) of an order.

**order**  
[out] An object of a trade order. The order object must be first created using theIMTServerAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of an order with the specified ticket to the order object.

# IMTServerAPI::OrderGet

Gets open orders of a client.
    
    
    MTAPIRES  IMTServerAPI::OrderGet(
       const UINT64    login,      // Client login
       IMTOrderArray*  orders      // An object of the array of orders
       )

### Parameters

**login**  
[in] The login of the client, whose orders you need to get.

**orders**  
[out] An object of the array of orders. The orders object must be first created using theIMTServerAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

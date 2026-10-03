[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderGet

[Previous](OrderCreateArray.md) | [Next](OrderSelect.md)

# IMTReportAPI::OrderGet

Get an open trade order by a ticket.
    
    
    MTAPIRES  IMTReportAPI::OrderGet(
       const UINT64  ticket,     // Ticket
       IMTOrder*     order       // An order object
       )

### Parameters

**ticket**  
[in] The number (ticket) of an order.

**order**  
[out] An object of a trade order. The object object must be first created using theIMTReportAPI::OrderCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies data of an order with the specified ticket to the order object.

# IMTReportAPI::OrderGet

Gets open orders of a client.
    
    
    MTAPIRES  IMTReportAPI::OrderGet(
       const UINT64    login,      // Client login
       IMTOrderArray*  orders      // An object of the array of orders
       )

### Parameters

**login**  
[in] The login of the client, whose orders you need to get.

**orders**  
[out] An object of the array of orders. The orders object must be first created using theIMTReportAPI::OrderCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

To get the orders, generation of an appropriate snapshot must be turned on in a report ([MTReportInfo::SNAPSHOT_ORDERS (#ensnapshots)](../../../../Structures/MTReportInfo.md#ensnapshots) or [MTReportInfo::SNAPSHOT_ORDERS_FULL (#ensnapshots)](../../../../Structures/MTReportInfo.md#ensnapshots)).

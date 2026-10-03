[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryGetByGroup

[Previous](HistoryGet.md) | [Next](HistoryGetByGroupSymbol.md)

# IMTServerAPI::HistoryGetByGroup

Request closed orders (history) related to a client group.
    
    
    MTAPIRES  IMTServerAPI::HistoryGetByGroup(
       LPCWSTR            group,         // Group
       const INT64        from,          // Period from
       const INT64        to,            // Period to
       IMTOrderArray*     orders         // The object of the orders array
       )

### Parameters

**group**  
[in] The group for which the orders are requested.

**from**  
[in] The beginning of the period you want to receive orders for. The date is specified in seconds which have elapsed since 01.01.1970.

**to**  
[in] The end of the period you want to receive orders for. The date is specified in seconds which have elapsed since 01.01.1970.

**orders**  
[out] An object of the array of orders. The 'orders' object should be first created using theIMTServerAPI::OrderCreateArraymethod.

### Returned Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies to the 'orders' object the data of all closed orders belonging to clients in the specified groups.

[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Orders](../Orders.md) / HistoryGetTotal

[Previous](HistoryGet.md) | [Next](HistoryGetPage.md)

# MT5WebAPI.HistoryGetTotal

Get the number of closed orders of a client by the login in the specified time range.
    
    
    MTRetCode  MT5WebAPI.HistoryGetTotal(
       ulong     login,     // Login
       long      from,      // Beginning of period
       long      to,        // End of period
       out uint  total      // The number of orders
       )

### Parameters

**login**  
[in] The login of a client.

**from**  
[in] The beginning of the period for requesting orders. The date is specified in seconds since January 1, 1970.

**to**  
[in] The end of the period for requesting orders. The date is specified in seconds since January 1, 1970.

**total**  
[out] The number of closed orders of a client in the specified time range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

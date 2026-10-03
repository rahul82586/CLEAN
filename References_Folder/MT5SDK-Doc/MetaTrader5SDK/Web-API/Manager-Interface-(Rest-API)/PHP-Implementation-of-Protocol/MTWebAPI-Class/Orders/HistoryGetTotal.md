[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Orders](../Orders.md) / HistoryGetTotal

[Previous](HistoryGet.md) | [Next](HistoryGetPage.md)

# MTWebAPI::HistoryGetTotal

Get the number of closed orders of a client by the login in the specified time range.
    
    
    MTAPIRES  MTWebAPI::HistoryGetTotal(
       int  $login,     // Login
       int  $from,      // Beginning of period
       int  $to,        // End of period
       int  $total      // Number of orders
       )

### Parameters

**$login**  
[in] The login of a client.

**$from**  
[in] The beginning of the period for requesting orders. The date is specified in seconds since January 1, 1970.

**$to**  
[in] The end of the period for requesting orders. The date is specified in seconds since January 1, 1970.

**$total**  
[out] The number of closed orders of a client in the specified time range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

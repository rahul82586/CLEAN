[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Deals](../Deals.md) / DealGetTotal

[Previous](DealGet.md) | [Next](DealGetPage.md)

# MTWebAPI::DealGetTotal

Get the number of a client's deals by the login.
    
    
    MTAPIRES  MTWebAPI::DealGetTotal(
       int  $login,     // Login
       int  $from,      // Beginning of period
       int  $to,        // End of period
       int  $total      // Number of deals
       )

### Parameters

**$login**  
[in] The login of a client.

**$from**  
[in] The beginning of the period for requesting deals. The date is specified in seconds since January 1, 1970.

**$to**  
[in] The end of the period for requesting deals. The date is specified in seconds since January 1, 1970.

**$total**  
[out] The number of deals of the client with the specified login.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

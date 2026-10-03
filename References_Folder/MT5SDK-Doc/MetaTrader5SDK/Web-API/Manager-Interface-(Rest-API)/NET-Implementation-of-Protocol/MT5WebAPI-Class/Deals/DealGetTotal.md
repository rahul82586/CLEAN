[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Deals](../Deals.md) / DealGetTotal

[Previous](DealGet.md) | [Next](DealGetPage.md)

# MT5WebAPI.DealGetTotal

Get the number of a client's deals by the login.
    
    
    MTRetCode  MT5WebAPI.DealGetTotal(
       ulong     login,     // Login
       long      from,      // Beginning of period
       long      to,        // End of period
       out uint  total      // Number of deals
       )

### Parameters

**login**  
[in] The login of a client.

**from**  
[in] The beginning of the period for requesting deals. The date is specified in seconds since January 1, 1970.

**to**  
[in] The end of the period for requesting deals. The date is specified in seconds since January 1, 1970.

**total**  
[out] The number of deals of the client with the specified login.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

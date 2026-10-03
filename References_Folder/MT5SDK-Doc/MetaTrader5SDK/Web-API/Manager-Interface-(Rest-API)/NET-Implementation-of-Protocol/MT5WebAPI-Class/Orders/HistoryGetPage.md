[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Orders](../Orders.md) / HistoryGetPage

[Previous](HistoryGetTotal.md) | [Next](../Deals.md)

# MT5WebAPI.HistoryGetPage

Get closed orders of a client by the login.
    
    
    MTRetCode  MT5WebAPI.HistoryGetPage(
       ulong              login,   // Login
       long               from,    // Beginning of period
       long               to,      // End of period
       uint               offset,  // Order index
       uint               total,   // The number of orders
       out List<MTOrder>  orders   // The array of orders
       )

### Parameters

**login**  
[in] The login of the client whose closed orders you need to get.

**from**  
[in] The beginning of the period for requesting orders. The date is specified in seconds since January 1, 1970.

**to**  
[in] The end of the period for requesting orders. The date is specified in seconds since January 1, 1970.

**offset**  
[in] The index of the order starting from which you need to get orders. Numbering starts from 0.

**total**  
[in] The number of orders that should be obtained. The maximum number of orders that can be requested in one method call is 100.

**orders**  
[out] The MTOrder array of structures in which trade orders are described. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method allows to easily arrange a paged output of resulting orders. First you should get the total number of a client's orders using the [MT5WebAPI.HistoryGetTotal](HistoryGetTotal.md) method. After defining the number of orders that should be shown on one page (set by the total parameter), you can easily find the offset parameter for each page.

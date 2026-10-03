[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Orders](../Orders.md) / OrderGetTotal

[Previous](OrderGet.md) | [Next](OrderGetPage.md)

# MTWebAPI::OrderGetTotal

Get the number of open orders of a client by the login.
    
    
    MTAPIRES  MTWebAPI::OrderGetTotal(
       int  $login,     // Login
       int  $total      // Number of orders
       )

### Parameters

**$login**  
[in] The login of a client.

**$total**  
[out] The number of open orders of a client with the specified login.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

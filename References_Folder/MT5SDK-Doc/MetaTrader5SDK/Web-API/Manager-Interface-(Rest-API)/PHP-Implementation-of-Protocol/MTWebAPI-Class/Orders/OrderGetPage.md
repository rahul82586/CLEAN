[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Orders](../Orders.md) / OrderGetPage

[Previous](OrderGetTotal.md) | [Next](HistoryGet.md)

# MTWebAPI::OrderGetPage

Get open orders of a client by the login.
    
    
    MTAPIRES  MTWebAPI::OrderGetPage(
       int      $login,      // Login
       int      $offset,     // Order index
       int      $total,      // Number of orders
       MTOrder  $orders      // Array of orders
       )

### Parameters

**$login**  
[in] The login of the client whose orders you need to get.

**$offset**  
[in] The index of the order starting from which you need to get orders. Numbering starts from 0.

**$total**  
[in] The number of orders that should be obtained. The maximum number of orders that can be requested in one method call is 100.

**$orders**  
[out] The MTOrder array of structures in which trade orders are described. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method allows to easily arrange a paged output of resulting orders. First you should get the total number of a client's orders using the [MTWebAPI::OrderGetTotal](OrderGetTotal.md) method. After defining the number of orders that should be shown on one page (set by the total parameter), you can easily find the offset parameter for each page.

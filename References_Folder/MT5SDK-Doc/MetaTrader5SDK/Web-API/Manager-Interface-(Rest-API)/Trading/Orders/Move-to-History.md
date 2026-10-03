[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Move to History

[Previous](Delete-Open.md) | [Next](Get-Closed-by-Ticket.md)

# Move an open order to history

The request allows moving one or more open orders to history.

## Rest API

Request format
    
    
    GET /api/order/cancel?ticket=tickets
    POST /api/order/cancel?ticket=tickets
    POST /api/order/cancel
    [
      1012,
      4034
    ]

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/order/delete?ticket=73339,73340
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    ORDER_DELETE|TICKET=tickets\r\n

Response format
    
    
    ORDER_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * ticket — the ticket of the order to be moved to history. Multiple names can be specified as separated by commas. Also, the tickets can be specified as an array in the POST request body.



## Response parameters

  * RETCODE — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.



## Notes

  * When an order is transferred, its state changes to [IMTOrder::ORDER_STATE_CANCELED (#enorderstate)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate). Such orders are not executed or triggered, and no margin is charged for them.
  * An order can only be moved to history when connected to the same trade server on which it was created. If the order with the specified ticket is not found, response code [13](../../../../Return-Codes/Common-errors.md) is returned.



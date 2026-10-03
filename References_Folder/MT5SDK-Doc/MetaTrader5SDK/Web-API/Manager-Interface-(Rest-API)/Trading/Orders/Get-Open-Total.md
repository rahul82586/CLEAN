[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Get Open Total

[Previous](Get-Open-by-Ticket.md) | [Next](Get-Open-Paged.md)

# Getting the Number of Open Orders

This request allows to get the total number of open orders of a client by the login.

## Rest API

Request format
    
    
    GET /api/order/get_total?login=login
    POST /api/order/get_total?login=login

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/order/get_total?login=1020
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "10" }
    }

## Raw API

Request format
    
    
    ORDER_GET_TOTAL|LOGIN=login|\r\n

Response format
    
    
    ORDER_GET_TOTAL|RETCODE=code description|TOTAL=zzzz|\r\n

Example
    
    
    //--- request to the server
    003800010ORDER_GET_TOTAL|LOGIN=1020|
    //--- server response
    ORDER_GET_TOTAL|RETCODE=0 Done|TOTAL=10|

## Request Parameters

  * login — the login of a client



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * total — the number of open orders of a client with the specified login.



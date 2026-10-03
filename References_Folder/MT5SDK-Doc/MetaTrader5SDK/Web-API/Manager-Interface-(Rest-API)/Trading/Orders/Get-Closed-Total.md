[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Get Closed Total

[Previous](Get-Closed-by-Ticket.md) | [Next](Get-Closed-Paged.md)

# Getting the Number of Closed Orders

This request is used for obtaining the total number of orders in a client's history in the specified time range.

## Rest API

Request format
    
    
    GET /api/history/get_total?login=login&from=date&to=date
    POST /api/history/get_total?login=login&from=date&to=date

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/history/get_total?login=873061&from=1546345925&to=1569933125
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "428" }
    }

## Raw API

Request format
    
    
    HISTORY_GET_TOTAL|LOGIN=login|FROM=date|TO=date|\r\n

Response format
    
    
    HISTORY_GET_TOTAL|RETCODE=code description|TOTAL=number|\r\n

Example
    
    
    //--- request to the server
    007800010HISTORY_GET_TOTAL|LOGIN=1020|FROM=1314882419|TO=1315573619|
    //--- server response
    HISTORY_GET_TOTAL|RETCODE=0 Done|TOTAL=10|

## Request Parameters

  * login — the login of a client
  * from — the beginning of the period for requesting orders. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — the end of the period for requesting orders. The date is specified in seconds that have elapsed since 01.01.1970.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * total — the number of open orders of a client with the specified login.



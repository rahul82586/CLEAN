[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Deals](../Deals.md) / Get Total

[Previous](Get-by-Ticket.md) | [Next](Get-Paged.md)

# Getting the Number of Deals

This request is used for obtaining the total number of deals performed by a client in the specified time range.

## Rest API

Request format
    
    
    GET /api/deal/get_total?login=login&from=date&to=date
    POST /api/deal/get_total?login=login&from=date&to=date

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/deal/get_total?login=1020&from=1314882419&to=1315573619
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "10" }
    }

## Raw API

Request format
    
    
    DEAL_GET_TOTAL|LOGIN=login|FROM=date|TO=date|\r\n

Response format
    
    
    DEAL_GET_TOTAL|RETCODE=code description|TOTAL=zzzz|\r\n

Example
    
    
    //--- request to the server
    007200010DEAL_GET_TOTAL|LOGIN=1020|FROM=1314882419|TO=1315573619|
    //--- server response
    DEAL_GET_TOTAL|RETCODE=0 Done|TOTAL=10|

## Request Parameters

  * login — the login of a client
  * from — the beginning of the period for requesting deals. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — the end of the period for requesting deals. The date is specified in seconds that have elapsed since 01.01.1970.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * total — the number of deals performed by the client in the specified time range.



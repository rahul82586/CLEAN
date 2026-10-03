[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Get Total

[Previous](Get-by-Symbol.md) | [Next](Get-Paged.md)

# Getting the Number of Positions

This request allows to get the total number of open positions of a client.

## Rest API

Request format
    
    
    GET /api/position/get_total?login=login
    POST /api/position/get_total?login=login

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/position/get_total?login=1020
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "10" }
    }

## Raw API

Request format
    
    
    POSITION_GET_TOTAL|LOGIN=xxxx|\r\n

Response format
    
    
    POSITION_GET_TOTAL|RETCODE=xxxx yyyy|TOTAL=zzzz|\r\n

Example
    
    
    //--- request to the server
    003E00010POSITION_GET_TOTAL|LOGIN=1020|
    //--- server response
    POSITION_GET_TOTAL|RETCODE=0 Done|TOTAL=1|

## Request Parameters

  * login — the login of a client



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * total — the number of a client's positions that are currently open.



## Note

The request only works with open positions on the client's account. The history of positions is formed on the side of client terminals based on the history of trades. It is impossible to obtain it.

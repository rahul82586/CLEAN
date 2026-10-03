[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get Total

[Previous](Shift.md) | [Next](Get-List.md)

# Getting a Number of Symbols

This request allows to receive the number of symbols available on a trade server.

## Rest API

Request format
    
    
    GET /api/symbol/total
    POST /api/symbol/total

Response format
    
    
    {
     "retcode" : "code description",
      "answer" : { "Total" : "zzzz" }
    }

Example
    
    
    //--- request to the server
    GET /api/symbol/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "563" }
    }

## Raw API

Request format
    
    
    SYMBOL_TOTAL\r\n

Response format
    
    
    SYMBOL_TOTAL|RETCODE=code description|TOTAL=number|\r\n

Example
    
    
    //--- request to the server
    001e00010SYMBOL_TOTAL|
    //--- server response
    SYMBOL_TOTAL|RETCODE=0 Done|TOTAL=20|

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * total — the number of symbols on a server.



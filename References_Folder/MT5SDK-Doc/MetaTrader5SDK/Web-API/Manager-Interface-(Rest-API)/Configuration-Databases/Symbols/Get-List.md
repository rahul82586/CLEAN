[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get List

[Previous](Get-Total.md) | [Next](Get-by-Index.md)

# Getting a list of symbols

This request allows receiving the list of symbols available on the trading server.

## Rest API

Request Format
    
    
    GET /api/symbol/list
    POST /api/symbol/list

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ list of symbols ]
    }

The example
    
    
    //--- request to the server
    GET /api/symbol/list
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
         EURUSD,
         GBPUSD,
         USDCHF
      ]
    }

## Raw API

Request Format
    
    
    SYMBOL_LIST\r\n

Response Format
    
    
    SYMBOL_LIST|RETCODE=code description|\r\n
    [ list of symbols ]

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — list of available symbols.



## Note

The request takes into account the availability of symbols for the manager account which is used for [connection to the server](../../Text-Protocol-(Raw-API)/Authentication.md).

[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get the Number of Configurations

Getting the number of floating margin configurations existing on the trading server.

## Rest API

Request Format
    
    
    GET /api/leverage/total
    POST /api/leverage/total

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : { "Total" : "zzzz" }
    }

Example
    
    
    //--- request to the server
    GET /api/leverage/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "24" }
    }

## Raw API

Request Format
    
    
    SYMBOL_TOTAL\r\n

Response Format
    
    
    SYMBOL_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, the code of the encountered error is returned.
  * total — total number of configurations on the server.



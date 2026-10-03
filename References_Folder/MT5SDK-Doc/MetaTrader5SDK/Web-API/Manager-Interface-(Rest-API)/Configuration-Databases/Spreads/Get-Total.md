[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get the Number of Configurations

The request allows receiving the number of spread configurations available in the platform.

## Rest API

Request Format
    
    
    GET /api/spread/total
    POST /api/spread/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/spread/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    SPREAD_TOTAL\r\n

Response Format
    
    
    SPREAD_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the number of spread configurations in the trading platform.



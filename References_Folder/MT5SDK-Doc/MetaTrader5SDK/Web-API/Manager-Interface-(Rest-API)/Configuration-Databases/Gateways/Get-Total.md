[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get Total Gateways

The request allows receiving the number of gateway configurations available in the platform.

## Rest API

Request Format
    
    
    GET /api/gateway/total
    POST /api/gateway/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/gateway/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    GATEWAY_TOTAL\r\n

Response Format
    
    
    GATEWAY_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the number of gateway configurations in the trading platform.



[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get the number of subscription configurations

The request allows receiving the number of subscription configurations available in the platform.

## Rest API

Request Format
    
    
    GET /api/subscription/config/total
    POST /api/subscription/config/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/subscription/config/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_CFG_TOTAL\r\n

Response Format
    
    
    SUBSCRIPTION_CFG_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the number of subscription configurations in the trading platform.



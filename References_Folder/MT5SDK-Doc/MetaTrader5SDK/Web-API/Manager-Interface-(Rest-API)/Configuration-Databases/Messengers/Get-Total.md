[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get the Number of Messengers

The request allows receiving the number of messenger configurations available in the platform.

## Rest API

Request Format
    
    
    GET /api/messenger/total
    POST /api/messenger/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/messenger/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    MESSENGER_TOTAL\r\n

Response Format
    
    
    MESSENGER_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the number of messenger configurations in the trading platform.



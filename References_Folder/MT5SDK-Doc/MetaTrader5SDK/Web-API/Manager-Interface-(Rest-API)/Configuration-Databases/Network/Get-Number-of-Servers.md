[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Get Number of Servers

[Previous](Shift-Server.md) | [Next](Get-Server-by-Index.md)

# Get Number of Servers

The request allows receiving the number of server configurations available in the platform.

## Rest API

Request format
    
    
    GET /api/server/total
    POST /api/server/total

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/server/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request format
    
    
    SERVER_TOTAL\r\n

Response format
    
    
    SERVER_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — number of server configurations in the trading platform.



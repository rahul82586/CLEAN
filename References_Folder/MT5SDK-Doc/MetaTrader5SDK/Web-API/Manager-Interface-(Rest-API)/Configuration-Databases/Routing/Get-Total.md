[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get the Total Number of Routing Rules

The request allows receiving the number of routing rules available in the platform.

## Rest API

Request Format
    
    
    GET /api/route/total
    POST /api/route/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/route/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    ROUTE_TOTAL\r\n

Response Format
    
    
    ROUTE_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — number of routing rules in the trading platform.



[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Getting a number of groups

This request allows to receive the number of groups available on a trade server.

## Rest API

Request format
    
    
    GET /api/group/total
    POST /api/group/total

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/group/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "563" }
    }

## Raw API

Request format
    
    
    GROUP_TOTAL\r\n

Response format
    
    
    GROUP_TOTAL|RETCODE=code description|TOTAL=number|\r\n

Example
    
    
    //--- request to the server
    001c00010GROUP_TOTAL|
    //--- server response
    GROUP_TOTAL|RETCODE=0 Done|TOTAL=5|

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * total — the number of groups on a server.



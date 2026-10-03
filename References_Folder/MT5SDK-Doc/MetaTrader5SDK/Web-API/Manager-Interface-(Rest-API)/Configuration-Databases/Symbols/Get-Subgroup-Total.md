[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get Subgroup Total

[Previous](Shift-Subgroup.md) | [Next](Get-Subgroup-by-Index.md)

# Get the Number of Subgroups

Get the total number of symbol subgroups existing in the platform.

## Rest API

Request Format
    
    
    GET /api/symbol_group/total
    POST /api/symbol_group/total

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : { "Total" : "zzzz" }
    }

Example
    
    
    //--- request to the server
    GET /api/symbol_group/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "563" }
    }

## Raw API

Request Format
    
    
    SYMBOL_GROUP_TOTAL\r\n

Response Format
    
    
    SYMBOL_GROUP_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the total number of symbol subgroups on the server.



## Note

The request takes into account the availability of symbols for the manager account which is used for [connecting to the server](../../Text-Protocol-(Raw-API)/Authentication.md).

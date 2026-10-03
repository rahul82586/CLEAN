[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Shift Subgroup

[Previous](Delete-Subgroup.md) | [Next](Get-Subgroup-Total.md)

Subgroup Shift

Change the position of a subgroup of symbols in a list.

## Rest API

Request Format
    
    
    GET /api/symbol_group/shift?index=index&shift=shift
    POST /api/symbol_group/shift?index=index&shift=shift

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/symbol_group/shift?index0&shift=2
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    SYMBOL_GROUP_SHIFT|INDEX=index|SHIFT=shift]|\r\n

Response Format
    
    
    SYMBOL__GROUP_SHIFT|RETCODE=code description|\r\n

## Query Parameters

  * index — the position of the subgroup you want to shift, starting with 0.


  * shift — the shift of the subgroup relative to its current position. A negative value means shifting towards the top of the list, a positive value means shifting towards its end.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

The command only works when connected to the main trading server. Otherwise, error [12001](../../../../Return-Codes/API.md) is returned.

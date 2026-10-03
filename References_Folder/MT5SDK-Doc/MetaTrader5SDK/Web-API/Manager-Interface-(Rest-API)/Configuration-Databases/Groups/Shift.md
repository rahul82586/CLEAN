[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Shift

[Previous](Delete-Multiple.md) | [Next](Get-Total.md)

# Shift Groups

The requests allows changing of a group configuration position in a list.

## Rest API

Request format
    
    
    GET /api/group/shift?index=index&shift=shift
    POST /api/group/shift?index=index&shift=shift

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/group/shift?index0&shift=2
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    GROUP_SHIFT|INDEX=index|SHIFT=shift|\r\n

Response format
    
    
    GROUP_SHIFT|RETCODE=code description|\r\n

## Request Parameters

  * index — position of configuration to be shifted, starting from 0. Multiple IDs can be specified as separated by commas.
  * shift — shift of the configuration relative to its current position. A negative value means the shift towards the top of the list, a positive value means shifting towards its end.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit group configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.



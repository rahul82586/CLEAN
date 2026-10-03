[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / Shift

[Previous](Delete.md) | [Next](Get-Total.md)

# Shift Configuration

Change the position of a floating margin configuration in the list.

## Rest API

Request Format
    
    
    GET /api/leverage/shift?index=index&shift=shift
    POST /api/leverage/shift?index=index&shift=shift

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/leverage/shift?index0&shift=2
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    LEVERAGE_SHIFT|INDEX=index|SHIFT=shift|\r\n

Response Format
    
    
    LEVERAGE_SHIFT|RETCODE=code description|\r\n

## Request Parameters

  * index — position of configuration to be shifted, starting from 0. You can specify multiple values separated by commas.
  * shift — shift of the configuration relative to its current position. A negative value means shifting towards the top of the list, a positive value means shifting towards its end.



## Response Parameters

  * retcode — if successful, the query returns [response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit leverage configurations. Otherwise, error code [8](../../../../Return-Codes/Common-errors.md) is returned.



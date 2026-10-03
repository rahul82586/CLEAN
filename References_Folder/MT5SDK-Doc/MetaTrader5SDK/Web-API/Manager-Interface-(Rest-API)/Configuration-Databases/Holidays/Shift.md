[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / Shift

[Previous](Delete.md) | [Next](Get-Total.md)

# Shift Holiday

The requests allows changing the position of a holiday configuration in the list.

## Rest API

Request Format
    
    
    GET /api/holiday/shift?index=index&shift=shift
    POST /api/holiday/shift?index=index&shift=shift

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    GET /api/holiday/shift?index=0&shift=2
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    HOLIDAY_SHIFT|INDEX=index|SHIFT=shift|\r\n

Response Format
    
    
    HOLIDAY_SHIFT|RETCODE=code description|\r\n

## Request Parameters

  * index — the position of the rule to be shifted, starting from 0. Multiple tickets can be specified as separated by commas.
  * shift — shift of a rule relative to its current position. A negative value means shifting towards the top of the list, a positive value means shifting towards its end.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit holiday configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.



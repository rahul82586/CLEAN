[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / Delete

[Previous](Add.md) | [Next](Shift.md)

# Delete Configuration

Delete a floating margin configuration with the specified name.

## Rest API

Request Format
    
    
    GET /api/leverage/delete?name=name
    POST /api/leverage/delete?name=name

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/leverage/delete?name=Leverage
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    LEVERAGE_DELETE|NAME=name|\r\n

Response Format
    
    
    LEVERAGE_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * name — name of the configuration to be deleted.



## Response Parameters

  * retcode — if successful, the command returns [response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, the code of the encountered error is returned.



## Note

  * This command works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the command, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and to edit leverage configurations. Otherwise, error code [8](../../../../Return-Codes/Common-errors.md) is returned.



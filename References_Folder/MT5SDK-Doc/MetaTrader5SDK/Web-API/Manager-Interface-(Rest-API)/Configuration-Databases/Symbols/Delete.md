[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Delete

[Previous](Add-Multiple.md) | [Next](Delete-Multiple.md)

# Deleting a Symbol

Using this request you can delete a symbol with the specified name.

## Rest API

Request format
    
    
    GET /api/symbol/delete?symbol=name
    POST /api/symbol/delete?symbol=name

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/symbol/delete?group=EURUSD
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    SYMBOL_DELETE|SYMBOL=name|\r\n

Response format
    
    
    SYMBOL_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * symbol — the name of the symbol to delete.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.



## Notes

  * This command works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the command, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and edit symbol configurations. Otherwise, it returns the error code [8](../../../../Return-Codes/Common-errors.md).



[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / Delete

[Previous](Add.md) | [Next](Shift.md)

# Delete Messenger

The request allows deleting messenger configurations from the trading platform.

## Rest API

Request Format
    
    
    GET /api/messenger/delete?index=indices
    GET /api/messenger/delete?name=names
    POST /api/messenger/delete?index=indices
    POST /api/messenger/delete?name=names

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    GET /api/messenger/delete?index=0
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    MESSENGER_DELETE|INDEX=indices\r\n

Response Format
    
    
    MESSENGER_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * index — position of configuration to be deleted, starting from 0. Multiple tickets can be specified as separated by commas.
  * name — the name of the configuration to be deleted. Multiple tickets can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * Only one of the parameters can be specified in the request: index or name.
  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit messenger configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.



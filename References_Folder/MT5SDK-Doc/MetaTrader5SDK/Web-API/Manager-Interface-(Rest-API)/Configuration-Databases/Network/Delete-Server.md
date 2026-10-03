[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Delete Server

[Previous](Add-Server.md) | [Next](Shift-Server.md)

# Removing the Server

The request enables the deletion of platform server configurations.

## Rest API

Request format
    
    
    GET /api/server/delete?id=identifiers
    GET /api/server/delete?index=indexes
     
    POST /api/server/delete?id=identifiers
    POST /api/server/delete?index=indexes

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/server/delete?id=2
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    SERVER_DELETE|ID=identifiers\r\n
    SERVER_DELETE|INDEX=indexes\r\n

Response format
    
    
    SERVER_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * id — the identifier of the server to be deleted. Multiple IDs can be specified as separated by commas.
  * index — position of configuration to be deleted, starting from 0. Multiple IDs can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * Only one of the parameters can be specified in a request, i.e. id or index. Indication of two lists simultaneously is not allowed.
  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit group configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.



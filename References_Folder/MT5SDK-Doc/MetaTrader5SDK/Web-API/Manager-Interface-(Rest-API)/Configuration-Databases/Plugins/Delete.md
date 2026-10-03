[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / Delete

[Previous](Add.md) | [Next](Shift.md)

# Delete Plugin

The request allows deleting plugin configurations from the trading platform.

## Rest API

Request Format
    
    
    GET /api/plugin/delete?server=identifier&name=names
    POST /api/plugin/delete?server=identifier&name=names

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    GET /api/plugin/delete?server=1&name=Manager%20API%20Extension
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    PLUGIN_DELETE|SERVER=identifier|NAME=names\r\n

Response Format
    
    
    PLUGIN_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * server — the identifier of the server from which the plugin configuration should be deleted.
  * name — the name of the configuration to be deleted. Multiple indices can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit plugin configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.



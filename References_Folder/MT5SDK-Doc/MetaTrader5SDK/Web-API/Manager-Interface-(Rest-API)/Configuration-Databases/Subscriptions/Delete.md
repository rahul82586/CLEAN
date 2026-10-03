[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / Delete

[Previous](Add.md) | [Next](Shift.md)

# Delete a subscription configuration

The request enables the deletion of subscription configurations in the platform.

## Rest API

Request Format
    
    
    GET /api/subscription/config/delete?id=identifiers
    GET /api/subscription/config/delete?index=indices
     
    POST /api/subscription/config/delete?id=identifiers
    POST /api/subscription/config/delete?index=indices

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/subscription/config/delete?id=2
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    SUBSCRIPTION_CFG_DELETE|ID=identifiers\r\n
    SUBSCRIPTION_CFG_DELETE|INDEX=indices\r\n

Response Format
    
    
    SUBSCRIPTION_CFG_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * id — the identifier of the subscription configuration to be deleted. Multiple indices can be specified as separated by commas.
  * index — position of configuration to be deleted, starting from 0. Multiple indices can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * Only one of the parameters can be specified in a request, i.e. id or index. Indication of two lists simultaneously is not allowed.
  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to access the Subscriptions section. Otherwise, error code [8](../../../../Return-Codes/Common-errors.md) is returned.



[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / Restart

[Previous](Data-Structure.md) | [Next](Add.md)

# Restart Gateways

The request allows restarting all gateways in the platform.

## Rest API

Request Format
    
    
    GET /api/gateway/restart
    POST /api/gateway/restart

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/gateway/restart
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    GATEWAY_RESTART|\r\n

Response Format
    
    
    GATEWAY_RESTART|RETCODE=code description|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



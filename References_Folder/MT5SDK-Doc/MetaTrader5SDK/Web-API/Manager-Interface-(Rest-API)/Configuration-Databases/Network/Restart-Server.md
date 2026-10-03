[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Restart Server

[Previous](Get-Server-by-Identifier.md) | [Next](Add-Certificate.md)

# Server Restart

This request restarts the server to which the Web client is connected. If a Web client is connected to the main trade server, this command will restart all the trading platform.

## Rest API

Request format
    
    
    GET /api/server/restart
    POST /api/server/restart

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/server/restart
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    SERVER_RESTART\r\n

Response format
    
    
    SERVER_RESTART|RETCODE=code description|\r\n

## Response parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.



## Notes

Restart servers only on weekends and holidays or at night when the trading activity is minimal. Restarting the server may take several seconds (up to a minute), during this time connection to the server is impossible.

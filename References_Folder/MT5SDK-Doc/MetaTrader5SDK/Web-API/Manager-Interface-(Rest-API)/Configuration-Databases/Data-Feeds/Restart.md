[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / Restart

[Previous](Data-Structure.md) | [Next](Add.md)

# Restart Data Feed

The request allows restarting all data feeds in the platform.

## Rest API

Request Format
    
    
    GET /api/feeder/restart
    POST /api/feeder/restart

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    GET /api/feeder/restart
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    FEEDER_RESTART|\r\n

Response Format
    
    
    FEEDER_RESTART|RETCODE=code description|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



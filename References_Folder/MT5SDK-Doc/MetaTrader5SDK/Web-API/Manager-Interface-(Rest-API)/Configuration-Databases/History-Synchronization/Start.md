[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / Start

[Previous](Data-Structure.md) | [Next](Add.md)

# Start History Synchronization

The request allows starting history synchronization in accordance with configuration settings.

## Rest API

Request Format
    
    
    GET /api/history_sync/start
    POST /api/history_sync/start

Response Format
    
    
    {
     "retcode" : "code description"
    }

The example
    
    
    //--- request to the server
    GET /api/history_sync/start
    //--- server response
    {
     "retcode" : "0 Done"
    }

## Raw API

Request Format
    
    
    HISTORY_SYNC_START|\r\n

Response Format
    
    
    HISTORY_SYNC_START|RETCODE=code description|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent manager is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.



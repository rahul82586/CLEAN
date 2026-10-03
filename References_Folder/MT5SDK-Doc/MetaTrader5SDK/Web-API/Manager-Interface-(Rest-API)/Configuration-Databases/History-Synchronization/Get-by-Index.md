[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / Get by Index

[Previous](Get-Total.md) | [Next](../Spreads.md)

# Get Configuration by Index

Get one or more history synchronization configurations by index in the list.

## Rest API

Request Format
    
    
    GET /api/history_sync/next?index=index&count=number
    POST /api/history_sync/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/history_sync/next?index=0
    //--- server response
    {
     "retcode" : "0 Done",
     "answer" : {
       "Enable" : "1",
       "Server" : "access.metatrader5.com:443",
       "ServerType" : "1",
       "Mode" : "0",
       "From" : "0",
       "To" : "0",
       "TimeCorrect" : "-1500",
       "Flags" : "0",
       "Data" : "2",
       "Symbols" : [
         {
          "Path" : "*"
         }
       ]
     }
    }

## Raw API

Request Format
    
    
    HISTORY_SYNC_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    HISTORY_SYNC_NEXT|RETCODE=code description|\r\n
    Configuration description in JSON format

## Request Parameters

  * index — index of the history synchronization configuration starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent configuration is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — description of the configuration in JSON format. The complete description of passed parameters is available under the ["Data structure"](Data-Structure.md) section.



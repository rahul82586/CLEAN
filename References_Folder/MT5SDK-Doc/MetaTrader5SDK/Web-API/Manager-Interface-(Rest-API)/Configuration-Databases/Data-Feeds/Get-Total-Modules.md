[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / Get Total Modules

[Previous](Get-by-Name.md) | [Next](Get-Module-by-Index.md)

# Get Total Data Feed Modules

The request allows receiving the number of data feed modules available in the platform.

## Rest API

Request Format
    
    
    GET /api/feeder/module/total
    POST /api/feeder/module/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/feeder/module/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "total" : "11" }
    }

## Raw API

Request Format
    
    
    FEEDER_MODULE_TOTAL\r\n

Response Format
    
    
    FEEDER_MODULE_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — number of data feed modules in the trading platform.



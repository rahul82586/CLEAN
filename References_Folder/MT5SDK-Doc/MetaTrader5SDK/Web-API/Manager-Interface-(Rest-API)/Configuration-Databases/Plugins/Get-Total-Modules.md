[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / Get Total Modules

[Previous](Get-by-Name.md) | [Next](Get-Module-by-Index.md)

# Get Total Plugin Modules

The request allows receiving the number of plugin modules available in the platform.

## Rest API

Request Format
    
    
    GET /api/plugin/module/total
    POST /api/plugin/module/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/plugin/module/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    PLUGIN_MODULE_TOTAL\r\n

Response Format
    
    
    PLUGIN_MODULE_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — number of plugin modules in the trading platform.



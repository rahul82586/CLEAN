[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](Get-Total-Modules.md)

# Get Plugin by Name

This request allows receiving a plugin configuration by its name.

## Rest API

Request Format
    
    
    GET /api/plugin/get?server=identifier&name=name
    POST /api/plugin/get?server=identifier&name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/plugin/get?server=1&name=Trade%20Transaction%20Report
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "Trade Transaction Report",
        "Server" : "5",
        "Module" : "Trades.Transaction.Reports64.dll",
        "Enable" : "1",
        "Flags" : "0",
        "Params" : [
          {
            "Type" : "6",
            "Name" : "Groups",
            "Value" : "*"
          }
        ]
      }
    }

## Raw API

Request Format
    
    
    PLUGIN_GET|SERVER=identifier|NAME=name|\r\n

Response Format
    
    
    PLUGIN_GET|RETCODE=code description|\r\n
    Configuration description in JSON format

## Request Parameters

  * server — the identifier of the server for which the plugin configuration is requested.
  * name — plugin configuration name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the plugin configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



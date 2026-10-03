[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / Get Module by Name

[Previous](Get-Module-by-Index.md) | [Next](../Subscriptions.md)

# Get Plugin Module by Name

This request allows receiving a report module description by its name.

## Rest API

Request Format
    
    
    GET /api/plugin/module/get?server=identifier&name=name
    POST /api/plugin/module/get?server=identifier&name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/plugin/module/get?server=1&name=Trade%20Transaction%20Report
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Server" : "5",
        "Module" : "Trades.Transaction.Reports64.dll",
        "Version" : "100",
        "VersionApi" : "2361",
        "Name" : "Trade Transaction Report",
        "Copyright" : "Copyright 2000-2021, MetaQuotes Software Corp.",
        "Description" : "Plugin for collect information for Trades.Transaction.Reports",
        "Path" : "Trades.Transaction.Reports64.dll",
        "Params" : [
          {
            "Type" : "6",
            "Name" : "Groups",
            "Value" : "*,!demo*,!contest*"
          }
        ]
      }
    }

## Raw API

Request Format
    
    
    PLUGIN_MODULE_GET|NAME=name|\r\n

Response Format
    
    
    PLUGIN_MODULE_GET|RETCODE=code description|\r\n
    Module description in JSON format

## Request Parameters

  * name — data feed module name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — plugin module name in JSON format. The complete description of passed server parameters is available under the ["Data structure" (#module)](Data-Structure.md#module) section.



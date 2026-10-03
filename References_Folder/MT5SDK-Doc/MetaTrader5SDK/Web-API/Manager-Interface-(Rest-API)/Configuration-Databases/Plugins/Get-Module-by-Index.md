[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / Get Module by Index

[Previous](Get-Total-Modules.md) | [Next](Get-Module-by-Name.md)

# Get Plugin Module by Index

The request allows receiving a report module description by an index in the list.

## Rest API

Request Format
    
    
    GET /api/report/module/next?index=index
    POST /api/report/module/next?index=index

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/report/module/next?index=0
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
    
    
    PLUGIN_MODULE_NEXT|INDEX=index\r\n

Response Format
    
    
    PLUGIN_MODULE_NEXT|RETCODE=code description|\r\n
    Module description in JSON format

## Request Parameters

  * index — the index of the module in the list starting with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent module is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — plugin module name in JSON format. The complete description of passed server parameters is available under the ["Data structure" (#module)](Data-Structure.md#module) section.



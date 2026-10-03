[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / Get Module by Index

[Previous](Get-Total-Modules.md) | [Next](Get-Module-by-Name.md)

# Get Data Feed Module by Index

The request allows receiving a data feed module description by an index in the list.

## Rest API

Request Format
    
    
    GET /api/feeder/module/next?index=index
    POST /api/feeder/module/next?index=index

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/feeder/module/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "MetaTrader 5 Feeder",
        "Module" : "MetaTrader5Feeder64.exe",
        "Server" : "access.metatrader5.com:443",
        "Login" : "1000",
        "Password" : "password",
        "Copyright" : "Copyright 2000-2021, MetaQuotes Software Corp.",
        "Description" : "The datafeed translates quotes and news from remote MetaTrader 5 server ",
        "Version" : "2380",
        "Modes" : "3",
        "Fields" : "15",
        "VersionApi" : "2361",
        "BuildDate" : "2 Apr 2020",
        "BuildApiDate" : "08 Mar 2020",
        "Params" : [
          {
            "Type" : "0",
            "Name" : "Quotes Time Original",
            "Value" : "No"
          },
          ...
        ]
      }
    }

## Raw API

Request Format
    
    
    FEEDER_MODULE_NEXT|INDEX=index\r\n

Response Format
    
    
    FEEDER_MODULE_NEXT|RETCODE=code description|\r\n
    Module description in JSON format

## Request Parameters

  * index — the index of the module in the list starting with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent module is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — data feed module name in JSON format. The complete description of passed server parameters is available under the ["Data structure" (#module)](Data-Structure.md#module) section.



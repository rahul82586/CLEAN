[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / Get Module by Name

[Previous](Get-Module-by-Index.md) | [Next](../Reports.md)

# Get Data Feed Module by Name

This request allows receiving a data feed module description by its name.

## Rest API

Request Format
    
    
    GET /api/feeder/module/get?name=name
    POST /api/feeder/module/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/feeder/module/get?name=MetaTrader5Feeder64.exe
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
    
    
    FEEDER_MODULE_GET|NAME=name|\r\n

Response Format
    
    
    FEEDER_MODULE_GET|RETCODE=code description|\r\n
    The description of the module in JSON format

## Request Parameters

  * name — data feed module name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — data feed module name in JSON format. The complete description of passed server parameters is available under the ["Data structure" (#module)](Data-Structure.md#module) section.



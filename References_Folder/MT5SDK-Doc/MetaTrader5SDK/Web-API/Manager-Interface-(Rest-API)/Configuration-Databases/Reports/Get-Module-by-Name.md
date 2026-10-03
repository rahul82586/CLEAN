[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Get Module by Name

[Previous](Get-Module-by-Index.md) | [Next](../Plugins.md)

# Get Report Module by Name

This request allows receiving a report module description by its name.

## Rest API

Request Format
    
    
    GET /api/report/module/get?server=identifier&name=name
    POST /api/report/module/get?server=identifier&name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/report/module/get?server=1&name=Credit%20Facility
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Server" : "1",
        "Name" : "Credit Facility",
        "Filename" : "Trades.Standard.Reports64.dll",
        "Copyright" : "Copyright 2000-2021, MetaQuotes Software Corp.",
        "Description" : "MetaTrader 5 Report API plug-in",
        "Version" : "100",
        "VersionApi" : "2361",
        "VersionIe" : "0",
        "Timeout" : "0",
        "Types" : "2",
        "Snapshots" : "0",
        "Path" : "Trades.Standard.Reports64.dll",
        "Category" : "Trades",
        "ParamsConfig" : [],
        "ParamsRequest" : [
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
    
    
    REPORT_MODULE_GET|NAME=name|\r\n

Response Format
    
    
    REPORT_MODULE_GET|RETCODE=code description|\r\n
    Module description in JSON format

## Request Parameters

  * name — data feed module name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — report module name in JSON format. The complete description of passed server parameters is available under the ["Data structure" (#module)](Data-Structure.md#module) section.



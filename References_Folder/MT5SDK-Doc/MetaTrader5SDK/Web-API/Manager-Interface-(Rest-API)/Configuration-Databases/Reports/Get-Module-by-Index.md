[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Get Module by Index

[Previous](Get-Total-Modules.md) | [Next](Get-Module-by-Name.md)

# Get Report Module by Index

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
    
    
    REPORT_MODULE_NEXT|INDEX=index\r\n

Response Format
    
    
    REPORT_MODULE_NEXT|RETCODE=code description|\r\n
    Module description in JSON format

## Request Parameters

  * index — the index of the module in the list starting with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent module is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — report module name in JSON format. The complete description of passed server parameters is available under the ["Data structure" (#module)](Data-Structure.md#module) section.



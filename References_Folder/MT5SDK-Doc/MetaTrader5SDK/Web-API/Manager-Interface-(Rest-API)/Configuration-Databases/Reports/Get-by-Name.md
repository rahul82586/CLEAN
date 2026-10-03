[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](Get-Total-Modules.md)

# Get Report by Name

This request allows receiving a report configuration by its name.

## Rest API

Request Format
    
    
    GET /api/report/get?server=identifier&name=name
    POST /api/report/get?server=identifier&name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/report/get?server=1&name=Daily%20Trades
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "Daily Trades",
        "Server" : "1",
        "Template" : "Daily Trades",
        "Enable" : "1",
        "Params" : [
          {
            "Type" : "0",
            "Name" : "Currency",
            "Value" : "USD"
          }
        ]
      }
    }

## Raw API

Request Format
    
    
    REPORT_GET|SERVER=identifier|NAME=name|\r\n

Response Format
    
    
    REPORT_GET|RETCODE=code description|\r\n
    Configuration description in JSON format

## Request Parameters

  * server — the identifier of the server for which the report configuration is requested.
  * name — report configuration name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the report configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



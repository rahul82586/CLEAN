[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Get Report by Index

Get the configuration of one or more reports by index in the list.

## Rest API

Request Format
    
    
    GET /api/report/next?index=index&count=number
    POST /api/report/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/report/next?index=0
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
    
    
    REPORT_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    REPORT_NEXT|RETCODE=code description|\r\n
    Configuration description in JSON format

## Request Parameters

  * index — report configuration index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent report is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — description of the report configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



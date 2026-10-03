[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get Total Reports

The request allows receiving the number of report configurations available in the platform.

## Rest API

Request Format
    
    
    GET /api/report/total
    POST /api/report/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/report/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    REPORT_TOTAL\r\n

Response Format
    
    
    REPORT_TOTAL|RETCODE=coed description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the number of report configurations in the trading platform.



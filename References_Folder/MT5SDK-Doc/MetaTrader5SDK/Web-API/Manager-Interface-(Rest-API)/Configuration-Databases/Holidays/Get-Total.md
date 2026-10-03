[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get the Number of Holidays

The request allows receiving the number of holiday configurations available in the platform.

## Rest API

Request Format
    
    
    GET /api/holiday/total
    POST /api/holiday/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/holiday/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    HOLIDAY_TOTAL\r\n

Response Format
    
    
    HOLIDAY_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the number of holiday configurations in the trading platform.



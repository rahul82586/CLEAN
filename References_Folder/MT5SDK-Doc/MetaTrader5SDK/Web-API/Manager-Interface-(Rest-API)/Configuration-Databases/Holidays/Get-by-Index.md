[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / Get by Index

[Previous](Get-Total.md) | [Next](../Managers.md)

# Get Holiday by Index

The request allows receiving a holiday configuration by an index in the list.

## Rest API

Request Format
    
    
    GET /api/holiday/next?index=index
    POST /api/holiday/next?index=index

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/holiday/next?index=0
    {
      "retcode" : "0 Done",
      "answer" : {
        "Mode" : "1",
        "Year" : "2010",
        "Month" : "1",
        "Day" : "1",
        "From" : "754",
        "To" : "825",
        "Description" : "Holiday",
        "Symbols" : [
          {
           "Path" : "*"
          }
        ]
      }
    }
    }

## Raw API

Request Format
    
    
    HOLIDAY_NEXT|INDEX=index\r\n

Response Format
    
    
    HOLIDAY_NEXT|RETCODE=code description|\r\n
    The description of a holiday configuration in JSON format

## Request Parameters

  * index — holiday configuration index starting with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent holiday is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — description of the holiday configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



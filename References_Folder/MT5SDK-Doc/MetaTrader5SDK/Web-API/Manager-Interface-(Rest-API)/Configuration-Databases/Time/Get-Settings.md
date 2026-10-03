[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Get Settings

[Previous](Get-Server.md) | [Next](Update-Settings.md)

# Getting Time Settings

This request is used for receiving the working time settings of the platform.

## Rest API

Request format
    
    
    GET /api/time/get
    POST /api/time/get

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/time/get
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Daylight" : "1",
        "DaylightState" : "0",
        "TimeZone" : "60",
        "TimeServer" : "10.150.180.65",
        "Days" : [
          [Array], [Array],
          [Array], [Array],
          [Array], [Array],
          [Array]
        ]
      }
    }

## Raw API

Request format
    
    
    TIME_GET\r\n

Response format
    
    
    TIME_GET|RETCODE=code description|\r\n
    The body of the time configuration in JSON format

Example
    
    
    //--- request to the server
    001600010TIME_GET|
    //--- server response
    TIME_GET|RETCODE=0 Done|
    {
    "Daylight" : "1",
    "TimeZone" : "60",
    "TimeServer" : "clock.psu.edu",
    "Days" : [
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
    ]
    }

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — platform working time configuration in JSON format. The description of the passed parameters is given in the ["Data structure"](Data-Structure.md) section.



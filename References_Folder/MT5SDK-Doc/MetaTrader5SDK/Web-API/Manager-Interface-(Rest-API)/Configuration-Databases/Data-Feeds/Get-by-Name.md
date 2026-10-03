[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](Get-Total-Modules.md)

# Get Data Feed by Name

This request allows receiving a data feed configuration by its name.

## Rest API

Request Format
    
    
    GET /api/feeder/get?name=name
    POST /api/feeder/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/feeder/get?name=MetaTrader%205%20MetaQuotes
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Feeder" : "MetaTrader 5 MetaQuotes",
        "Module" : "MetaTrader5Feeder64.exe",
        "GatewayServer" : "127.0.0.1:16391",
        "GatewayLogin" : "4",
        "GatewayPassword" : "password",
        "FeedServer" : "access.metatrader5.com:443",
        "FeedLogin" : "1000",
        "FeedPassword" : "password",
        "Enable" : "1",
        "Mode" : "3",
        "TimeoutReconnect" : "1",
        "TimeoutSleep" : "60",
        "AttemptsSleep" : "5",
        "State" : {
          "SysConnection" : "1",
          "SysLastTime" : "1586353138",
          "Company" : "MetaQuotes Ltd.",
          ...
        },
        "Params" : [
          {
            "Type" : "0",
            "Name" : "CalendarHolidays",
            "Value" : ""
         ]
       }
    }

## Raw API

Request Format
    
    
    FEEDER_GET|NAME=name|\r\n

Response Format
    
    
    FEEDER_GET|RETCODE=code description|\r\n
    The description of the configuration in JSON format

## Request Parameters

  * name — data feed configuration name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the data feed configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



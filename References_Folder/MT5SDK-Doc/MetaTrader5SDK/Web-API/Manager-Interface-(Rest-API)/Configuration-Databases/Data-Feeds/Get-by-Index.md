[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Get Data Feed by Index

Get the configuration of one or more data feeds by index in the list.

## Rest API

Request Format
    
    
    GET /api/feeder/next?index=index&count=number
    POST /api/feeder/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/feeder/next?index=0
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
    
    
    FEEDER_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    FEEDER_NEXT|RETCODE=code description|\r\n
    The description of the configuration in JSON format

## Request Parameters

  * index — data feed configuration index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent data feed is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — description of the data feed configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](../Gateways/Data-Structure.md) section.



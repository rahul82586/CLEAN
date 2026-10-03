[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Get Gateway by Index

Get the configuration of one or more gateways by index in the list.

## Rest API

Request Format
    
    
    GET /api/gateway/next?index=index&count=number
    POST /api/gateway/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/gateway/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "MetaTrader 5 Gateway",
        "Module" : "MetaTrader5Gateway64.exe",
        "GatewayServer" : "127.0.0.1:16389",
        "GatewayLogin" : "6",
        "GatewayPassword" : "password",
        "TradingServer" : "access.metatrader5.com:443",
        "TradingLogin" : "1000",
        "TradingPassword" : "password",
        "Enable" : "0",
        "Flags" : "2",
        "ID" : "6",
        "Gateway" : "MT5GWTMT5",
        "AccountSummary" : "0",
        "TimeoutReconnect" : "1",
        "TimeoutSleep" : "60",
        "AttemptsSleep" : "5",
        ...
      }
    }

## Raw API

Request Format
    
    
    GATEWAY_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    GATEWAY_NEXT|RETCODE=code description|\r\n
    The description of the gateway configuration in JSON format

## Request Parameters

  * index — gateway configuration index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent gateway is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — description of the gateway configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



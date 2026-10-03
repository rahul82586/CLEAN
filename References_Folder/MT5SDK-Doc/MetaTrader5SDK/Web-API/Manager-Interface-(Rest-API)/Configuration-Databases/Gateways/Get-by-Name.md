[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](Get-Total-Modules.md)

# Get Gateway by Name

This request allows receiving a gateway configuration by its name.

## Rest API

Request Format
    
    
    GET /api/gateway/get?name=name
    POST /api/gateway/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/gateway/get?name=MetaTrader%205%20Gateway
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
    
    
    GATEWAY_GET|NAME=name|\r\n

Response Format
    
    
    GATEWAY_GET|RETCODE=code description|\r\n
    The description of the gateway configuration in JSON format

## Request Parameters

  * name — gateway configuration name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the gateway configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



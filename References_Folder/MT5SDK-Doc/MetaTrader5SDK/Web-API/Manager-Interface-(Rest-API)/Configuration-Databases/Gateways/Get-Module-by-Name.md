[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / Get Module by Name

[Previous](Get-Module-by-Index.md) | [Next](Get-Positions.md)

# Get Gateway Module by Name

This request allows receiving a gateway module description by its name.

## Rest API

Request Format
    
    
    GET /api/gateway/module/get?name=name
    POST /api/gateway/module/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/gateway/module/get?name=MetaTrader5Gateway64.exe
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "MetaTrader 5 Gateway",
        "Module" : "MetaTrader5Gateway64.exe",
        "Gateway" : "MT5GWTMT5",
        "Server" : "access.metatrader5.com:443",
        "Login" : "1000",
        "Password" : "password",
        "Copyright" : "Copyright 2000-2024, MetaQuotes Ltd.",
        "Description" : "This gateway allows connecting to a remote MetaTrader 5 Platform ",
        "Version" : "2374",
        "Flags" : "32",
        "Fields" : "15",
        "VersionApi" : "2361",
        "BuildDate" : "27 Mar 2020",
        "BuildApiDate" : "08 Mar 2020",
        "Params" : [
          {
            "Type" : "0",
            "Name" : "Max Price Deviation",
            "Value" : "50"
          }
        ]
      }
    }
    }

## Raw API

Request Format
    
    
    GATEWAY_MODULE_GET|NAME=name|\r\n

Response Format
    
    
    GATEWAY_MODULE_GET|RETCODE=code description|\r\n
    The description of the gateway module in JSON format

## Request Parameters

  * name — gateway module name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the gateway module in JSON format. The complete description of passed server parameters is available under the ["Data structure" (#module)](Data-Structure.md#module) section.



[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Get

[Previous](Data-Structure.md) | [Next](Set.md)

# Getting Common Configuration

The command allows requesting the common settings of the trading platform.

## Rest API

Request format
    
    
    GET /api/common/get
    POST /api/common/get

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/common/get
    //--- server response
    {
      "retcode" : "0 Done",
      "answer ": {
        "Name" : "Demo",
        "Owner" : "Broker",
        "OwnerID" : "Broker",
        "OwnerHost" : "broker.com",
        "OwnerEmail" : "",
        "Product" : "MetaTrader 5",
        "ExpirationLicense" : "1577750400",
        "ExpirationSupport" : "1577750400",
        "LimitTradeServers" : "5",
        "LimitWebServers" : "5",
    ...
      }
    }

## Raw API

Request format
    
    
    COMMON_GET\r\n

Response format
    
    
    COMMON_GET|RETCODE=code description|\r\n
    Common configuration body in JSON format

Example
    
    
    //--- request to the server
    001a00010COMMON_GET|
    //--- server response
    COMMON_GET|RETCODE=0 Done|
    {
    "Name" : "Demo",\r\n
    "NameFull" : "Broker-Demo",\r\n
    "Owner" : "Broker",\r\n
    "OwnerID" : "BrokerID",\r\n
    "OwnerHost" : "broker.com",\r\n
    "OwnerEmail" : "",\r\n
    "Product" : "MetaTrader 5",\r\n
    "ExpirationLicense" : "2012.01.01",\r\n
    "ExpirationSupport" : "2012.01.01",\r\n
    "LimitTradeServers" : "5",\r\n
    "LimitWebServers" : "5",\r\n
    "LimitAccounts" : "0",\r\n
    "LimitDeals" : "0",\r\n
    "LimitGroups" : "4096",\r\n
    "LiveUpdateMode" : "1"\r\n
    }

## Response parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — platform common configuration in JSON format. The description of the passed parameters is given in the ["Data structure"](Data-Structure.md) section.



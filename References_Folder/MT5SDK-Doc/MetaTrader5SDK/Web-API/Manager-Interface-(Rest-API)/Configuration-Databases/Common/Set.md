[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Set

[Previous](Get.md) | [Next](../Network.md)

# Update Common Configuration

The request allows updating general platform settings.

## Rest API

Request format
    
    
    POST /api/common/set
    Common configuration in JSON format

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/common/set
    {
        "Name" : "Demo",
        "LiveUpdateMode" : "1",
        "AccountUrl" : "Broker",
        "AccountDepositUrl" : "broker.com",
        "AccountWithdrawalUrl" : "",
        "AccountAuto" : "0",
    ...
      }
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
    
    
    COMMON_SET\r\n
    Common configuration body in JSON format

Response format
    
    
    COMMON_SET|RETCODE=code description|\r\n
    Common configuration body in JSON format

## Request Parameters

The request has no parameters. Common configuration description is passed in JSON format as an additional body. Only the following parameters can be changed:

  * Name
  * LiveUpdateMode
  * AccountUrl
  * AccountDepositUrl
  * AccountWithdrawalUrl
  * AccountAuto
  * AccountGroup



The complete description of server parameters is available under the ["Data structure"](../Network/Data-Structure.md) section.

The JSON description of the configuration passed during the update is the same as the description returned by the server.

## Response Parameters

  * retcode — if successful, the [response code](../../../../Return-Codes/Successful-completion.md) 0 is returned. Otherwise, an error code is returned.
  * answer — common platform configuration after the update, in JSON format. Description of passed parameters is provided under the ["Data structure"](Data-Structure.md) section.



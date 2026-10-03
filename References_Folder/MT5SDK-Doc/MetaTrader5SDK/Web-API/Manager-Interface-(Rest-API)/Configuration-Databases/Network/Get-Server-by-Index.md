[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Get Server by Index

[Previous](Get-Number-of-Servers.md) | [Next](Get-Server-by-Identifier.md)

# Get Server by Index

Get the configuration of one or more servers by index in the list.

## Rest API

Request format
    
    
    GET /api/server/next?index=index&count=number
    POST /api/server/next?index=index&count=number

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/server/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Type" : "0",
        "Name" : "Trade Main",
        "Address" : "10.14.33.98:441",
        "Login" : "1",
        "Adapter" : "Microsoft Hyper-V Network Adapter",
        "ServiceTime" : "227",
        "Adapters" : ["Microsoft Hyper-V Network Adapter"],
        "Addresses" : ["625973325"],
        "Binds" : [
          {
           "Address" : "10.14.33.98:441"
          }
          ],
        "Points" : [
          {
           "Address" : "10.14.33.98:441"
          }
          ],
        "TradeServer" : {
          "DemoMode" : "1",
          "DemoPeriod" : "999",
    ...
    }

## Raw API

Request format
    
    
    SERVER_NEXT|INDEX=index|COUNT=number\r\n

Response format
    
    
    SERVER_NEXT|RETCODE=code description|\r\n
    Server configuration body in JSON format

## Request Parameters

  * index — server configuration index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent group is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — server configuration in the JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



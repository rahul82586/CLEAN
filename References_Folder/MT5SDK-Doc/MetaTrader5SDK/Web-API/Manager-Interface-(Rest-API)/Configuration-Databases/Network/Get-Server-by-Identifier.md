[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Get Server by Identifier

[Previous](Get-Server-by-Index.md) | [Next](Restart-Server.md)

# Get Server by Identifier

The request allows receiving server configurations by a list of IDs or indexes in a list.

## Rest API

Request format
    
    
    GET /api/server/get?index=indexes
    GET /api/server/get?id=identifiers
     
    POST /api/server/get?index=indexes
    POST /api/server/get?id=identifiers

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/server/get?id=1
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
    
    
    SERVER_NEXT|INDEX=index\r\n

Response format
    
    
    SERVER_NEXT|RETCODE=code description|\r\n
    Server configuration body in JSON format

## Request Parameters

  * id — the identifier of the server to be received. Multiple IDs can be specified as separated by commas.
  * index — server configuration index starting with 0. Multiple IDs can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent group is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — server configuration in the JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



## Note

Only one of the parameters can be specified in a request, i.e. id or index. Indication of two lists simultaneously is not allowed.

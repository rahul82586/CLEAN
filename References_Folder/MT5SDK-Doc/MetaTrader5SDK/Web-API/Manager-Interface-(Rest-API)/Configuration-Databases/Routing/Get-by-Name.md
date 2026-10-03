[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](../History-Synchronization.md)

# Get Routing Rule by Name

The request allows receiving a routing rule by its name.

## Rest API

Request Format
    
    
    GET /api/route/get?name=name
    POST /api/route/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/route/get?name=Send%20to%20gateway
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "Send to gateway",
        "Mode" : "1",
        "Request" : "33554431",
        "Type" : "255",
        "Flags" : "0",
        "Action" : "1001",
        "ActionValueInt" : "0",
        "ActionValueUInt" : "0",
        "ActionValueFloat" : "0.00",
        "ActionValueString" : "",
        "Conditions" : [
          {
           "Condition" : "1000",
           "Rule" : "3",
           "ValueInt" : "0",
           "ValueUInt" : "1815998",
           "ValueFloat" : "0.00",
           "ValueString" : ""
         }
      ]
      "Dealers" : [
        {
         "Login" : "227",
         "Name" : "MetaTrader 5 Gateway"
        }
      ]
      }
    }

## Raw API

Request Format
    
    
    ROUTE_GET|LOGIN=login|\r\n

Response Format
    
    
    ROUTE_GET|RETCODE=code description|\r\n
    The description of a routing rule in JSON format

## Request Parameters

  * name — the name of the routing rule.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — the description of the routing rule in JSON format. The complete description of passed rule parameters is available under the ["Data structure"](Data-Structure.md) section.



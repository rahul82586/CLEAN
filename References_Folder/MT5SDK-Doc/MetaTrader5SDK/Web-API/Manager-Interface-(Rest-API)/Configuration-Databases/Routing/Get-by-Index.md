[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Get Routing Rule by Index

Get one or more routing rules by index in the list.

## Rest API

Request Format
    
    
    GET /api/route/next?index=index&count=number
    POST /api/route/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/route/next?index=0
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
    
    
    ROUTE_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    ROUTE_NEXT|RETCODE=code description|\r\n
    The description of a routing rule in JSON format

## Request Parameters

  * index — the routing rule index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent rule is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — the description of the routing rule in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



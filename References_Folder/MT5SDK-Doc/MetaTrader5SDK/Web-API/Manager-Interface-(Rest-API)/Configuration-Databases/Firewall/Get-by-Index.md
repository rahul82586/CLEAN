[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Get by Index

[Previous](Get-Total.md) | [Next](../Holidays.md)

# Get Firewall Rule by Index

Get one or more firewall rules by index in the list.

## Rest API

Request Format
    
    
    GET /api/firewall/next?index=index&count=number
    POST /api/firewall/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/firewall/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "IPFrom" : "192.168.0.1",
        "IPTo" : "192.168.0.255",
        "Action" : "2",
        "Comment" : "Local network"
      }
    }

## Raw API

Request Format
    
    
    FIREWALL_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    FIREWALL_NEXT|RETCODE=code description|\r\n
    The description of a firewall rule in JSON format

## Request Parameters

  * index — the firewall rule index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent rule is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — the description of the firewall rule in the JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Login.md)

# Get Manager by Index

Get one or more manager configurations by index in the list.

## Rest API

Request Format
    
    
    GET /api/manager/next?index=index&count=number
    POST /api/manager/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/manager/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Login" : "1200",
        "Name" : "John Smith",
        "Mailbox" : "Administrator",
        "Server" : "1",
        "Rights" : ["1", "1", "1", ...],
        "RequestLimitLogs" : "0",
        "RequestLimitReports" : "0",
        "Groups" : [
          {
           "Group" : "*"
          }
        ],
        "Access" : [],
      }
    }

## Raw API

Request Format
    
    
    MANAGER_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    MANAGER_NEXT|RETCODE=code description|\r\n
    The description of a manager configuration in JSON format

## Request Parameters

  * index — manager configuration index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent manager is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — manager configuration description in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



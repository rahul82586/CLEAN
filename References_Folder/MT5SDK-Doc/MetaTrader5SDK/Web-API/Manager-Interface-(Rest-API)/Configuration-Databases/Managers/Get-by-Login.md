[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / Get by Login

[Previous](Get-by-Index.md) | [Next](../Routing.md)

# Get Manager by Login

The request allows receiving manager configuration by login.

## Rest API

Request Format
    
    
    GET /api/manager/get?login=login
    POST /api/manager/get?login=login

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/manager/get?login=1020
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
    
    
    MANAGER_GET|LOGIN=login|\r\n

Response Format
    
    
    MANAGER_GET|RETCODE=code description|\r\n
    The description of a manager configuration in JSON format

## Request Parameters

  * login — manager login.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — manager configuration in JSON format. The complete description of passed parameters is available under the ["Data structure"](Data-Structure.md) section.



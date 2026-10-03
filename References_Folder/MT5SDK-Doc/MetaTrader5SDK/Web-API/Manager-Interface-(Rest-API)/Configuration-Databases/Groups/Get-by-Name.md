[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](../Symbols.md)

# Getting a Group by Name

This request is used for receiving configuration of a group by its name.

## Rest API

Request format
    
    
    GET /api/group/get?group=name
    POST /api/group/get?group=name

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/group/get?group=demo\\forex
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Group" : "demo\\forex",
        "Server" : "0",
        "PermissionsFlags" : "2",
        "AuthMode" : "0",
    ...
    }

## Raw API

Request format
    
    
    GROUP_GET|GROUP=name|\r\n

Response format
    
    
    GROUP_GET|RETCODE=code description|\r\n
    The body of the group configuration in JSON format

Example
    
    
    //--- request to the server
    005400010GROUP_GET|GROUP=managers\\administrators|
    //--- server response
    GROUP_GET|RETCODE=0 Done|
    {
    "Group" : "demo\\forex",
    "Server" : "0",
    "PermissionsFlags" : "2",
    "AuthMode" : "0",
    "AuthPasswordMin" : "5",
    ...
    }

## Request Parameters

  * group — group name.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — group configuration is passed in JSON format. A complete description of the passed parameters of groups is given in the ["Data structure" (#group)](Data-Structure.md#group) section.



[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Getting a Group by Index

Get the configuration of one or more groups by index in the list.

## Rest API

Request format
    
    
    GET /api/group/next?index=index&count=number
    POST /api/group/next?index=index&count=number

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/group/next?index=0
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
    
    
    GROUP_NEXT|INDEX=index|COUNT=number\r\n

Response format
    
    
    GROUP_NEXT|RETCODE=code description|\r\n
    The body of the group configuration in JSON format

Example
    
    
    //--- request to the server
    002a00010GROUP_NEXT|INDEX=0|
    //--- server response
    GROUP_NEXT|RETCODE=0 Done|
    {
    "Group" : "demo\\forex",
    "Server" : "0",
    "PermissionsFlags" : "2",
    "AuthMode" : "0",
    ...
    }

## Request Parameters

  * index — the index of the group starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code will be returned. If an index of a nonexistent group is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — group configuration is passed in JSON format. A complete description of the passed parameters of groups is given in the ["Data structure" (#group)](Data-Structure.md#group) section.



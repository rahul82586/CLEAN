[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Delete

[Previous](Add-Multiple.md) | [Next](Delete-Multiple.md)

# Deleting a Group

Using this request you can delete a group with the specified name.

## Rest API

Request format
    
    
    GET /api/group/delete?group=name
    POST /api/group/delete?group=name

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/group/delete?group=demoforex
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    GROUP_DELETE|GROUP=name\r\n

Response format
    
    
    GROUP_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * group — the name of the group to delete (including the path).



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.



## Notes

  * This command works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the command, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and edit group configurations. Otherwise, it returns the error code [8](../../../../Return-Codes/Common-errors.md).
  * You cannot delete a group which contains at least one account. At an attempt to delete, the error code [2003](../../../../Return-Codes/Configuration-Management.md) is returned.
  * You cannot delete the last manager group on a server. At an attempt to delete, the error code [2001](../../../../Return-Codes/Configuration-Management.md) is returned.



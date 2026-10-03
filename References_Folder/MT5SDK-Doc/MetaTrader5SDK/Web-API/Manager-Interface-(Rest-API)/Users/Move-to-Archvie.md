[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Move to Archvie

[Previous](Check-Balance.md) | [Next](Get-from-Archive.md)

# Move User to Archive

The request allows moving a user to archive.

## Rest API

Request format
    
    
    GET /api/user/archive/add?login=login
    POST /api/user/archive/add?login=login

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/user/archive/add?login=126993
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    USER_ARCHIVE|LOGIN=login|\r\n

Response format
    
    
    USER_ARCHIVE|RETCODE=code description|\r\n

## Request Parameters

  * login — the login of the user to be moved to the archive database.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



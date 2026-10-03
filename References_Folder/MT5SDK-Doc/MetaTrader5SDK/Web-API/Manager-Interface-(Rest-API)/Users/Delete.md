[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Delete

[Previous](Update.md) | [Next](Get-by-Login.md)

# Deleting a User

This request allows to delete a user account with the specified login.

## Rest API

Request format
    
    
    GET /api/user/delete?login=login
    POST /api/user/delete?login=login

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/user/delete?login=73339
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    USER_DELETE|LOGIN=login|\r\n

Response format
    
    
    USER_DELETE|RETCODE=code description|\r\n

Example
    
    
    //--- request to the server
    002c00010USER_DELETE|LOGIN=1023|
    //--- server response
    USER_DELETE|RETCODE=0 Done|

## Request Parameters

  * login — the login of an account which should be deleted.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.



## Notes

  * A user account can be deleted only when connecting to the same trade server where the account is located. If an account with the specified login is not found, code [13](../../../Return-Codes/Common-errors.md) is returned.
  * Accounts that belong to manager and administrator groups cannot be deleted.



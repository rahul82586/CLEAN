[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Check Password

[Previous](Get-Multiple.md) | [Next](Change-Password.md)

# Checking User Password

This request allows to check a user's password.

## Rest API

Request format
    
    
    GET /api/user/check_password?login=login&type=type&password=password
    POST /api/user/check_password
    { 
      "Login" : "login",
      "Type" : "type",
      "Password" : "password",
     }

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    POST /api/user/check_password
    { 
      "Login" : "764636",
      "Type" : "main",
      "Password" : "ps12Rt12"
    }
    //--- server response
    { "retcode" : "3006 Invalid account password" }

## Raw API

Request format
    
    
    USER_PASS_CHECK|LOGIN=login|TYPE=type|PASSWORD=password|\r\n

Response format
    
    
    USER_PASS_CHECK|RETCODE=code description|\r\n

Example
    
    
    //--- request to the server
    008200010USER_PASS_CHECK|LOGIN=0|TYPE=INVESTOR|PASSWORD=invest_password|
    //--- server response
    USER_PASS_CHECK|RETCODE=3006 Invalid account password|

## Request Parameters

• login

• type

• main

• investor

• api

  * Client description can be passed in the command parameters, in an additional body in the JSON format, or both at once. A description passed in an additional body has higher priority.


  * We strongly urge you against passing passwords in the command parameters since request addresses may be logged/cached by intermediary network devices the request passes through on its way from the client to the server. Always send passwords in an additional request body.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code will be returned. For example, code [3006](../../../Return-Codes/User-management.md) indicates that the password is incorrect.



[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Change Password

[Previous](Check-Password.md) | [Next](Get-Trade-State.md)

# Changing the User Password

This request allows to change the password of a client.

## Rest API

Request format
    
    
    GET /api/user/change_password?login=login&type=type&password=password
    POST /api/user/change_password
    { 
      "Login" : "login",
      "Type" : "type",
      "Password" : "password",
     }

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    POST /api/user/change_password
    { 
      "Login" : "764636",
      "Type" : "main",
      "Password" : "ps12Rt12"
    }
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    USER_PASS_CHANGE|LOGIN=login|TYPE=type|PASSWORD=password|\r\n

Response format
    
    
    USER_PASS_CHECK|RETCODE=code description|\r\n

Example
    
    
    //--- request to the server
    008000010USER_PASS_CHANGE|LOGIN=1000|TYPE=MAIN|PASSWORD=new_main_password|
    //--- server response
    USER_PASS_CHANGE|RETCODE=0 Done|

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

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.



## Notes

The main, investor and API passwords must comply with the security requirements: a password must contain at least two of three types of characters (lower case, upper case and digits) and meet the minimum length requirements set for the [group](../Configuration-Databases/Groups.md).

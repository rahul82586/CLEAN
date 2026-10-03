[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get Group

[Previous](Get-Total.md) | [Next](Update-Certificate.md)

# Get User Group by Login

The request allows receiving a user group by the user login.

## Rest API

Request format
    
    
    GET /api/user/group?login=login
    POST /api/user/group?login=login

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Group" : "group" }
    }

Example
    
    
    //--- request to the server
    GET /api/user/group?login=126993
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Group" : "demo\\demoforex" }
    }

## Raw API

Request format
    
    
    USER_GROUP|LOGIN=login|\r\n

Response format
    
    
    USER_GROUP|RETCODE=code description|GROUP=group|\r\n

## Request Parameters

  * login — the login of the user whose group you want to receive.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * group — the name of the group to which the user belongs.



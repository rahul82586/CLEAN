[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get List

[Previous](Get-Multiple-Trade-States.md) | [Next](Get-Total.md)

# Getting the login list

Use this request to receive the list of client accounts in the specified groups.

## Rest API

Request format
    
    
    GET /api/user/logins?group=groups
    POST /api/user/logins?group=groups

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [login array]
    }

Example
    
    
    //--- request to the server
    GET //api/user/logins?group=demoforex,demo\\forex-usd
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
    "104221",
    "104253",
    "104370",
    "104373",
    "104374",
    "104375",
    "104376" ]
    }

## Raw API

Request format
    
    
    USER_LOGINS|GROUP=groups|\r\n

Response format
    
    
    USER_LOGINS|RETCODE=code description|\r\n
    Login array in JSON format

Example
    
    
    //--- request to the server
    003800010USER_LOGINS|GROUP=demoforex|
    //--- server response
    USER_LOGINS|RETCODE=0 Ok|
    {
    ["1000","1001","1002","1003"]
    }

## Request Parameters

  * group — comma separated group names, for which you need to receive the list of accounts. You may use the mask "*" and the negation sign "!" to specify groups. Example:


  * group=demoforex, democfd — get the list of accounts in groups demoforex and democfd.
  * group=demo\*, forexreal — get the list of accounts in groups of the demo subgroup and in the forexreal group.
  * group=demo\*,!forex — get the list of accounts in all groups in the demo subgroup except for demo\forex group.
  * group=demo* — get the list of accounts in all groups whose names (including path) start with demo.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — login list in JSON format.



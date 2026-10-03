[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Bind Account

[Previous](Get-Identifiers.md) | [Next](Unbind-Account.md)

# Bind an Account to a Client

The request allows binding a trading account to a client.

## Rest API

Request Format
    
    
    GET /api/client/user/add?client=identifier&user=account
    POST /api/client/user/add
    {
      [
       {"user": "account number", "client": "client identifier"},
       {"user": "account number", "client": "client identifier"},
        ...
      ]
    }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ response code, response code, ... ]
    }

The example
    
    
    //--- request to the server
    GET /api/client/user/add
    {
      [
        {"user": "3018855", "client": "1032"},
        {"user": "3018856", "client": "1032"}
      ]
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [ 0, 3 ]
    }

## Raw API

Request Format
    
    
    CLIENT_USER_ADD|CLIENT=identifier|USER=account|\r\n
    CLIENT_USER_ADD|\r\n
    {
      [
       {"user": "account number", "client": "client identifier"},
       {"user": "account number", "client": "client identifier"},
        ...
      ]
    }

Response Format
    
    
    CLIENT_USER_ADD|RETCODE=code description|\r\n
    { [ response code, response code, ... ] }

## Request Parameters

  * client — the ID of the client to whom the account should be bound.
  * user — the login of the account which should be bound to the client.



To perform group binding operations, pass account numbers and customer identifiers in the POST request body. Do not indicate parameters in the string, as they have higher priority: if parameters are specified, the request body is ignored.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * The method does not create a trading account. It binds an existing account to a client.
  * When binding, [account data are not copied (#binding)](https://support.metaquotes.net/en/docs/mt5/platform/administration/clients#binding) to the client record.



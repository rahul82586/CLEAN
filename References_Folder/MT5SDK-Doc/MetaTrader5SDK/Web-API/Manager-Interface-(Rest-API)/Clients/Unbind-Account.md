[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Unbind Account

[Previous](Bind-Account.md) | [Next](Get-Accounts.md)

# Unbind an Account from a Client

The request allows unbinding a trading account from a client.

## Rest API

Request Format
    
    
    GET /api/client/user/delete?client=identifier&user=account
    POST /api/client/user/delete
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
    GET /api/client/user/delete
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
    
    
    CLIENT_USER_DELETE|CLIENT=identifier|USER=account|\r\n
    CLIENT_USER_DELETE|\r\n
    {
      [
       {"user": "account number", "client": "client identifier"},
       {"user": "account number", "client": "client identifier"},
        ...
      ]
    }

Response Format
    
    
    CLIENT_USER_DELETE|RETCODE=code description|\r\n
    { [ response code, response code, ... ] }

## Request Parameters

  * client — the ID of the client from whom the account should be unbound.
  * user — the login of the account which should be unbound from the client.



To perform group unbinding operations, pass account numbers and customer identifiers in the POST request body. Do not indicate parameters in the string, as they have higher priority: if parameters are specified, the request body is ignored.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of response codes related to the unbinding of each of the specified accounts.



## Note

The request does not delete the trading account. It unbinds the account from the client.

[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get Trade State

[Previous](Change-Password.md) | [Next](Get-Multiple-Trade-States.md)

# Getting User Trading Status

This request allows to get the total number of open positions of a client.

## Rest API

Request format
    
    
    GET /api/user/account/get?login=login
    POST /api/user/account/get?login=login

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/user/account/get?login=764636
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Login" : "764636",
        "CurrencyDigits" : "2",
        "Balance"": "26000.00",
        "Credit"": "0.00",
        "Margin" : "11.73",
        "MarginFree" : "25981.83",
        "MarginLevel"": "221598.98",
        "MarginLeverage" : "10",
        "Profit" : "-6.44",
    ...
      }
    }

## Raw API

Request format
    
    
    USER_ACCOUNT_GET|LOGIN=login|\r\n

Response format
    
    
    USER_ACCOUNT_GET|RETCODE=code description|\r\n
    Trading account body in JSON format

## Request Parameters

  * login — the login of an account for which the trade account state is requested.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — trading account parameters in JSON format. The complete description of the passed account parameters is given in the ["Data structure" (#account)](Data-Structure.md#account) section.



## Notes

The state of a trade account can be received only in case it has open orders or positions or a trade activity has been detected at the account after the last server restart.

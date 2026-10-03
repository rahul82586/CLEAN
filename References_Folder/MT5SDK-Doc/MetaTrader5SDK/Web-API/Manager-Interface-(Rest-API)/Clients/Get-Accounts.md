[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Get Accounts

[Previous](Unbind-Account.md) | [Next](Add-Document.md)

# Get the List of a Client's Accounts

The request allows receiving a list of accounts bound to a client record.

## Rest API

Request Format
    
    
    GET /api/client/user/get_logins?client=identifiers
    POST /api/client/user/get_logins?client=identifiers

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : {
        "identifier" : [ list of accounts ], 
        "identifier" : [ list of accounts ],
        ... 
      }
    }

The example
    
    
    //--- request to the server
    GET /api/client/user/get_logins?client=1032,1033
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "1032" : [ 18969, 18970, 18971, 18972 ],
        "1033" : [ 25976, 25977, 25978 ]
      }
    }

## Raw API

Request Format
    
    
    CLIENT_USER_LOGINS|CLIENT=identifiers|\r\n

Response Format
    
    
    CLIENT_USER_LOGINGS|RETCODE=code description|\r\n
    List of a client's account

## Request Parameters

  * client — the identifier of the client whose accounts you wish to obtain. Multiple tickets can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — the list of account for each client specified in the report.



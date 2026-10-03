[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Check Balance

[Previous](Sync-with-External-System.md) | [Next](Move-to-Archvie.md)

# Check User Balance

This request allows you to check and, if necessary, adjust user balance and credit funds.

## Rest API

Request format
    
    
    GET /api/user/check_balance?login=login&fixflag=flag
    POST /api/user/check_balance?login=login&fixflag=flag

Response format
    
    
    {
     "retcode" : "code description",
      "answer" : {
       "Balance": { "User" : "New value", "History" : "Old value" },
       "Credit": { "User" : "New value", "History" : "Old value" }
    }

Example
    
    
    //--- request to the server
    GET /api/user/check_balance?login=611129&fixflag=1
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Balance": { "User" : "3000.000000", "History" : "2495.000000" },
        "Credit": { "User" : "100.000000", "History" : "96.000000" }
    }

## Raw API

Request format
    
    
    USER_BALANCE_CHECK|LOGIN=login|FIXFLAG=flag|\r\n

Response format
    
    
    USER_BALANCE_CHECK|RETCODE=code description|\r\n
    {
       "Balance": { "User" : "New value", "History" : "Old value" },
       "Credit": { "User" : "New value", "History" : "Old value" }
    }

## Request Parameters

  * login — the login of the user whose balance you want to check.
  * fixflag — the flag of the need to correct a client's balance and credit funds after the check. If fixflag is equal to 1, the client's balance and credit funds are adjusted in accordance with the history of [deals](../../../Database-Interfaces/Trade/Deals.md). If the flag is 0, no correction will be made.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * balance — [user balance](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Balance.md) after correction (user) and before correction (history).
  * credit — [user's credit funds](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Credit.md) after correction (user) and before correction (history).



## Note

This request checks the user's balance on the basis of the history of his or her deals and makes corrections in the client balance if necessary. The credit funds are checked based on the [IMTDeal::Credit (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) type deals.

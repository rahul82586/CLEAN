[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Trade Requests](../Trade-Requests.md) / DepositWithdrawal

[Previous](Data-Structure.md) | [Next](Calculate-Conversion-Rate-for-Buy.md)

# Deposit/Withdrawal

This request allows to conduct balance operations on client accounts.

## Rest API

Request format
    
    
    GET /api/trade/balance?login=login&type=type&balance=sum&comment=comment
    POST /api/trade/balance?login=login&type=type&balance=sum&comment=comment

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Ticket" : "ticket" }
    }

Example
    
    
    //--- request to the server
    GET /api/trade/balance?login=764636&type=2&balance=1000&comment=onlinedeposit
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Ticket" : "136623" }
    }

## Raw API

Request format
    
    
    TRADE_BALANCE|LOGIN=xxxx|TYPE=y|BALANCE=zzzz|COMMENT=aaaa|CHECK_MARGIN=1\r\n

Response format
    
    
    TRADE_BALANCE|RETCODE=xxxx yyyy|TICKET=xxxx|\r\n

Example
    
    
    //--- request to the server
    007800010TRADE_BALANCE|LOGIN=1020|TYPE=3|BALANCE=1000|COMMENT=credit|
    //--- server response
    TRADE_BALANCE|RETCODE=0 Done|TICKET=1000|

## Request Parameters

  * login — the login of an account for which a balance operation should be conducted.
  * type — type of the balance operation. Specified as a value of the [EnDealAction (#endealaction)](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) enumeration:


  * 2 — a balance operation.
  * 3 — a credit operation.
  * 4 — additional adding/withdrawing.
  * 5 — corrective operations.
  * 6 — adding bonuses.
  * balance — the amount to change the balance. To add money, set a positive value. To withdraw money, set a negative value.
  * comment — a comment to a balance operation. The maximum comment length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut 
  * check_margin — if the value of this parameter is 1, the free margin is checked before conducting the balance operation. If the amount withdraw is greater than the free margin value, error 10019 is returned. If the parameter is set to zero, the margin is not checked and the requested amount will be withdrawn even if it's greater then the free margin. If the parameter is not passed, the check is considered enabled.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * ticket — ticket of a [deal](../Deals.md) the balance operation has been performed by.



## Notes

  * Balance operations are conducted as [deals](../Deals.md).
  * In case the deal type is incorrect, the code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * An amount of money accrued/withdrawn with a single operation cannot exceed 1000000000. In case this value is exceeded, the code [4005](../../../../Return-Codes/Trade-management.md) will be returned.
  * An amount of withdrawal cannot exceed the current free margin. In case this amount is exceeded the code [10019](../../../../Return-Codes/Trade-Requests.md) is returned.
  * An amount of withdrawal during a credit operation (TYPE=3) cannot exceed the amount of previously issued credit assets. In case this amount is exceeded the code [10019](../../../../Return-Codes/Trade-Requests.md) is returned.
  * An amount of withdrawal during any balance operation cannot exceed the current balance. In case this amount is exceeded the code [10019](../../../../Return-Codes/Trade-Requests.md) is returned.



[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Trade](../Trade.md) / Balance

[Previous](UserDepositChange.md) | [Next](../Mailbox.md)

# MT5WebAPI.TradeBalance

Conduct balance operations on an account without getting the balance deal ticket.
    
    
    MTRetCode  MT5WebAPI.TradeBalance(
       ulong                login,       // Login
       MTDeal.EnDealAction  type         // Type of operation
       double               balance,     // Amount
       string               comment,     // Comment
       )

### Parameters

**login**  
[in] The login of a client.

**type**  
[in] Type of the balance operation. Passed using the following values of theMTDeal.EnDealActionenumeration:

**balance**  
[in] The amount to add to an account or subtract from it (negative value).

**comment**  
[in] A comment to a balance operation.

  * DEAL_BALANCE — a balance operation.
  * DEAL_CREDIT — a credit operation.
  * DEAL_CHARGE — additional adding/withdrawing.
  * DEAL_CORRECTION — corrective operations.
  * DEAL_BONUS — adding bonuses.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# MT5WebAPI.TradeBalance

Conduct balance operations on an account with getting the balance deal ticket.
    
    
    MTRetCode  MT5WebAPI.TradeBalance(
       ulong                login,       // Login
       MTDeal.EnDealAction  type         // Type of operation
       double               balance,     // Amount
       string               comment,     // Comment
       ulong                ticket,      // Ticket
       )

### Parameters

**login**  
[in] The login of a client.

**type**  
[in] Type of the balance operation. Passed using the following values of theMTDeal.EnDealActionenumeration:

**balance**  
[in] The amount to add to an account or subtract from it (negative value).

**comment**  
[in] A comment to a balance operation.

**ticket**  
[out] Ticket of the balance deal.

  * DEAL_BALANCE — a balance operation.
  * DEAL_CREDIT — a credit operation.
  * DEAL_CHARGE — additional adding/withdrawing.
  * DEAL_CORRECTION — corrective operations.
  * DEAL_BONUS — adding bonuses.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# MT5WebAPI.TradeBalance

Conduct balance operations on an account with getting the balance deal ticket and checking free margin.
    
    
    MTRetCode  MT5WebAPI.TradeBalance(
       ulong                login,        // Login
       MTDeal.EnDealAction  type          // Type of operation
       double               balance,      // Amount
       string               comment,      // Comment
       bool                 checkMargin,  // Margin check
       ulong                ticket,       // Ticket
       )

### Parameters

**login**  
[in] The login of a client.

**type**  
[in] Type of the balance operation. Passed using the following values of theMTDeal.EnDealActionenumeration:

**balance**  
[in] The amount to add to an account or subtract from it (negative value).

**comment**  
[in] A comment to a balance operation.

**check_margin**  
[in] If the value of this parameter is true, the free margin is checked before conducting the balance operation. If the amount withdraw is greater than the free margin value, errorMT_RET_REQUEST_NO_MONEYis returned. If the parameter is set to false, the margin is not checked and the requested amount will be withdrawn even if it's greater then the free margin. If the parameter is not passed, the check is considered enabled.

**ticket**  
[out] Ticket of the balance deal.

  * DEAL_BALANCE — a balance operation.
  * DEAL_CREDIT — a credit operation.
  * DEAL_CHARGE — additional adding/withdrawing.
  * DEAL_CORRECTION — corrective operations.
  * DEAL_BONUS — adding bonuses.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Notes

  * Balance operations are conducted as [deals](../Deals.md).
  * In case the deal type is incorrect, the code [MT_RET_ERR_PARAMS](../../../../../Return-Codes/Common-errors.md) is returned.
  * An amount of money accrued/withdrawn with a single operation cannot exceed 1000000000. In case this value is exceeded, the code [MT_RET_TRADE_MAX_MONEY](../../../../../Return-Codes/Trade-management.md) is returned.
  * An amount of withdrawal cannot exceed the current free margin. In case this amount is exceeded the code [MT_RET_REQUEST_NO_MONEY](../../../../../Return-Codes/Trade-Requests.md) is returned.
  * An amount of withdrawal during a credit operation (TYPE=DEAL_CREDIT) cannot exceed the amount of previously issued credit assets. In case this amount is exceeded the code [MT_RET_REQUEST_NO_MONEY](../../../../../Return-Codes/Trade-Requests.md) is returned.
  * An amount of withdrawal during any balance operation cannot exceed the current balance. In case this amount is exceeded the code [MT_RET_REQUEST_NO_MONEY](../../../../../Return-Codes/Trade-Requests.md) is returned.



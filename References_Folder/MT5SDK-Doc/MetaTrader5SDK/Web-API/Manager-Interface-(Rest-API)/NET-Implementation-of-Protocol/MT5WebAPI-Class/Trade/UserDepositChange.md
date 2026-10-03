[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Trade](../Trade.md) / UserDepositChange

[Previous](../Trade.md) | [Next](Balance.md)

# MT5WebAPI.UserDepositChange

Conduct balance operations on an account.
    
    
    MTRetCode  MT5WebAPI.UserDepositChange(
       ulong                login,       // Login
       double               newDeposit,  // Amount
       string               comment,     // Comment
       MTDeal.EnDealAction  type         // Type of operation
       )

### Parameters

**login**  
[in] The login of a client.

**newDeposit**  
[in] The amount to add to an account or subtract from it (negative value).

**comment**  
[in] A comment to a balance operation.

**type**  
[in] Type of the balance operation. Passed using the following values of theMTDeal.EnDealActionenumeration:

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



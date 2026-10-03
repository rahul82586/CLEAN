[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / Credit

[Previous](Balance.md) | [Next](Margin.md)

# IMTAccount::Credit

Get the current amount of credit given to an account.

C++
    
    
    double  IMTAccount::Credit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.Credit()

### Return Value

The current amount of credit given to an account.

### Note

Client's credit funds are the total sum of all operations of the "Credit" ([EnDealAction::DEAL_CREDIT (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction)) and "Bonus" ([EnDealAction::DEAL_BONUS (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction)).

# IMTAccount::Credit

Set the current amount of credit given to an account.

C++
    
    
    MTAPIRES  IMTAccount::Credit(
       const double  credit      // Amount of credit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.Credit(
       double        credit      // Amount of credit
       )

### Parameters

**credit**  
[in] The amount of money credited to the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Client's credit funds are the total sum of all operations of the "Credit" ([EnDealAction::DEAL_CREDIT (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction)) and "Bonus" ([EnDealAction::DEAL_BONUS (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction)).

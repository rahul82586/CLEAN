[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserBalanceCheck

[Previous](UserExternalSync.md) | [Next](UserBalanceCheckBatch.md)

# IMTManagerAPI::UserBalanceCheck

Check and correct the client's balance and credit funds.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserBalanceCheck(
       const UINT64  login,               // Login
       const UINT    fixflag,             // Balance correction flags
       double&       balance_user,        // Balance at the moment of checking
       double&       balance_history      // Balance based on the deals history
       double&       credit_user,         // Credit funds at the moment of checking
       double&       credit_history       // Credit funds based on the deals history
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserBalanceCheck(
       ulong         login,               // Login
       bool          fixflag,             // Balance correction flags
       out double    balance_user,        // Balance at the moment of checking
       out double    balance_history      // Balance based on the deals history
       out double    credit_user,         // Credit funds at the moment of checking
       out double    credit_history       // Credit funds based on the deals history
       )

Python
    
    
    ManagerAPI.UserBalanceCheck(
       login,        # Login
       fixflag       # Balance correction flags
       )

### Parameters

**login**  
[in] The login of the client whose balance and credit funds should be checked.

**fixflag**  
[in] Flag of the need to correct a client's balance and credit funds after the check. If fixflag is equal to 1, the client's balance and credit funds are adjusted in accordance with the history ofdeals. If the flag is 0, no correction will be made.

**balance_user**  
[out] The value of theclient's balancestored in the client record at the time of check.

**balance_history**  
[out] The value of the client's balance calculated by analyzing the history of deals.

**credit_user**  
[out] Theclient's credit funds, stored in the client record at the moment of checking.

**credit_history**  
[out] The client's credit funds calculated by analyzing the history of deals.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

This function checks the client's balance on the basis of the history of his or her deals and makes corrections in the client's balance if necessary. The credit funds are checked based on the [IMTDeal::DEAL_CREDIT (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) deals.

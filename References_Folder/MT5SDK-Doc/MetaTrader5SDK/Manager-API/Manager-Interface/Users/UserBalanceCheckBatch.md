[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserBalanceCheckBatch

[Previous](UserBalanceCheck.md) | [Next](NotificationsSend.md)

# IMTManagerAPI::UserBalanceCheckBatch

Check and adjust balance and credit funds for multiple clients.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserBalanceCheckBatch(
       const UINT64*  logins,             // list of logins
       const UINT     logins_total,       // number of logins
       const UINT     fixflag,            // balance adjustment flag
       MTAPIRES*      results,            // array of check results
       double*        balance_user,       // array with balances as of the check time
       double*        balance_history     // array with balances from the history of deals
       double*        credit_user,        // array with credit funds as of the check time
       double*        credit_history      // array with credit funds from the history of deals
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserBalanceCheckBatch(
       ulong[]        logins,             // list of logins
       bool           fixflag,            // balance adjustment flag
       MTRetCode[]    res,                // array of check results
       out double[]   balance_user,       // array with balances as of the check time
       out double[]   balance_history     // array with balances from the history of deals
       out double[]   credit_user,        // array with credit funds as of the check time
       out double[]   credit_history      // array with credit funds from the history of deals
       )

Python
    
    
    ManagerAPI.UserBalanceCheckBatch(
       logins,        # list of logins
       fixflag        # balance adjustment flag
       )

### Parameters

**logins**  
[in] The array of client logins for which you want to check balances.

**logins_total**  
[in] Number of logins in the 'logins' array.

**fixflag**  
[in] Flag indicating the need to adjust the client's balance and credit funds after the check. If fixflag is equal to 1, the client's balance and credit funds are adjusted in accordance with the history ofdeals. If the flag is 0, no correction will be made.

**results**  
[out] Array with balance check results. The size of the 'results' array must not be less than that of 'logins'.

**balance_user**  
[out] Array withbalancevalues existing on the accounts at the check time. The index of the value corresponds to the index of the account in the source array.

**balance_history**  
[out] Array with balance values calculated based on the history of deals on the accounts. The index of the value corresponds to the index of the account in the source array.

**credit_user**  
[out] Array withcreditvalues existing on the accounts at the check time. The index of the value corresponds to the index of the account in the source array.

**credit_history**  
[out] Array with credit values calculated based on the history of deals on the accounts. The index of the value corresponds to the index of the account in the source array. The credit funds are checked based on the deals with theIMTDeal::DEAL_CREDITtype.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all of the specified accounts have been checked. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) code indicates that only some of the accounts have been checked.

### Note

The method checks the clients' balances based on their trading history and adjust the balances if necessary.

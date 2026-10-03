[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeAccount

[Previous](FeePeriod.md) | [Next](FeeManagementType.md)

# IMTConFund::FeeAccount

Get the account to which the fund management and success fees are charged.

C++
    
    
    UINT  IMTConFund::FeeAccount()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeeAccount()

### Return Value

The account ([IMTUser::Login](../../../Database-Interfaces/Users/IMTUser/Login.md)), to which the fund management and success fees are charged.

# IMTConFund::FeeAccount

Set the account to which the fund management and success fees are charged.

C++
    
    
    MTAPIRES  IMTConFund::FeeAccount(
       const UINT  fee_account    // Account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeAccount(
       uint        fee_account    // Account
       )

### Parameters

**fee_account**  
[in] The account (IMTUser::Login), to which the fund management and success fees are charged.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

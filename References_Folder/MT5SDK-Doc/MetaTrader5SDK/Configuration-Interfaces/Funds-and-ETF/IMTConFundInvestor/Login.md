[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundInvestor](../IMTConFundInvestor.md) / Login

[Previous](Clear.md) | [Next](Name.md)

# IMTConFundInvestor::Login

Get the login of the account used by the fund investor.

C++
    
    
    UINT64  IMTConFundInvestor::Login()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFundInvestor.Login()

### Return Value

Fund investor's account login ([IMTUser::Login](../../../Database-Interfaces/Users/IMTUser/Login.md)).

# IMTConFundInvestor::Login

Set the login of the account used by the fund investor.

C++
    
    
    MTAPIRES  IMTConFundInvestor::Login(
       const UINT64  login     // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFundInvestor.Login(
       uint          login     // Login
       )

### Parameters

**login**  
[in] Fund investor's account login (IMTUser::Login).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

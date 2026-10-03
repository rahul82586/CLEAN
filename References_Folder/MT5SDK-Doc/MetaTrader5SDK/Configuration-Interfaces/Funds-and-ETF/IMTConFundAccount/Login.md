[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundAccount](../IMTConFundAccount.md) / Login

[Previous](Clear.md) | [Next](Name.md)

# IMTConFundAccount::Login

Get the login of the account used by the manager for fund management operations.

C++
    
    
    UINT64  IMTConFundAccount::Login()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFundAccount.Login()

### Return Value

Fund manager's account login ([IMTUser::Login](../../../Database-Interfaces/Users/IMTUser/Login.md)).

# IMTConFundAccount::Login

Set the login of the account used by the manager for fund management operations.

C++
    
    
    MTAPIRES  IMTConFundAccount::Login(
       const UINT64  login     // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFundAccount.Login(
       uint          login     // Login
       )

### Parameters

**login**  
[in] Fund manager's account login (IMTUser::Login).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

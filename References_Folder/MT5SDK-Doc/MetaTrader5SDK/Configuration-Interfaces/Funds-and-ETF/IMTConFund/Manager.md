[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Manager

[Previous](Server.md) | [Next](Flags.md)

# IMTConFund::Manager

Get the login of the manager responsible for the fund.

C++
    
    
    UINT64  IMTConFund::Manager()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.Manager()

### Return Value

The login of the manager ([IMTConManager::Login](../../Managers/IMTConManager/Login.md)) responsible for the fund.

# IMTConFund::Manager

Set the login of the manager responsible for the fund.

C++
    
    
    MTAPIRES  IMTConFund::Manager(
       const UINT64  manager     // Manager login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Manager(
       uint          manager     // Manager login
       )

### Parameters

**manager**  
[in] The login of the manager (IMTConManager::Login) responsible for the fund.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

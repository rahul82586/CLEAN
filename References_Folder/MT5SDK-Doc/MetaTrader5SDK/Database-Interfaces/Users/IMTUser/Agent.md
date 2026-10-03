[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Agent

[Previous](CommissionAgentMonthly.md) | [Next](Balance.md)

# IMTUser::Agent

Get the number of a client's agent account.

C++
    
    
    UINT64  IMTUser::Agent()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTUser.Agent()

### Return Value

Agent account number.

# IMTUser::Agent

Set the number of a client's agent account.

C++
    
    
    MTAPIRES  IMTUser::Agent(
       const UINT64  agent      // Agent account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Agent(
       ulong         agent      // Agent account
       )

### Parameters

**agent**  
[in] The number of an agent account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

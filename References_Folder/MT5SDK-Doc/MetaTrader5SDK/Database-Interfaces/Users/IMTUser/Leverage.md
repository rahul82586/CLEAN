[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Leverage

[Previous](OTPSecret.md) | [Next](LeadSource.md)

# IMTUser::Leverage

Get the size of a client's leverage.

C++
    
    
    UINT  IMTUser::Leverage()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTUser.Leverage()

### Return Value

Client's leverage.

# IMTUser::Leverage

Set the size of a client's leverage.

C++
    
    
    MTAPIRES  IMTUser::Leverage(
       const UINT  leverage      // Leverage
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Leverage(
       uint        leverage      // Leverage
       )

### Parameters

**leverage**  
[in] The size of a client's leverage in the range from 1 to 5000.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

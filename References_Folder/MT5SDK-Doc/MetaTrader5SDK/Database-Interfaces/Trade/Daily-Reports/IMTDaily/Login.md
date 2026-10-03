[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Login

[Previous](DatetimePrev.md) | [Next](Name.md)

# IMTDaily::Login

Get the [login](../../../Users/IMTUser.md) of the client for whom the daily report is generated.

C++
    
    
    UINT64  IMTDaily::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDaily.Login()

### Return Value

The login of a client for whom the daily report is generated.

# IMTDaily::Login

Set the [login](../../../Users/IMTUser.md) of a client in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Login(
       const UINT64  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Login(
       ulong         login      // Login
       )

### Parameters

**login**  
[in] Client login in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

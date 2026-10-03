[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Login

[Previous](IMTHistoryMatching-Order.md) | [Next](IMTHistoryMatching-Server.md)

# IMTECNHistoryMatching::Login

Get the login of the client, to whom the matching order belongs.

C++
    
    
    UINT64  IMTECNHistoryMatching::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIIMTECNHistoryMatching.Login()

### Return Value

The login of the client, to whom the matching order belongs.

# IMTECNHistoryMatching::Login

Set the login of the client, to whom the matching order belongs.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Login(
       const UINT64  login      // login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Login(
       ulong         login      // login
       )

### Parameters

**order**  
[in] The login of the client, to whom the matching order belongs.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

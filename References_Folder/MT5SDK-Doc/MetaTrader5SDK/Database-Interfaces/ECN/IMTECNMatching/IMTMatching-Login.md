[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Login

[Previous](IMTMatching-Order.md) | [Next](IMTMatching-Server.md)

# IMTECNMatching::Login

Get the login of the client, to whom the matching order belongs.

C++
    
    
    UINT64  IMTECNMatching::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNMatching.Login()

### Return Value

The login of the client, to whom the matching order belongs.

# IMTECNMatching::Login

Set the login of the client, to whom the matching order belongs.

C++
    
    
    MTAPIRES  IMTECNMatching::Login(
       const UINT64  login      // login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Login(
       ulong         login      // login
       )

### Parameters

**order**  
[in] The login of the client, to whom the matching order belongs.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

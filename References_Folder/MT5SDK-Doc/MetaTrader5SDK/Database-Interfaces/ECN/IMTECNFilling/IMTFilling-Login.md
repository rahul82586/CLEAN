[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Login

[Previous](IMTFilling-Clear.md) | [Next](IMTFilling-Order.md)

# IMTECNFilling::Login

Get the login of the client, whom the filling order belongs to.

C++
    
    
    UINT64  IMTECNFilling::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNFilling.Login()

### Return Value

The login of the client (on the MetaTrader 5 side), to whom the filling order belongs.

# IMTECNFilling::Login

Set the login of the client, whom the filling order belongs to.

C++
    
    
    MTAPIRES  IMTECNFilling::Login(
       const UINT64  login      // login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Login(
       ulong         login      // login
       )

### Parameters

**order**  
[in] The login of the client (on the MetaTrader 5 side), to whom the order belongs.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

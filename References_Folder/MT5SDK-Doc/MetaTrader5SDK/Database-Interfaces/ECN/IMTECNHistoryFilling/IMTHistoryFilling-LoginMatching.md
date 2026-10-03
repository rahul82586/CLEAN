[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling LoginMatching

[Previous](IMTHistoryFilling-Login.md) | [Next](IMTHistoryFilling-Server.md)

# IMTECNHistoryFilling::LoginMatching

Get the login of the client who has placed the opposite order which is used to match the current order.

C++
    
    
    UINT64  IMTECNHistoryFilling::LoginMatching()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryFilling.LoginMatching()

### Return Value

The login of the client who has placed the opposite order which is used to match the current order.

### Note

It is filled in only if the order is matched within the cluster, with the counter order of another client in MetaTrader 5.

# IMTECNHistoryFilling::LoginMatching

Set the login of the client who has placed the opposite order which is used to match the current order.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::LoginMatching(
       const UINT64  login      // login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.LoginMatching(
       ulong         login      // login
       )

### Parameters

**order**  
[in] The login of the client who has placed the opposite order which is used to match the current order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

It is filled in only if the order is matched within the cluster, with the counter order of another client in MetaTrader 5.

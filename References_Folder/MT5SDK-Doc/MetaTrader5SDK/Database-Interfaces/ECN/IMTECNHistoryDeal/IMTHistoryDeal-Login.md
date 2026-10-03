[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Login

[Previous](IMTHistoryDeal-DealGateway.md) | [Next](IMTHistoryDeal-Server.md)

# IMTECNHistoryDeal::Login

Get the login of the client, to whom the original order belongs.

C++
    
    
    UINT64  IMTECNHistoryDeal::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryDeal.Login()

### Return Value

The login of the client (on the MetaTrader 5 side), to whom the original order belongs.

# IMTECNHistoryDeal::Login

Set the login of the client, to whom the original order belongs.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Login(
       const UINT64  login      // login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Login(
       ulong         login      // login
       )

### Parameters

**order**  
[in] The login of the client (on the MetaTrader 5 side), to whom the original order belongs.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

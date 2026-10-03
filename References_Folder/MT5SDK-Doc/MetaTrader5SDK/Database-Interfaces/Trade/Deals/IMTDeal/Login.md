[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Login

[Previous](ExternalID.md) | [Next](Dealer.md)

# IMTDeal::Login

Get the login of the client, to whom the deal belongs.

C++
    
    
    UINT64  IMTDeal::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.Login()

### Return Value

The login of the client, to whom the order belongs.

# IMTDeal::Login

Set the login of the client, to whom the deal belongs.

C++
    
    
    MTAPIRES  IMTDeal::Login(
       const UINT64  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Login(
       ulong         login      // Login
       )

### Parameters

**login**  
[in] The login of the client, to whom the deal belongs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

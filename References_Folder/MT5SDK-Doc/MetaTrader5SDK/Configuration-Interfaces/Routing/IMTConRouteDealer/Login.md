[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRouteDealer](../IMTConRouteDealer.md) / Login

[Previous](Clear.md) | [Next](Name.md)

# IMTConRouteDealer::Login

Get the login of a dealer to whom requests under this rule will be sent.

C++
    
    
    UINT64  IMTConRouteDealer::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConRouteDealer.Login()

Python (Manager API)
    
    
    MTConRouteDealer.Login

### Return Value

The login of a dealer.

# IMTConRouteDealer::Login

Set the login of a dealer to whom requests under this rule will be sent.

C++
    
    
    MTAPIRES  IMTConRouteDealer::Login(
       const UINT64  login      // Dealer's login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRouteDealer.Login(
       ulong         login      // Dealer's login
       )

Python (Manager API)
    
    
    MTConRouteDealer.Login

### Parameters

**login**  
[in] The login of a dealer.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

An existing manager account with dealing permissions must be specified as the login.

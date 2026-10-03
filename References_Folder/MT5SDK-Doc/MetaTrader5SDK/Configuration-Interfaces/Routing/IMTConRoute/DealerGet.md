[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerGet

[Previous](DealerNext.md) | [Next](../IMTConCondition.md)

# IMTConRoute::DealerGet

Get a dealer entry in a routing rule by the login.

C++
    
    
    MTAPIRES  IMTConRoute::DealerGet(
       const UINT64        login,      // Dealer's login
       IMTConRouteDealer*  dealer      // An object of a dealer entry
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCoe  CIMTConRoute.DealerGet(
       uint                login,      // Dealer's login
       CIMTConRouteDealer  dealer      // An object of a dealer entry
       )

Python (Manager API)
    
    
    MTConRoute.DealerGet()

### Parameters

**login**  
[in] The login of a dealer.

**dealer**  
[out] An object of a dealer entry. The dealer object must be first created using theIMTAdminAPI::RouteDealerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The [IMTConRouteDealer::Login()](../IMTConRouteDealer/Login.md) value is used as the login.

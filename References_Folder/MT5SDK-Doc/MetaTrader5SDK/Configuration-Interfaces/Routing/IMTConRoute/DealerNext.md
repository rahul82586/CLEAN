[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerNext

[Previous](DealerTotal.md) | [Next](DealerGet.md)

# IMTConRoute::DealerNext

Get a dealer entry in a routing rule by the index.

C++
    
    
    MTAPIRES  IMTConRoute::DealerNext(
       const UINT          pos,        // Position of a dealer entry
       IMTConRouteDealer*  dealer      // An object of a dealer entry
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.DealerNext(
       uint                pos,        // Position of a dealer entry
       CIMTConRouteDealer  dealer      // An object of a dealer entry
       )

Python (Manager API)
    
    
    MTConRoute.DealerNext(
       pos,                # Position of a dealer entry
       dealer              # An object of a dealer entry
       )

### Parameters

**pos**  
[in] Position of a dealer entry in the list, starting with 0.

**dealer**  
[out] An object of a dealer entry. The dealer object must be first created using theIMTAdminAPI::RouteDealerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

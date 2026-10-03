[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerUpdate

[Previous](DealerAdd.md) | [Next](DealerDelete.md)

# IMTConRoute::DealerUpdate

Update a dealer to whom requests under the conditions of this rule will be sent for processing.

C++
    
    
    MTAPIRES  IMTConRoute::DealerUpdate(
       const UINT                pos,        // Position of a dealer entry
       const IMTConRouteDealer*  dealer      // An object of a dealer entry
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.DealerUpdate(
       uint                      pos,        // Position of a dealer entry
       CIMTConRouteDealer        dealer      // An object of a dealer entry
       )

Python (Manager API)
    
    
    MTConRoute.DealerUpdate(
       pos,                      # Position of a dealer entry
       dealer                    # An object of a dealer entry
       )

### Parameters

**pos**  
[in] Position of a dealer entry in the list, starting with 0.

**dealer**  
[in] An object of a dealer entry.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
